---
title: 機械功率（mechanical power）
type: concept
sources: [hong2021]
updated: 2026-11-15
---

# 機械功率（mechanical power）

## 直覺（生活比喻）

開車時，只看「油門踩多深」或「瞬間最高時速」都不夠，真正累積磨損的是「一段時間內引擎總共出了多少力」。呼吸器也是：潮氣量、壓力、呼吸速率各是一個旋鈕，機械功率把它們合成一個「單位時間內灌進肺裡的總力道」的數字。這個比喻是本 wiki 的說明，不是論文的話；論文本身沒有用「力道」這樣的說法。

## 定義

- 機械通氣（mechanical ventilation, MV）：重症急性呼吸衰竭病人常需要的侵入性通氣，能維持氣體交換，但本身也可能造成肺損傷。[hong2021, p.1]
- 保護性通氣：限制潮氣量、平台壓與驅動壓，用來減少通氣造成的肺損傷；指引常見的數值建議是 ARDS 病人潮氣量小於 6 ml/kg、平台壓小於 30 cmH2O。[hong2021, p.1]
- 機械功率（mechanical power, MP）：把平台壓、呼吸速率與呼氣末正壓（PEEP）等幾個機械參數合成一個數字。論文引用的研究說 MP 能提供較好的肺損傷預測；比較的對象，論文未說明：來源未提及。[hong2021, p.1]
- 單位是 Joules/min，論文以「每增加 5 Joules/min」報告風險比。[hong2021, p.1]
- 兩個版本：動態 MP（MP_dynamic）與靜態 MP（MP_static）。公式由呼吸速率、潮氣量、峰值吸氣壓、平台壓與 PEEP 算出；文字萃取中的公式有亂碼，本 wiki 不重述。[hong2021, p.2]
- 靜態 MP 與存活的關聯比動態 MP 強（靜態的風險比一貫較高），所以 DTR 那一步只最佳化 MP_static。[hong2021, p.3]
- 數值感：整體中位數，靜態 MP 為 14.8（IQR 11.6 至 19.5）、動態 MP 為 12.9（IQR 10.2 至 16.9）Joules/min。[hong2021, p.3]

## 在各篇怎麼出現

### 在 hong2021 中

- MP 是 DTR 裡被調整的「劑量」：論文為每位病人在前 48 小時、每 8 小時的各個時間點估計最佳 MP。[hong2021, p.2-3]
- 實際 MP 減最佳 MP 記為 ΔMP：ΔMP 等於零代表實際用的就是最佳值，小於零是通氣不足（hypoventilation），大於零是過度通氣（over ventilation）；ΔMP 大於 5 Joules/min 在圖說中稱為 hyperventilation。[hong2021, p.5] [hong2021, p.8]
- ΔMP 分成 very low、low、optimal、high、very high 五類，切點為 10、5、5、10 Joules/min。[hong2021, p.4]
- 最佳 MP_static 因類別而異，數值與單位的疑點見 [[hong2021]]；類別的來源見 [[finite-mixture-subphenotypes]]。[hong2021, p.4]
- 關聯估計（觀察性資料）：MP_static 每增加 5 Joules/min，死亡風險比在 Class 1 為 1.29、在 Class 3 為 1.83。[hong2021, p.1]
- ΔMP 偏低或偏高都與住院死亡風險增加有關（OR 分別為 1.08 與 1.07）。[hong2021, p.4]

## 常見誤解

- 「MP 越低越好」：論文不是這個意思。論文的說明是，高 MP 可能造成肺損傷，但低於最佳值的 MP 可能造成通氣不足，導致二氧化碳滯留與氧氣供應不足，這兩者是已知的死亡危險因子；結果上偏低與偏高的 ΔMP 都與較高的死亡風險有關。[hong2021, p.5]
- 「所有人的最佳 MP 都一樣」：論文估出的最佳 MP_static 在三個類別不同，Class 3 的較低、Class 2 的較高。[hong2021, p.4]
- 「MP 是呼吸器上一個可以直接轉的旋鈕」：論文說 MP 是由多個機械參數組合算出的，要調哪個參數才能改變 MP：來源未提及。[hong2021, p.1]
- 「最佳 MP 就是指引的標準」：指引常見的建議是潮氣量與平台壓的上限，不是 MP；論文的最佳 MP 是模型估出來的目標。[hong2021, p.1] [hong2021, p.8]
- 「論文證明降低 MP 能降低死亡」：論文的結果是風險比與勝算比這類關聯，論文自己說還需要對照試驗來檢驗。[hong2021, p.7]

## 相關頁面

- [[dynamic-treatment-regime]]
- [[optimal-dynamic-treatment-rule]]
- [[finite-mixture-subphenotypes]]
- [[blip-function]]
- 來源頁：[[hong2021]]
- 名詞速查：[[glossary]]
