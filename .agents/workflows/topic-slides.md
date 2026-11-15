# Workflow: /topic-slides — teaching HTML deck from the wiki (graph v2)

Changes from v1 (after the first real run, see `docs/run_notes.md`):
- **G4b term check moved forward** from the G5 AI review to a script at the draft node: a glossary
  term must be glossed or explained in the Note on the slide where it first appears.
- **Card subject rule** at N2: a claim names whose finding it is and its scope (which study, which
  population). Two of the G5 failures (wrong attribution, over-generalisation) started in cards.
- Draft length budget at N4: ≤5 bullets, each ≤ about 60 characters before the citation;
  explanations go to the Note.
- G5 reviews only slides changed since the last review.

v2.1 (after round 2): the G4b term rule made the drafter add explanations, and 5 of them were
textbook definitions the wiki does not contain (plus 1 that was wrong). So N4 may now also read
`wiki/glossary.md` and the concept pages of its claims, and **a gloss must be copied or condensed
from those pages** — the same "only from the wiki" rule as bullets. G5 checks glosses against them.

Input: a topic sentence. Output: `topic-<slug>/deck.html` + `topic-<slug>/report.md`.
Only wiki content may be used — never `raw/` and never general knowledge.
Every state is a file in `topic-<slug>/`, so each node can be opened, committed and re-run alone.

```
N1 retrieve ──► G1 coverage gate ──► N2 evidence cards (one per source, parallel)
                  │ <3 pages → STOP       │
                  ▼                       ▼
                                   G2 card check (script) ──fail──► redo that card only
                                          ▼
                                   N3 outline ──► G3 outline check (script) + HUMAN gate
                                          ▲            │ missing sub-topic → back to N1
                                          │            ▼
                                   N4 slide drafts (inner loop ≤2: write → check → fix)
                                          ▼
                                   G4 draft check (script) ──fail──► that slide only
                                          ▼
                                   G5 faithfulness review (fresh-context AI) ──fail──► that slide only
                                          ▼                                  (card wrong → back to N2 for that source)
                                   N5 render (build_deck.py, deterministic, may not change text)
                                          ▼
                                   G6 render check (overflow + text identical) ──fail──► N4 shorten that slide
                                          ▼
                                   N6 report.md ──► deliver
```

## Node contracts (what each node may read / must not do)

| Node | Reads only | Writes | Must not |
|---|---|---|---|
| N1 retrieve | `wiki/index.md`, page frontmatter | `sources.md` (pages + why) | read `raw/` |
| N2 cards | one source page + the concept/synthesis pages that cite that source | `cards/<id>.md` | mix in another source's claims |
| N3 outline | `cards/` | `outline.md` | add claims not on a card |
| N4 drafts | `outline.md` + the cards a slide is assigned (+ v2.1: `wiki/glossary.md` and concept pages, for glosses only) | `drafts/sNN.md` | cite anything outside its assigned claims; write a gloss the wiki does not support |
| G5 review | one draft + its claims' wiki pages | `review.md` | edit drafts itself |
| N5 render | passed drafts | `deck.html` | change a single word |
| G* checks | product + its sources | check output | fix things themselves |

## File formats

Card line: `- <id>-C<n>: <claim in 中文> [<id>, p.N] ← [[<wiki-page>]]`
(the citation must be copied from that wiki page; the claim restates that page's line).

Draft `drafts/sNN.md`:
```
---
slide: 3
title: <title>
layout: title | bullets | two-col | compare | quote
claims: [williams2024-C1, williams2024-C4]
---
- <bullet with citation [williams2024, p.3]>
Note: <speaker note, optional>
```
Lines with a number or a factual statement carry the citation of the claim they came from.

## Checks (scripts are the definition of done)

- G1 `python tools/check_deck.py <dir> sources` — at least 3 wiki pages; every source id covered.
- G2 `... cards` — card citations exist verbatim in the linked wiki page; numbers match raw pages.
- G3 `... outline` — 8–15 slides; every card used at least once (coverage); then the human
  confirms the outline.
- G4 `... drafts` — every slide has ≥1 citation; citations ⊆ assigned claims; numbers appear in
  the assigned claims; numbers found on the raw page.
- G4b (v2, same command) — every `wiki/glossary.md` term is glossed in （…） or named in the Note on
  the slide where it first appears.
- G5 fresh-context reviewer (a new agent that never saw the drafting): per slide PASS/FAIL on
  faithfulness to the cited wiki page and on "would a beginner understand this".
- G6 `... html` — every draft line's text appears in `deck.html`; then the browser overflow check
  (`window.deckOverflow()` in the rendered page) must return an empty list.

## Brakes

- Outer graph: a node may be sent back at most 3 times; then stop and report.
- Inner loop in N4: at most 2 fix rounds per slide.
- Fewer than 3 relevant wiki pages at G1: stop and say what to ingest.
- Fix only what the check report lists; do not rewrite passing slides.
