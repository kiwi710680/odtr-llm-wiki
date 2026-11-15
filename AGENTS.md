# AGENTS.md — ODTR LLM Wiki

This folder is an LLM Wiki in the style of Karpathy's "LLM Wiki" idea: the agent reads raw
sources once, writes and maintains interlinked Markdown pages, and later answers questions or
builds teaching material from the wiki instead of from the raw PDFs. The requirements behind
every rule below are in `docs/01_interview.md` (agreed with the user before any file was made).

## 1. Purpose and reader

- Topic: optimal dynamic treatment regimes (ODTR / DTR) — learning "which treatment, for whom,
  at each decision point" from observational data.
- Reader: a classmate with no causal-inference background. Intuition first, terms second,
  formulas only when unavoidable. Every term page gives an everyday analogy.
- Language: Traditional Chinese. On first use in a page, write a term as 中文（English）.

## 2. Folder layout

```
raw/                 source PDFs (read-only, never edit)  — <id>.pdf
raw/text/            page-marked text, made by tools/extract_text.py — never hand-edit
wiki/index.md        catalogue: every page, one line each, grouped by type
wiki/log.md          append-only log: date | operation | pages touched | lint result
wiki/glossary.md     中文 / English / one-line definition / [[concept page]]
wiki/sources/<id>.md one page per raw source
wiki/concepts/*.md   cross-source concepts (kebab-case file names)
wiki/syntheses/*.md  comparisons across sources and disagreements
tools/               extract_text.py, lint_wiki.py, check_deck.py
.agents/workflows/   topic-slides.md (the slide-deck workflow)
topic-*/             one folder per slide-deck run (state files of that workflow)
docs/                interview, design notes, reflection
```

Source ids: `williams2024`, `bluemlein2022`, `hong2021`, `desman2025`, `renson2025`.

## 3. Page format

Every wiki page except `index.md` and `log.md` starts with this frontmatter:

```yaml
---
title: <中文標題>
type: source | concept | synthesis | glossary
sources: [<id>, ...]        # ids actually cited on this page
updated: YYYY-MM-DD
---
```

Source pages use these sections, in order: 一句話、研究問題、資料與情境、方法（直覺版）、
主要結果、限制、和其他頁的關係. Concept pages: 直覺（生活比喻）、定義、在各篇怎麼出現、
常見誤解、相關頁面.

## 4. Citation and link rules (checked by `tools/lint_wiki.py`)

- Cite as `[<id>, p.<N>]` or `[<id>, p.<N>-<M>]`, where N is the PDF page index (1-based), the
  same numbering as the `=== p.N ===` markers in `raw/text/<id>.txt`.
- Any line that states a number (a result, a sample size, a percentage, a year) carries a
  citation on the same line. The number must appear on a cited page of the cited source.
  Copy numbers exactly as the source prints them; do not round or convert.
- Do not write claims the sources do not make. If the sources do not say it, write
  「來源未提及」 rather than filling in from general knowledge.
- Link wiki pages as `[[file-stem]]` (no folder, no `.md`). Every page is listed in
  `index.md` and is linked from at least one other page besides `index.md`.
- Disagreements between sources: never pick a side. Put both, with each source's conditions,
  in `wiki/syntheses/disagreements.md`.

## 5. Operations

### Ingest (one source at a time)

1. Read `raw/text/<id>.txt` (all pages). Do not read other sources in the same ingest.
2. Write `wiki/sources/<id>.md`.
3. Create or update concept pages the source touches; add this source's angle to existing
   pages rather than duplicating them. Update `glossary.md` and the syntheses when the source
   compares to, or disagrees with, an already-ingested source.
4. Update `index.md`; append one line to `log.md`.
5. Run `python tools/lint_wiki.py`. Fix every error (at most 3 rounds). Only a clean lint may
   be committed: `git commit -m "ingest: <id>"`.

### Query

Answer from wiki pages only, citing the wiki pages (and through them the sources). If the
wiki does not cover the question, say so and name the missing source or page; do not answer
from memory. A good answer worth keeping may be filed as a new synthesis page.

### Lint

`python tools/lint_wiki.py` checks: broken links, pages missing from `index.md`, orphan
pages, frontmatter fields, unknown source ids or page numbers, lines with numbers but no
citation, and numbers not found on the cited page. Exit code 0 = pass.

### Teaching slide deck

Follow `.agents/workflows/topic-slides.md`. The deck may use only wiki content.

## 6. Do not

- Edit anything in `raw/`.
- Mix sources inside one ingest, or cite a page you did not read.
- Commit with a failing lint, or suppress a lint rule to make it pass.
