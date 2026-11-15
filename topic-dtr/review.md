# G5 faithfulness review, round 3 (last round): topic-dtr drafts

Reviewer: fresh-context verifier (did not write the drafts). Scope: s07–s14 (s01–s06 passed earlier).
Inputs read: `drafts/s07.md`–`drafts/s14.md`, `cards/*.md`, `review_round2.md`, `wiki/glossary.md`, `wiki/sources/{bluemlein2022,desman2025}.md` (relevant sections), and `wiki/concepts/{identification-assumptions,rate-double-robustness,doubly-robust-learner,cross-fitting,causal-tree-and-forest,finite-mixture-subphenotypes,mechanical-power,reinforcement-learning-mdp,off-policy-evaluation}.md`. I also grepped `wiki/` for each glossed term (協變數, 涵蓋率, 保護性, 呼氣末正壓, 肺損傷, 敏感度分析, ARDS). Drafts were not edited.

Rule applied, as in round 2: a gloss whose content is nowhere in the wiki, or contradicts it, fails F1. Analogies that assert no facts are allowed.

| slide | F1 | F2 | F3 | F4 | round-2 fixed? | problem (quote exact text) | minimal fix |
|---|---|---|---|---|---|---|---|
| s07 | PASS | PASS | PASS | PASS | yes. The Note now says 「一致性＝在實際接受的那個治療下，假想的結局就是真正觀察到的結局」. That matches `identification-assumptions`: 「一個觀察值在其實際接受的治療水準下，反事實結局就是我們真正觀察到的結局」. | none (see non-blocking items 1–2) | — |
| s08 | PASS | PASS | PASS | PASS | yes. (a) The Note now says 「兩個輔助模型只要有一個設定正確，估計就一致；但要算出可信的信賴區間，論文的變異數估計要求兩個輔助模型都被一致地估計」. That matches `rate-double-robustness`: 「這個變異數估計式要求兩個干擾函數都被一致地估計」. (b) The 名目涵蓋率 gloss was removed. The bullet now reads 「涵蓋率符合宣稱的信賴區間」, which only restates 「名目涵蓋率」 in plain words and adds no new fact. | none (see non-blocking items 3–5) | — |
| s09 | PASS | PASS | PASS | PASS | yes. The Note now says 「因果森林＝許多棵因果樹的集成，用相似病人的加權平均估計每個人的治療效果」. That matches the glossary: 「許多棵因果樹的集成，以局部鄰域的加權平均估計每位病人的處理效應」. | none (see non-blocking item 6) | — |
| s10 | PASS | PASS | PASS | PASS | yes. (a) The Note now says 「急性呼吸衰竭＝需要立即處置的急症，論文定義為在室內空氣下低血氧與／或高二氧化碳」, which matches the glossary word for word. (b) The Note now says 「潮氣量、平台壓都是呼吸器的參數，保護性通氣會限制它們以減少肺損傷」. That matches `mechanical-power`: 「保護性通氣：限制潮氣量、平台壓與驅動壓，用來減少通氣造成的肺損傷」. The 機械功率 gloss (平台壓、呼吸速率與呼氣末正壓) matches the same page. | none (see non-blocking items 7–8) | — |
| s11 | PASS | PASS | PASS | PASS | yes. The Note now says 「SOFA 分數＝論文用來反映病人嚴重度的指標之一」. | none (see non-blocking item 9) | — |
| s12 | PASS | PASS | PASS | PASS | yes. The slide now says 「報酬是把上一頁的『獎勵』逐小時累加的分數」. That matches `reinforcement-learning-mdp`: 「累積獎勵｜依血糖範圍計分、再逐小時累加。[desman2025, p.2] [desman2025, p.9]」. The slide's citations are the same two pages. The physicians' −1.29 is no longer at odds with the 「最低到 −1」 on s11. | none (see non-blocking items 10–11) | — |
| s13 | PASS | PASS | PASS | PASS | yes. The Note now says 「鴉片使用障礙（opioid use disorder）是 williams2024 範例的疾病情境」. That matches the glossary: 「論文範例的疾病情境」. | none (see non-blocking item 12) | — |
| s14 | PASS | PASS | PASS | PASS | yes. The 前瞻性 gloss was removed. The Note now repeats only what the paper says: 「論文自己說，目前的結果還需要前瞻性研究與臨床試驗來驗證」 (`off-policy-evaluation`, `desman2025` C12). | none (see non-blocking item 13) | — |

## 非阻擋建議

1. s07 (carried over from round 2, item 3, still unchanged): the Note 「最直覺的一條是正值性：如果資料裡沒人照某條規則做過，就沒有東西可以拿來學或比較」 merges positivity with the rule-support condition. `identification-assumptions` lists that condition separately as an 額外條件. The title also says 「三個前提」, but bullet 2 adds a fourth condition. Consider 「最直覺的是正值性：如果某種病人從來沒人接受過某個治療，就無從比較」, and in bullet 2, 「另外還要求：…」.
2. s07: the gloss 「協變數＝要一併考慮的背景資料」 is not defined in the wiki. The wiki's examples include time-varying measures such as blood gases (hong2021, 「血氣與實驗室指標等協變數」), so 「背景資料」 is slightly narrow. Consider 「協變數＝分析時一併納入的病人資料，例如年齡、血氣」.
3. s08 bullet 5, 「在單一時間點的問題上」 (carried over from round 2, item 5): `doubly-robust-learner` qualifies this with 「以平均處理效應為例」, and `renson2025` notes that some estimands have no EIF (e.g. 「連續治療的劑量反應曲線」). Consider 「以平均處理效應這類問題為例」.
4. s08 F4: 「一致」, 「涵蓋率」, 「標準誤」, 「推論」 and 「輔助模型」 are not explained for beginners. The glossary entry for 干擾函數 offers 「需要估計但不是最終目標的函數，例如結局迴歸、傾向分數」 for 輔助模型.
5. s08: the analogy 「出題的人和評分用的資料不要是同一批」 mixes a person with data. The wiki's own analogy is clearer: 「一半用來教、另一半用來考」 (`cross-fitting`).
6. s09 (carried over from round 2, items 7–9): 「變數重要性」 and the 「累積」 in 累積後悔值 are not explained. Bullet 2 shows an unweighted mean difference, but the wiki says 「結局先以逆傾向分數加權」. The kicker says 「方法路線二」, but no slide is labelled 方法路線一.
7. s10 bullet 5 (carried over from round 2, item 11): 「所以通氣策略要隨時調整」 drops the attribution in C7 (「論文以此說明為什麼…」). Consider 「論文以此說明通氣策略要隨時調整」.
8. s10 (carried over from round 2, item 10): 「ARDS」 is still not explained. In the wiki's hong2021 cohort, ARDS is 117 位（1%） of the ARF patients. Bullet 4, 「用兩種分群方法檢查，都指向 3 類」, is acceptable. Note, though, that `finite-mixture-subphenotypes` warns that AIC and SABIC did not stop at 3 classes.
9. s11 reward bullet (carried over from round 2, item 12): it omits the dose penalty (`reinforcement-learning-mdp`: 「另有一項隨劑量增大的懲罰」).
10. s12 (carried over from round 2, item 13): 「內部測試＝…沒用來訓練的病人」 is correct. The wiki adds, however, that the internal test set was used to pick GLUCOSE from 200 models (「外部驗證的 −0.63 才是沒參與挑選的估計」). 「醫師盲評」 still has no context (C9 is not used).
11. s12 F4: the bullet 「報酬是…逐小時累加的分數」 is immediately followed by 「最高獎勵是 +0.2，所以 0.0 只表示在這個計分下的平均表現」. A beginner may ask why an hourly maximum explains a summed total. The sentence is a faithful copy of C13, so this is a clarity point only.
12. s13 Note 「依病人當下的情況」 (carried over from round 2, item 14): s03 defined the rule input as the history up to now. Consider 「依病人到那時為止的情況」.
13. s14 (carried over from round 2, item 15): the takeaway 「但從資料學出的規則，仍要驗證才能說它有益。」 still has no citation. In item 2, 「這類估計式」 still has no antecedent on the slide; write 「倍增穩健這類估計式（第 8 頁）」.

13 non-blocking items in total.

G5: PASS
