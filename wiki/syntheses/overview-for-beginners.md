---
title: 如果你只讀一頁：動態治療策略導覽
type: synthesis
sources: [williams2024, renson2025, bluemlein2022, hong2021, desman2025]
updated: 2026-11-15
---

# 如果你只讀一頁：動態治療策略導覽

這一頁把五篇來源與主要概念，依「先懂問題、再懂規則、再懂怎麼學、最後懂怎麼檢查」的順序串起來，每一步連到概念頁。內容只整理來源已寫的事；生活比喻與整理語句是本 wiki 的說明，不是論文的話，也不評斷誰對。

## 直覺（生活比喻）

把動態治療策略想成一個好的導航軟體：它不會一次規劃到底，而是每個路口都看「到目前為止走過的路與現在的路況」，再重新決定直走還是轉彎。學習這個導航，就是從很多人過去的行車紀錄，學出「在什麼路況該怎麼轉」。最後還要有辦法檢查：這個新導航真的比大家原本的走法好嗎？（比喻為本 wiki 的說明，不是論文的話。）

## 五篇來源一覽

| 來源 | 一句話 | 在這份導覽中的角色 |
|---|---|---|
| [[williams2024]] | 教學型論文：教應用研究者從追蹤多個時間點的資料，學出「每個決策時間點、對什麼樣的人、該不該給治療」的規則，範例是 BUP-NX 劑量。[williams2024, p.1] | 主幹：問題與基本詞彙 |
| [[renson2025]] | 教學型論文：教怎麼從統計估計目標一步步推導出可搭配機器學習、又有有效信賴區間的估計式。[renson2025, p.1] | 統計工具箱 |
| [[bluemlein2022]] | 方法論文：提出 DTR-CT 與 DTR-CF 兩個以因果樹與因果森林學最佳 DTR 的新方法。[bluemlein2022, p.1] | 可解釋的學習方法 |
| [[hong2021]] | 臨床應用：先以有限混合模型分類，再以 DTR 估計個人化的機械功率。[hong2021, p.1] | 連續劑量的加護病房案例 |
| [[desman2025]] | 臨床應用：用分布式離線強化學習建議心臟手術後每小時的胰島素劑量。[desman2025, p.1] | 強化學習路線的案例 |

## 閱讀順序

### 第一步：為什麼不能只看平均

- 平均處理效應只描述平均，沒有告訴我們治療對某一個人的效果。[williams2024, p.1]
- 治療常常是一連串的決定，所以要學的不只是「不同人受益不同」，還有「同一個人在情況變化時受益也不同」。[williams2024, p.1]
- 詳見 [[treatment-effect-heterogeneity]]。

### 第二步：規則是什麼

- 治療規則是一個函數：輸入治療前的變數，輸出要給的治療。靜態規則讓每個人拿到同一個治療；動態規則依個人已量測的病史而定。[williams2024, p.2]
- 有多個時間點時，每個時間點各有一條規則，每條規則都看到當時為止的病史。[williams2024, p.2]
- 治療可以是開關，也可以是連續的劑量：bluemlein2022 處理的是治療或不治療，hong2021 的劑量是機械功率，desman2025 的劑量是每小時的胰島素量。[bluemlein2022, p.4] [hong2021, p.3] [desman2025, p.9]
- 詳見 [[dynamic-treatment-regime]]、[[decision-points-and-history]]。

### 第三步：「最佳」是什麼意思

- 所有可能的動態規則中，讓族群受益最大的那一條稱為最佳動態治療規則；規則的價值，是依這條規則治療時反事實結局的期望值。[williams2024, p.2]
- 「最佳」是族群平均意義上的最佳；範例中學出的規則與預先指定的動態規則相比，論文說差異不具意義，所以沒有保證一定贏過臨床規則。[williams2024, p.6]
- 詳見 [[optimal-dynamic-treatment-rule]]。

### 第四步：從觀察資料學需要什麼前提

- 把「接受治療的反事實結局」寫成可由資料估計的量，需要三個假設：一致性、無未測量干擾（可交換性）與正值性。[williams2024, p.3]
- bluemlein2022 把前提寫成四個，多了一位病人的結局與其他病人的治療指派無關這一項，並把可交換性寫成每個時間步、以病史為條件的版本。[bluemlein2022, p.5]
- hong2021 與 desman2025 都沒有列出或討論這些假設：來源未提及。
- 詳見 [[identification-assumptions]]。

### 第五步：怎麼學出規則（三條路）

- 迴歸式與倍增穩健：先估 blip 函數，也就是兩種治療的結局差如何隨變數而變，為正就給治療。倍增穩健的意思是 Q 或 g 只要有一個被一致估計，就能得到無偏的 blip 估計。[williams2024, p.3] 詳見 [[blip-function]]、[[doubly-robust-learner]]。
- 古典的線性迴歸式方法（Q 學習、DWOLS、G 估計）來自統計學，假設函數形式已知、維度低。[bluemlein2022, p.22] 詳見 [[q-learning-dwols-g-estimation]]。
- 從最後一個時間點往回推：前面時間點的最佳決定，取決於後面的時間點之後會如何被最佳地決定。[williams2024, p.3] bluemlein2022 把這個倒推遞迴與因果樹、因果森林合在一起。[bluemlein2022, p.6] 詳見 [[backward-recursion]]、[[causal-tree-and-forest]]。
- 強化學習：代理在環境中採取行動，以最大化累積獎勵來學習決策；離線強化學習只從固定的資料集學；分布式強化學習看結果的整個分布，而不只看期望。[desman2025, p.2] 詳見 [[reinforcement-learning-mdp]]、[[offline-reinforcement-learning]]、[[distributional-reinforcement-learning]]。
- 先分類再估計：hong2021 先用有限混合模型把病人自動分類，再把類別放進估計規則的模型。[hong2021, p.1] [hong2021, p.3] 詳見 [[finite-mixture-subphenotypes]]。

### 第六步：統計工具箱（可以晚點讀）

- renson2025 教的是：為一個還沒有現成估計式的因果參數，推導出可搭配機器學習、又有有效推論的估計式；它只討論單一時間點，動態規則的學習來源未提及。[renson2025, p.1] [renson2025, p.2]
- 它的關鍵零件是有效影響函數與速率倍增穩健。[renson2025, p.1]
- 詳見 [[statistical-estimand]]、[[nuisance-functions]]、[[efficient-influence-function]]、[[plug-in-and-one-step-estimators]]、[[rate-double-robustness]]、[[cross-fitting]]。

### 第七步：怎麼檢查學出來的規則

- 有真值的模擬：看後悔值與決策準確度。[bluemlein2022, p.13] 真實資料沒有真值，改看期望增益。[bluemlein2022, p.16]
- hong2021 看實際機械功率偏離最佳值，與死亡的關聯。[hong2021, p.3]
- desman2025 用離線策略評估估計策略的報酬，並請專家比較建議的劑量、盲評安全性與有效性。[desman2025, p.9] [desman2025, p.5] [desman2025, p.6]
- 詳見 [[regret-and-decision-accuracy]]、[[off-policy-evaluation]]。
- 規則要不要「看得懂」：bluemlein2022 區分決策邏輯本身透明的可詮釋，與靠替代模型提供洞察的可說明；desman2025 以 SHAP 事後估計各特徵的貢獻。[bluemlein2022, p.2] [desman2025, p.10] 詳見 [[interpretability]]。

### 第八步：臨床案例並排

- 四個臨床情境（鴉片使用障礙的 BUP-NX 劑量、加護病房的開關式處置、機械功率、術後的胰島素劑量）在 [[dtr-clinical-applications]] 並排；方法差異整理在 [[method-comparison]]。名詞見 [[mechanical-power]]、[[glossary]]。[williams2024, p.4] [bluemlein2022, p.14] [hong2021, p.1] [desman2025, p.1]

## 讀結果時要記得的三件事（本 wiki 的整理）

- 「估計的最佳」不是「證明有效」：hong2021 說依 DTR 調整通氣是否改善死亡，還需要前瞻性試驗；desman2025 說回溯性的發現需要前瞻性研究與臨床試驗驗證。[hong2021, p.2] [hong2021, p.8] [desman2025, p.7]
- 關聯不是因果：hong2021 的結果以風險比與勝算比這類關聯估計呈現；desman2025 的離線估計報酬是對自己建議的估計，不是觀察到的病人結局。[hong2021, p.4] [desman2025, p.2]
- 看有沒有外部資料：hong2021 的外部資料驗證來源未提及；desman2025 另用 eICU-CRD 做外部驗證。[desman2025, p.2]

## 相關頁面

- [[method-comparison]]
- [[dtr-clinical-applications]]
- [[glossary]]
- 來源頁：[[williams2024]]、[[renson2025]]、[[bluemlein2022]]、[[hong2021]]、[[desman2025]]
