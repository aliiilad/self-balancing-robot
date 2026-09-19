#!/usr/bin/env python3
"""Convert a .docx file to Markdown.

Used to re-render the Word originals (roadmap, engineering log) into the
GitHub-readable Markdown under docs/. Writes to stdout by default so it never
clobbers a hand-tidied file -- diff the output against docs/ and merge in the
new entries.

Usage:
    python3 tools/docx2md.py Self_Balancing_Robot_Engineering_Log.docx
    python3 tools/docx2md.py Self_Balancing_Robot_25_Day_Roadmap.docx -o out.md

No third-party dependencies: a .docx is a zip of XML, and the standard library
can read both.
"""

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def text_of(node):
    """Concatenate every run of text under a node, honouring tabs and breaks."""
    out = []
    for el in node.iter():
        if el.tag == W + "t":
            out.append(el.text or "")
        elif el.tag in (W + "tab",):
            out.append(" ")
        elif el.tag in (W + "br", W + "cr"):
            out.append("\n")
    return "".join(out)


def heading_level(para):
    """Return 1-6 if the paragraph uses a Word Heading style, else None."""
    style = para.find(f"{W}pPr/{W}pStyle")
    if style is None:
        return None
    val = style.get(W + "val", "")
    m = re.fullmatch(r"[Hh]eading\s*([1-6])", val)
    return int(m.group(1)) if m else None


def is_list_item(para):
    return para.find(f"{W}pPr/{W}numPr") is not None


def render_paragraph(para):
    txt = text_of(para).strip()
    if not txt:
        return None
    level = heading_level(para)
    if level:
        return "#" * level + " " + txt
    if is_list_item(para):
        return "- " + txt
    return txt


def render_table(tbl):
    """Render a w:tbl as a Markdown table, collapsing newlines inside cells."""
    rows = []
    for tr in tbl.findall(f"{W}tr"):
        cells = [
            text_of(tc).strip().replace("\n", " ").replace("|", r"\|")
            for tc in tr.findall(f"{W}tc")
        ]
        rows.append(cells)

    rows = [r for r in rows if any(r)]
    if not rows:
        return None

    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]

    lines = ["| " + " | ".join(rows[0]) + " |",
             "|" + "|".join([" --- "] * width) + "|"]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def convert(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))

    body = root.find(W + "body")
    if body is None:
        return ""

    blocks = []
    for child in body:
        if child.tag == W + "p":
            rendered = render_paragraph(child)
        elif child.tag == W + "tbl":
            rendered = render_table(child)
        else:
            rendered = None
        if rendered:
            blocks.append(rendered)

    md = "\n\n".join(blocks)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", help="path to the .docx file")
    ap.add_argument("-o", "--output", help="write here instead of stdout")
    args = ap.parse_args()

    try:
        md = convert(args.docx)
    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        sys.exit(f"could not read {args.docx}: {exc}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(md)
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
