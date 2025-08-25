---
title: Thermal Derating Report
description: LDMOS駆動ICの熱挙動とデレート発生の評価
nav_order: 2
---

# 🌡️ Thermal Derating Report
*🌡️ Thermal Derating Report*

本ページでは、0.35 µm LDMOS 駆動ICの熱挙動を評価し、  
どのフェーズでデレート（出力制限）やシャットダウンが発生するかを示します。  
*This page evaluates the thermal behavior of the 0.35 µm LDMOS driver IC,  
showing at which phases derating (output limiting) or shutdown occurs.*

---

## 📊 サンプル結果

| 環境温度 (°C) | フェーズ | 消費電力 (W) | 接合温度 (°C) | デレート発生 | シャットダウン |
|---------------|----------|--------------|---------------|--------------|----------------|
| 25            | walk     | 4.0          | 97.0          | False        | False          |
| 25            | lift     | 8.0          | 115.0         | True         | False          |
| 25            | idle     | 1.0          | 43.0          | False        | False          |
| 40            | walk     | 4.0          | 112.0         | True         | False          |
| 40            | lift     | 8.0          | 130.0         | True         | True           |
| 40            | idle     | 1.0          | 58.0          | False        | False          |

*Example results for mission phases at different ambient temperatures.*

---

## 🔎 読み方 / How to interpret
- **derated=True** → 出力制限がかかり、トルク性能が低下  
  *When `derated=True`, output torque is limited.*  
- **shutdown=True** → 安全のため駆動停止、継続不可  
  *When `shutdown=True`, the driver stops for protection.*  
- 高温環境（40℃）＋高負荷（lift）ではシャットダウンに至る可能性あり  
  *At high ambient (40°C) + heavy load (lift), shutdown may occur.*  

---

## 📈 グラフ例
フェーズごとの接合温度とデレートライン：

![Thermal vs Phase (Ambient=40°C)](../systemdk/reports/thermal_derating/thermal_vs_phase_40C.png)

*Junction temperature vs phase at ambient=40°C.*

---

## ✅ 設計判断 / Design Decision
- 通常環境 (25°C) では安全動作  
- 高温環境 (40°C) では **liftフェーズでデレート・シャットダウンリスク**  
- 対策候補:  
  - ヒートシンク強化  
  - PWM制御による発熱低減  
  - 連続高負荷動作の制限  

---

[⬅️ 戻る Back](../)
