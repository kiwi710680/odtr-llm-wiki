# 證據卡：desman2025

- desman2025-C1: 這篇研究的演算法叫 GLUCOSE，要建議心臟手術後第一天、每小時該給多少常規胰島素，目標是讓血糖落在適當範圍。 [desman2025, p.1] ← [[desman2025]]
- desman2025-C2: 強化學習的「狀態」，就是病人某一小時的整體情況：人口學、共病、實驗室值、生命徵象、用藥、機械通氣與 SOFA 分數，另外加上前四小時的血糖。 [desman2025, p.9] ← [[reinforcement-learning-mdp]]
- desman2025-C3: 強化學習的「行動」，就是每小時給多少常規胰島素；劑量是連續的，建議劑量上限為每小時 10 單位。 [desman2025, p.9] ← [[reinforcement-learning-mdp]]
- desman2025-C4: 強化學習的「獎勵」是依血糖是否在目標範圍打分：血糖在 140 至 180 mg/dL 時最高為 +0.2，離開範圍後罰則越來越重，最低到 −1。 [desman2025, p.9] ← [[reinforcement-learning-mdp]]
- desman2025-C5: 這篇的「離線」學習，意思是只用已經收集好的紀錄來學，學習過程不與病人互動，不是在病人身上邊做邊試。 [desman2025, p.2] ← [[reinforcement-learning-mdp]]
- desman2025-C6: 離線策略評估（OPE）不實際施行新策略，而是從既有資料估計學到的策略的表現；論文用它來估計 GLUCOSE 的表現。 [desman2025, p.9] ← [[off-policy-evaluation]]
- desman2025-C7: 離線評估的結果：GLUCOSE 的估計報酬在內部測試為 0.0、外部驗證為 −0.63；醫師的報酬分別為 −1.29 與 −1.02。 [desman2025, p.2] ← [[off-policy-evaluation]]
- desman2025-C8: 估計報酬高不等於證明比醫師好：論文用「顯著改善」描述，但它仍是對自己建議的離線估計，不是觀察到的病人結局。 [desman2025, p.2] ← [[off-policy-evaluation]]
- desman2025-C9: 除了離線評估，論文還請兩位資深加護醫師，對 GLUCOSE 與全部 8 組人類建議做盲評，對象是同一批病人，用 5 分的 Likert 量表評安全性、有效性與可接受度。 [desman2025, p.5] ← [[desman2025]]
- desman2025-C10: 醫師盲評的結果：GLUCOSE 的安全性、有效性與可接受度評分和所有人類建議相當，或顯著較高。 [desman2025, p.6] ← [[desman2025]]
- desman2025-C11: 論文另外用外部驗證資料 eICU-CRD 來檢查：它來自 208 家美國醫院，年份為 2014 年至 2015 年。 [desman2025, p.8] ← [[desman2025]]
- desman2025-C12: 論文自己承認的限制：這是回溯性研究，需要大型、多樣病人群的前瞻性研究與臨床試驗來驗證。 [desman2025, p.7] ← [[desman2025]]
