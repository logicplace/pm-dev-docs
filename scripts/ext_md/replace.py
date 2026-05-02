import re
import xml.etree.ElementTree as etree

from markdown import Extension, Markdown
from markdown.blockparser import BlockParser
from markdown.blockprocessors import BlockProcessor
from markdown.treeprocessors import Treeprocessor
from markdown.util import AtomicString

ESCAPE_CHARSET = str.maketrans({"]": r'\]', "-": r'\-', "^": r'\^', "\\": r'\\'})
REPL = list[tuple[int, re.Pattern, str, bool]]

class ReplaceExtension(Extension):
	"""
	Create custom inline replacements.
	Example usage:
	  *;^...^:<sup>...</sup>
	"""

	def __init__(self, symbols: str = "", **kwargs):
		super().__init__(**kwargs)
		self.symbols = symbols
		self.replacements: REPL = []

	def extendMarkdown(self, md):
		for x in self.symbols:
			if x not in md.ESCAPED_CHARS:
				md.ESCAPED_CHARS.append(x)
		md.registerExtension(self)
		md.treeprocessors.register(
			ReplaceTreeprocessor(md, self.replacements),
			"replace", 175)
		sym = "".join(md.ESCAPED_CHARS).replace(".", "")
		md.parser.blockprocessors.register(
			ReplaceBlockprocessor(md.parser, self.replacements, sym),
			"replace", 176)

class ReplaceTreeprocessor(Treeprocessor):
	""" Perform replacements """
	def __init__(self, md: Markdown, replacements: REPL):
		self.replacements = replacements
		super().__init__(md)

	def replace(self, m: re.Match[str]):
		escapes = m.group(1)
		l = len(escapes)
		pfx = "\\" * (l // 2)
		if l % 2:
			# Return escaped form
			return pfx + m.group(2)
		for _, r, sub, wraps in self.replacements:
			if m2 := r.fullmatch(m.group(2)):
				if wraps:
					return pfx + sub.replace("...", m2.group(1), 1)
				return pfx + sub

	def iter_element(self, el: etree.Element, parent: etree.Element | None = None):
		for child in reversed(el):
			self.iter_element(child, el)
		if el.text and not isinstance(el.text, AtomicString):
			el.text = self.RE.sub(self.replace, el.text)
		if parent is not None and el.tail and not isinstance(el.tail, AtomicString):
			el.tail = self.RE.sub(self.replace, el.tail)

	def run(self, root: etree.Element) -> etree.Element | None:
		if not self.replacements:
			# No replacements defined. Skip running processor.
			return
		# Sort by longest open bound first
		self.replacements.sort(reverse=True, key=lambda x: x[0])
		self.RE = re.compile(r'(\\*)(' + "|".join(
			r[1].pattern
			for r in self.replacements) + ")")
		self.iter_element(root)


class ReplaceBlockprocessor(BlockProcessor):
	def __init__(self, parser: BlockParser, replacements: REPL, symbols: str):
		symbols = symbols.translate(ESCAPE_CHARSET)
		bound = f"[{symbols}]+(?:[a-zA-Z0-9]+[{symbols}]+)?"
		self.define_syntax = re.compile(
			r'^\*;[ \t]*({b})(?:\.\.\.({b}))?\s*:[ \t]*(.*)$'.format(
				b=bound), re.M)
		self.replacements = replacements
		super().__init__(parser)

	def test(self, parent: etree.Element, block: str) -> bool:
		return True

	def run(self, parent: etree.Element, blocks: list[str]) -> bool:
		"""
		Find and remove all definitions from the text.
		Each reference is added to the replacement collection.
		"""
		block = blocks.pop(0)
		m = self.define_syntax.search(block)
		if m:
			b1, b2, sub = m.groups()
			pattern = re.escape(b1)
			if b2:
				pattern = r'{b1}(.+?){b2}'.format(
					b1=pattern, b2=re.escape(b2))
			pattern = re.compile(pattern)

			self.replacements.append((len(b1), pattern, sub, bool(b2)))

			if block[m.end():].strip():
				# Add any content after match back to blocks as separate block
				blocks.insert(0, block[m.end():].lstrip('\n'))
			if block[:m.start()].strip():
				# Add any content before match back to blocks as separate block
				blocks.insert(0, block[:m.start()].rstrip('\n'))
			return True

		# No match. Restore block.
		blocks.insert(0, block)
		return False
