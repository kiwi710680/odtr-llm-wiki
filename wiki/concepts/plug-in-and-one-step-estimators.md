---
title: 代入式估計式與單步估計式（plug-in／one-step）
type: concept
sources: [renson2025, williams2024]
updated: 2026-11-15
---

# 代入式估計式與單步估計式（plug-in／one-step）

## 直覺（生活比喻）

用手機導航估算到達時間：代入式（plug-in）像是完全相信導航的路線圖，直接讀出預估時間。單步式（one-step）則是在讀出預估時間後，再拿一路上實際遇到的塞車與順暢情形，把預估值修正一下。修正量從哪裡來？就是 [[efficient-influence-function]] 頁講的那個「斜率」。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- 代入式估計式（plug-in estimator）：把估計出的分布各部分代進估計目標。論文的範例是 `ψ(P̂) = (1/n) Σ q̂(W_i)`，對應 g 計算法（g-computation）。[renson2025, p.3]
- 論文稱代入式為「直覺、但不一定最好」的估計式；用機器學習估計 `q̂(W)` 時，它一般無法給出正確推論。[renson2025, p.3]
- 單步估計式（one-step estimator）：在代入式上加上「估計 EIF 的樣本平均」，即 `ψ̂_os = ψ(P̂) + (1/n) Σ φ(O_i, P̂)`。[renson2025, p.3]
- 範例的單步估計式化簡成 `(1/n) Σ { I(A_i=0)/ĝ(W_i) × (Y_i − q̂(W_i)) + q̂(W_i) }`。[renson2025, p.3]
- 這個形式也叫增強型逆機率加權（augmented inverse probability weighted, AIPW）估計式；做法是用迴歸估計 `ĝ` 與 `q̂`（可用機器學習），再取樣本平均。[renson2025, p.3]
- 論文說單步估計式是「可論證最簡單」的 EIF 型估計式；另外還有目標最大概似／最小損失估計（targeted minimum loss/maximum likelihood estimation, TMLE）與估計方程式法。[renson2025, p.3]
- 論文在討論處補充：雙重／去偏機器學習（double/debiased machine learning）把單步估計式當作特例，並指出另一篇相關論文示範如何用 EIF 建構 TMLE。[renson2025, p.5]
- 論文對比：倍增穩健估計式在使用機器學習時，仍可得到（大樣本下）名目涵蓋率的信賴區間，g 計算法除了特殊情況外做不到。[renson2025, p.1]

## 在各篇怎麼出現

### 在 renson2025 中

- 這是第三步：先講代入式，再講為什麼要加上 EIF 的樣本平均。[renson2025, p.3]
- 論文把 g 計算法與逆機率加權（IPW）估計式歸為「非速率倍增穩健」的例子，誤差是各自干擾估計式的平均誤差。[renson2025, p.3]
- 論文提到有些機器學習演算法快到足以讓 g 計算法或 IPW 容納，也有演算法具 Donsker 類性質，可免樣本分割使用速率倍增穩健估計式；高度適應性 lasso（highly adaptive lasso）在適當條件下兩者兼具。[renson2025, p.5]

### williams2024

- williams2024 的「增強型逆機率加權（AIPW）」轉換用來產生 blip 函數的無偏轉換，而不是估計平均結局本身。[williams2024, p.3]
- 兩篇都用到 AIPW 這個名字，但目標不同；詳見 [[method-comparison]]，這是本 wiki 的整理。

## 常見誤解

- 「代入式一定不能用」：論文只說它在機器學習下一般無法給出正確推論，並說某些演算法夠快時仍可用。[renson2025, p.5]
- 「單步估計式和 AIPW 是兩個不同的方法」：在論文的範例中，兩者是同一個式子。[renson2025, p.3]
- 「單步估計式只是在原式上做個小調整，不需要再證明什麼」：論文說仍需證明速率倍增穩健性，見 [[rate-double-robustness]]。[renson2025, p.3]

## 相關頁面

- [[statistical-estimand]]
- [[efficient-influence-function]]
- [[nuisance-functions]]
- [[rate-double-robustness]]
- [[cross-fitting]]
- [[doubly-robust-learner]]
- [[method-comparison]]
- 來源頁：[[renson2025]]、[[williams2024]]
