# ODTR Wiki 目錄

主題：最佳動態治療策略（Optimal Dynamic Treatment Regimes）。讀者：沒學過因果推論的同學。
規則見 `AGENTS.md`；操作紀錄見 [[log]]。

## 來源（sources）

- [[williams2024]] — Williams 等人：從縱貫資料學習最佳動態治療規則（教學型論文，BUP-NX 劑量範例）。
- [[renson2025]] — Renson 等人：從統計估計目標推導機器學習估計式（EIF、單步估計式、速率倍增穩健）。
- [[bluemlein2022]] — Blümlein 等人：用因果樹與因果森林學最佳動態治療策略（DTR-CT／DTR-CF，倒推遞迴，模擬與 MIMIC-III 加護病房資料）。
- [[hong2021]] — Hong 等人：以有限混合模型把急性呼吸衰竭分成三類，再用 DTR 估計個人化機械功率（MIMIC-IV 加護病房資料，臨床應用）。
- [[desman2025]] — Desman 等人：以分布式離線強化學習建議心臟手術後第一天每小時的胰島素劑量（GLUCOSE；MIMIC-IV 開發、eICU-CRD 外部驗證、三階段人類評估）。

## 概念（concepts）

- [[dynamic-treatment-regime]] — 動態治療策略：靜態與動態規則。
- [[decision-points-and-history]] — 決策時間點與病史：連續決策。
- [[optimal-dynamic-treatment-rule]] — 最佳動態治療規則（ODTR）與規則的價值。
- [[treatment-effect-heterogeneity]] — 平均效果與處理效應異質性。
- [[blip-function]] — Blip 函數（條件平均處理效應）。
- [[doubly-robust-learner]] — 倍增穩健學習器：從資料學出規則的方法。
- [[identification-assumptions]] — 因果識別的前提假設。
- [[statistical-estimand]] — 統計估計目標：想知道什麼數字，與估計式的差別。
- [[nuisance-functions]] — 干擾函數：結局迴歸、傾向分數等輔助估計對象。
- [[efficient-influence-function]] — 有效影響函數（EIF）：估計目標的「斜率」。
- [[plug-in-and-one-step-estimators]] — 代入式與單步（AIPW）估計式。
- [[rate-double-robustness]] — 速率倍增穩健：為什麼能配機器學習又有有效推論。
- [[cross-fitting]] — 交叉擬合與樣本分割。
- [[backward-recursion]] — 倒推遞迴與偽結局：從最後一個時間點往前估計。
- [[q-learning-dwols-g-estimation]] — Q 學習、DWOLS 與 G 估計：古典的線性迴歸式方法。
- [[causal-tree-and-forest]] — 因果樹與因果森林：誠實分割、用樹估計處理效應。
- [[interpretability]] — 可解釋性：interpretable 與 explainable 的差別。
- [[regret-and-decision-accuracy]] — 後悔值與決策準確度：模擬與真實資料怎麼評估學出的規則。
- [[mechanical-power]] — 機械功率（MP）：呼吸器參數合成的一個數字，hong2021 的「劑量」。
- [[finite-mixture-subphenotypes]] — 有限混合模型與表型：先不看標籤把病人自動分類。
- [[reinforcement-learning-mdp]] — 強化學習與馬可夫決策過程：狀態、行動、獎勵、折扣因子（desman2025 的框架）。
- [[offline-reinforcement-learning]] — 離線強化學習與保守 Q 學習（CQL）：只從固定資料學，並對資料之外的行動保守。
- [[distributional-reinforcement-learning]] — 分布式強化學習：看結果的整個分布，不只看平均。
- [[off-policy-evaluation]] — 離線策略評估（OPE）與擬合 Q 評估（FQE）：不上線也估計策略的表現。

## 比較與綜合（syntheses）

- [[overview-for-beginners]] — 如果你只讀一頁：五篇來源與主要概念，依教學順序串成的導覽。
- [[method-comparison]] — 方法比較：估計式家族，「倍增穩健」的幾種意思，以及三篇在多時間點、可解釋性、評估方式上的對照；文末加入 hong2021 後的四篇對照，再加入 desman2025（強化學習路線）的對照。
- [[dtr-clinical-applications]] — DTR 的臨床應用：三個情境（藥物劑量、ICU 開關式處置、連續劑量）並排，以及怎麼檢查規則；文末加上第四個情境（desman2025，術後胰島素劑量）。

## 術語表

- [[glossary]] — 中文／English／一句話定義／詳見頁面。
