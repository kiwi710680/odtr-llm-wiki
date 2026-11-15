"""Checks for the /topic-slides workflow (.agents/workflows/topic-slides.md).

Usage: python tools/check_deck.py <topic-dir> <stage>
  stage = sources | cards | outline | drafts | html | all
Exit code 0 = pass. Each problem is printed as `<file>: [<stage>] <problem>`.
"""
from __future__ import annotations

import html as htmllib
import re
import sys
from pathlib import Path

from common import CITE_RE, LINK_RE, ROOT, WIKI, RAW_TEXT, check_citations_and_numbers, numbers_in

CLAIM_RE = re.compile(r"^- ([a-z]+\d{4}-C\d+):\s*(.+)$")
ALL_SOURCES = sorted(p.stem for p in RAW_TEXT.glob("*.txt"))
WIKI_PAGES = {p.stem: p for p in WIKI.rglob("*.md")}


def front(text: str) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    meta: dict[str, str] = {}
    if lines and lines[0].strip() == "---":
        end = lines.index("---", 1)
        for raw in lines[1:end]:
            if ":" in raw:
                k, v = raw.split(":", 1)
                meta[k.strip()] = v.strip()
        lines = lines[end + 1:]
    return meta, lines


def check_sources(d: Path) -> list[str]:
    f = d / "sources.md"
    if not f.exists():
        return ["sources.md: [sources] missing"]
    pages = [p for p in LINK_RE.findall(f.read_text(encoding="utf-8"))]
    errs = [f"sources.md: [sources] unknown wiki page [[{p}]]" for p in pages if p not in WIKI_PAGES]
    good = [p for p in pages if p in WIKI_PAGES]
    if len(set(good)) < 3:
        errs.append(f"sources.md: [sources] only {len(set(good))} relevant wiki pages (<3) -> STOP")
    covered = set()
    for p in good:
        meta, _ = front(WIKI_PAGES[p].read_text(encoding="utf-8"))
        covered |= set(re.findall(r"[a-z]+\d{4}", meta.get("sources", "")))
    for s in ALL_SOURCES:
        if s not in covered:
            errs.append(f"sources.md: [sources] source '{s}' not covered by any selected page")
    return errs


def load_claims(d: Path) -> dict[str, tuple[str, str]]:
    """claim id -> (claim text, card file name)."""
    claims = {}
    for card in sorted((d / "cards").glob("*.md")):
        for line in card.read_text(encoding="utf-8").splitlines():
            m = CLAIM_RE.match(line.strip())
            if m:
                claims[m.group(1)] = (m.group(2), card.name)
    return claims


def check_cards(d: Path) -> list[str]:
    errs = []
    cards = sorted((d / "cards").glob("*.md"))
    if not cards:
        return ["cards/: [cards] no cards"]
    for card in cards:
        n = 0
        for line in card.read_text(encoding="utf-8").splitlines():
            m = CLAIM_RE.match(line.strip())
            if not m:
                continue
            n += 1
            cid, body = m.groups()
            where = f"cards/{card.name}: {cid}"
            if not cid.startswith(card.stem + "-"):
                errs.append(f"{where}: [cards] claim id does not belong to card '{card.stem}'")
            links = LINK_RE.findall(body)
            cites = [c.group(0) for c in CITE_RE.finditer(body)]
            if not links or not cites:
                errs.append(f"{where}: [cards] needs a citation and a ← [[wiki-page]]")
                continue
            page = links[-1]
            if page not in WIKI_PAGES:
                errs.append(f"{where}: [cards] wiki page [[{page}]] does not exist")
                continue
            ptext = WIKI_PAGES[page].read_text(encoding="utf-8")
            norm = lambda s: re.sub(r"\s+", "", s)
            for c in cites:
                if norm(c) not in norm(ptext):
                    errs.append(f"{where}: [cards] citation {c} does not appear in [[{page}]]")
                if not c.startswith(f"[{card.stem},"):
                    errs.append(f"{where}: [cards] cites another source {c} (one card = one source)")
            for num in numbers_in(body):
                if num not in ptext:
                    errs.append(f"{where}: [cards] number '{num}' is not in [[{page}]]")
            errs += [f"{where}: [cards] {p}" for p in check_citations_and_numbers(body)]
        if n == 0:
            errs.append(f"cards/{card.name}: [cards] no claims in the expected format")
    return errs


def outline_rows(d: Path) -> list[tuple[str, str, list[str]]]:
    rows = []
    for line in (d / "outline.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- (s\d{2}) \| (.+?) \|.*claims:\s*(.*)$", line.strip())
        if m:
            rows.append((m.group(1), m.group(2), re.findall(r"[a-z]+\d{4}-C\d+", m.group(3))))
    return rows


def check_outline(d: Path) -> list[str]:
    if not (d / "outline.md").exists():
        return ["outline.md: [outline] missing"]
    errs = []
    rows = outline_rows(d)
    claims = load_claims(d)
    if not 8 <= len(rows) <= 15:
        errs.append(f"outline.md: [outline] {len(rows)} slides (need 8-15)")
    used = set()
    for sid, _, cl in rows:
        for c in cl:
            if c not in claims:
                errs.append(f"outline.md: [outline] {sid} uses unknown claim {c}")
            used.add(c.split("-C")[0])
    for card in (d / "cards").glob("*.md"):
        if card.stem not in used:
            errs.append(f"outline.md: [outline] card '{card.stem}' is never used (coverage)")
    return errs


def draft_files(d: Path) -> list[Path]:
    return sorted((d / "drafts").glob("s*.md"))


def check_drafts(d: Path) -> list[str]:
    errs = []
    claims = load_claims(d)
    files = draft_files(d)
    if not files:
        return ["drafts/: [drafts] no drafts"]
    for f in files:
        meta, body = front(f.read_text(encoding="utf-8"))
        where = f"drafts/{f.name}"
        assigned = re.findall(r"[a-z]+\d{4}-C\d+", meta.get("claims", ""))
        missing = [c for c in assigned if c not in claims]
        if missing:
            errs.append(f"{where}: [drafts] unknown claims {missing}")
        allowed_cites = set()
        allowed_text = ""
        for c in assigned:
            if c in claims:
                allowed_text += claims[c][0]
                allowed_cites |= {re.sub(r"\s+", "", m.group(0)) for m in CITE_RE.finditer(claims[c][0])}
        n_cites = 0
        for i, line in enumerate(body, 1):
            if not line.strip():
                continue
            cites = [re.sub(r"\s+", "", m.group(0)) for m in CITE_RE.finditer(line)]
            n_cites += len(cites)
            for c in cites:
                if c not in allowed_cites:
                    errs.append(f"{where}:{i}: [drafts] citation {c} is not on an assigned claim")
            for num in numbers_in(line):
                if len(num) > 1 and num not in allowed_text:
                    errs.append(f"{where}:{i}: [drafts] number '{num}' is not in the assigned claims")
            errs += [f"{where}:{i}: [drafts] {p}" for p in check_citations_and_numbers(line)]
        if meta.get("layout") != "title" and n_cites == 0:
            errs.append(f"{where}: [drafts] no citation on a content slide")
    return errs


def visible_text(line: str) -> str:
    line = re.sub(r"^Note:\s*", "", line.strip())
    line = re.sub(r"^[-*]\s+|^\d+\.\s+|^>\s*|^#+\s*", "", line)
    line = CITE_RE.sub("", line)
    line = LINK_RE.sub(lambda m: m.group(1), line)
    line = re.sub(r"\*\*|__|`", "", line)
    return re.sub(r"\s+", "", line)


def check_html(d: Path) -> list[str]:
    f = d / "deck.html"
    if not f.exists():
        return ["deck.html: [html] missing"]
    raw = f.read_text(encoding="utf-8")
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    text = re.sub(r"\s+", "", htmllib.unescape(re.sub(r"<[^>]+>", "", raw)))
    errs = []
    for df in draft_files(d):
        meta, body = front(df.read_text(encoding="utf-8"))
        for i, line in enumerate(body, 1):
            if line.strip().startswith("|"):
                cells = [visible_text(c) for c in line.strip().strip("|").split("|")]
                parts = [c for c in cells if c and not re.fullmatch(r"[-:]+", c)]
            else:
                parts = [visible_text(line)]
            for p in parts:
                if p and p not in text:
                    errs.append(f"deck.html: [html] text of drafts/{df.name}:{i} changed or missing: '{p[:40]}'")
        if visible_text(meta.get("title", "")) not in text:
            errs.append(f"deck.html: [html] title of drafts/{df.name} missing")
    return errs


STAGES = {"sources": check_sources, "cards": check_cards, "outline": check_outline,
          "drafts": check_drafts, "html": check_html}


def main() -> int:
    d = (ROOT / sys.argv[1]).resolve()
    stage = sys.argv[2]
    stages = list(STAGES) if stage == "all" else [stage]
    errs = []
    for s in stages:
        errs += STAGES[s](d)
    for e in errs:
        print(e)
    print(f"check_deck {stage}: {len(errs)} error(s) -> {'PASS' if not errs else 'FAIL'}")
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.exit(main())
