---
layout: clean
title: PID制御仕様書（AITL-H PoC）
nav_order: 3
description: FSM出力に基づくPID制御ブロックの設計仕様
permalink: /AITL-H/PoC/pid_design_spec/
---

---

# ⚙️ pid_design_spec.md — PID制御仕様書（AITL-H PoC）

本ドキュメントでは、FSMが出力する制御目標に対して、PID制御ブロックがどのように動作し、どのようなパラメータ設定・信号処理を行うかを明記します。  
この設計は、PoCレベルのPython実装と、将来のRTL化・アナログ実装の両方を想定した**抽象度の高い制御設計仕様**です。

---

## 🎯 目的と適用範囲

| 項目 | 内容 |
|------|------|
| 対象ブロック | `pid_controller.py` |
| 入力信号 | `target_speed`, `target_angle`, `distance`, `angle` |
| 出力信号 | `control_pwm`（PWMデューティ比） |
| 動作モード | 速度制御、角度制御の2モード（FSMから切替） |
| 実装形式 | Python（PoC）、将来的にVerilog等 |

---

## 🧮 PID制御モデル

### 📐 離散時間形式の制御式
```
u(t) = Kp·e(t) + Ki·∑e(t)·Δt + Kd·(e(t) - e(t-1)) / Δt
```
- `e(t)` = 目標値 - 実測値
- `Δt` = サンプリング周期（例：50ms）
- `u(t)` = 内部制御出力 → PWMへ変換

---

## 🚶 前進動作モード（速度制御）

| 項目           | 内容                                |
|----------------|-------------------------------------|
| 目標速度       | `target_speed = 5.0 cm/s`（FSMより） |
| 実測速度       | `distance / Δt` で近似              |
| 誤差定義       | `error = target_speed - actual_speed` |
| ゲイン設定例   | `Kp = 2.0`, `Ki = 0.5`, `Kd = 0.1`  |
| サンプリング周期 | 50ms                               |
| 出力           | `control_pwm`（0〜255, 8bit）       |

---

## 🔁 回転動作モード（角度制御）

| 項目           | 内容                             |
|----------------|----------------------------------|
| 目標角度       | `target_angle = 90 deg`（FSMより） |
| 実測角度       | `angle`（センサ入力）           |
| 誤差定義       | `error = target_angle - angle`  |
| ゲイン設定例   | `Kp = 1.5`, `Ki = 0.3`, `Kd = 0.05` |
| サンプリング周期 | 50ms                           |
| 終了判定       | `|error| < 1 deg`                |
| 出力           | `control_pwm`（0〜255, 8bit）   |

---

## 💻 擬似コード（Python実装イメージ）

```python
# PID計算ループ
error = target - measured
integral += error * dt
derivative = (error - prev_error) / dt
u = Kp * error + Ki * integral + Kd * derivative

# スケーリングしてPWM出力へ変換
control_pwm = max(0, min(255, int(u)))
```

---

## 📤 出力信号仕様

| 信号名       | 範囲     | 単位   | 備考                   |
|--------------|----------|--------|------------------------|
| `control_pwm`| 0〜255   | 無次元 | PWM duty（8bit制御）   |
| PWM周期      | ≥2kHz    | Hz     | 実装依存               |
| 制限条件     | 255でクリップされる            |

---

## 🔗 関連仕様と接続関係

- FSM設計仕様：[`fsm_state_table.md`](./fsm_state_table.md)
- インタフェース仕様：[`interface_spec.md`](./interface_spec.md)
- PWM制御ブロック：`pwm_driver.py`
- センサインタフェース：`sensor_interface.py`

---

## 📝 将来の展開（RTL/SoC）

- ゲインを固定小数点（例：Q8.8形式）に変換
- PID演算器をモジュール化し、FSMとの接続を信号線で管理
- `u(t)` のスケーリング方式をハードウェア向けに確定
- 複数制御対象に応じた切替（速度・角度の動的切替制御）
- アナログ制御への応用（オペアンプPID実装の参考）

---
