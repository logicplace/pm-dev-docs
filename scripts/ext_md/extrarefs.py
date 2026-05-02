from markdown import Extension
from markdown.preprocessors import Preprocessor

Refs = dict[str, tuple[str, str]]

class ExtraRefsExtension(Extension):
	def __init__(self, refs: Refs, **kwargs):
		super().__init__(**kwargs)
		self.refs = refs

	def extendMarkdown(self, md):
		md.registerExtension(self)
		md.preprocessors.register(Bleh(md, self.refs), "extrarefs", 1)

class Bleh(Preprocessor):
	def __init__(self, md, refs: Refs):
		super().__init__(md)
		self.refs = refs

	def run(self, lines):
		self.md.references.update(self.refs)
		return lines
