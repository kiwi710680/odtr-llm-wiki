---
title: 倍增穩健學習器（從資料學出規則的方法）
type: concept
sources: [williams2024]
updated: 2026-11-15
---

# 倍增穩健學習器（從資料學出規則的方法）

## 直覺（生活比喻）

請兩位預報員各自預測明天會不會下雨：一位看氣象雲圖（預測結局），一位看過去的天氣紀錄推測今天為什麼是這個天氣（預測誰拿到哪種治療）。「倍增穩健」（doubly robust）的意思是：只要兩位之中有一位夠準，最後的結論就大致可靠。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 論文描述的是一個非參數、倍增穩健、以迴歸為基礎的方法，稱為 DR 估計式（DR estimator）或 DR 學習器（DR learner）。[williams2024, p.1-3]
- 核心概念是無偏轉換（unbiased transformation）：資料的函數 D(O) 在 V 條件下的期望值等於 [[blip-function]] B(V)。[williams2024, p.3]
- 論文用的是增強型逆機率加權（augmented inverse probability weighting, AIPW）轉換。除了結局迴歸 Q(H, A)，還要估計實際拿到所觀察到治療的機率 g(A, H)。[williams2024, p.3]
- 倍增穩健的意思：Q 或 g 只要有一個被一致地估計，就能得到 B(V) 的無偏估計。[williams2024, p.3]
- 這個性質也讓分析者能用彈性的資料自適應演算法來配模型，並以標準統計理論做推論。[williams2024, p.3]
- 單一時間點的步驟（Algorithm 1）：用 H 與 A 迴歸 Y，用 H 迴歸 A 得到 g；把 A 分別設為 1 與 0 預測 Q；組成 AIPW 轉換值；再把轉換值對 V 迴歸得到 blip 估計；預測為正就給治療。[williams2024, p.4]
- 多個時間點（Algorithm 2）：從最後一個時間點倒著做；每個時間點重複上述步驟，並把「依最佳規則給治療」的預測值當作下一輪往前一個時間點的結局。[williams2024, p.5]
- 論文說，各步迴歸都可以用資料自適應的機器學習演算法，在維持有效統計推論下增加模型彈性。[williams2024, p.4]

## 在各篇怎麼出現

### williams2024

- 範例中 Q 與 g 的估計用交叉擬合與離散超級學習器；候選學習器包含 lasso（ℓ1 正規化）、多變量適應性迴歸樣條、梯度提升；元學習器採「贏者全拿」，選交叉驗證均方誤差最小的學習器。[williams2024, p.5]
- blip 的估計用 ℓ1 正規化；最佳規則下的平均結局用依序倍增穩健（sequentially doubly robust）估計式，並使用相同的超級學習器候選庫。[williams2024, p.5]
- 論文指出，另一類做法是分類式方法（outcome-weighted learning 等）；在各自假設成立時，所有提到的演算法在漸近上都是一致的，但有限樣本表現可能不同。[williams2024, p.6]
- 論文提供的 R 套件在 GitHub 上可下載，並以有限的模擬研究確認實作正確。[williams2024, p.4]
- 一致估計最佳規則下的平均結局另需額外條件，見 [[identification-assumptions]]；其中一個條件是這些被估計的函數「夠平滑」，但可以用樣本分割（sample-splitting）繞過。[williams2024, p.4]

## 常見誤解

- 「倍增穩健就是不會錯」：它只要求 Q 與 g 其中一個被一致地估計；論文另外列出推論還需要的條件。[williams2024, p.4]
- 「簡單的替代式估計就夠了」：論文說它的表現可能不好，才轉向無偏轉換。[williams2024, p.3]
- 「模擬研究證明這個方法比別的方法好」：作者明說有限的模擬不代表一般的估計式表現。[williams2024, p.4]

## 相關頁面

- [[blip-function]]
- [[identification-assumptions]]
- [[optimal-dynamic-treatment-rule]]
- [[decision-points-and-history]]
- 來源頁：[[williams2024]]
- 名詞速查：[[glossary]]
