---
title: Blip 函數（條件平均處理效應）
type: concept
sources: [williams2024, bluemlein2022, hong2021]
updated: 2026-11-15
---

# Blip 函數（條件平均處理效應）

## 直覺（生活比喻）

想像為每位同學算一張「補習的加分表」：有補習的預期成績減去沒補習的預期成績。加分是正的，就建議補習；是負的，就不補。blip 函數就是這張加分表，只是它是「按特徵分群」算出來的平均差。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 條件平均處理效應（conditional average treatment effect, CATE）通常稱為 blip 函數（blip function），是用迴歸方法學出最佳規則的關鍵成分。[williams2024, p.3]
- 因果寫法：B(V) 等於在 V 條件下「接受治療的反事實結局」減「沒接受治療的反事實結局」的期望值；觀察資料寫法則是對 `E[Y|H, A = 1] - E[Y|H, A = 0]` 在 V 條件下取期望。[williams2024, p.3]
- 這兩個寫法要相等，需要三個假設：一致性（consistency）、無未測量干擾（可交換性，exchangeability）與正值性（positivity），見 [[identification-assumptions]]。[williams2024, p.3]
- 決策規則：若目標是讓結局期望值最大，就對 Bn(V) 為正的人給治療、為負的人不給。論文給的是最大化版本；最小化版本（例如要讓 RROU 最小）的寫法來源未提及，方向相反是讀者的推論。[williams2024, p.3]
- 簡單的替代式（substitution）估計：先估 Q(H, A) = E[Y|H, A]，再把 A 分別設為 1 與 0 做預測、相減，最後把差值對 V 迴歸。[williams2024, p.3]
- 論文指出這種簡單估計式的表現可能不好，因此改用無偏轉換（unbiased transformation），見 [[doubly-robust-learner]]。[williams2024, p.3]
- 時間變動版本：第一個時間點的 blip 要重新定義成「假設之後的治療已依最佳規則指派」下的差。[williams2024, p.4]

## 在各篇怎麼出現

### williams2024

- 是論文估計 ODTR 的核心：先學 blip，再以符號決定治療。[williams2024, p.3]
- 範例中檢查各週的 blip 模型，發現所有用來做決策的變數都沒被選進去，模型變成只有截距，所以每週的最佳規則就只由偽結局的正負號決定。[williams2024, p.6]
- 論文提到的一個一致估計 ψ 的條件：blip 不可為零，也就是 `P(B(V) = 0) = 0`，沒有任何個體的 CATE 剛好是零。[williams2024, p.4]
- 論文提到可以用決策樹估計 B(V)，得到好解讀的決策規則。[williams2024, p.4]

### 在 bluemlein2022 中

- 論文把 blip 函數寫成：在病史條件下，若在時間 t 治療或不治療、且之後都依最佳決定，兩者潛在結局的期望差。概念出自 Robins（2004），論文也稱它為異質處理效應（heterogeneous treatment effect, HTE）。[bluemlein2022, p.5]
- 若 HTE 已知，最佳決定就是對 HTE 為正的人給治療（假設沒有治療成本或限制）。[bluemlein2022, p.5]
- 實際只觀察得到實際治療下的結局，所以 HTE 是反事實量，要靠假設才能從資料識別，見 [[identification-assumptions]]。[bluemlein2022, p.5]
- 估計方式：DTR-CT 以每片葉子內治療組與未治療組的（逆傾向分數加權）平均結局之差，當作該葉的 HTE；DTR-CF 以局部鄰域的加權平均估計。見 [[causal-tree-and-forest]]。[bluemlein2022, p.9]
- 古典方法（Q 學習等）則假設 blip 是病史的線性函數，稱為 blip model（治療交互作用模型），見 [[q-learning-dwols-g-estimation]]。[bluemlein2022, p.22]
- 與 williams2024 的對照：williams2024 的範例以 ℓ1 正規化估計 blip；bluemlein2022 直接用樹或森林估計。[williams2024, p.5] [bluemlein2022, p.9]
- 真實資料的樹中，每片葉子標示該亞群的估計處理效應與對應的最佳決定。[bluemlein2022, p.16-17]

### 在 hong2021 中

- 論文把死亡結局的期望值拆成兩塊：「沒有治療的模型」加上「blip 函數」；blip 函數由一組參數表達，描述治療（這裡是機械功率劑量）的效果。[hong2021, p.3]
- 這裡的治療是連續劑量：MP 的分布假設為 Gamma 分布，連結函數取對數；blip 中同時有 MP 的一次項與二次項。與一次項交互的變數包含年齡、呼吸速率、收縮壓、心率、類別、血氣與實驗室指標；與二次項交互的只有類別與 P/F 比值。[hong2021, p.3]
- 本 wiki 的讀法（不是論文的話）：劑量只有一次項時，結局對劑量是一條直線，最佳劑量只會落在可用範圍的兩端；加入二次項，最佳劑量才可能落在中間。
- 與前兩篇不同：williams2024 與 bluemlein2022 的 blip 是「給治療」減「不給治療」的差，hong2021 的 blip 是劑量的函數；blip 係數的數值，以及相對於哪個基準劑量：來源未提及。[williams2024, p.3] [williams2024, p.5] [bluemlein2022, p.5] [hong2021, p.3]

## 常見誤解

- 「blip 是某一個人的真實效果」：它是在 V 相同的人之中的平均差，不是個人的效果；論文把它稱為 CATE。[williams2024, p.3]
- 「blip 估計出來之後，規則就一定有用」：範例中 blip 模型退化為截距，結果規則與病人特徵無關，見上。[williams2024, p.6]

## 相關頁面

- [[treatment-effect-heterogeneity]]
- [[doubly-robust-learner]]
- [[optimal-dynamic-treatment-rule]]
- [[identification-assumptions]]
- [[causal-tree-and-forest]]
- [[q-learning-dwols-g-estimation]]
- 來源頁：[[williams2024]]、[[bluemlein2022]]、[[hong2021]]
