---
title: 可解釋性（interpretable 與 explainable）
type: concept
sources: [bluemlein2022, williams2024]
updated: 2026-11-15
---

# 可解釋性（interpretable 與 explainable）

## 直覺（生活比喻）

可詮釋（interpretable）像是把食譜直接攤在桌上，每一步你都看得到；可說明（explainable）像是廚房是黑盒子，但服務生會告訴你「這道菜主要靠哪幾種食材」。兩種都讓你比較放心，但放心的程度不同。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 論文說，把降低 DTR 不透明程度的方法稱為「explainable」。[bluemlein2022, p.2]
- 論文也提到有些作者做區分：決策邏輯本身透明稱為 interpretable；靠替代模型提供洞察稱為 explainable。在這個用詞下，DTR-CT 屬於 interpretable，DTR-CF 屬於 explainable。[bluemlein2022, p.2]
- 為什麼重要：論文說，在醫療決策與個人化醫療中，對個別病人治療決定的依據必須透明且好懂。[bluemlein2022, p.2]
- DTR-CT：每個時間步都可以把決策樹畫出來，看哪些變數解釋了處理效應在病人之間的差異，供醫師檢視。[bluemlein2022, p.10]
- DTR-CF：每個時間步可以檢視變數重要性，看哪些變數對治療決定最具指示性。[bluemlein2022, p.11]
- 對照：古典線性方法好解釋但結構簡單；機器學習路線多為黑箱；強化學習多以深度學習或神經網路為基礎，不易解釋。[bluemlein2022, p.2] [bluemlein2022, p.4]

## 在各篇怎麼出現

### 在 bluemlein2022 中

- 真實資料的樹（Fig. 3）：分裂變數包含舒張壓、心率、收縮壓與呼吸速率；每片葉子標示該亞群的估計處理效應與對應的最佳決定。論文說醫師可以拿這棵樹對照臨床做法與領域知識。[bluemlein2022, p.16-17]
- 真實資料的變數重要性（Fig. 4，只展示一個時間步）：是否使用機械通氣，主要依據前兩個時間步的呼吸速率與血氧；是否使用血管加壓素，則以前兩個時間步的平均血壓與收縮壓最重要。作者說這符合醫學知識，因此增加結果的可信度。[bluemlein2022, p.17]
- 作者承認：即使學出的規則沒有涵蓋臨床做法的所有細節，仍可能是有用的個人化決策支援。[bluemlein2022, p.17]
- 臨床人員是否實際評估過這些樹與重要性圖：來源未提及。

### williams2024

- 論文提到用決策樹估計 blip 函數，可得到好解讀的決策規則。[williams2024, p.4]

### renson2025

- 來源未提及可解釋性。

## 常見誤解

- 「可說明就等於可詮釋」：論文自己的用詞把兩者分開，DTR-CF 只算可說明。[bluemlein2022, p.2]
- 「變數重要就代表因果上重要」：這是本 wiki 的提醒，不是論文的話；論文只說這些變數對估計的處理效應差異最具指示性，並以醫學知識「看起來合理」作旁證。[bluemlein2022, p.17]
- 「可解釋所以比較準」：論文的比較只納入可解釋或前人用過的基準，沒有和不可解釋的方法比較。[bluemlein2022, p.18]

## 相關頁面

- [[causal-tree-and-forest]]
- [[treatment-effect-heterogeneity]]
- [[dynamic-treatment-regime]]
- [[blip-function]]
- 來源頁：[[bluemlein2022]]、[[williams2024]]
- 名詞速查：[[glossary]]
