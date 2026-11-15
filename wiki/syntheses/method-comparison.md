---
title: 方法比較：估計式家族與「倍增穩健」的兩種意思
type: synthesis
sources: [renson2025, williams2024, bluemlein2022, hong2021, desman2025]
updated: 2026-11-15
---

# 方法比較：估計式家族與「倍增穩健」的兩種意思

這一頁把 [[renson2025]] 與 [[williams2024]] 對同一批工具的說法放在一起。重點是：兩篇的目標不同，所以同一個名字（AIPW、倍增穩健）出現時，要先問「它在估計什麼」。本頁只整理兩篇各自說了什麼，不評斷誰對。加入 [[bluemlein2022]] 之後（見文末「加入 bluemlein2022 之後」一節），仍沒有發現互相矛盾的陳述：各篇談的是不同性質或不同條件，所以沒有建立 disagreements 頁。

## 兩篇的目標不同

- renson2025：教學如何為一個估計目標推導出能搭配機器學習、又有有效推論的估計式；範例估計目標是不治療時的平均結局。[renson2025, p.2]
- williams2024：教學如何從縱貫資料學出最佳動態治療規則；方法的核心是估計 blip 函數，並用依序倍增穩健估計式估計最佳規則下的平均結局。[williams2024, p.5]
- 動態治療規則的學習，renson2025 沒有討論：來源未提及。[renson2025, p.2]

## 估計式對照

| 工具 | renson2025 怎麼說 | williams2024 怎麼說 |
|---|---|---|
| g 計算法／代入式 | 範例的代入式估計式對應 g 計算法；用機器學習估計干擾函數時一般無法正確推論。[renson2025, p.3] | 本 wiki 的 williams2024 頁未記載。 |
| 逆機率加權（IPW） | 與 g 計算法同屬非速率倍增穩健的例子。[renson2025, p.3] | 本 wiki 的 williams2024 頁未記載。 |
| 增強型逆機率加權（AIPW） | 單步估計式就是 AIPW，用來估計不治療時的平均結局。[renson2025, p.3] | AIPW 轉換是 blip 函數的無偏轉換，估計 blip 而非平均結局。[williams2024, p.3] |
| 目標最大概似估計（TMLE）、雙重／去偏機器學習 | 提到這兩類 EIF 型估計式，單步估計式是雙重／去偏機器學習的特例。[renson2025, p.5] | 本 wiki 的 williams2024 頁未記載。 |
| 交叉擬合／樣本分割 | 干擾函數須在另一份樣本估計，簡單版是分成兩半再交換。[renson2025, p.4] | 範例中 Q 與 g 用交叉擬合估計；樣本分割可繞過「夠平滑」的條件。[williams2024, p.5] |
| 超級學習器 | 來源未提及。 | 範例用離散超級學習器估計 Q 與 g。[williams2024, p.5] |
| 變異數估計 | 以估計 EIF 的樣本變異數除以 n。[renson2025, p.5] | 以 log RR 影響函數的樣本變異數估計風險比的變異數。[williams2024, p.5] |

## 「倍增穩健」的兩種意思

- williams2024 的說法：Q 或 g 只要有一個被一致估計，就能得到 blip 函數的無偏估計。條件：兩個函數至少一個一致。[williams2024, p.3]
- renson2025 區分兩個性質。倍增穩健一致性：兩個干擾估計式中有一個設定正確，估計式就一致。速率倍增穩健：估計式誤差是兩個干擾估計式誤差的乘積，用來保證有效推論。[renson2025, p.4]
- renson2025 的變異數估計式要求兩個干擾函數都被一致估計。條件：兩者都一致。[renson2025, p.5]
- 本 wiki 的判讀：williams2024 的「倍增穩健」描述的是第一種性質，renson2025 把它與第二種性質分開；兩者談的是不同性質，並不互相否定。williams2024 是否討論速率倍增穩健：來源未提及。
- 詳見 [[doubly-robust-learner]]、[[rate-double-robustness]]。

## 加入 bluemlein2022 之後

[[bluemlein2022]] 的目標是提出新方法：用因果樹與因果森林學最佳 DTR。它和前兩篇的重疊在「多個時間點」與「倍增穩健」。本節只整理三篇各自說了什麼。[bluemlein2022, p.1]

| 面向 | williams2024 | renson2025 | bluemlein2022 |
|---|---|---|---|
| 目標 | 教學如何從縱貫資料學最佳規則。[williams2024, p.1] | 教學如何推導搭配機器學習的估計式。[renson2025, p.1] | 提出 DTR-CT 與 DTR-CF 兩個新方法。[bluemlein2022, p.1] |
| 多個時間點 | 從最後一個時間點往回做。[williams2024, p.5] | 只討論單一時間點。[renson2025, p.2] | 倒推遞迴與偽結局，見 [[backward-recursion]]。[bluemlein2022, p.7] |
| 估計 blip／HTE 的工具 | 倍增穩健的 AIPW 轉換，再迴歸。[williams2024, p.3] | 估計目標不是 blip。[renson2025, p.3] | 逆傾向分數加權後，用因果樹或因果森林。[bluemlein2022, p.7] |
| 傾向分數與結局模型 | 範例用交叉擬合的超級學習器。[williams2024, p.5] | 兩者是干擾函數，可用機器學習估計。[renson2025, p.3] | 傾向分數用邏輯斯迴歸，結局模型由樹或森林擔任。[bluemlein2022, p.7] |
| 樣本分割 | 範例用交叉擬合。[williams2024, p.5] | 干擾函數須在另一份樣本估計。[renson2025, p.4] | 誠實分割：訓練集與估計集。[bluemlein2022, p.8] |
| 可解釋性 | 提到決策樹可得到好解讀的規則。[williams2024, p.4] | 來源未提及。 | 核心賣點，見 [[interpretability]]。[bluemlein2022, p.2] |
| 實證 | 鴉片使用障礙病人的劑量資料。[williams2024, p.5] | 沒有新資料。[renson2025, p.5] | 模擬資料與 MIMIC-III 加護病房資料。[bluemlein2022, p.1] |
| 評估學出的規則 | 規則價值的估計與風險比。[williams2024, p.6] | 沒有。[renson2025, p.5] | 後悔值、決策準確度、期望增益，見 [[regret-and-decision-accuracy]]。[bluemlein2022, p.13] |
| Q 學習 | 只列名為迴歸式方法的一類。[williams2024, p.3] | 來源未提及。 | 線性基準方法，見 [[q-learning-dwols-g-estimation]]。[bluemlein2022, p.12] |

### 「倍增穩健」的第三種說法

- bluemlein2022 的說法：類比 DWOLS，用逆傾向分數加權結局；每個時間步只要傾向分數模型或處理效應模型有一個設定正確且無偏，就得到無偏的處理效應估計。條件：兩個模型至少一個設定正確。[bluemlein2022, p.10]
- 它的論證方式：因果樹與因果森林是 HTE 的無偏估計式，最大概似是邏輯斯迴歸參數的無偏估計式，所以方法也是倍增穩健。[bluemlein2022, p.10]
- 與 williams2024 的對照：兩者的條件都是「兩個函數至少一個正確」，但 williams2024 用 AIPW 轉換，bluemlein2022 用逆傾向分數加權。[williams2024, p.3] [bluemlein2022, p.7]
- 與 renson2025 的對照：renson2025 把「倍增穩健一致性」與「速率倍增穩健」分開，並說逆機率加權（IPW）不是速率倍增穩健的例子。[renson2025, p.3] [renson2025, p.4]
- bluemlein2022 是否討論收斂速率或信賴區間：來源未提及。
- 本 wiki 的判讀：bluemlein2022 的「倍增穩健」屬於第一種性質（一致性或無偏性），沒有主張第二種性質（速率）；所以三篇沒有互相否定。但 bluemlein2022 的論證是以無偏性類推，正文沒有看到速率層面的說明，日後引用時要說清楚是哪一種。

### 其他並排觀察

- 估計 HTE 的做法：williams2024 以迴歸（例如 ℓ1 正規化）估計 blip，bluemlein2022 以樹或森林估計；兩者都屬資料自適應的方法，但可解釋性的程度不同，見 [[interpretability]]。[williams2024, p.5] [bluemlein2022, p.10]
- 古典 Q 學習的假設：低維、線性、已知的函數形式；williams2024 與 renson2025 的方法則強調可以搭配彈性的機器學習。[bluemlein2022, p.22] [williams2024, p.4] [renson2025, p.1]

## 加入 hong2021 之後

[[hong2021]] 是臨床應用研究，不是方法論文：它用既有的 dWOLS 估計連續劑量的最佳規則，前面多了一步無監督分類。本節只整理四篇各自說了什麼；臨床情境的並排見 [[dtr-clinical-applications]]。[hong2021, p.1] [hong2021, p.3]

| 面向 | williams2024 | bluemlein2022 | hong2021 |
|---|---|---|---|
| 目標 | 教學如何從縱貫資料學最佳規則。[williams2024, p.1] | 提出 DTR-CT 與 DTR-CF 兩個新方法。[bluemlein2022, p.1] | 臨床應用：把個人化通氣策略形式化。[hong2021, p.1] |
| 治療的型態 | 二元：每週劑量有沒有增加。[williams2024, p.5] | 二元：治療或不治療。[bluemlein2022, p.4] | 連續劑量（機械功率），見 [[mechanical-power]]。[hong2021, p.3] |
| 估計 blip 的工具 | 倍增穩健的 AIPW 轉換，再迴歸。[williams2024, p.3] | 因果樹或因果森林。[bluemlein2022, p.7] | dWOLS，參數式的 blip，含劑量的一次項與二次項。[hong2021, p.3] |
| 先分亞型？ | 本 wiki 的 williams2024 頁未記載。 | 樹的葉子是依處理效應分出的群。[bluemlein2022, p.8] | 先以有限混合模型分成三類，再放進模型，見 [[finite-mixture-subphenotypes]]。[hong2021, p.2] [hong2021, p.3] |
| 資料 | 試驗的 BUP-NX 組。[williams2024, p.5] | 模擬資料與 MIMIC-III。[bluemlein2022, p.1] | MIMIC-IV 單一資料庫。[hong2021, p.2] |
| 時間點 | 每週。[williams2024, p.2] | 模擬 3 個時間步，真實資料前 10 小時。[bluemlein2022, p.11] [bluemlein2022, p.15] | 每 8 小時，共 7 個時間點。[hong2021, p.2] |
| 評估學出的規則 | 規則價值的估計與風險比。[williams2024, p.6] | 後悔值、決策準確度、期望增益。[bluemlein2022, p.13] | ΔMP 與死亡的關聯。[hong2021, p.4] |
| 倍增穩健 | 主張，條件是 Q 或 g 至少一個一致。[williams2024, p.3] | 主張，條件是兩個模型至少一個設定正確。[bluemlein2022, p.10] | 正文沒有主張；引用文獻的標題含倍增穩健。[hong2021, p.3] [hong2021, p.9] |

### 並排觀察

- 「驗證」的意思不同：williams2024 估計規則價值，bluemlein2022 在真實資料看期望增益，hong2021 看實際用量偏離最佳用量與死亡的關聯。三者回答的是不同問題，彼此沒有矛盾。[williams2024, p.6] [bluemlein2022, p.16] [hong2021, p.4]
- 函數形式：bluemlein2022 說古典線性方法假設函數形式已知而受限；hong2021 用 dWOLS 並由作者指定交互作用項與二次項，沒有與其他方法比較。兩篇的目的不同（比較方法表現，對臨床應用），所以不是互相否定。[bluemlein2022, p.22] [hong2021, p.3]
- 結論的措辭：hong2021 的結論是最佳 MP 可能有助於改善存活，需要前瞻性試驗檢驗；本 wiki 把它的估計當成關聯，不當成因果。[hong2021, p.1] [hong2021, p.8]
- 加入 hong2021 之後仍沒有發現互相矛盾的陳述，所以沒有新增 disagreements 條目。

## 加入 desman2025 之後

[[desman2025]] 是臨床應用研究，但用的是強化學習這條路線：保守 Q 學習加分布式的部分，不是前四篇的迴歸式、樹式或估計式推導。本節只整理它與其他篇各自說了什麼；整體導覽見 [[overview-for-beginners]]。[desman2025, p.1] [desman2025, p.9]

| 面向 | desman2025 | 對照的來源怎麼說 |
|---|---|---|
| 目標 | 建一個建議每小時胰島素劑量的演算法。[desman2025, p.1] | hong2021：把個人化通氣策略形式化。[hong2021, p.1] |
| 治療的型態 | 連續劑量，每小時的胰島素量。[desman2025, p.9] | hong2021：連續劑量（機械功率）；bluemlein2022：二元。[hong2021, p.3] [bluemlein2022, p.4] |
| 時間點 | 每小時，只用前 24 小時。[desman2025, p.8] | hong2021：每 8 小時，共 7 個時間點；bluemlein2022：真實資料前 10 小時。[hong2021, p.2] [bluemlein2022, p.15] |
| 估計規則的工具 | 保守 Q 學習加隱含分位數網路，三層隱藏層的神經網路。[desman2025, p.9] | hong2021：dWOLS；bluemlein2022：因果樹或因果森林。[hong2021, p.3] [bluemlein2022, p.7] |
| 時間結構的處理 | 馬可夫決策過程加折扣因子，見 [[reinforcement-learning-mdp]]；倒推遞迴：來源未提及。[desman2025, p.9] | bluemlein2022：倒推遞迴與偽結局，見 [[backward-recursion]]。[bluemlein2022, p.7] |
| 評估學出的規則 | 離線策略評估、血糖在範圍內的時間比例、與內分泌科醫師的平均絕對誤差、盲評；見 [[off-policy-evaluation]]。[desman2025, p.2] [desman2025, p.5] [desman2025, p.6] | hong2021：ΔMP 與死亡的關聯；bluemlein2022：後悔值、決策準確度、期望增益。[hong2021, p.4] [bluemlein2022, p.13] |
| 外部資料驗證 | eICU-CRD。[desman2025, p.2] | 前三篇：來源未提及，見 [[dtr-clinical-applications]]。 |
| 倍增穩健、有效影響函數 | 來源未提及。 | williams2024、bluemlein2022 主張倍增穩健；renson2025 推導相關估計式。[williams2024, p.3] [bluemlein2022, p.10] [renson2025, p.1] |

### 並排觀察

- 「Q 學習」同名但不同脈絡：desman2025 的保守 Q 學習屬於離線強化學習；bluemlein2022 的 Q 學習是來自統計學的線性迴歸式方法。論文沒有說明兩者的關係：來源未提及。見 [[q-learning-dwols-g-estimation]]。[desman2025, p.8] [bluemlein2022, p.22]
- 「驗證」的意思不同：desman2025 是離線估計的報酬加專家評估，hong2021 是偏離最佳用量與死亡的關聯，williams2024 是規則價值的估計。三者回答不同的問題，彼此沒有矛盾。[desman2025, p.2] [hong2021, p.4] [williams2024, p.6]
- 可解釋性：bluemlein2022 說強化學習多為深度學習、不易解釋；desman2025 用的是神經網路加事後的 SHAP 說明，兩者談的是不同層次（路線的一般特徵、對一個模型的事後說明），不是互相否定。見 [[interpretability]]。[bluemlein2022, p.2] [desman2025, p.10]
- 加入 desman2025 之後仍沒有發現互相矛盾的陳述，所以沒有新增 disagreements 條目。

## 相關頁面

- [[plug-in-and-one-step-estimators]]
- [[cross-fitting]]
- [[nuisance-functions]]
- [[efficient-influence-function]]
- [[backward-recursion]]
- [[causal-tree-and-forest]]
- [[interpretability]]
- [[regret-and-decision-accuracy]]
- [[q-learning-dwols-g-estimation]]
- [[mechanical-power]]
- [[finite-mixture-subphenotypes]]
- [[dtr-clinical-applications]]
- [[reinforcement-learning-mdp]]
- [[offline-reinforcement-learning]]
- [[distributional-reinforcement-learning]]
- [[off-policy-evaluation]]
- [[overview-for-beginners]]

- [[glossary]]
