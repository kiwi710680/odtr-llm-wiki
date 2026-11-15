"""Self-test of the citation/number checker. Run: python tools/test_common.py"""
from common import check_citations_and_numbers as chk, source_pages

assert source_pages("williams2024") is not None
# Page 1 of williams2024 prints the volume number 193 and pages 1768.
assert chk("期刊卷號 193 [williams2024, p.1]") == [], chk("期刊卷號 193 [williams2024, p.1]")
assert any("not found" in p for p in chk("樣本 98765 人 [williams2024, p.1]"))
assert any("without a citation" in p for p in chk("樣本 98765 人"))
assert any("unknown source" in p for p in chk("x [nobody2020, p.1]"))
assert any("has no page" in p for p in chk("x [williams2024, p.99]"))
assert chk("分成 2 個階段，見 [[q-learning]]") != []  # number with no cite still flagged
assert chk("沒有數字的句子") == []
print("test_common: all assertions passed")
