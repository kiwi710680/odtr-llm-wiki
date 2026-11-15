# G5 faithfulness review, round 2: topic-dtr drafts

Reviewer: fresh-context verifier (did not write the drafts). Scope: s01, s03, s04, s05, s07–s14 (s02, s06 passed in round 1 and are unchanged).
Inputs read: `drafts/sNN.md` for the slides in scope, `cards/*.md`, `review_round1.md`, `wiki/glossary.md`, `wiki/sources/{williams2024,bluemlein2022,hong2021,renson2025,desman2025}.md`,
`wiki/concepts/{dynamic-treatment-regime,identification-assumptions,backward-recursion,cross-fitting,doubly-robust-learner,statistical-estimand,plug-in-and-one-step-estimators,rate-double-robustness,causal-tree-and-forest,regret-and-decision-accuracy,mechanical-power,finite-mixture-subphenotypes,reinforcement-learning-mdp,off-policy-evaluation}.md`.
I also ran grep over `wiki/` to check whether a glossed term is defined anywhere in the wiki. Drafts were not edited.

How I applied F1 to glosses: the brief says a gloss that "contradicts or goes beyond the wiki is a FAIL", and AGENTS.md §4 says the deck "may use only wiki content". So a gloss whose content appears nowhere in the wiki counts as FAIL even when it is a correct textbook definition. These failures are marked **[gloss]**; each needs only a one-line fix. The failures marked **[substance]** misstate a source or lead a beginner to a conclusion the wiki explicitly rejects.

| slide | F1 | F2 | F3 | F4 | round-1 fixed? | problem (quote exact text) | minimal fix |
|---|---|---|---|---|---|---|---|
| s01 | PASS | PASS | PASS | PASS | yes (claims now `[williams2024-C4]`, and the text matches C4 exactly) | none | — |
| s03 | PASS | PASS | PASS | PASS | yes (「一個簡單的動態規則例子 d1」 / 「d1 就是一條簡單的…規則」) | none | — |
| s04 | PASS | PASS | PASS | PASS | yes (the takeaway is now cited and names what the rule looks at) | none (see non-blocking item 2) | — |
| s05 | PASS | PASS | PASS | PASS | n/a (passed in round 1) | none | — |
| s07 | FAIL | PASS | PASS | PASS | yes: hong2021 line now matches C10 with its own p.2 citation; glosses added; title changed | **[gloss]** Note 「一致性＝紀錄上接受的治療，就是我們想比較的那個治療」 is about the treatment, but the wiki defines consistency in terms of the outcome: 「一個觀察值在其實際接受的治療水準下，反事實結局就是我們真正觀察到的結局」 (`identification-assumptions`; glossary: 「觀察到的治療水準下，反事實結局就是實際觀察到的結局」). This wording came from round 1's suggested fix, but it is not what the wiki says. | 「一致性＝病人實際接受了某個治療，我們看到的結局，就是『接受那個治療』時會有的結局」 |
| s08 | FAIL | PASS | PASS | PASS | partly: the scope line (「只討論二元治療…單一時間點」) and the glosses were added; 「以平均處理效應為例」 was replaced by 「在單一時間點的問題上」 (see non-blocking item 5) | (a) **[substance]** Note 「倍增穩健＝需要兩個輔助模型，只要有一個設定正確，估計就站得住。」 sits next to the bullet 「倍增穩健…仍可得到（大樣本下）名目涵蓋率的信賴區間」. Read together, they say "one correct model is enough for a valid CI". The wiki lists exactly this as a misconception (`rate-double-robustness`): 「『兩個干擾估計式只要有一個準就夠做推論』：論文的變異數估計式要求兩個干擾函數都被一致估計。[renson2025, p.5]」. (b) **[gloss]** 「名目涵蓋率＝區間宣稱有多少把握，實際包到真值的比例就真的接近多少」: the wiki never defines 名目涵蓋率 (grep finds it only in the C7 sentence). | (a) 「倍增穩健＝兩個輔助模型只要有一個設定正確，估計值就會趨近正確答案；但要信賴區間可信，論文還要求兩個都估得夠好（見第 14 頁）」 (b) Drop the gloss and write 「…仍可得到大樣本下可信的信賴區間」, or have the wiki define the term first. |
| s09 | FAIL | PASS | PASS | PASS | yes: comparator 「與表現最好的基準方法相比」 added; 後悔值 explained | **[gloss]** Note 「因果森林＝很多棵因果樹一起投票」. The wiki describes a weighted neighbour average, not voting: 「某位病人的 HTE 不是簡單平均，而是對局部鄰域的加權平均，權重是其他病人與他落在同一片葉子的頻率」 (`causal-tree-and-forest`; glossary 「許多棵因果樹的集成，以局部鄰域的加權平均估計」). Round 1 had suggested 「投票」. | 「因果森林＝很多棵因果樹合在一起；估某位病人時，看『常和他分在同一群的人』的平均效果」 |
| s10 | FAIL | FAIL | PASS | PASS | yes: ARDS scope restored, entropy/k-means replaced, kicker changed, 機械功率 glossed | (a) **[substance]** Note 「急性呼吸衰竭＝肺突然無法順利交換氣體、需要呼吸器幫忙的情況」 turns 「重症…常需要用呼吸器」 (hong2021-C1; glossary 機械通氣: 「重症 ARF 常需要的侵入性通氣」) into part of the definition. The wiki's definition is 「在室內空氣下低血氧與／或高二氧化碳」 (glossary). (b) **[gloss]** 「潮氣量＝每次呼吸送進肺的氣體量；平台壓＝送氣時肺裡承受的壓力」: neither term is defined anywhere in the wiki. | (a) 「急性呼吸衰竭＝在沒有額外給氧時，血氧太低或二氧化碳太高；重症病人常需要呼吸器」 (b) Drop both glosses and write 「潮氣量、平台壓都是呼吸器的設定數值，指引對它們訂了上限」 (`mechanical-power`: 「指引常見的建議是潮氣量與平台壓的上限」). |
| s11 | FAIL | PASS | PASS | PASS | n/a (passed in round 1; the optional SOFA gloss was added) | **[gloss]** 「SOFA 分數＝器官衰竭嚴重度分數」: the wiki only says SOFA is one of the 「反映病人嚴重度的指標」 (`desman2025`, SHAP results). 「器官衰竭」 is not in the wiki. | 「SOFA 分數＝反映病人病情嚴重度的指標之一」 |
| s12 | FAIL | PASS | PASS | FAIL | partly: the 報酬–獎勵 link and the scale were added, but 報酬 was equated with 獎勵 instead of defined as the accumulated reward | **[substance]** 「這裡的報酬就是上一頁的『獎勵』：0.0 是作者設計的計分尺度上的數字，最高獎勵是 +0.2…」. In the wiki, the return is the reward added up over the hours (`reinforcement-learning-mdp`: 「結局 ↔ 累積獎勵：依血糖範圍計分、再逐小時累加」), and the reward also includes a dose penalty. If 報酬 equalled 獎勵, the physicians' −1.29 on the same slide could not exist, because s11 says the reward 「最低到 −1」. A classmate who checks this gets two contradictory numbers. | 「這裡的報酬是把上一頁每小時的『獎勵』累加起來的估計值（作者自訂尺度，越高越好）；最高獎勵是 +0.2，所以 0.0 只表示在這個計分下的平均表現」 |
| s13 | FAIL | PASS | PASS | PASS | n/a (passed in round 1; the OUD gloss is new) | **[gloss]** Note 「鴉片使用障礙＝使用鴉片類藥物而造成問題、需要治療的情況」: the wiki gives no definition (glossary: 「論文範例的疾病情境」). | 「鴉片使用障礙＝論文範例的疾病；BUP-NX 是用來治療它的藥物」 (`dynamic-treatment-regime`: 「BUP-NX 為治療鴉片使用障礙的藥物」) |
| s14 | FAIL | PASS | PASS | PASS | yes: items 3–4 now scoped 「以呼吸器研究為例」/「以胰島素研究為例」; the 「常見誤解」 framing is gone; 餘項 and 有限樣本 rephrased | **[gloss]** Note 「前瞻性＝先訂好計畫，再往前收集資料」: the wiki does not define 前瞻性. (「回溯性＝回頭用過去的紀錄來研究」 is fine: the wiki uses 回溯性 for analyses of existing database records.) | 「前瞻性研究與臨床試驗＝不是翻舊紀錄，而是之後真的在病人身上檢驗」 (`off-policy-evaluation` misconception: 「OPE 的結果等於把策略在病人身上試過：不是…需要前瞻性研究與臨床試驗驗證」) |

If the caller decides that correct textbook definitions of terms are allowed even when the wiki lacks them, the **[gloss]** items above become non-blocking. In that case G5 would still FAIL on s08(a), s10(a) and s12, and s07, s09, s11, s13, s14 would pass.

## 非阻擋建議

1. s03 Note 「所有人吃同一種藥、同一個劑量」: the wiki warns that a schedule that raises the dose over time can still be static (`dynamic-treatment-regime`, 常見誤解, scenario 2). Consider 「所有人照同一套給藥安排」.
2. s04 takeaway 「規則看的是前一週有沒有用鴉片」 describes d1 only. The learned rule uses 「所有基線與時間變動共變數」 (`williams2024`, 限制, p.5). Write 「d1 這條規則看的是…」.
3. s07 Note 「最直覺的一條是正值性：如果資料裡沒人照某條規則做過…」 merges positivity with the separate rule-support condition (`identification-assumptions` lists 「所有規則都必須在資料中有支持」 as an 額外條件). The title also says 「三個前提」 while bullet 2 adds a fourth condition.
4. s07 「無未測量干擾（可交換性）」 gloss and 敏感度分析 gloss are fine. The 一致性 fix above also covers the round-1 F4 point.
5. s08 bullet 5 scope 「在單一時間點的問題上」: the wiki (`doubly-robust-learner`) qualifies this with 「以平均處理效應為例」, and renson2025 notes some single-time-point estimands have no EIF (`renson2025`, 限制). Consider 「以平均處理效應這類單一時間點的問題為例」.
6. s08 「輔助模型」, 「標準誤」 and 「推論」 have no gloss. Glossary 干擾函數 offers 「需要估計但不是最終目標的函數，例如結局迴歸、傾向分數」.
7. s09 「變數重要性」 and 「累積」後悔值 are unexplained. `regret-and-decision-accuracy` gives 「把一位病人各時間步的後悔值加總」.
8. s09 bullet 2 (carried over from round 1): the leaf effect is shown as an unweighted mean difference, but the wiki says the outcomes are first inverse-propensity weighted.
9. Kickers say 「方法路線二」 (s09) and 「方法路線三」 (s11), but no slide in the deck is labelled 方法路線一. s08 was relabelled 「基礎」.
10. s10 「ARDS」 is never explained, so a classmate cannot see how ARDS relates to 急性呼吸衰竭 (wiki: ARDS 117 位（1%） of the ARF cohort, `hong2021`). The 機械功率 gloss 「每分鐘送進肺的能量」 matches only the wiki's own analogy and the unit; consider 「把壓力、呼吸速率等呼吸器參數合成的一個數字（單位：焦耳／分鐘）」.
11. s10 bullet 5 drops the attribution: C7 says 「論文以此說明為什麼…」, but the slide states 「所以通氣策略要隨時調整」 as fact.
12. s11 reward bullet omits the dose penalty (wiki: 「再加上一項隨劑量增大的懲罰」). Adding it would also make s12's −1.29 less puzzling.
13. s12 「內部測試」 was also used to choose GLUCOSE out of 200 models (`desman2025`: 「內部測試集也被用來挑模型，外部驗證的 −0.63 才是沒參與挑選的估計」). 「醫師盲評」 has no context (claim desman2025-C9 is not used: two senior ICU physicians, 20 patients, 5-point Likert).
14. s13 Note 「依病人當下的情況」: the deck defined the rule input as the history up to now (s03). Consider 「依病人到那時為止的情況」.
15. s14 takeaway 「但從資料學出的規則，仍要驗證才能說它有益。」 has no citation and generalises to every learned rule. Cite [hong2021, p.8] [desman2025, p.7], or scope it to 「今天這幾篇」. In item 2, 「這類估計式」 has no antecedent on the slide; write 「倍增穩健這類估計式（第 8 頁）」.

G5: FAIL (slides: s07, s08, s09, s10, s11, s12, s13, s14)
