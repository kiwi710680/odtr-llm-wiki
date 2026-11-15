---
title: Q 學習、DWOLS 與 G 估計（古典迴歸式方法）
type: concept
sources: [bluemlein2022, williams2024]
updated: 2026-11-15
---

# Q 學習、DWOLS 與 G 估計（古典迴歸式方法）

## 直覺（生活比喻）

三位會計用同一張表格記帳，表格的格子都是直線型的（線性）。第一位照實填數字；第二位把每一筆依「這筆帳被分到這個項目的機率」加權後再填；第三位則把那個機率直接寫進結算公式。三種做法的表格長相一樣，只是處理「誰被分到哪一組」的方式不同。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 三者在論文中都是「古典、以線性迴歸為基礎」的 DTR 方法，源自統計學。[bluemlein2022, p.22]
- 共同架構：每個時間步，把觀察結局的期望值拆成兩塊，「沒有治療時的模型」（treatment-free model）加上「治療與病史的交互作用模型」（treatment-interaction model，也叫 blip model）。[bluemlein2022, p.22]
- 因為是加法分離，治療決定完全由交互作用那一塊決定；參數若已知，處理效應就是病史的線性組合，估計值為正就給治療。[bluemlein2022, p.22]
- Q 學習（Q-learning，Moodie 等人 2012）：以普通最小平方法（OLS）估計 blip 參數；也可以理解成分別用線性模型建兩個潛在結局再相減。[bluemlein2022, p.12] [bluemlein2022, p.22]
- DWOLS（dynamic weighted ordinary least squares，Wallace 與 Moodie 2015）：在 Q 學習上加逆傾向分數權重；論文說這使它對模型設定錯誤具倍增穩健性。[bluemlein2022, p.12] [bluemlein2022, p.23]
- G 估計（G-estimation，Robins 2004）：不加權，而是把估計的傾向分數放進估計方程式；同樣是倍增穩健、以迴歸為基礎的方法。[bluemlein2022, p.12] [bluemlein2022, p.23]
- 它們共同的假設：真實模型是低維、對參數線性、函數形式與變數已知；也假設結局預測與處理效應異質性靠同一組共變數。實務上這兩組可能不同且未知。[bluemlein2022, p.22]

## 在各篇怎麼出現

### 在 bluemlein2022 中

- 三者都是基準方法，各自放進 Algorithm 1 取代因果樹／因果森林。[bluemlein2022, p.22]
- 為了公平，兩個成分都用同一組共變數：整段病史。[bluemlein2022, p.12]
- 線性情境中，Q 學習與 DWOLS 的測試集累積後悔值為 23.730 與 23.566，遠高於 DTR-CT 的 3.223 與 DTR-CF 的 3.052。[bluemlein2022, p.14]
- G 估計在線性情境的累積後悔值最高（55.807），在非線性情境（20.434）卻是五個基準中最低；原因論文未解釋：來源未提及。[bluemlein2022, p.14]
- 本 wiki 的觀察（不是論文的話）：在作者設計的線性情境，三個線性方法的後悔值都沒有低過 CART 的 4.188。[bluemlein2022, p.14]

### williams2024

- 只把 Q-learning 與 A-learning 列為「以條件平均處理效應迴歸為基礎」的一類方法；細節，以及 DWOLS 與 G 估計：本 wiki 的 williams2024 頁未記載。[williams2024, p.3]

## 常見誤解

- 「Q 學習就是深度強化學習」：論文把 Q 學習歸為來自統計學的古典方法（線性迴歸），與另外提到、多以深度學習為基礎的強化學習研究是不同的路線。[bluemlein2022, p.4] [bluemlein2022, p.22]
- 「DWOLS 加了權重就不會錯」：論文只說它對模型設定錯誤具倍增穩健性，且前提仍是線性、低維的模型形式。[bluemlein2022, p.22-23]
- 「線性方法在線性情境一定贏」：在作者的模擬中沒有；原因來源未提及。[bluemlein2022, p.14]

## 相關頁面

- [[backward-recursion]]
- [[blip-function]]
- [[doubly-robust-learner]]
- [[causal-tree-and-forest]]
- [[optimal-dynamic-treatment-rule]]
- 來源頁：[[bluemlein2022]]、[[williams2024]]
- 名詞速查：[[glossary]]
