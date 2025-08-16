---
layout: clean
title: "第00章：PoC設計全体像と三層アーキテクチャの背景"
permalink: /docs/chapter00_overview.html
description: "AITL-H PoCの全体像、目的、三層（FSM/PID/LLM）アーキテクチャ、信号I/Fとデータフロー、将来拡張方針を概説。"
show_title: false
---

---

# 🧠 **第00章：PoC設計全体像と三層アーキテクチャの背景**  
_**Chapter 00: Overall PoC Design & Three-Layer Architecture**_

> **要旨 / Abstract**  
> 本章は **AITL-H（All-in-Theory Logic - Hybrid）** の**設計思想**と**PoC全体像**を示し、三層（**FSM** / **PID** / **LLM**）による**決定性 × 連続制御 × 柔軟知性**の統合を、**実装に繋がる具体仕様**まで落とし込みます。  
> This chapter presents the **design philosophy** and **overall architecture** of **AITL-H**, detailing how the three-layer model (**FSM**, **PID**, **LLM**) integrates **deterministic control**, **continuous regulation**, and **flexible intelligence**, down to **practical implementation specifications**.

[![📚 Docs Index](https://img.shields.io/badge/Docs-Index-brightgreen?logo=github)](/AITL-H/docs/)  
[![⚖ Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](/AITL-H/docs/#-ライセンス--license)

---

## 🎯 **0.1 目的 / Purpose**

- **統合制御アーキテクチャの実証**  
  _Proof of an integrated control architecture (FSM / PID / LLM separation)_
- **行動・反応・適応の三層制御の模擬**  
  _Simulation of behavior, reaction, and adaptation layers_
- **LLMによる柔軟な知性判断と自己修復の統合テスト**  
  _Integration test for flexible decision-making and self-healing using LLM_
- **RTL展開への橋渡し**（再利用可能な設計思想）  
  _Bridge to RTL deployment with reusable design concepts_

---

## 🧬 **0.2 三層アーキテクチャ / Three-Layer Architecture**

| 層 / Layer | 機能 / Function | 担当モジュール / Module |
|---|---|---|
| **本能層 Instinct** | **行動パターン生成** / Behavior pattern generation | **FSM**（有限状態機械 / Finite State Machine） |
| **理性層 Reason** | **物理量制御・補正** / Physical control & compensation | **PID**（比例・積分・微分制御 / Proportional-Integral-Derivative Control） |
| **知性層 Intelligence** | **状況判断・自己修復** / Situation assessment & self-healing | **LLM**（大規模言語モデル / Large Language Model） |

> **設計思想 / Design Philosophy:** 責務を明確に分離することで、**検証容易性**と**移植性**を確保。  
> _Clear separation of responsibilities ensures **ease of testing** and **portability**._

---

## 🧩 **0.3 システムブロック / System Block Diagram**

    ```mermaid
    flowchart TB
      subgraph LLM[LLM Intelligence Layer]
        U[UART/Host Command] -->|parsed intent| ILLM[Intent Mapper]
      end

      subgraph FSM[Instinct Layer: FSM Engine]
        ILLM -->|goal: target_speed, target_angle| S1[State Machine<br/>IDLE/ALIGN/TRACK/FAULT]
        S1 -->|goals| OUT1[Goals to PID]
      end

      subgraph PID[Reason Layer: PID Controller]
        OUT1 --> P1[PID(speed)]
        OUT1 --> P2[PID(angle)]
        P1 --> MUX[[Mixer]]
        P2 --> MUX
        MUX --> PWM[PWM Driver]
      end

      subgraph IO[Physical I/O]
        PWM --> ACT[Actuator]
        SEN[Sensor Suite] -->|measured speed/angle/dist| PID
        SEN --> FSM
      end

      LOG[Logging/Telemetry] --- FSM
      LOG --- PID
      U <--> LOG
    ```

---

## 🔌 **0.4 インタフェース仕様 / Interfaces**

### FSM ⇄ PID
- **入力 / Input**: `target_speed [float]`, `target_angle [float]`, `mode [enum: IDLE/ALIGN/TRACK]`
- **出力 / Output**: `pwm_left [0..1]`, `pwm_right [0..1]`
- **周期 / Timing**: `Ts_control = 10ms`

### PID ⇄ I/O
- **センサ入力 / Sensor Input**: `meas_speed`, `meas_angle`, `battery_v`, `dist`(optional)
- **アクチュエータ出力 / Actuator Output**: `PWM_CHx duty [0..1]`
- **保護 / Protection**: 異常時は安全モード遷移（FAULT通知）  
  _On abnormal condition, transition to safe mode (FAULT notification)_

### Host/LLM ⇄ UART
    ```text
    <SOF=0xAA> <VER=0x01> <TYPE> <LEN> <PAYLOAD...> <CRC16>
    TYPE:
      0x10: CMD_GOAL   (target_speed, target_angle, mode)
      0x11: CMD_GAIN   (Kp, Ki, Kd, id)
      0x20: GET_TELEM  (subscribe bitmap)
      0x30: HEALTH     (watchdog, heartbeat)
    ```

---

## ⚙️ **0.5 PID設計ガイド（抜粋） / PID Tuning (Excerpt)**

- **アンチワインドアップ / Anti-windup**: `I_term = clamp(I_term, I_min, I_max)`
- **微分フィルタ / Derivative Filter**: `D_term = (N * dErr) / (1 + N * Ts)`
- **設計順序 / Design Order**: P → D → I
- **推奨ログ / Recommended Logging**: `err, u, meas, target, sat_flag, anti_windup_flag`

---

## 🦺 **0.6 安全・自己修復 / Safety & Self-Healing**

- **ウォッチドッグ / Watchdog**: `heartbeat` 欠落で `FSM → FAULT`
- **フェイルセーフ / Fail-safe**: `SENSOR_LOSS` / `LOW_BATT` / `OVERTEMP`
- **LLM支援 / LLM Support**: 異常要因の要約・推奨対処の提示・確認後の設定再投入

---

## 📡 **0.7 ログ & テレメトリ / Logging & Telemetry**

**最低収集項目 / Minimum Set**:  
`fsm_state`, `goal_speed/angle`, `meas_speed/angle`, `u_speed/u_angle`, `flags`,  
`battery_v`, `temp`, `fault_code`, `latency_ms`,  
`rx_count`, `rx_crc_err`, `tx_count`

**収集周期 / Sampling Rate**:  
- 制御ログ / Control Log: **100 Hz**  
- テレメトリ / Telemetry: **10–20 Hz**

---

## 🛣 **0.8 今後の展開 / Roadmap**

- 第01章 / Ch.1: PoC仕様 & 要件定義  
- 第03章 / Ch.3: FSM詳細  
- 第04章 / Ch.4: センサ・PWM I/F実装  
- 第06章 / Ch.6: run_main統合  
- 第08章 / Ch.8: LLM連携  
- 第11章 / Ch.11: 出口戦略

---

## ✅ **0.9 本章チェックリスト / Readiness Checklist**

- [ ] 責務境界の明確化  
- [ ] I/F定義済み  
- [ ] UARTフレーム仕様確定  
- [ ] 安全遷移と自己修復方針合意  
- [ ] 後続章リンク確認

---

## 📎 **0.10 付録 / Appendix**

**データ型例 / Example Data Types**:
    ```c
    typedef struct {
      float target_speed;
      float target_angle;
      uint8_t mode;
    } goal_t;

    typedef struct {
      float kp, ki, kd;
      float i_min, i_max;
    } pid_gain_t;

    typedef struct {
      float meas_speed;
      float meas_angle;
      float battery_v;
      uint16_t flags;
    } telem_t;
    ```

**PID一周期（擬似コード） / PID Cycle (Pseudocode)**:
    ```pseudo
    err_s  = target_speed - meas_speed
    I_s    = clamp(I_s + err_s*Ts, Imin, Imax)
    D_s    = (N*(err_s - err_s_prev)) / (1 + N*Ts)
    u_s    = kp*err_s + ki*I_s + kd*D_s
    u_s    = saturate(u_s, 0, 1)
    err_s_prev = err_s
    ```

---

## 🔚 **まとめ / Summary**

AITL-H PoCは、**決定性（FSM） × 連続制御（PID） × 柔軟知性（LLM）** を  
**明確な責務分離**と**検証容易なI/F**で統合する設計です。  
本章は後続の実装章への**起点**となります。

---

### 📝 **ライセンス / License**

- **Code:** MIT  
- **Text:** CC BY 4.0  
- **Figures:** CC BY-NC 4.0  
（詳細は [Docs Index のライセンス表](/docs/#-ライセンス--license) を参照）

### 🔗 **ナビゲーション / Navigation**
- 🏠 **[AITL-H PoC マニュアル README](/docs/)**
- ▶️ **[次の章 / Next: 第01章 PoC仕様策定と要件定義](/docs/chapter01_aitl_architecture.html)**  
  _PoC Specification & Requirements_
