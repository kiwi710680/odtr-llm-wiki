"""Render topic-<slug>/drafts/*.md into topic-<slug>/deck.html (node N5).

Deterministic: the text of every draft line is copied verbatim; citations become numbered
footnotes on the same slide, [[links]] become plain text plus a "Wiki:" footer.
Usage: python tools/build_deck.py <topic-dir> "<deck title>"
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from common import CITE_RE, LINK_RE, ROOT

AUTHORS = {
    "williams2024": "Williams et al., Am J Epidemiol 2024",
    "bluemlein2022": "Blümlein et al., PMLR (MLHC) 2022",
    "hong2021": "Hong et al., EClinicalMedicine 2021",
    "desman2025": "Desman et al., npj Digit Med 2025",
    "renson2025": "Renson et al., Am J Epidemiol 2025",
}
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮"
DIAGRAMS_DIR = ROOT / "tools" / "diagrams"


def inline(text: str, notes: list[str], wiki: list[str]) -> str:
    def cite(m: re.Match) -> str:
        key = f"{AUTHORS.get(m.group(1), m.group(1))}, p.{m.group(2)}" + (f"–{m.group(3)}" if m.group(3) else "")
        if key not in notes:
            notes.append(key)
        return f"\x00{notes.index(key)}\x00"

    def link(m: re.Match) -> str:
        if m.group(1) not in wiki:
            wiki.append(m.group(1))
        return m.group(1)

    text = CITE_RE.sub(cite, text)
    text = LINK_RE.sub(link, text)
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: f'<sup class="fn">{CIRCLED[int(m.group(1))]}</sup>', text)
    return text.strip()


def render_body(lines: list[str], notes: list[str], wiki: list[str]) -> tuple[str, str]:
    out, speaker, i = [], [], 0
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("Note:"):
            speaker.append(inline(s[5:], notes, wiki))
        elif s == "||":
            out.append("</div><div class='col'>")
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head = "".join(f"<th>{inline(c, notes, wiki)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c, notes, wiki)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
            continue
        elif s.startswith(">"):
            out.append(f"<blockquote>{inline(s[1:], notes, wiki)}</blockquote>")
        elif re.match(r"^[-*] ", s):
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i].strip()):
                items.append(f"<li>{inline(lines[i].strip()[2:], notes, wiki)}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif re.match(r"^\d+\. ", s):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i].strip()), notes, wiki)}</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        else:
            out.append(f"<p>{inline(s, notes, wiki)}</p>")
        i += 1
    return "\n".join(out), " ".join(speaker)


def parse(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    end = lines.index("---", 1)
    meta = {}
    for raw in lines[1:end]:
        k, v = raw.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, lines[end + 1:]


def main() -> None:
    d = (ROOT / sys.argv[1]).resolve()
    deck_title = sys.argv[2]
    slides = []
    drafts = sorted((d / "drafts").glob("s*.md"))
    for n, f in enumerate(drafts, 1):
        meta, body = parse(f)
        notes: list[str] = []
        wiki: list[str] = []
        layout = meta.get("layout", "bullets")
        title = inline(meta["title"], notes, wiki)
        content, speaker = render_body(body, notes, wiki)
        if layout == "two-col":
            content = f"<div class='cols'><div class='col'>{content}</div></div>"
        diagram = ""
        if meta.get("diagram"):
            diagram = (DIAGRAMS_DIR / f"{meta['diagram']}.svg").read_text(encoding="utf-8")
            diagram = f"<figure class='diagram'>{diagram}</figure>"
        foot = ""
        if notes or wiki:
            fn = " ".join(f"<span>{CIRCLED[k]} {html.escape(v)}</span>" for k, v in enumerate(notes))
            wk = ("<span class='wk'>Wiki：" + "、".join(html.escape(w) for w in wiki) + "</span>") if wiki else ""
            foot = f"<footer class='refs'>{fn}{wk}</footer>"
        kicker = html.escape(meta.get("kicker", ""))
        slides.append(
            f"<section class='slide {layout}' data-n='{n}' data-src='{f.name}'>"
            f"<div class='content'>{f'<p class=kicker>{kicker}</p>' if kicker else ''}<h2>{title}</h2>{diagram}{content}</div>"
            f"{foot}<aside class='notes'>{speaker}</aside><div class='pageno'>{n} / {len(drafts)}</div></section>"
        )
    template = (ROOT / "tools" / "deck_template.html").read_text(encoding="utf-8")
    out = template.replace("{{TITLE}}", html.escape(deck_title)).replace("{{SLIDES}}", "\n".join(slides))
    (d / "deck.html").write_text(out, encoding="utf-8")
    print(f"build_deck: {len(slides)} slides -> {(d / 'deck.html').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
