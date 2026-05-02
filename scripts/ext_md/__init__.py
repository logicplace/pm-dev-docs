from typing import Any

from jinja2 import nodes
from jinja2.ext import Extension

class ExtendedMarkdownExtension(Extension):
	tags = {"md"}
	refs_by_fn = dict[str, dict[str, tuple[str, str]]]()

	def parse(self, parser):
		first = next(parser.stream)
		assert first.value == "md"
		lineno = first.lineno

		args = []
		if parser.stream.current.type != "block_end":
			args.append(parser.parse_expression())
		else:
			args.append(nodes.Dict({}))

		if parser.filename not in self.refs_by_fn:
			from markdown.blockprocessors import ReferenceProcessor
			refs = self.refs_by_fn[parser.filename] = dict[str, tuple[str, str]]()
			for l in open(parser.filename, "rt", encoding="utf8"):
				m = ReferenceProcessor.RE.match(l)
				if m:
					id = m.group(1).strip().lower()
					link = m.group(2).lstrip('<').rstrip('>')
					title = m.group(5) or m.group(6)
					refs[id] = (link, title)
		args.append(nodes.Const(self.refs_by_fn[parser.filename]))

		body = parser.parse_statements(
			["name:endmd"], drop_needle=True)

		return nodes.CallBlock(
            self.call_method("_convert", args), [], [], body
        ).set_lineno(lineno)

	def _convert(self, args: dict[str, Any], refs: dict[str, tuple[str, str]], caller):
		import markdown
		from .replace import ReplaceExtension
		from .extrarefs import ExtraRefsExtension
		from tables_extended import TableExtension

		symbols = args.pop("symbols", "")
		return markdown.markdown(caller(), extensions=[
			"footnotes",
			ExtraRefsExtension(refs),
			ReplaceExtension(symbols),
			TableExtension(),
		])
