---
title: Q 學習、DWOLS 與 G 估計（古典迴歸式方法）
type: concept
sources: [bluemlein2022, williams2024, hong2021, desman2025]
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

### 在 hong2021 中

- 論文以動態加權普通最小平方法（dWOLS，也就是本頁的 DWOLS）依序估計最佳 MP，輸出 0 到 48 小時的個人化最佳劑量策略。[hong2021, p.3]
- 論文為這一步引用的文獻之一，標題含「最佳劑量策略的倍增穩健估計」；但正文沒有主張自己的估計具有倍增穩健性，也沒有說明傾向分數（連續劑量的指派機制）怎麼建模與加權：來源未提及。[hong2021, p.3] [hong2021, p.9]
- 函數形式由作者事先指定（哪些變數與 MP 交互、二次項只與類別和 P/F 比值交互），屬於參數式迴歸；bluemlein2022 對這類古典方法的描述是假設函數形式與變數已知。[hong2021, p.3] [bluemlein2022, p.22]
- hong2021 沒有把 dWOLS 和其他方法比較，也沒有模擬研究：來源未提及。這和 bluemlein2022 把它當作基準方法的用途不同。[hong2021, p.3] [bluemlein2022, p.12]

### 在 desman2025 中

- 論文用的演算法叫保守 Q 學習（CQL），是離線強化學習的方法，見 [[offline-reinforcement-learning]]。[desman2025, p.8]
- CQL 與本頁的 Q 學習（以線性迴歸估計 blip 參數）是不是同一脈絡：論文沒有說明：來源未提及。bluemlein2022 把 Q 學習歸為統計學的古典線性方法，與強化學習是不同的路線。[bluemlein2022, p.4] [bluemlein2022, p.22]
- desman2025 沒有使用 DWOLS 或 G 估計：來源未提及。

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
- [[offline-reinforcement-learning]]
- 來源頁：[[bluemlein2022]]、[[williams2024]]、[[hong2021]]、[[desman2025]]
- 名詞速查：[[glossary]]
