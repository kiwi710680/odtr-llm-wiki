# N3 outline — 動態治療策略是什麼？（14 頁）

教學主線：為什麼平均不夠 → 什麼是動態規則 → 一個完整例子 → 怎麼學 → 結果怎麼讀 → 前提 → 三條方法路線（倍增穩健／因果樹／強化學習）→ 怎麼評估 → 帶走什麼。
格式：`- sNN | 標題 | 這頁要讓外行人懂什麼 | claims: ...`

- s01 | 動態治療策略是什麼？ | 封面：一句話說出主題與讀者 | claims:
- s02 | 平均效果，回答不了「我該怎麼治療」 | 平均處理效應只描述平均；治療是一連串決定 | claims: williams2024-C3, williams2024-C4
- s03 | 靜態規則 vs 動態規則 | 兩種規則的差別，用 d1 當最簡單的動態規則例子 | claims: williams2024-C1, williams2024-C2, williams2024-C6
- s04 | 例子：BUP-NX 什麼時候該加量？ | 把抽象概念落到一個具體問題：時間點、治療、目標 | claims: williams2024-C5, williams2024-C6
- s05 | 怎麼學：從最後一步往回推 | 倒推遞迴與偽結局的直覺 | claims: bluemlein2022-C1, bluemlein2022-C2, bluemlein2022-C3, williams2024-C7
- s06 | 學出來的規則有比較好嗎？ | 讀懂風險、RR、信賴區間，以及「跟簡單規則差不多」 | claims: williams2024-C8, williams2024-C9, williams2024-C10, williams2024-C11
- s07 | 用病歷資料學規則，先要有三個前提 | 一致性、可交換性、正值性；資料裡要有人照規則做過 | claims: williams2024-C13, williams2024-C14, hong2021-C10
- s08 | 先決定「想要的數字」，再選估計方法 | estimand 先於 estimator；直接代入 ML 預測的問題；交叉擬合 | claims: renson2025-C1, renson2025-C4, renson2025-C6, renson2025-C7
- s09 | 看得懂的規則：因果樹 | 為什麼要可解釋；樹怎麼分群；模擬結果 | claims: bluemlein2022-C5, bluemlein2022-C6, bluemlein2022-C7, bluemlein2022-C11
- s10 | 例子：呼吸器的「劑量」也能動態調整 | 連續劑量、先分群、類別隨時間改變、結果是關聯 | claims: hong2021-C2, hong2021-C4, hong2021-C5, hong2021-C7, hong2021-C8
- s11 | 另一條路：強化學習調胰島素 | 狀態、行動、獎勵；離線學習 | claims: desman2025-C1, desman2025-C2, desman2025-C3, desman2025-C4, desman2025-C5
- s12 | 不能拿病人試，怎麼知道規則好不好？ | 離線評估、外部驗證、醫師盲評，以及它們不能證明什麼 | claims: desman2025-C6, desman2025-C7, desman2025-C8, desman2025-C10, desman2025-C11
- s13 | 四個例子並排看 | 同一個概念在不同臨床問題長什麼樣 | claims: williams2024-C5, bluemlein2022-C8, hong2021-C4, desman2025-C1
- s14 | 帶走三件事 | 動態規則的價值、證據的強度、常見誤解 | claims: williams2024-C12, renson2025-C9, hong2021-C9, desman2025-C12
