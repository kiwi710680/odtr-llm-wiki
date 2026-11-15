---
title: 因果樹與因果森林（causal tree / causal forest）
type: concept
sources: [bluemlein2022, williams2024]
updated: 2026-11-15
---

# 因果樹與因果森林（causal tree / causal forest）

## 直覺（生活比喻）

把全班同學分成幾個小組：同一組的人背景相似，不同組的人對「補習有沒有用」的反應差很多；接著在每一組內，比較有補習與沒補習的平均成績差，這就是那一組的補習效果。這就是因果樹。因果森林則像請很多位老師各自分組，再對某位同學看「哪些同學常和他被分在同一組」，用這些「鄰居」的平均來估他的補習效果。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 因果樹（causal tree，Athey 與 Imbens 2016）與因果森林（causal forest）是估計異質處理效應（HTE）的方法，原本為靜態（單一時間點）設定設計，論文說它們尚未被用來學最佳 DTR。[bluemlein2022, p.3]
- 與一般的 CART 或隨機森林不同：後者沒有明確建模因果效應；因果樹以量身訂做的分裂準則，直接估計有因果解釋的 HTE。[bluemlein2022, p.3-4]
- 分裂準則：獎勵「葉子內處理效應相近、葉子之間處理效應不同」的分群方式。[bluemlein2022, p.8]
- 誠實分割（honest splitting）：把資料分成訓練集（用來決定怎麼分群，即模型選擇）與估計集（用來估計每個葉子的效應，即模型估計），兩者不重疊；目的是確保無偏並避免過度配適。[bluemlein2022, p.8]
- 葉子的處理效應：該葉內治療組與未治療組的平均結局之差，結局先以逆傾向分數加權。[bluemlein2022, p.9]
- 因果森林：許多棵因果樹的集成，像自適應的最近鄰估計式；某位病人的 HTE 不是簡單平均，而是對局部鄰域的加權平均，權重是其他病人與他落在同一片葉子的頻率。[bluemlein2022, p.9-10]
- 森林版也遵守誠實原則：結局與傾向分數以「袋外」（out-of-bag）方式預測，不用該病人自己的資料。[bluemlein2022, p.9]

## 在各篇怎麼出現

### 在 bluemlein2022 中

- DTR-CT 用單棵因果樹，DTR-CF 用因果森林，各自放在倒推遞迴的每一個時間步（見 [[backward-recursion]]）。[bluemlein2022, p.6]
- 設定：DTR-CT 以 50 % 訓練、50 % 估計；每片葉子的治療與對照病人合計至少 20 位（各 10 位）；分裂用的桶最多 20 個；5 折交叉驗證決定剪枝。DTR-CF 每個時間步用 500 棵樹。[bluemlein2022, p.24]
- 論文說這兩個方法的優勢，是不必假設關係已知，也不必假設所有病人由同一組變數決定治療。[bluemlein2022, p.17]
- 敏感度：葉子最小人數在 10 到 70 之間變動，結果變化很小。[bluemlein2022, p.14]
- 作者也推測樹與森林會自動偵測要控制哪些共變數，因此可能比線性模型更不受未測量干擾影響；這是推測，沒有直接檢驗。[bluemlein2022, p.25]

### williams2024

- 論文提到可以用決策樹估計 blip 函數 B(V)，得到好解讀的決策規則；因果樹的分裂準則與誠實分割：本 wiki 的 williams2024 頁未記載。[williams2024, p.4]

### renson2025

- 來源未提及因果樹或因果森林。

## 常見誤解

- 「因果樹就是一般決策樹」：論文把 CART 當成基準，並說它不是為了估計因果 HTE 而設計的。[bluemlein2022, p.12]
- 「樹分出來的群組一定有因果意義」：論文的識別仍需要假設（例如序列可交換性），見 [[identification-assumptions]]。[bluemlein2022, p.6]
- 「森林就不能解釋」：論文用變數重要性解釋 DTR-CF，並在自己的用詞下稱 DTR-CF 為「可說明」（explainable）、DTR-CT 為「可詮釋」（interpretable），見 [[interpretability]]。[bluemlein2022, p.2] [bluemlein2022, p.11]

## 相關頁面

- [[blip-function]]
- [[treatment-effect-heterogeneity]]
- [[cross-fitting]]
- [[interpretability]]
- [[backward-recursion]]
- [[q-learning-dwols-g-estimation]]
- 來源頁：[[bluemlein2022]]、[[williams2024]]
- 名詞速查：[[glossary]]
