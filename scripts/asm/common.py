import re
import html
from io import TextIOBase
from typing import Self, Sequence
from dataclasses import dataclass, field

SPACE = re.compile(r'(\s+)')

CLASSNAME_TO_COLOR = {
	"keyword": "#d73a49",
	"variable.language": "#d73a49",
	"title.function": "#6f42c1",
	"literal": "#005cc5",
	"meta": "#005cc5",
	"number": "#005cc5",
	"variable": "#005cc5",
	"string": "#032f62",
	"built_in": "#e36209",
	"symbol": "#e36209",
	"comment": "#6a737d",
}

def _id(id_: str) -> str:
	return f"user-content-{id_}" if id_ else ""

def _class(cls: str) -> str:
	return "hljs-" + " ".join(
		x + "_" * i
		for i, x in enumerate(cls.split("."))
	)

@dataclass
class AccentedData:
	data: str|Self
	prefix: str = ""
	suffix: str = ""
	classname: str = ""

	def _render(self, data: str, anchor: str = "") -> str:
		pfx = ""
		if self.classname:
			classname = f' class="{_class(self.classname)}"'
			if self.classname in CLASSNAME_TO_COLOR:
				classname += f' color="{CLASSNAME_TO_COLOR[self.classname]}"'

			if anchor:
				pfx, sfx = f'<a href="#{anchor}"{classname}>', "</a>"
		else:
			classname = ""

		if not pfx:
			pfx, sfx = f'<span{classname}>', "</span>"

		return (
			f'{html.escape(self.prefix.replace("\t", "    "))}'
			f'{pfx}{data}{sfx}'
			f'{html.escape(self.suffix)}'
		)

	def render(self) -> str:
		data = (
			self.data.render()
			if isinstance(self.data, AccentedData)
			else html.escape(self.data)
		)
		anchor = ""
		if self.classname in ("symbol", "variable", "title.function"):
			anchor = _id(str(self.data))
		return self._render(data, anchor)

	def __str__(self) -> str:
		return str(self.data)

	def __int__(self) -> int:
		sdata = str(self.data).lstrip("#").lower()
		if sdata.endswith("b"):
			return int(sdata[:-1], 2)
		if sdata[-1] in "oq":
			return int(sdata[:-1], 8)
		if sdata.endswith("h"):
			return int(sdata[:-1], 16)
		return int(sdata.rstrip("d"))

	def __bool__(self) -> bool:
		return bool(self.data)

class EmptyRender(AccentedData):
	def __init__(self) -> None:
		return super().__init__("")

	def render(self):
		return ""

	def __bool__(self):
		return False

class ConcatAccentedData(AccentedData):
	data: list[str|AccentedData]

	def __init__(self, *data: str|AccentedData) -> None:
		self.data = list(data)

	def render(self) -> str:
		data = "".join([
			d.render()
			if isinstance(d, AccentedData)
			else html.escape(d)
			for d in self.data
		])
		return self._render(data)

	def __str__(self) -> str:
		return str("".join(map(str, self.data)))

	def __int__(self) -> int:
		return int(str(self))

	def __bool__(self) -> bool:
		return bool(self.data)


@dataclass
class Line:
	label: AccentedData
	comment: AccentedData

	def _render(self, *mid: str):
		return self.label.render() + "".join(mid) + self.comment.render()

	def render(self):
		return self._render()

	def is_comment(self):
		return not self.label and self.comment

@dataclass
class OperatorLine(Line):
	mnemonic: AccentedData
	args: list[AccentedData]
	position: int = -1
	cycles: int = -1

	def render(self):
		return self._render(
			self.mnemonic.render(),
			*(x.render() for x in self.args),
		)

	def is_comment(self):
		return False

@dataclass
class DirectiveLine(Line):
	directive: AccentedData
	args: list[AccentedData]
	lefthand_arg: AccentedData = field(default_factory=EmptyRender)
	position: int = -1
	size: int = -1

	def render(self):
		return self._render(
			self.lefthand_arg.render(),
			self.directive.render(),
			*(x.render() for x in self.args),
		)

	def is_comment(self):
		return False

@dataclass
class MacroLine(Line):
	name: AccentedData
	symbol: AccentedData
	args: list[AccentedData]

	def render(self):
		return self._render(
			self.name.render(),
			self.symbol.render(),
			*(x.render() for x in self.args),
		)

	def is_comment(self):
		return False


def lines(x) -> Sequence[str]:
	if isinstance(x, str):
		return x.splitlines()
	if isinstance(x, TextIOBase):
		return iter(x)
	raise TypeError(type(x))


class Renderer:
	def __init__(self, use_positions=0) -> None:
		self.prefixes: list[str] = []
		self.lines: list[Line] = []
		self.label_anchors: dict[int,str] = {}
		self.prefix_anchors: dict[int,str] = {}
		self.use_positions = use_positions
		self.cur_line = 0
		self.preroll_start = -1

	def queue(self, line: Line) -> None:
		if not self.use_positions:
			self.prefixes.append(str(self.cur_line))
			self.prefix_anchors[self.cur_line] = str(self.cur_line)

		if line.is_comment():
			if self.use_positions:
				self.prefixes.append("")
			if self.preroll_start < 0:
				self.preroll_start = self.cur_line
		elif not line:
			if self.use_positions:
				self.prefixes.append("")
			self.preroll_start = -1
		else:
			if self.use_positions:
				if isinstance(line, (OperatorLine, DirectiveLine)) and line.position >= 0:
					pos = f"{line.position:0{self.use_positions}X}"
					self.prefix_anchors[self.cur_line] = pos
					self.prefixes.append(f"${pos}")
				else:
					self.prefixes.append("")

			if line.label:
				self.label_anchors[
					self.cur_line
					if self.preroll_start < 0
					else self.preroll_start
				] = str(line.label)
				self.preroll_start = -1

		self.lines.append(line)
		self.cur_line += 1

	def render(self) -> str:
		res = '<pre><code class="language-s1c88 hljs">'
		longest = max(len(x) for x in self.prefixes)
		prefix_class = 'color="#6e7781" class="line-number"'
		if self.use_positions:
			lines = zip(self.prefixes, self.lines)
		else:
			lines = self.lines

		for i, (p, l) in enumerate(lines):
			if p:
				if i in self.prefix_anchors:
					name = _id(self.prefix_anchors[i])
					res += f'<a name="{name}" href="#{name}" {prefix_class}>'
					suffix = "</a>"
				else:
					res += f"<span {prefix_class}>"
					suffix = "</span>"

				res += f"{p:>{longest}s}{suffix}"
			else:
				res += f'<span {prefix_class}>{" " * longest}</span>'

			if i in self.label_anchors:
				span_id = f' id="{_id(self.label_anchors[i])}"'
			else:
				span_id = ""
			res += f'  <span class="line-content"{span_id}>{l.render()}</span>\n'

		res += "</code></pre>"
		return res
