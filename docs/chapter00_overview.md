---
layout: clean
title: "第00章：PoC設計全体像と三層アーキテクチャの背景"
permalink: /AITL-H/docs/chapter00_overview.html
description: "AITL-H PoCの全体像、目的、三層（FSM/PID/LLM）アーキテクチャ、信号I/Fとデータフロー、将来拡張方針を概説。"
show_title: true
---

# 🧠 第00章：PoC設計全体像と三層アーキテクチャの背景  
_Chapter 00: Overall PoC Design & Three-Layer Architecture_

> **要旨 / Abstract:**  
> 本章はAITL-H（All-in-Theory Logic - Hybrid）の**設計思想とPoC全体像**を示し、三層（FSM/PID/LLM）による**決定性×連続制御×柔軟知性**の統合を、**実装に繋がる具体レベル**（信号I/F・ログ・UART連携）まで落とし込みます。  
> This chapter presents the overall design philosophy of AITL-H and shows how the three-layer model integrates deterministic behavior (FSM), continuous control (PID), and flexible intelligence (LLM) with practical interfaces that map directly to the PoC.

[![Back to Docs Index](https://img.shields.io/badge/Docs-Index-brightgreen?logo=github)](/AITL-H/docs/)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](/AITL-H/docs/#-ライセンス--license)

---

## 0.1 🎯 目的 / Purpose

- **統合制御アーキテクチャの実証**：FSM（本能）、PID（理性）、LLM（知性）の分離と連携をPoCで検証  
- **行動・反応・適応**の3層制御を**リアルタイム**前提で検証  
- **自己修復/安全設計**（フェイルセーフ・ウォッチドッグ・異常検知）を設計思想に内包  
- **RTL/PDK展開**（第11章）が見据える**仕様再利用性**の確保

---

## 0.2 🧬 三層アーキテクチャ / Three-Layer Architecture

| 層 / Layer | 主機能 / Function | 実装キーポイント / Key Points |
|---|---|---|
| **Instinct（本能）** | 行動パターン生成（決定的） | FSM：状態設計・遷移条件・安全遷移（fail-safe） |
| **Reason（理性）** | 物理量制御・補正（連続） | PID：ゲイン設計、アンチワインドアップ、飽和・デッドゾーン |
| **Intelligence（知性）** | 状況判断・意図推定（柔軟） | LLM：自然言語→制御命令、異常説明、自己修復提案 |

---

## 0.3 🧩 システムブロック / System Block (Mermaid)

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

## 0.4 🔌 インタフェース仕様 / Interfaces

### FSM ⇄ PID
- 入力（PID側）：`target_speed [float]`, `target_angle [float]`, `mode [enum: IDLE/ALIGN/TRACK]`
- 出力（PID側）：`pwm_left [0..1]`, `pwm_right [0..1]`（飽和・デッドバンド適用後）
- タイミング：`Ts_control = 10ms`

### PID ⇄ I/O
- センサ入力：`meas_speed`, `meas_angle`, `battery_v`, optional: `dist`
- アクチュエータ出力：`PWM_CHx duty [0..1]`
- 保護：バッテリ電圧低下・温度異常時は安全モード遷移

### Host/LLM ⇄ UART（PoC標準フレーム）

    ```text
    <SOF=0xAA> <VER=0x01> <TYPE> <LEN> <PAYLOAD...> <CRC16>
    TYPE:
      0x10: CMD_GOAL   (target_speed, target_angle, mode)
      0x11: CMD_GAIN   (Kp, Ki, Kd, id)
      0x20: GET_TELEM  (subscribe bitmap)
      0x30: HEALTH     (watchdog, heartbeat)
    ```

---

## 0.5 ⚙️ PID設計ガイド（抜粋）

- アンチワインドアップ：`I_term = clamp(I_term, I_min, I_max)`
- 微分フィルタ：`D_term = (N * dErr) / (1 + N * Ts)`
- 実装順序：P → D → I
- 推奨ログ：`err, u, meas, target, sat_flag, anti_windup_flag`

---

## 0.6 🦺 安全・自己修復

- ウォッチドッグ：`heartbeat`欠落で`FSM → FAULT`
- フェイルセーフ遷移：`SENSOR_LOSS`/`LOW_BATT`/`OVERTEMP`
- LLM補助：異常要因要約・推奨対処提示・確認後設定再投入

---

## 0.7 🧪 ログ & テレメトリ

最低収集セット：
- `fsm_state`, `goal_speed/angle`, `meas_speed/angle`, `u_speed/u_angle`, `flags`
- `battery_v`, `temp`, `fault_code`, `latency_ms`
- `rx_count`, `rx_crc_err`, `tx_count`

周期：
- 制御ログ：100 Hz
- テレメトリ：10–20 Hz

---

## 0.8 🛣 今後の展開

- 第01章：PoC仕様 & 非機能要件
- 第03章：FSM詳細
- 第04章：センサ/PWM I/F実装
- 第06章：run_main統合
- 第08章：LLM連携
- 第11章：出口戦略

---

## 0.9 ✅ 本章チェックリスト

- [ ] 三層の責務境界明確化
- [ ] I/F定義済み
- [ ] UARTフレーム定義済み
- [ ] 安全遷移・自己修復方針合意
- [ ] 後続章参照先明確化

---

## 0.10 📎 付録

代表的データ型（例）：

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

PID一周期（擬似コード）：

    ```pseudo
    err_s  = target_speed - meas_speed
    I_s    = clamp(I_s + err_s*Ts, Imin, Imax)
    D_s    = (N*(err_s - err_s_prev)) / (1 + N*Ts)
    u_s    = kp*err_s + ki*I_s + kd*D_s
    u_s    = saturate(u_s, 0, 1)
    err_s_prev = err_s
    ```

---

## 🔚 まとめ

AITL-H PoCは、決定性（FSM）×連続制御（PID）×柔軟知性（LLM）を明確な責務分離と検証容易なI/Fで束ねる設計です。

---

### ナビゲーション

- ⏮ なし
- ▶️ 次へ：[第01章：PoC仕様策定と要件定義](/AITL-H/docs/chapter01_aitl_architecture.html)

---

### ライセンス

- Code: MIT  
- Text: CC BY 4.0  
- Figures: CC BY-NC 4.0  
