# N1 retrieve — 主題：「動態治療策略是什麼？」（給沒學過因果推論的同學）

只讀 `wiki/index.md` 與各頁 frontmatter 挑選。挑選原則：外行人需要的「是什麼 → 為什麼難 → 怎麼學 → 實際例子 → 要小心什麼」。

## 選用
- [[overview-for-beginners]] — 教學順序的骨架
- [[dynamic-treatment-regime]] — 核心定義：靜態 vs 動態規則
- [[decision-points-and-history]] — 連續決策、病史
- [[optimal-dynamic-treatment-rule]] — 「最佳」與規則的價值
- [[treatment-effect-heterogeneity]] — 為什麼要個人化
- [[identification-assumptions]] — 用觀察資料要成立的前提
- [[backward-recursion]] — 從最後一步倒推
- [[doubly-robust-learner]] — 學規則的方法（williams2024）
- [[causal-tree-and-forest]] — 樹狀規則、可解釋（bluemlein2022）
- [[reinforcement-learning-mdp]] — 強化學習路線（desman2025）
- [[off-policy-evaluation]] — 不上線怎麼評估
- [[cross-fitting]] — 用 ML 估計時的防過擬合手段（renson2025）
- [[dtr-clinical-applications]] — 四個臨床情境並排
- [[method-comparison]] — 方法家族對照
- 來源頁：[[williams2024]]、[[renson2025]]、[[bluemlein2022]]、[[hong2021]]、[[desman2025]]

## 刻意不選
- efficient-influence-function、rate-double-robustness、plug-in-and-one-step-estimators：需要微積分直覺，超出外行讀者；
  renson2025 的角色改由 cross-fitting 與 source 頁承接。
- mechanical-power、finite-mixture-subphenotypes：只在 hong2021 例子裡用一句帶過。
