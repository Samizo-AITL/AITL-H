---
title: PWM → ADC Ripple Report
description: PWM駆動がADCの実効ENOBに与える影響を評価
nav_order: 1
---

---

# ⚡ PWM → ADC Ripple Report
*⚡ PWM → ADC Ripple Report*

本ページでは、PWM駆動による電源リップルが ADC の実効ビット数（ENOB）に与える影響を示します。  
*This page shows how PWM-driven supply ripple affects the effective number of bits (ENOB) of the ADC.*

---

## 📊 サンプル結果 (Duty = 0.5)

| PWM周波数 (kHz) | リップル (mVrms) | ENOB低下 (bit) | 実効ENOB (bit) |
|-----------------|------------------|----------------|----------------|
| 20              | ~20              | 0.6            | **14.6**       |
| 40              | ~10              | 0.3            | **14.9**       |
| 80              | ~5               | 0.15           | **15.0**       |

*Ripple vs ENOB drop for duty=0.5 (worst-case).*

---

## 🔎 読み方 / How to interpret
- **リップルが大きいほど ENOB が下がる**  
  *The larger the ripple, the more ENOB decreases.*  
- **12 bit 以上**あれば姿勢制御用IMUに十分  
  *≥12 bits is sufficient for IMU-based posture control.*  
- **14 bit 以上**あれば力覚/圧力センサに理想的  
  *≥14 bits is ideal for force/pressure sensing.*  

👉 この結果では **すべて14bit以上確保**できており、40–80kHz動作で十分余裕があります。  
👉 In this result, all cases ensure ≥14 bits, and 40–80 kHz operation gives sufficient margin.

---

## 📈 グラフ例
Dutyごとの PWM周波数 vs 実効ENOB:

![ENOB vs PWM freq (duty=0.5)](../systemdk/reports/pwm_to_adc_ripple/enob_vs_freq_duty_0_5.png)

*Effective ENOB vs PWM frequency at duty=0.5.*

---

## ✅ 設計判断 / Design Decision
- PWM周波数は **40kHz以上**を推奨  
  *PWM frequency ≥40 kHz recommended.*  
- 20kHzでも使用可能だが余裕が小さい  
  *20 kHz is usable but with limited margin.*  
- さらなる改善には  
  - コンデンサ容量増加  
  - 配線インダクタンス・抵抗低減  
  *For further improvement: increase capacitance, reduce trace inductance/resistance.*

---

[⬅️ 戻る Back](../)
