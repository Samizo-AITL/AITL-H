---
title: Flagship PoC Slides
description: Samizo-AITL集大成 人型ロボットPoC 発表用スライド
nav_order: 4
layout: clean
permalink: /AITL-H/PoC/humanoid/docs/flagship_poc_slides/
---

---

# 🚩 Samizo-AITL 集大成：人型ロボットPoC  
*🚩 Samizo-AITL Culmination: Humanoid Robot PoC*

---

## 🧭 コンセプト / Concept
- **FSM × PID × 状態空間 × LLM の三層制御**  
  *Three-layer control: FSM × PID × State-space × LLM*  
- **クロスノード統合設計 (22nm SoC / 0.18µm AMS / 0.35µm LDMOS / Energy Harvest)**  
  *Cross-node integrated design (22nm SoC / 0.18µm AMS / 0.35µm LDMOS / Energy Harvest)*  
- **教育 × PoC × 政策提言 を一体化**  
  *Integration of Education × PoC × Policy Proposal*

---

## 🧩 クロスノード・チップセット / Cross-Node Chipset
| ブロック / Block | ノード / Node | 役割 / Role |
|-----------------|---------------|-------------|
| **Brain SoC** | 22nm | FSM＋PID＋LLM制御、状態空間制御<br/>*FSM+PID+LLM control, state-space control* |
| **Sensor Hub** | 0.18µm AMS | CMOSカメラ / IMU / 力覚センサ<br/>*CMOS camera / IMU / force sensors* |
| **Power Drive** | 0.35µm LDMOS | PWM/Hブリッジ、トルク制御<br/>*PWM/H-bridge, torque control* |
| **Energy Harvest** | MEMS / PV / Regen | 自己発電・蓄電<br/>*Energy harvesting & storage* |

---

## ⚙️ 成果1：PWMリップル → ADC精度  
*Result 1: PWM Ripple → ADC Accuracy*  
- **20kHz:** ENOB ~14.6bit  
- **40kHz:** ENOB ~14.9bit  
- **80kHz:** ENOB ~15bit  
👉 **40kHz以上で安全マージン確保**  
*Safe margin ensured at ≥40kHz*

<p align="center">
  <img src="../systemdk/reports/pwm_to_adc_ripple/enob_vs_freq_duty_0_5.png" alt="ENOB vs PWM freq" width="80%">
</p>

---

## 🌡️ 成果2：熱デレーティング  
*Result 2: Thermal Derating*  
- **25℃:** 安定動作  
  *Stable operation at 25°C*  
- **40℃:** Liftフェーズでデレート → シャットダウンリスク  
  *Derating in Lift phase → shutdown risk at 40°C*  
👉 **冷却強化 or 負荷制御で解決**  
*Solution: enhanced cooling or load control*

<p align="center">
  <img src="../systemdk/reports/thermal_derating/thermal_vs_phase_40C.png" alt="Thermal vs Phase" width="80%">
</p>

---

## 🔋 成果3：自己発電寄与率  
*Result 3: Contribution of Self-Powering*  
- 全体消費の ~12% を自己発電で補填  
  *~12% of total consumption supplied by self-powering*  
- KPI目標: 20%  
  *Target KPI: 20%*  
👉 **圧電アレイ拡張 / PV面積増加で改善可能**  
*Improvement: expand piezo array / increase PV area*

<p align="center">
  <img src="../systemdk/reports/mission_energy/soc_vs_phase.png" alt="SOC vs Phase" width="80%">
</p>

---

## 🎯 総合KPI / Summary KPI
- **姿勢回復 ≤ 200ms ✅**  
  *Posture recovery ≤200ms*  
- **歩容安定度 +30% ✅**  
  *Gait stability +30%*  
- **エネルギー効率 +15% ✅**  
  *Energy efficiency +15%*  
- **自己発電寄与率 ~12%（改善余地あり）**  
  *Self-powering contribution ~12% (room for improvement)*

---

## 📌 結論 / Conclusion
**Samizo-AITL 集大成：勝てるテーマ**  
*Samizo-AITL Culmination: A Winning Theme*  

- **教育:** 制御理論〜半導体設計を貫通  
  *Education: spanning from control theory to semiconductor design*  
- **産業:** クロスノード SoC＋AMS＋LDMOS 設計実証  
  *Industry: cross-node SoC+AMS+LDMOS design verification*  
- **政策:** 省エネ・標準化戦略に直結  
  *Policy: directly linked to energy-saving & standardization strategies*

---

[⬅️ 戻る Back](../)
