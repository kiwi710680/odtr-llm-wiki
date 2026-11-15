---
title: 最佳動態治療規則（ODTR）與規則的價值
type: concept
sources: [williams2024, bluemlein2022]
updated: 2026-11-15
---

# 最佳動態治療規則（ODTR）與規則的價值

## 直覺（生活比喻）

把每一種可能的「補習安排」都當成一個候選計畫：週一誰去、週三誰不去。最佳計畫就是「全班平均成績最好」的那一個。要比較計畫，得先知道「如果照這個計畫做，平均會怎樣」，這個平均就是規則的「價值」。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 所有可能的動態規則所成的集合記為 D；其中讓族群受益最大的那一條稱為最佳動態治療規則（optimal dynamic treatment rule, ODTR）。[williams2024, p.2]
- 「受益」的定義：對某個以共變數值 V = v 描述的子群，若「接受治療時」的（可能觀察不到的）反事實結局（counterfactual outcome）比「沒接受治療時」更大（結局是好事時）或更小（結局是壞事時），就算有益。[williams2024, p.2]
- 規則的價值：在規則 d 之下的反事實結局期望值 `E[Yd]`；ODTR 是在所有規則中讓它最大（好結局）或最小（壞結局）的規則。[williams2024, p.2]
- 時間變動的版本：ODTR 是一串規則，使整串規則之下的反事實結局期望值最大或最小。[williams2024, p.3]
- 目標參數 ψ：照最佳規則治療時的反事實結局平均值，也就是「即使與實際觀察到的不同，假如治療是依最佳規則指派，平均結局會是多少」。[williams2024, p.3]
- 估計 ODTR 的方法大致分兩類：以條件平均處理效應迴歸為基礎（最常見的是 Q-learning 與 A-learning），以及直接估計規則的分類方法（outcome-weighted learning 等）。[williams2024, p.3]

## 在各篇怎麼出現

### williams2024

- 論文用 ODTR 的語言提出兩類研究問題：只看單一時間點的「用收案（intake）時蒐集的資訊決定哪些病人在 1 個月後加量」，以及時間變動的「每週決定要不要加量」。[williams2024, p.3]
- 範例中學出的 ODTR 對應的價值估計是 0.324（95% CI, 0.261-0.38），固定劑量規則是 0.388（95% CI, 0.358-0.419），動態規則 d1 是 0.348（95% CI, 0.327-0.369）。[williams2024, p.6]
- 學出的規則在範例中變成「每週加量（第 3 週除外）」，論文認為這在只看前 6 週的設定下不令人意外。[williams2024, p.6]
- 作者提到「ODTR 集成」（ODTR ensembles）：讓回歸類、分類類與簡單靜態策略一起「競爭」，由資料自適應地選出最佳策略。[williams2024, p.6]

### 在 bluemlein2022 中

- 論文的估計目標是最佳 DTR：在所有可能 DTR 的集合中，讓規則的價值（若人人依該規則治療，結局的母體平均）最大的那一條。[bluemlein2022, p.5]
- 論文以潛在結局架構（Neyman 1923；Rubin 1974）表達，結局以「越大越好」為準（不失一般性）。[bluemlein2022, p.5] [bluemlein2022, p.4]
- 作者宣稱這是第一篇把因果樹方法用來學最佳 DTR 的論文。[bluemlein2022, p.1]
- 評估方式：模擬資料有真值，用後悔值與決策準確度；真實資料用期望增益。見 [[regret-and-decision-accuracy]]。[bluemlein2022, p.13] [bluemlein2022, p.16]
- 論文報告的是上述指標，沒有報告學出規則之價值（平均結局）的估計與信賴區間：來源未提及。
- 估計 ODTR 的另一類做法（Q 學習等古典迴歸式方法）見 [[q-learning-dwols-g-estimation]]。

## 常見誤解

- 「最佳」是指在族群平均意義上讓反事實結局最好；論文並沒有保證學出的規則一定贏過臨床規則：與 d1 的比較，論文說差異不具意義（RR = 0.93; 95% CI, 0.77-1.13）。[williams2024, p.6]
- 最佳規則不一定複雜：論文指出最佳策略也可能其實是簡單的靜態規則。[williams2024, p.6]
- 估計 ψ 是另一件事：論文提到可以用標靶最小損失估計（targeted minimum loss-based estimation）或倍增穩健轉換的估計式；一致估計 ψ 與其信賴區間還需要額外條件，見 [[identification-assumptions]]。[williams2024, p.4]

## 相關頁面

- [[dynamic-treatment-regime]]
- [[decision-points-and-history]]
- [[blip-function]]
- [[doubly-robust-learner]]
- [[regret-and-decision-accuracy]]
- [[q-learning-dwols-g-estimation]]
- 來源頁：[[williams2024]]、[[bluemlein2022]]
