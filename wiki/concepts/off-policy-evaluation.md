---
title: 離線策略評估（OPE）與擬合 Q 評估（FQE）
type: concept
sources: [desman2025, williams2024]
updated: 2026-11-15
---

# 離線策略評估（OPE）與擬合 Q 評估（FQE）

## 直覺（生活比喻）

想知道「如果全校都改用新的上學路線，平均通學時間會變多少」，但不可能真的叫全校改路線。只能拿過去大家走舊路線的紀錄，用一個模型去推估走新路線會怎樣。推估出來的是「估計」，不是實測。離線策略評估（off-policy evaluation, OPE）做的就是這種推估。（比喻為本 wiki 的說明，不是論文的話。）

## 定義

- OPE：不實際施行新策略，而是從既有資料估計學到的策略的表現。論文用它來估計 GLUCOSE 的表現。[desman2025, p.9]
- 擬合 Q 評估（fitted Q evaluation, FQE）：論文採用的 OPE 方法。論文說它能處理學到的策略與觀察到的行為差異很大的情況，也能處理隨機性，並在多個醫療基準上顯示出一致性與校準。這是作者引用文獻的說法。[desman2025, p.9]
- 信賴區間：對所有病程（episode）重抽樣、取後放回 10,000 次，得到 95% 信賴區間。[desman2025, p.9]
- 比較的方式：圖中實線是 GLUCOSE 經 OPE 得到的估計表現，虛線是觀察到的醫師行為的表現；挑選模型時，拿 GLUCOSE 信賴區間的下界與醫師信賴區間的上界比。[desman2025, p.2] [desman2025, p.4]
- 結果：GLUCOSE 的估計報酬在內部測試為 0.0（−0.07 至 0.06）、外部驗證為 −0.63（−0.74 至 −0.52）；醫師的報酬分別為 −1.29（−1.37 至 −1.20）與 −1.02（−1.16 至 −0.89）。[desman2025, p.2]
- 做不到的情況：eICU-CRD 中胰島素紀錄含糊、被排除的病人，因為 OPE 與直接比較都需要準確的胰島素給藥紀錄，所以無法做。[desman2025, p.6]

## 在各篇怎麼出現

### 在 desman2025 中

- OPE 是整個研究的主要評估：GLUCOSE 的估計報酬在兩個資料集都高於醫師的報酬。[desman2025, p.2]
- 論文把 OPE 的全名在正文寫成 off-policy evaluation，在方法段寫成 offline policy estimation；本 wiki 照記，不判斷。[desman2025, p.2] [desman2025, p.9]
- 本 wiki 的讀法（不是論文的話）：報酬是作者自訂的計分尺度，所以這些數字不是臨床單位；醫師的報酬是觀察到的，GLUCOSE 的是估計出來的，兩邊的算法不同。[desman2025, p.2] [desman2025, p.9]
- OPE 需要哪些前提才能當成因果估計（例如不能有未測量干擾）：來源未提及。見 [[identification-assumptions]]。

### 與 williams2024 的對照（本 wiki 的整理）

- williams2024 在範例中估計各規則之下結局的價值並給信賴區間，見 [[optimal-dynamic-treatment-rule]]；OPE 回答的是同一類問題：「若依這條規則做，平均結局會怎樣」。但論文沒有把兩者並論，所用的估計式也不同：來源未提及。[williams2024, p.6]

## 常見誤解

- 「OPE 的結果等於把策略在病人身上試過」：不是。論文自己說這是回溯性研究，需要前瞻性研究與臨床試驗驗證。[desman2025, p.7]
- 「報酬 0.0 代表血糖完美」：0.0 是作者設計的獎勵尺度上的一個數字，最高獎勵是 +0.2，所以 0.0 只表示在這個計分下的平均表現。[desman2025, p.2] [desman2025, p.9]
- 「估計報酬高就是比醫師好」：論文用「顯著改善」描述，依據是信賴區間下界高於醫師的上界；它仍是對自己建議的離線估計。[desman2025, p.2]

## 相關頁面

- [[reinforcement-learning-mdp]]
- [[offline-reinforcement-learning]]
- [[optimal-dynamic-treatment-rule]]
- [[regret-and-decision-accuracy]]
- [[identification-assumptions]]
- 來源頁：[[desman2025]]、[[williams2024]]
- 名詞速查：[[glossary]]
