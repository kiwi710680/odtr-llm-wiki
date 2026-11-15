# 證據卡：bluemlein2022

- bluemlein2022-C1: 「倒推」只是估計的順序從最後一個決策時間點開始往前做，資料仍按時間記錄；因為現在該怎麼決定，要考慮之後會採取哪些決定。 [bluemlein2022, p.5] ← [[backward-recursion]]
- bluemlein2022-C2: 結局只在最後一步才看得到，所以每一步改為最佳化「偽結局」，也就是假如病人在之後的時間步都被最佳治療，會有的潛在結局。 [bluemlein2022, p.6] ← [[backward-recursion]]
- bluemlein2022-C3: 倒推時每一步都先估計「治療的效果」，效果為正就給治療，否則不給。 [bluemlein2022, p.7] ← [[backward-recursion]]
- bluemlein2022-C4: 論文說，若把完整病史只配一個模型，會得到有偏的動態治療策略，所以要把連續決策拆成一組單步問題。 [bluemlein2022, p.6] ← [[backward-recursion]]
- bluemlein2022-C5: 論文要找「可解釋、又能處理複雜關係」的學習方法，因為來自機器學習的路線多為黑箱，一般不適合個人化醫療。 [bluemlein2022, p.2] ← [[bluemlein2022]]
- bluemlein2022-C6: 因果樹把病人分成幾群，每一群（葉子）的治療效果，就是該群治療組與未治療組平均結局的差。 [bluemlein2022, p.9] ← [[causal-tree-and-forest]]
- bluemlein2022-C7: 用因果樹的版本（DTR-CT）可以把每個時間步的決策樹畫出來，讓人看得懂規則；用因果森林的版本（DTR-CF）則看變數重要性。 [bluemlein2022, p.10-11] ← [[bluemlein2022]]
- bluemlein2022-C8: 真實資料的應用是 MIMIC-III 的加護病房觀察資料：依序決定要不要使用機械通氣或血管加壓素，目標是縮短住院時間。 [bluemlein2022, p.14] ← [[bluemlein2022]]
- bluemlein2022-C9: 真實資料只納入至少被治療過十次的病人（共 8,059 位），並使用前面一段時間（前 10 小時）的病史。 [bluemlein2022, p.15] ← [[bluemlein2022]]
- bluemlein2022-C10: 論文摘要說，在模擬資料上，兩個方法在累積後悔值與最佳決策的百分比上，以相當大的差距勝過最新基準方法。 [bluemlein2022, p.1] ← [[bluemlein2022]]
- bluemlein2022-C11: 在非線性交互作用的模擬情境中，DTR-CT 與 DTR-CF 的累積後悔值分別降低 25.1 % 與 48.2 %（後悔值越小越好）。 [bluemlein2022, p.13] ← [[bluemlein2022]]
- bluemlein2022-C12: 真實資料沒有真正的最佳答案可比，論文明說不與其他方法比較，因為估計的處理效應尺度隨方法而異，所以不同方法的數字不應直接比大小。 [bluemlein2022, p.16] ← [[bluemlein2022]]
