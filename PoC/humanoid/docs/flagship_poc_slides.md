---
title: Flagship PoC Slides
description: Samizo-AITL集大成 人型ロボットPoC 発表用スライド
nav_order: 4
---

---

# 🚩 Samizo-AITL 集大成：人型ロボットPoC
*Flagship PoC: Humanoid Robot*

---

## 🧭 コンセプト / Concept
- FSM × PID × 状態空間 × LLM の三層制御
- クロスノード統合設計 (22nm SoC / 0.18µm AMS / 0.35µm LDMOS / Energy Harvest)
- **教育 × PoC × 政策提言** を一体化

---

## 🧩 クロスノード・チップセット
| ブロック | ノード | 役割 |
|----------|--------|------|
| Brain SoC | 22nm | FSM+PID+LLM制御、状態空間制御 |
| Sensor Hub | 0.18µm AMS | CMOSカメラ / IMU / 力覚センサ |
| Power Drive | 0.35µm LDMOS | PWM/Hブリッジ、トルク制御 |
| Energy Harvest | MEMS/PV/Regen | 自己発電・蓄電 |

---

## ⚙️ 成果1：PWMリップル → ADC精度
- 20kHz: ENOB ~14.6bit
- 40kHz: ENOB ~14.9bit
- 80kHz: ENOB ~15bit  
👉 **40kHz以上で安全マージン確保**

![ENOB vs PWM freq](../systemdk/reports/pwm_to_adc_ripple/enob_vs_freq_duty_0_5.png)

---

## 🌡️ 成果2：熱デレーティング
- 25℃: 安定動作
- 40℃: Liftフェーズでデレート→シャットダウンリスク  
👉 **冷却強化 or 負荷制御で解決**

![Thermal](../systemdk/reports/thermal_derating/thermal_vs_phase_40C.png)

---

## 🔋 成果3：自己発電寄与率
- 全体消費の ~12% を自己発電で補填
- KPI目標: 20%  
👉 圧電アレイ拡張 / PV面積増加で改善可能

![SOC](../systemdk/reports/mission_energy/soc_vs_phase.png)

---

## 🎯 総合KPI / Summary KPI
- 姿勢回復 ≤ 200ms ✅
- 歩容安定度 +30% ✅
- エネルギー効率 +15% ✅
- 自己発電寄与率 ~12%（改善余地あり）

---

## 📌 結論 / Conclusion
**Samizo-AITL 集大成：勝てるテーマ**  
- 教育：制御理論〜半導体設計を貫通  
- 産業：クロスノードSoC+AMS+LDMOS設計実証  
- 政策：省エネ・標準化戦略に直結

---

[⬅️ 戻る Back](../)
