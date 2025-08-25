---
title: Mission Energy Report
description: 自己発電（回生・圧電・PV）の寄与率とバッテリSOC変動を評価
nav_order: 3
layout: clean
permalink: /PoC/humanoid/docs/mission_energy/
---

---

# 🔋 Mission Energy Report  
*🔋 Mission Energy Report*

本ページでは、人型ロボットのミッション実行時における  
負荷電力と自己発電（回生・圧電・PV）の寄与を評価します。  
*This page evaluates the contribution of regenerative, piezoelectric, and PV harvesting  
during mission execution of the humanoid robot.*

---

## 📊 サンプル結果 / Example Results

| フェーズ / Phase | 時間 (s) / Time (s) | 負荷 (Wh) / Load (Wh) | 発電 (Wh) / Harvested (Wh) | バッテリSOC (%) / Battery SOC (%) |
|------------------|---------------------|-----------------------|----------------------------|-----------------------------------|
| walk_phase1      | 300                 | 2.1                   | 0.25                       | 68.5 |
| lift_phase       | 60                  | 0.67                  | 0.05                       | 67.9 |
| walk_phase2      | 300                 | 1.7                   | 0.22                       | 66.9 |
| idle_phase       | 120                 | 0.33                  | 0.04                       | 66.6 |

*Example mission profile results with regenerative, piezoelectric, and PV harvesting.*

---

## 🔎 読み方 / How to Interpret
- **harvest_wh**：そのフェーズで得られた発電量  
  *Harvested energy during the phase*  
- **soc_pct**：ミッション後のバッテリ残量  
  *Battery state-of-charge after each phase*  
- **寄与率（harvest_contribution_pct）** = 発電量 ÷ 消費量  
  *Contribution rate = harvested / consumed energy*  

👉 この例では **全体消費の約 12% を自己発電で補填**。  
👉 KPI（20%補填目標）には未達、さらなる最適化が必要。  
*In this example, ~12% of total consumption is supplied by self-harvesting.  
The KPI target (20%) is not yet achieved, requiring further optimization.*

---

## 📈 グラフ例 / Example Graphs

バッテリSOC推移：  
*Battery SOC transition over mission phases:*

<p align="center">
  <img src="https://samizo-aitl.github.io/AITL-H/PoC/humanoid/systemdk/reports/mission_energy/soc_vs_phase.png"
       alt="SOC vs Phase" width="80%">
</p>

---

## ✅ 設計判断 / Design Decision
- **現状 / Current:** 寄与率 ~12%  
  *Contribution ~12%*  
- **目標 / Target:** 20% 以上  
  *≥20% contribution*  
- **改善策 / Improvements:**  
  - 回生効率を 0.9 に向上  
    *Increase regenerative efficiency to 0.9*  
  - 圧電アレイの出力増強  
    *Enhance output of piezo array*  
  - 外装PVセルの面積拡大  
    *Expand surface area of exterior PV cells*

---

[⬅️ 戻る Back](../)
