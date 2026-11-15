---
title: 倒推遞迴與偽結局（backward recursion）
type: concept
sources: [bluemlein2022, williams2024, renson2025]
updated: 2026-11-15
---

# 倒推遞迴與偽結局（backward recursion）

## 直覺（生活比喻）

想像要在期末前排好一整學期的讀書計畫。你會先決定「考前最後一週」怎麼讀最有效，再回頭決定上一週，因為上一週讀什麼好，要看之後那一週打算怎麼讀。倒推遞迴就是這種「從終點往回排」的做法。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 倒推遞迴（backward recursion）是學習最佳 DTR 的動態規劃（dynamic programming）方法；論文引用 Murphy（2003）的研究。[bluemlein2022, p.6]
- 它處理兩個難題。第一，要同時考慮過去決定與當下決定的預後效果與延遲效果。第二，時間變動共變數依測量時間而定，可能既是干擾因子，也是治療效果的中介。[bluemlein2022, p.6]
- 因此，把治療後才量到的共變數也放進同一個模型，會因為「解釋掉」（explaining-away）治療效果而造成治療後偏誤（post-treatment bias）；論文說，對完整病史只配一個模型，會得到有偏的 DTR。[bluemlein2022, p.6]
- 做法：把連續決策拆成一組單步問題；每一步配一個結局模型來估計處理效應，再解出那一步的最佳決定。[bluemlein2022, p.6]
- 結局只在最後一步觀察到，所以每一步改為最佳化「偽結局」（pseudo-outcome）：假如病人在之後的時間步都被最佳治療，會有的潛在結局。[bluemlein2022, p.6]
- Algorithm 1 的流程：先把 DTR 設成資料中實際的治療序列，把偽結局設成觀察到的結局；然後 t 從 T 倒數到 1，每一步依序做五件事。[bluemlein2022, p.7]
  - 估計傾向分數。[bluemlein2022, p.7]
  - 用因果樹或因果森林估計處理效應。[bluemlein2022, p.7]
  - 處理效應為正就給治療，否則不給。[bluemlein2022, p.7]
  - 以代入原則（plug-in principle），把估計的最佳決定寫進 DTR。[bluemlein2022, p.7]
  - 更新偽結局：下一輪（前一個時間步）的偽結局，等於這一步的偽結局，再加上「實際治療與估計的最佳治療不同時」的處理效應。所以偽結局記錄的是最佳決定帶來的改善量。[bluemlein2022, p.7-8]

## 在各篇怎麼出現

### 在 bluemlein2022 中

- 這是 DTR-CT 與 DTR-CF 的骨架；五個基準方法也放在同一套遞迴裡，只是把每步估計處理效應的部分換掉。[bluemlein2022, p.12]
- 每一步都用「到該步為止的完整病史」估計處理效應。[bluemlein2022, p.12]

### williams2024

- 同樣從最後一個時間點往回做；每個時間點重複同樣步驟，並把「依最佳規則給治療」的預測值當作往前一個時間點的結局。[williams2024, p.5]
- 差別在每一步估計處理效應的工具：williams2024 用倍增穩健的無偏轉換再迴歸（見 [[doubly-robust-learner]]），bluemlein2022 用因果樹或因果森林（見 [[causal-tree-and-forest]]）。[williams2024, p.4] [bluemlein2022, p.7]

### renson2025

- 論文只討論二元治療與單一時間點的資料結構；倒推遞迴：來源未提及。[renson2025, p.2]

## 常見誤解

- 「倒推就是讓時間倒流」：倒的只是估計的順序，資料仍按時間記錄；原因是現在該怎麼決定，要考慮之後會採取哪些決定。[bluemlein2022, p.5]
- 「偽結局是真的觀察值」：只有最後一步用的是觀察到的結局；之前各步用的是在估計的最佳決定下算出的結局。[bluemlein2022, p.6-7]
- 「一個模型吃下整段病史就好」：論文說這樣會得到有偏的 DTR。[bluemlein2022, p.6]

## 相關頁面

- [[decision-points-and-history]]
- [[optimal-dynamic-treatment-rule]]
- [[blip-function]]
- [[causal-tree-and-forest]]
- [[q-learning-dwols-g-estimation]]
- [[doubly-robust-learner]]
- 來源頁：[[bluemlein2022]]、[[williams2024]]、[[renson2025]]
- 名詞速查：[[glossary]]
