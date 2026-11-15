# 執行紀錄（邊做邊記，反思用）

## Wiki ingest（一次一篇，lint 全過才 commit）

| # | 來源 | lint 執行次數 | 錯誤 | 原因與修正 | commit |
|---|---|---|---|---|---|
| 1 | williams2024 | 2 | 第 1 次 1 個 `[cites/numbers]`：`dynamic-treatment-regime.md:27 number(s) ['1'] without a citation`（「Table 1 的四個情境」那行沒附出處） | 補 `[williams2024, p.2]` | `ingest: williams2024` |
| 2 | renson2025 | 1 | 0 | — | `ingest: renson2025` |
| 3 | bluemlein2022 | 1 | 0 | ingest agent 先讀了 lint 原始碼才寫，所以一次過；但它也因此發現 lint 的兩個漏洞（見下） | `ingest: bluemlein2022` |

| 4 | hong2021 | 1 | 0 | agent 另寫交叉檢查（含個位數）抓到 1 行出處頁不對（「小於 1」只引 p.8，補 p.4）；Table 1 欄位用加總驗證 | `ingest: hong2021` |

| 5 | desman2025 | 2（首次 PASS 在第 2 次） | 第 1 次 1 個 `[cites/numbers]`：`desman2025.md:67 number(s) ['95', '95'] without a citation`（表頭寫「（95% CI）」沒出處） | 表頭改成「（信賴區間）」，上一句已有出處 | `ingest: desman2025` |

另外 agent 自己發現並改掉一處**說法過頭**：把 bluemlein2022 寫成「把強化學習視為多為黑箱的路線」，
原文只說「多以深度學習為基礎、不易解釋」。這種「沒有數字的扭曲」lint 完全看不到 → 簡報流程需要 AI 審查關卡。

### lint 本身的錯（第 3 篇 ingest 時發現，已修）
- **數字黏在中文字旁就不被檢查**：`NUM_RE` 用 `\w` 當邊界，而 Python 把中文字也算 `\w`，
  所以「共8059人」這種寫法完全躲過「數字要有出處」檢查。改成只用 ASCII 邊界，加測試
  `共98765人 → 必須報錯`。修完重跑整個 wiki（23 頁）：仍 0 錯（前兩篇剛好都有空格或有出處）。
- **PDF 抽出的「5, 000」被拆成兩個數字**：只比對到「000」。正規化改成把「逗號＋空格＋三位數」併回去，
  加測試 `N = 5, 000 → 5000`、`2, 3 → 2 和 3`。
- 教訓：檢查腳本本身也需要測試；「ingest agent 先讀 lint 再寫」會讓 lint 很難抓到錯，
  反而是它回報的「我怎麼繞過」最有價值 → 之後每篇 brief 都要求回報「lint 抓不到的地方」。

### ingest 時發現、但 lint 抓不到的問題
- renson2025 的公式全放在行內程式碼（反引號）裡，lint 會先把反引號內容移除再找數字 →
  公式裡的數字（例如收斂速率的次方）**沒有被程式檢查**，只靠 ingest agent 自己對 PDF。
  → 決定：簡報不放公式（讀者是外行），所以這個漏洞不會流進簡報；記為已知限制。
- 第 2 篇 ingest 後，第 1 篇來源頁仍寫著「目前只 ingest 了這一篇」→ 舊頁面的交叉引用會過期。
  lint 不檢查「內容過期」。人工修正，並在之後的 ingest brief 允許 agent 更新其他來源頁的
  「和其他頁的關係」一節。
