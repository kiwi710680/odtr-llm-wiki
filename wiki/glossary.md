---
title: 術語表
type: glossary
sources: [williams2024]
updated: 2026-11-15
---

# 術語表

每列：中文 ／ English ／ 一句話定義 ／ 詳見頁面。定義只依據已 ingest 的來源；目前來源：[[williams2024]]。

| 中文 | English | 一句話定義 | 詳見 |
|---|---|---|---|
| 治療規則 | treatment rule | 把治療前變數 V 對應到要給的治療 A 的函數。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 靜態規則 | static rule | 每個人都拿到同一個治療值。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 動態規則 | dynamic rule | 治療依個人已量測的病史而定。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 病史 | history | 到某次治療之前的所有變數紀錄，記為 Ht。[williams2024, p.3] | [[decision-points-and-history]] |
| 決策時間點 | decision point | 病人可以選擇要不要接受（或加量）治療的離散時間點。[williams2024, p.2] | [[decision-points-and-history]] |
| 最佳動態治療規則 | optimal dynamic treatment rule（ODTR） | 在所有可能規則中，讓反事實結局期望值最大（或最小）的規則。[williams2024, p.2] | [[optimal-dynamic-treatment-rule]] |
| 反事實結局 | counterfactual outcome | 若治療依某規則指派，結局會有的假想值。[williams2024, p.2] | [[optimal-dynamic-treatment-rule]] |
| 平均處理效應 | average treatment effect（ATE） | 全部的人都接受治療相對全部不接受時，結局的平均差。[williams2024, p.1] | [[treatment-effect-heterogeneity]] |
| 處理效應異質性 | treatment effect heterogeneity | 平均有益的治療仍可能使有些人受益、有些人受害。[williams2024, p.1] | [[treatment-effect-heterogeneity]] |
| 條件平均處理效應 | conditional average treatment effect（CATE） | 在 V 條件下兩種治療的結局差，常稱 blip 函數。[williams2024, p.3] | [[blip-function]] |
| Blip 函數 | blip function | CATE 的別名，是迴歸式學出最佳規則的關鍵成分。[williams2024, p.3] | [[blip-function]] |
| 無偏轉換 | unbiased transformation | 資料的函數，其在 V 條件下的期望值等於 blip。[williams2024, p.3] | [[doubly-robust-learner]] |
| 增強型逆機率加權 | augmented inverse probability weighting（AIPW） | 論文採用的倍增穩健無偏轉換。[williams2024, p.3] | [[doubly-robust-learner]] |
| 倍增穩健 | doubly robust | Q 或 g 只要有一個被一致估計，就能得到無偏的 blip 估計。[williams2024, p.3] | [[doubly-robust-learner]] |
| 傾向分數 | propensity score | 實際拿到所觀察到治療的機率，論文中記為 g(A, H)。[williams2024, p.3] | [[doubly-robust-learner]] |
| Q 學習 | Q-learning | 以條件平均處理效應迴歸為基礎的 ODTR 估計方法之一。[williams2024, p.3] | [[optimal-dynamic-treatment-rule]] |
| 超級學習器 | super learner | 以另一個演算法（元學習器）組合一組使用者指定學習器的預測。[williams2024, p.5] | [[doubly-robust-learner]] |
| 交叉擬合 | cross-fitting | 範例中用來估計 Q 與 g 的做法，論文在別處以樣本分割說明可避開平滑性要求。[williams2024, p.5] | [[doubly-robust-learner]] |
| 一致性 | consistency | 觀察到的治療水準下，反事實結局就是實際觀察到的結局。[williams2024, p.3] | [[identification-assumptions]] |
| 可交換性（無未測量干擾） | exchangeability（no unmeasured confounding） | 所有同時影響暴露與結局的共同原因都已測量並調整。[williams2024, p.3] | [[identification-assumptions]] |
| 正值性 | positivity | 在所有層內，各治療水準出現的機率都不為零。[williams2024, p.3] | [[identification-assumptions]] |
| 回到規律鴉片使用 | return to regular opioid use（RROU） | 論文範例的結局，定義見來源頁。[williams2024, p.5] | [[williams2024]] |
| 鴉片使用障礙 | opioid use disorder（OUD） | 論文範例的疾病情境。[williams2024, p.1] | [[williams2024]] |
| 丁基原啡因加納洛酮 | buprenorphine-naloxone（BUP-NX） | 論文範例中被調整劑量的藥物。[williams2024, p.1] | [[williams2024]] |
