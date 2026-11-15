"""Extract page-marked text from each raw/<id>.pdf into raw/text/<id>.txt.

Page markers look like `=== p.3 ===` (1-based PDF page index), so wiki
citations [id, p.3] and the lint number check refer to the same pages.
Usage: python tools/extract_text.py
"""
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
OUT = RAW / "text"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for pdf in sorted(RAW.glob("*.pdf")):
        doc = fitz.open(pdf)
        parts = []
        for i, page in enumerate(doc, start=1):
            parts.append(f"=== p.{i} ===\n{page.get_text()}")
        (OUT / f"{pdf.stem}.txt").write_text("\n".join(parts), encoding="utf-8")
        print(f"{pdf.stem}: {doc.page_count} pages")


if __name__ == "__main__":
    main()
