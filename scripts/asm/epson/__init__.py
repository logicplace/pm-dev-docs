from collections import defaultdict
import re

from ..common import *
from .ops import OPS


# Parse a single line of EPSON-style asm.
# Combine any lines which end in \ first.
EPSON_S1C88_LINE = re.compile(
	r'''
	^(\s*[a-z_][a-z0-9_]*\s*:)?
	(?:
		(\s*)        # indentation (or space after label)
		([^;\s]+)    # operator, directive, macro name
		(?:
			(\s+)    # space required before the first arg
			([^;]+)  # args
		)?
	)?
	(\s*)(;.*)?
	''',
	re.VERBOSE | re.IGNORECASE
)
EPSON_S1C88_ARG = re.compile(
	r'''
	(?:
		(macro|set|equ)
		(\s+)
	|	(
			"(?:""|[^"]+)"
			|'(?:''|[^']+)'
			|[^,;]+?
		)
		(\s*,\s*|\s*\Z)
	)
	''',
	re.VERBOSE | re.IGNORECASE
)
EPSON_S1C88_LABEL = re.compile(r'[a-z_][a-z0-9_]*')

POS_LABEL_DIS1 = re.compile(r'x([0-9A-F]+)')
POS_LABEL_MINDIS2 = re.compile(r'loc_0x([0-9A-F]+)')

EPSON_DIRECTIVES = {
	"calls", "symb",
	"align", "comment", "define", "defsect",
	"end", "fail", "include", "msg",
	"radix", "sect", "undef", "warn",
	"extern", "global", "local", "name",
	"ascii", "asciz", "db", "ds", "dw",
	"dup", "dupa", "dupc", "dupf",
	"endif", "endm", "exitm", "if", "macro", "pmacro",
}

EPSON_REGISTER = {
	"b", "a", "ba", "h", "l", "hl",
	"br", "sc", "cc", "ix", "iy",
	"pc", "sp", "ep", "xp", "yp",
	"cb", "nb", "ip", "all", "ale"
}

EPSON_FLAG_CONDITIONS = {
	"c", "nc", "z", "nz",
	"lt", "le", "gt", "ge",
	"v", "nv", "p", "m",
	"f0", "f1", "f2", "f3",
	"nf0", "nf1", "nf2", "nf3",
}

EPSON_DEFSECT_ARGS = {
	"code", "data", "short", "tiny", #"fit",
	"clear", "noclear", "init", "overlay",
	"romdata", "max", "join",
}


def get_num(s: str):
	if str(s).lower().endswith("h"):
		return int(s[:-1], 16)
	return int(s)


def get_str(s):
	s = str(s)
	if s.startswith('"'):
		return s.strip('"').replace('""', '"')
	if s.startswith("'"):
		return s.strip("'").replace("''", "'")


def identify_arg_class(arg: str):
	if arg:
		if arg[0] in "\"'":
			return "string"
		if arg[0] in "0123456789#":
			return "number"
		if arg.startswith("@"):
			return "built_in"

		lower = arg.lower()
		if lower in EPSON_REGISTER:
			return "variable.language"
		if lower in EPSON_FLAG_CONDITIONS:
			return "literal"
		if EPSON_S1C88_LABEL.fullmatch(lower):
			return "variable"
	return ""


def identify_arg_type(arg: str, *, index_ok=True):
	# Only used for ops so don't need to care about strings
	a0 = arg[0]
	if a0 == "#":
		return "#imm"
	if a0 in "0123456789":
		return "imm"

	lower = arg.lower()
	if index_ok and a0 == "[" and lower[-1] == "]":
		if lower.startswith("[br:"):
			return "[br:imm]"
		if "+" in lower:
			return "+".join(
				identify_arg_type(x, index_ok=False)
				for x in lower[1:-1].split("+", 1)
			).join("[]")
		return identify_arg_type(arg[1:-1], index_ok=False).join("[]")
	if lower in EPSON_REGISTER or lower in EPSON_FLAG_CONDITIONS:
		return lower

	if EPSON_S1C88_LABEL.fullmatch(lower):
		# Assume label
		return "imm"

	raise ValueError(f"unknown argument type: '{arg}'")

def process_epson(code, *, position=0, digits=6) -> Renderer:
	cont = ""
	macros = defaultdict(set)
	macro_sizes = defaultdict(int)
	macro_cycles = defaultdict(int)
	defsects: dict[int] = {}
	in_macro = ""

	def macro_or_op(x: str):
		if x.lower() in macros:
			return "title.function"
		return "keyword"

	renderer = Renderer(digits)

	for ln, line in enumerate(lines(code)):
		try:
			# TODO: remember and restore break points
			line = cont + line
			if line.endswith("\\"):
				cont = line[:-1]
				continue
			cont = ""

			if not line.strip():
				renderer.queue(Line(EmptyRender(), EmptyRender()))
				continue

			result = {"label": EmptyRender(), "comment": EmptyRender()}
			line_type = Line

			mo_line = EPSON_S1C88_LINE.match(line)
			if mo_line:
				label, sp, op, sp2, args, sp3, comment = mo_line.groups()
				if label:
					if label[0] in " \t":
						len_with_indent = len(label)
						nlabel = label.lstrip()
						pfx = label[:len_with_indent - len(nlabel)]
						label = nlabel
					else:
						pfx = ""
					spp = SPACE.search(label)
					split_at = spp.start if spp else -1
					name = label[:split_at]
					result["label"] = AccentedData(
						name,
						prefix=pfx,
						suffix=label[split_at:] + (not args and not comment and sp3 or ""),
						classname="symbol"
					)

					# Reset position if indicated
					mo1 = POS_LABEL_DIS1.fullmatch(name)
					mo2 = POS_LABEL_MINDIS2.fullmatch(name)
					mo = mo1 or mo2
					if mo:
						position = int(mo.group(1), 16)

				if op:
					op_data = AccentedData(op, prefix=sp or "", suffix=sp2 or "")
					if args and args.strip():
						arg_ends = [
							# TODO: parse args and accent pieces
							(AccentedData(
								x.group(1) or x.group(3),
								suffix=x.group(2) or x.group(4) or "",
								classname=identify_arg_class(x.group(1) or x.group(3))
							), x.end())
							for x in EPSON_S1C88_ARG.finditer(args)
						]

						if not comment:
							arg_ends[-1][0].suffix += sp3

						args = [x[0] for x in arg_ends]

						first = str(args[0].data).upper()
					else:
						arg_ends, args = [], []
						first = ""

					if first == "MACRO":
						in_macro = op_data.data
						line_type = MacroLine
						op_data.classname = "title.function"
						result["name"] = op_data
						sym = result["symbol"] = args.pop(0)
						sym.classname = "meta"
						macros[op_data.data.lower()].add(op_data.data)
					elif first in ("SET", "EQU"):
						line_type = DirectiveLine
						op_data.classname = "variable"
						result["lefthand_arg"] = op_data
						sym = result["directive"] = args.pop(0)
						sym.classname = "meta"
					elif op_data.data.lower() in EPSON_DIRECTIVES:
						lower = op_data.data.lower()
						sz = -1
						if lower == "endm":
							in_macro = ""
						elif lower == "defsect":
							sect = get_str(args[0])
							if len(args) > 1:
								# "AT addr" is space separated from other args
								# so separate it from the last arg
								an1 = SPACE.split(str(args[-1].data))
								if len(an1) > 3 and an1[-3].lower() == "at":
									f = args.pop()
									f.data = "".join(an1[-3:])
									sfx = ""
									if not an1[-4].strip():
										d, sfx = "".join(an1[:-4]), an1[-4]
									else:
										d, sfx = "".join(an1[:-3]), ""
									args.append(AccentedData(d, f.prefix, sfx))
									f.prefix = ""
									args.append(f)
							for i, a in enumerate(args[1:], 1):
								data = SPACE.sub(str(a.data).lower(), " ").strip()
								print(data)
								if data.startswith("at ") or data.startswith("at "):
									at, at_s, addr, *addr_s = SPACE.split(str(a.data))
									at = AccentedData(at, suffix=at_s)
									addr = AccentedData(addr, suffix="".join(addr_s), classname="number")
									defsects[sect] = int(addr)
									args[i] = ConcatAccentedData(at, addr)
								elif data.startswith("fit "):
									f, f_s, size, *size_s = SPACE.split(str(a.data))
									f = AccentedData(f, suffix=f_s, classname="literal")
									size = AccentedData(size, suffix="".join(size_s), classname="number")
									args[i] = ConcatAccentedData(f, sz)
								elif data in EPSON_DEFSECT_ARGS:
									a.classname = "literal"
						elif lower == "sect":
							sect = get_str(args[0])
							if sect in defsects:
								position = defsects[sect]
						elif lower == "end":
							position = -1
						elif lower in ("ascii", "asciz"):
							zero = int(lower.endswith("z"))
							sz = 0
							for s in args:
								s = get_str(args[0])
								sz += len(s) + zero
						elif lower == "db":
							sz = 0
							for a in args:
								c = identify_arg_class(a.data)
								if c == "string":
									sz += len(get_str(a))
								else:
									# TODO: check symbol type / size
									sz += 1
						elif lower == "dw":
							# All strings must be at most 2 characters
							# and 1-char strings are written as 2 bytes
							sz = len(args) * 2
						elif lower == "ds":
							sz = result["size"] = get_num(args[0])
							
						line_type = DirectiveLine
						sym = result["directive"] = op_data
						sym.classname = "meta"

						if sz >= 0:
							result["size"] = sz
							if not in_macro:
								result["position"] = position
								position += sz
					else:
						line_type = OperatorLine
						op_data.classname = macro_or_op(op_data.data)
						result["mnemonic"] = op_data
						arg_types = [identify_arg_type(str(a)) for a in args]
						key = (str(op_data.data).lower(), *arg_types)
						has_position = not in_macro and position >= 0
						if has_position:
							result["position"] = position
						if key in OPS:
							cycles, size = OPS[key]
							if has_position:
								position += size
							if in_macro:
								macro_sizes[in_macro] += size

							if isinstance(cycles, int):
								result["cycles"] = cycles
								if macro_cycles[in_macro] >= 0:
									macro_cycles[in_macro] += cycles
							else:
								# Variable number of cycles
								macro_cycles[in_macro] = -1
						elif has_position:
							position = -1

					result["args"] = args

				if comment:
					result["comment"] = AccentedData(
						comment,
						prefix=sp3,
						classname="comment"
					)

			renderer.queue(line_type(**result))
		except:
			print(f"error on line {ln+1}")
			raise

	return renderer


def render(code, *, position=0, digits=6) -> str:
	renderer = process_epson(code, position=position, digits=digits)
	return renderer.render()
