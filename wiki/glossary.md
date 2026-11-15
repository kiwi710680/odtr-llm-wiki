---
title: 術語表
type: glossary
sources: [williams2024, renson2025, bluemlein2022]
updated: 2026-11-15
---

# 術語表

每列：中文 ／ English ／ 一句話定義 ／ 詳見頁面。定義只依據已 ingest 的來源；目前來源：[[williams2024]]、[[renson2025]]、[[bluemlein2022]]。

| 中文 | English | 一句話定義 | 詳見 |
|---|---|---|---|
| 治療規則 | treatment rule | 把治療前變數 V 對應到要給的治療 A 的函數。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 靜態規則 | static rule | 每個人都拿到同一個治療值。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 動態規則 | dynamic rule | 治療依個人已量測的病史而定。[williams2024, p.2] | [[dynamic-treatment-regime]] |
| 病史 | history | 到某次治療之前的所有變數紀錄，記為 Ht。[williams2024, p.3] | [[decision-points-and-history]] |
| 決策時間點 | decision point | 病人可以選擇要不要接受（或加量）治療的離散時間點。[williams2024, p.2] | [[decision-points-and-history]] |
| 最佳動態治療規則 | optimal dynamic treatment rule（ODTR） | 在所有可能規則中，讓反事實結局期望值最大（或最小）的規則。[williams2024, p.2] | [[optimal-dynamic-treatment-rule]] |
| 反事實結局 | counterfactual outcome | 若治療依某規則指派，結局會有的假想值。[williams2024, p.2] | [[optimal-dynamic-treatment-rule]] |
| 平均處理效應 | average treatment effect（ATE） | 全部的人都接受治療相對全部不接受時，結局的平均差。[williams2024, p.1] | [[treatment-effect-heterogeneity]] |
| 處理效應異質性 | treatment effect heterogeneity | 平均有益的治療仍可能使有些人受益、有些人受害。[williams2024, p.1] | [[treatment-effect-heterogeneity]] |
| 條件平均處理效應 | conditional average treatment effect（CATE） | 在 V 條件下兩種治療的結局差，常稱 blip 函數。[williams2024, p.3] | [[blip-function]] |
| Blip 函數 | blip function | CATE 的別名，是迴歸式學出最佳規則的關鍵成分。[williams2024, p.3] | [[blip-function]] |
| 無偏轉換 | unbiased transformation | 資料的函數，其在 V 條件下的期望值等於 blip。[williams2024, p.3] | [[doubly-robust-learner]] |
| 增強型逆機率加權 | augmented inverse probability weighting（AIPW） | 論文採用的倍增穩健無偏轉換。[williams2024, p.3] renson2025 中，AIPW 估計式就是單步估計式。[renson2025, p.3] | [[doubly-robust-learner]]、[[plug-in-and-one-step-estimators]] |
| 倍增穩健 | doubly robust | Q 或 g 只要有一個被一致估計，就能得到無偏的 blip 估計。[williams2024, p.3] | [[doubly-robust-learner]] |
| 傾向分數 | propensity score | 實際拿到所觀察到治療的機率，論文中記為 g(A, H)。[williams2024, p.3] | [[doubly-robust-learner]] |
| Q 學習 | Q-learning | 以條件平均處理效應迴歸為基礎的 ODTR 估計方法之一。[williams2024, p.3] bluemlein2022 中，Q 學習以普通最小平方法估計線性的 blip 參數。[bluemlein2022, p.22] | [[optimal-dynamic-treatment-rule]]、[[q-learning-dwols-g-estimation]] |
| 超級學習器 | super learner | 以另一個演算法（元學習器）組合一組使用者指定學習器的預測。[williams2024, p.5] | [[doubly-robust-learner]] |
| 交叉擬合 | cross-fitting | 範例中用來估計 Q 與 g 的做法，論文在別處以樣本分割說明可避開平滑性要求。[williams2024, p.5] renson2025 中，要求干擾估計式在另一份樣本擬合，簡單版是把樣本分成兩半再交換。[renson2025, p.4] | [[doubly-robust-learner]]、[[cross-fitting]] |
| 一致性 | consistency | 觀察到的治療水準下，反事實結局就是實際觀察到的結局。[williams2024, p.3] | [[identification-assumptions]] |
| 可交換性（無未測量干擾） | exchangeability（no unmeasured confounding） | 所有同時影響暴露與結局的共同原因都已測量並調整。[williams2024, p.3] | [[identification-assumptions]] |
| 正值性 | positivity | 在所有層內，各治療水準出現的機率都不為零。[williams2024, p.3] | [[identification-assumptions]] |
| 回到規律鴉片使用 | return to regular opioid use（RROU） | 論文範例的結局，定義見來源頁。[williams2024, p.5] | [[williams2024]] |
| 鴉片使用障礙 | opioid use disorder（OUD） | 論文範例的疾病情境。[williams2024, p.1] | [[williams2024]] |
| 丁基原啡因加納洛酮 | buprenorphine-naloxone（BUP-NX） | 論文範例中被調整劑量的藥物。[williams2024, p.1] | [[williams2024]] |
| 估計目標 | estimand | 想知道的那個量；統計估計目標是只依賴觀察資料分布的映射 ψ(P)。[renson2025, p.2] | [[statistical-estimand]] |
| 估計式 | estimator | 從資料算出估計目標的方法，例如代入式、單步估計式。[renson2025, p.3] | [[statistical-estimand]]、[[plug-in-and-one-step-estimators]] |
| 識別 | identification | 用因果假設把因果參數等同於只依賴觀察資料分布的統計估計目標。[renson2025, p.2] | [[statistical-estimand]]、[[identification-assumptions]] |
| 干擾函數 | nuisance function | 需要估計但不是最終目標的函數，例如結局迴歸、傾向分數。[renson2025, p.1] | [[nuisance-functions]] |
| 有效影響函數 | efficient influence function（EIF） | 估計目標對資料分布的導數，描述估計式的一階誤差。[renson2025, p.2] | [[efficient-influence-function]] |
| 路徑可微分性 | pathwise differentiability | EIF 存在的條件：映射的導數存在且變異數有限。[renson2025, p.3] | [[efficient-influence-function]] |
| 代入式估計式 | plug-in estimator | 把估計出的分布各部分代進估計目標，範例中對應 g 計算法。[renson2025, p.3] | [[plug-in-and-one-step-estimators]] |
| g 計算法 | g-computation | 代入式估計式在範例中的別名；用機器學習時一般無法正確推論。[renson2025, p.3] | [[plug-in-and-one-step-estimators]] |
| 單步估計式 | one-step estimator | 代入式加上估計 EIF 的樣本平均，範例中等同 AIPW。[renson2025, p.3] | [[plug-in-and-one-step-estimators]] |
| 目標最大概似估計 | targeted minimum loss/maximum likelihood estimation（TMLE） | 另一類 EIF 型估計式，論文只簡述。[renson2025, p.5] | [[plug-in-and-one-step-estimators]] |
| 收斂速率 | convergence rate | 估計式的偏差與變異數趨近於零的快慢。[renson2025, p.3] | [[rate-double-robustness]] |
| 速率倍增穩健 | rate double robustness | 估計式的收斂速率等於兩個干擾函數收斂速率的乘積。[renson2025, p.4] | [[rate-double-robustness]] |
| 倍增穩健一致性 | doubly robust consistency | 兩個干擾估計式只要有一個設定正確，估計式就一致。[renson2025, p.4] | [[rate-double-robustness]]、[[doubly-robust-learner]] |
| 樣本分割 | sample splitting | 讓干擾函數與最後估計式使用不同樣本的做法，交叉擬合是其一種。[renson2025, p.4] | [[cross-fitting]] |
| 倒推遞迴 | backward recursion | 從最後一個時間步往前，每步估處理效應並決定治療的動態規劃式方法。[bluemlein2022, p.6] | [[backward-recursion]] |
| 偽結局 | pseudo-outcome | 假如病人在之後的時間步都被最佳治療，會有的潛在結局；用來取代只在最後一步才觀察到的結局。[bluemlein2022, p.6] | [[backward-recursion]] |
| 異質處理效應 | heterogeneous treatment effect（HTE） | bluemlein2022 對 blip 函數的稱呼：在病史條件下，治療與不治療的潛在結局期望差。[bluemlein2022, p.5] | [[blip-function]]、[[treatment-effect-heterogeneity]] |
| 因果樹 | causal tree | 以專為處理效應設計的分裂準則分群，並估計每片葉子處理效應的決策樹。[bluemlein2022, p.8] | [[causal-tree-and-forest]] |
| 因果森林 | causal forest | 許多棵因果樹的集成，以局部鄰域的加權平均估計每位病人的處理效應。[bluemlein2022, p.9] | [[causal-tree-and-forest]] |
| 誠實分割 | honest splitting | 把資料分成訓練集（決定分群）與估計集（估計葉內效應），兩者不重疊。[bluemlein2022, p.8] | [[causal-tree-and-forest]]、[[cross-fitting]] |
| DTR 因果樹／森林 | DTR-CT／DTR-CF | bluemlein2022 提出的兩個方法：把因果樹或因果森林放進倒推遞迴。[bluemlein2022, p.6] | [[bluemlein2022]]、[[causal-tree-and-forest]] |
| 逆傾向分數加權 | inverse propensity weighting | 以傾向分數的倒數加權結局，bluemlein2022 沿用 DWOLS 的做法。[bluemlein2022, p.7] | [[doubly-robust-learner]]、[[q-learning-dwols-g-estimation]] |
| DWOLS | dynamic weighted ordinary least squares | 在 Q 學習上加逆傾向分數權重的線性方法。[bluemlein2022, p.23] | [[q-learning-dwols-g-estimation]] |
| G 估計 | G-estimation | 把估計的傾向分數放進估計方程式的迴歸式方法。[bluemlein2022, p.23] | [[q-learning-dwols-g-estimation]] |
| 可詮釋 | interpretable | 決策邏輯本身透明；論文的用詞中，DTR-CT 屬於這一類。[bluemlein2022, p.2] | [[interpretability]] |
| 可說明 | explainable | 靠替代模型提供洞察；論文的用詞中，DTR-CF 屬於這一類。[bluemlein2022, p.2] | [[interpretability]] |
| 後悔值 | regret | 估計的最佳決定相對真正最佳決定，造成的結局損失；不為負，相同時為零。[bluemlein2022, p.13] | [[regret-and-decision-accuracy]] |
| 決策準確度 | decision accuracy | 估計的最佳決定與真正最佳決定相符的比例。[bluemlein2022, p.13] | [[regret-and-decision-accuracy]] |
| 期望增益 | expected gain（reward） | 真實資料中，依估計的最佳 DTR 治療相對於實際治療的預期結局增加量。[bluemlein2022, p.16] | [[regret-and-decision-accuracy]] |
| 序列可交換性 | sequential exchangeability | 以病史為條件，足以移除估計 HTE 時的干擾偏誤。[bluemlein2022, p.6] | [[identification-assumptions]] |
| 治療後偏誤 | post-treatment bias | 把治療後才量到的共變數放進模型，會「解釋掉」治療效果而造成的偏誤。[bluemlein2022, p.6] | [[backward-recursion]] |
