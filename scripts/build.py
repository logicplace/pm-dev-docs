import glob
from pathlib import Path

import jinja2

from asm import AssemblerHighlightExtension

base_path: Path = Path(__file__).parent.parent
env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(base_path),
	extensions=[AssemblerHighlightExtension],
)

def main():
	fn: str
	for fn in glob.glob("**/*.md.j2", root_dir=base_path, recursive=True):
		# Remoive the .j2 for the target
		target = (base_path / fn).with_suffix("")
		with target.open("wt", encoding="utf8") as f:
			name = fn.replace("\\", "/")
			out = env.get_template(name).render()
			f.write(out)

if __name__ == "__main__":
	main()
