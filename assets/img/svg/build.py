import re
from glob import glob
from lxml import etree

MARK = "<!-- replace next line with "
SPACES = re.compile("  +")

parser = etree.XMLParser(remove_blank_text=True)

for fn in glob("op-*-*.svg"):
    contents = []
    do_replace = False
    with open(fn, "rt") as f:
        skip_next = False
        for line in f:
            if skip_next:
                skip_next = False
                continue

            contents.append(line)
            if MARK in line:
                do_replace = True
                idx = line.find(MARK)
                replace_fn = line[idx + len(MARK):line.find(" -->", idx)]

                start = line[:idx]
                ending = line[-2:] if line[-2:] == "\r\n" else line[-1]

                elem = etree.parse(replace_fn, parser=parser)
                ns = elem.getroot().nsmap
                for path in elem.iterfind("//path[@d]", ns):
                    path.attrib["d"] = SPACES.sub("", path.get("d"))
                contents.append(
                    start
                    + etree.tostring(elem, encoding=str).replace(' xmlns="http://www.w3.org/2000/svg"', "")
                    + ending
                )
                skip_next = True

    if do_replace:
        with open(fn, "wt") as f:
            f.writelines(contents)
