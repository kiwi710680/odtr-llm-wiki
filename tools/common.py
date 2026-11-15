"""Shared helpers for lint_wiki.py and check_deck.py."""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_TEXT = ROOT / "raw" / "text"
WIKI = ROOT / "wiki"

# [williams2024, p.3] or [williams2024, p.3-4] or [williams2024, pp.3-4]
CITE_RE = re.compile(r"\[([a-z]+\d{4}),\s*pp?\.\s*(\d+)(?:\s*[-–]\s*(\d+))?\]")
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
# A "number" = digits with optional decimal part, not part of a word like "p3" or "k=2" ids.
NUM_RE = re.compile(r"(?<![\w.])(\d+(?:[.,]\d+)*)(?![\w])")


@lru_cache(maxsize=None)
def source_pages(src_id: str) -> dict[int, str] | None:
    """Return {page_number: normalised text} for a source, or None if the id is unknown."""
    path = RAW_TEXT / f"{src_id}.txt"
    if not path.exists():
        return None
    pages: dict[int, str] = {}
    chunks = re.split(r"^=== p\.(\d+) ===$", path.read_text(encoding="utf-8"), flags=re.M)
    for i in range(1, len(chunks), 2):
        pages[int(chunks[i])] = normalise(chunks[i + 1])
    return pages


def normalise(text: str) -> str:
    text = text.replace("−", "-").replace(" ", " ").replace(" ", " ")
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text)  # 1,234 -> 1234
    text = re.sub(r"(?<=\d) (?=\d{3}\b)", "", text)  # 1 234 -> 1234
    text = re.sub(r"(?<=\d)\s*\.\s*(?=\d)", ".", text)  # "0. 5" -> "0.5"
    return text


def strip_markup(line: str) -> str:
    """Remove citations, wiki links, inline code and URLs before looking for numbers."""
    line = CITE_RE.sub(" ", line)
    line = LINK_RE.sub(" ", line)
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"https?://\S+", " ", line)
    line = re.sub(r"\b[a-z]+\d{4}\b", " ", line)  # bare source ids
    return line


def numbers_in(line: str) -> list[str]:
    nums = []
    for m in NUM_RE.finditer(strip_markup(line)):
        n = re.sub(r"(?<=\d),(?=\d{3})", "", m.group(1))
        nums.append(n)
    return nums


def needs_source_match(num: str) -> bool:
    """Single-digit integers (counts like 2 個階段) are too common to match against a page."""
    return not (num.isdigit() and len(num) == 1)


def number_on_pages(num: str, src_id: str, first: int, last: int) -> bool:
    pages = source_pages(src_id)
    if pages is None:
        return False
    variants = {num}
    if num.startswith("0."):
        variants.add(num[1:])  # 0.5 printed as .5
    pat = re.compile(r"(?<![\d])(" + "|".join(re.escape(v) for v in variants) + r")(?![\d])")
    return any(pat.search(pages.get(p, "")) for p in range(first, last + 1))


def check_citations_and_numbers(line: str) -> list[str]:
    """Problems for one line: unknown ids/pages, numbers without citation, numbers not found."""
    problems = []
    cites = [(m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))) for m in CITE_RE.finditer(line)]
    for src, a, b in cites:
        pages = source_pages(src)
        if pages is None:
            problems.append(f"unknown source id '{src}'")
        elif a < 1 or b > max(pages) or a > b:
            problems.append(f"{src} has no page p.{a}-{b} (it has {max(pages)} pages)")
    nums = numbers_in(line)
    if nums and not cites:
        problems.append(f"number(s) {nums} without a citation on the same line")
    elif nums:
        for n in nums:
            if not needs_source_match(n):
                continue
            if not any(number_on_pages(n, s, a, b) for s, a, b in cites):
                problems.append(f"number '{n}' not found on the cited page(s) {[f'{s} p.{a}-{b}' for s, a, b in cites]}")
    return problems
