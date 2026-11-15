"""Lint the wiki. Exit code 0 = pass, 1 = errors (printed one per line).

Checks (agreed in docs/01_interview.md):
  links      every [[link]] resolves to a page in wiki/
  index      every page is listed in wiki/index.md
  orphans    every page is linked from at least one page other than index.md and itself
  front      frontmatter has title/type/sources/updated; type valid; source ids exist
  cites      [id, p.N] ids exist and page N exists in that source
  numbers    a line with a number has a citation; the number appears on a cited page
Usage: python tools/lint_wiki.py [--quiet]
"""
from __future__ import annotations

import re
import sys

from common import WIKI, LINK_RE, check_citations_and_numbers, source_pages

SPECIAL = {"index", "log"}
TYPES = {"source", "concept", "synthesis", "glossary"}
FIELDS = ("title", "type", "sources", "updated")


def split_front(text: str) -> tuple[dict[str, str] | None, list[tuple[int, str]]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, list(enumerate(lines, 1))
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, list(enumerate(lines, 1))
    front = {}
    for raw in lines[1:end]:
        if ":" in raw:
            k, v = raw.split(":", 1)
            front[k.strip()] = v.split("#", 1)[0].strip()
    return front, [(i + 1, l) for i, l in enumerate(lines) if i > end]


def main() -> int:
    pages = {p.stem: p for p in WIKI.rglob("*.md")}
    errors: list[str] = []
    inbound: dict[str, set[str]] = {s: set() for s in pages}
    index_links: set[str] = set()

    for stem, path in sorted(pages.items()):
        rel = path.relative_to(WIKI.parent).as_posix()
        text = path.read_text(encoding="utf-8")
        front, body = split_front(text)

        for target in LINK_RE.findall(text):
            target = target.strip()
            if target not in pages:
                errors.append(f"{rel}: [links] broken link [[{target}]]")
            elif target != stem:
                inbound[target].add(stem)
            if stem == "index":
                index_links.add(target)

        if stem in SPECIAL:
            continue
        if front is None:
            errors.append(f"{rel}: [front] missing frontmatter")
        else:
            for f in FIELDS:
                if not front.get(f):
                    errors.append(f"{rel}: [front] missing field '{f}'")
            if front.get("type") and front["type"] not in TYPES:
                errors.append(f"{rel}: [front] bad type '{front['type']}'")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", front.get("updated", "")):
                errors.append(f"{rel}: [front] 'updated' must be YYYY-MM-DD")
            for sid in re.findall(r"[a-z]+\d{4}", front.get("sources", "")):
                if source_pages(sid) is None:
                    errors.append(f"{rel}: [front] unknown source id '{sid}'")
            if "TODO" in text or "<" + "..." in text:
                errors.append(f"{rel}: [front] template placeholder left in page")

        in_code = False
        for lineno, line in body:
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code or line.lstrip().startswith("#"):
                continue
            for problem in check_citations_and_numbers(line):
                errors.append(f"{rel}:{lineno}: [cites/numbers] {problem}")

    for stem in pages:
        if stem in SPECIAL:
            continue
        if stem not in index_links:
            errors.append(f"wiki: [index] page '{stem}' is not listed in index.md")
        if not (inbound[stem] - {"index"}):
            errors.append(f"wiki: [orphans] page '{stem}' has no inbound link except index.md")

    for e in errors:
        print(e)
    n_pages = len([s for s in pages if s not in SPECIAL])
    print(f"lint_wiki: {n_pages} pages, {len(errors)} error(s) -> {'PASS' if not errors else 'FAIL'}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
