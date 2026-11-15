"""Bundle every wiki/*.md page into one browsable HTML file: site/wiki.html.

Pages are embedded as JSON and rendered in the browser with marked.js; [[links]] become
in-page links, citations [id, p.N] become small grey tags. Read-only view of wiki/.
Usage: python tools/build_wiki_site.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
OUT = ROOT / "site" / "wiki.html"

ORDER = {"index": 0, "overview-for-beginners": 1, "glossary": 3, "log": 4}


def main() -> None:
    pages = {}
    for p in sorted(WIKI.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        front = {}
        m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, flags=re.S)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    front[k.strip()] = v.strip()
            text = text[m.end():]
        group = p.parent.name if p.parent != WIKI else "top"
        pages[p.stem] = {"title": front.get("title") or p.stem, "type": front.get("type", ""),
                         "sources": front.get("sources", ""), "group": group, "md": text}
    tpl = (ROOT / "tools" / "wiki_template.html").read_text(encoding="utf-8")
    data = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(tpl.replace("/*PAGES*/null", data), encoding="utf-8")
    print(f"build_wiki_site: {len(pages)} pages -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
