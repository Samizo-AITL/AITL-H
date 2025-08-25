---
title: Thermal Derating Report
description: LDMOS駆動ICの熱挙動とデレート発生の評価
nav_order: 2
---

---

# 🌡️ Thermal Derating Report  
*🌡️ Thermal Derating Report*

本ページでは、0.35 µm LDMOS 駆動ICの熱挙動を評価し、  
どのフェーズでデレート（出力制限）やシャットダウンが発生するかを示します。  
*This page evaluates the thermal behavior of the 0.35 µm LDMOS driver IC,  
showing at which phases derating (output limiting) or shutdown occurs.*

---

## 📊 サンプル結果 / Example Results

| 環境温度 (°C) / Ambient Temp (°C) | フェーズ / Phase | 消費電力 (W) / Power (W) | 接合温度 (°C) / Junction Temp (°C) | デレート発生 / Derated | シャットダウン / Shutdown |
|----------------------------------|-----------------|--------------------------|------------------------------------|------------------------|---------------------------|
| 25                               | walk            | 4.0                      | 97.0                               | False                  | False |
| 25                               | lift            | 8.0                      | 115.0                              | True                   | False |
| 25                               | idle            | 1.0                      | 43.0                               | False                  | False |
| 40                               | walk            | 4.0                      | 112.0                              | True                   | False |
| 40                               | lift            | 8.0                      | 130.0                              | True                   | True  |
| 40                               | idle            | 1.0                      | 58.0                               | False                  | False |

*Example results for mission phases at different ambient temperatures.*

---

## 🔎 読み方 / How to Interpret
- **derated=True** → 出力制限がかかり、トルク性能が低下  
  *When `derated=True`, output torque is limited.*  
- **shutdown=True** → 安全のため駆動停止、継続不可  
  *When `shutdown=True`, the driver stops for protection.*  
- 高温環境（40℃）＋高負荷（lift）ではシャットダウンに至る可能性あり  
  *At high ambient (40°C) + heavy load (lift), shutdown may occur.*

---

## 📈 グラフ例 / Example Graph
フェーズごとの接合温度とデレートライン:  
*Junction temperature vs phase and derating line:*

<p align="center">
  <img src="../systemdk/reports/thermal_derating/thermal_vs_phase_40C.png" alt="Thermal vs Phase (Ambient=40°C)" width="80%">
</p>

---

## ✅ 設計判断 / Design Decision
- **通常環境 (25°C): 安全動作**  
  *Safe operation at 25°C*  
- **高温環境 (40°C): liftフェーズでデレート・シャットダウンリスク**  
  *At 40°C, derating and shutdown risk during lift phase*  
- **対策候補 / Countermeasures:**  
  - ヒートシンク強化  
    *Enhance heat sinking*  
  - PWM制御による発熱低減  
    *Reduce heating via PWM control*  
  - 連続高負荷動作の制限  
    *Limit continuous heavy load operation*

---

[⬅️ 戻る Back](../)
