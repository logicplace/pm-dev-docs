from jinja2 import nodes
from jinja2.ext import Extension

class AssemblerHighlightExtension(Extension):
	tags = {"asm"}

	def parse(self, parser):
		first = next(parser.stream)
		assert first.value == "asm"
		lineno = first.lineno

		args = [parser.parse_expression()]

		body = parser.parse_statements(
			["name:endasm"], drop_needle=True)

		return nodes.CallBlock(
            self.call_method("_highlight", args), [], [], body
        ).set_lineno(lineno)

	def _highlight(self, mode: str, caller):
		if mode == "epson":
			from asm.epson import render
		else:
			raise ValueError(mode)

		return render(caller())
