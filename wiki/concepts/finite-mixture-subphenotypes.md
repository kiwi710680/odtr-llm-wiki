---
title: 有限混合模型與表型（subphenotypes）
type: concept
sources: [hong2021, bluemlein2022]
updated: 2026-11-15
---

# 有限混合模型與表型（subphenotypes）

## 直覺（生活比喻）

水果攤老闆不看標籤，只看大小、顏色與軟硬，把一大堆水果自動堆成幾堆：同一堆內部很像，不同堆之間差很多。有限混合模型就是讓電腦做這件事，只是「要分成幾堆」要自己決定，而且每顆水果屬於哪一堆是用「機率」表示的。分出來的每一堆，在醫學上就叫一個「表型」或「亞型」。這個比喻是本 wiki 的說明，不是論文的話。

## 定義

- 有限混合模型（finite mixture modeling, FMM）：論文說它也稱為潛在剖面分析（latent profile analysis, LPA），用來找出 ARF 病人的類別。[hong2021, p.2]
- 論文在討論處把這個分類稱為非監督式機器學習演算法的應用；FMM 實際輸入了哪些變數、有沒有用到 MP 或死亡：來源未提及。[hong2021, p.5]
- 論文的用詞：類別（class）、表型（phenotype）、亞型（subtype）。[hong2021, p.1] [hong2021, p.2]
- 怎麼決定要分成幾類：由模型適配統計與臨床意義共同決定；用 bootstrap 概似比檢定比較 k 類與 k 減 1 類模型；AIC 與 SABIC 越低、entropy 越高越好；最小類別的比例須大於 10%；歸入某一類的最小機率須大於 0.85；最後用 k-means 分群確認。[hong2021, p.2]
- 論文的結果是 3 類：AIC 與 SABIC 從 2 類一路降到 10 類，沒有自己停在 3 類；4 類到 10 類的最小類別都不到 5% 的病人，entropy 指向 3 類。[hong2021, p.3-4]
- 論文說這個分類是可詮釋的，因為每一類對應一種臨床表型；這些類別無法完全由 COPD、ARDS、心衰竭或 sepsis 等傳統原因解釋。[hong2021, p.5-6]

| 類別 | 論文的稱呼 | 論文描述的特徵 | 出處 |
|---|---|---|---|
| Class 1 | Baseline Class（基線類） | 最大的一類，各變數接近平均。 | [hong2021, p.4] |
| Class 2 | Critical Class（危急類） | 代謝性酸中毒與組織灌流差；討論處稱為系統性組織低灌流與多重器官功能障礙。 | [hong2021, p.4] [hong2021, p.5] |
| Class 3 | Refractory Respiratory Failure Class（頑固性呼吸衰竭類） | 即使在通氣下仍有高 PaCO2 與低 PF，其他器官功能相對正常。 | [hong2021, p.4] [hong2021, p.6] |

## 在各篇怎麼出現

### 在 hong2021 中

- 分類是整個研究的第一步，之後類別被當成「會改變 MP 效果的變數」：Cox 迴歸裡有類別與 MP 的交互作用，DTR 的 blip 函數中類別也和 MP 交互。見 [[treatment-effect-heterogeneity]]、[[blip-function]]。[hong2021, p.2] [hong2021, p.3]
- 結果：MP_static 每增加 5 Joules/min 的死亡風險比，Class 1 最小（1.29），Class 3 最大（1.83）。這是觀察性資料的關聯估計。[hong2021, p.4]
- 類別會隨通氣天數改變：從 Class 2 轉到 Class 1 的病人較可能存活到出院，Class 3 維持不變；論文用這點說明策略必須隨病況調整，見 [[decision-points-and-history]]。[hong2021, p.4] [hong2021, p.5] [hong2021, p.7]
- 對照 bluemlein2022（本 wiki 的整理）：因果樹用專為處理效應設計的分裂準則分群，分群時就在看處理效應；hong2021 稱 FMM 為非監督式方法，分好類之後才檢查 MP 的效果是否隨類別而不同。[bluemlein2022, p.8] [hong2021, p.5]

## 常見誤解

- 「分成 3 類是唯一客觀的答案」：論文說 AIC 與 SABIC 一路下降，不會自己停在 3 類；最後靠 entropy、最小類別的比例與臨床意義決定，並用 k-means 確認。[hong2021, p.3] [hong2021, p.2]
- 「類別就是診斷」：論文說這些類別無法完全由傳統診斷解釋，而且病人的類別會隨時間改變。[hong2021, p.5-6] [hong2021, p.4]
- 「類別是治療造成的」：論文描述 Class 3 是即使在通氣下仍有高 PaCO2 與低 PF，沒有說這是通氣造成的。[hong2021, p.4]
- 「這三類在別的醫院、別的資料庫也會出現」：來源未提及；論文只用一個資料庫。[hong2021, p.2]
- 本 wiki 的觀察（不是論文的話）：方法段設的最小類別比例下限是大於 10%，而 Class 3 在第 0 小時有 759 位、占 8768 位的比例不到十分之一；論文沒有說明比例的分母，所以不能判斷是否違反自己的準則。[hong2021, p.2] [hong2021, p.4]

## 相關頁面

- [[treatment-effect-heterogeneity]]
- [[blip-function]]
- [[decision-points-and-history]]
- [[causal-tree-and-forest]]
- [[mechanical-power]]
- 來源頁：[[hong2021]]
- 名詞速查：[[glossary]]
