---
layout: default
title: モジュール間インタフェース仕様（AITL-H PoC）
nav_order: 2
description: FSMを起点とした制御ブロック（PID, PWM, UART, センサ）間の信号構造・入出力仕様
permalink: /AITL-H/interface_spec/
---

# 🔌 interface_spec.md — モジュール間インタフェース仕様（AITL-H PoC）

FSMを起点とした制御ブロック（PID, PWM, UART, センサ）間の信号構造・入出力仕様を定義します。

---

## 📂 モジュール一覧と概要

| モジュール名   | 機能                             |
|----------------|----------------------------------|
| `fsm_engine`   | 行動制御（状態管理）            |
| `pid_controller` | PID制御（速度・角度）           |
| `uart_driver`  | LLM命令受信／応答送信            |
| `sensor_interface` | 距離／角度センサの取得         |
| `pwm_driver`   | 出力用PWM波形制御                |

---

## 🔁 各モジュールの入出力信号定義

### 1. fsm_engine

| 信号名        | bit幅 | 方向 | 接続先         | 説明                        |
|---------------|--------|------|----------------|-----------------------------|
| `uart_cmd`    | 8bit  | IN   | `uart_driver`  | LLM命令文字列（ASCII）     |
| `distance`    | 16bit | IN   | `sensor_interface` | 距離センサ値（cm単位）     |
| `angle_error` | 16bit | IN   | `sensor_interface` | 角度誤差（deg単位）        |
| `fsm_state`   | 3bit  | OUT  | 全体           | 現在状態（IDLE=000, WALK=001...） |
| `target_speed`| 16bit | OUT  | `pid_controller` | 速度指令値（cm/s）         |
| `target_angle`| 16bit | OUT  | `pid_controller` | 回転角指令値（deg）        |
| `pwm_enable`  | 1bit  | OUT  | `pwm_driver`   | PWM動作ON/OFF制御          |
| `uart_resp`   | 8bit  | OUT  | `uart_driver`  | 状態応答メッセージ文字     |

---

### 2. pid_controller

| 信号名        | bit幅 | 方向 | 接続先         | 説明                        |
|---------------|--------|------|----------------|-----------------------------|
| `target_speed`| 16bit | IN   | `fsm_engine`   | 前進速度指令                |
| `target_angle`| 16bit | IN   | `fsm_engine`   | 回転角度指令                |
| `distance`    | 16bit | IN   | `sensor_interface` | 実距離                      |
| `angle`       | 16bit | IN   | `sensor_interface` | 実角度                      |
| `control_pwm` | 8bit  | OUT  | `pwm_driver`   | PWMデューティ出力           |

---

### 3. pwm_driver

| 信号名        | bit幅 | 方向 | 接続元           | 説明                      |
|---------------|--------|------|------------------|---------------------------|
| `pwm_enable`  | 1bit   | IN   | `fsm_engine`     | PWM出力のON/OFF信号      |
| `control_pwm` | 8bit   | IN   | `pid_controller` | デューティ比（0〜255）   |
| `pwm_out`     | 1bit   | OUT  | 外部（モータ）    | 実際のPWM波形出力        |

---

### 4. uart_driver

| 信号名     | bit幅 | 方向 | 接続先        | 説明                              |
|------------|--------|------|---------------|-----------------------------------|
| `uart_cmd` | 8bit  | OUT  | `fsm_engine`  | 受信したLLM命令（ASCII）         |
| `uart_resp`| 8bit  | IN   | `fsm_engine`  | 状態応答文字（"W", "S", "T"など） |
| `tx`       | 1bit  | OUT  | 外部UARTポート | UART送信ライン                    |
| `rx`       | 1bit  | IN   | 外部UARTポート | UART受信ライン                    |

---

### 5. sensor_interface

| 信号名        | bit幅 | 方向 | 接続先             | 説明                         |
|---------------|--------|------|--------------------|------------------------------|
| `distance`    | 16bit | OUT  | `fsm_engine`, `pid_controller` | 距離センサ値（単位：cm）     |
| `angle`       | 16bit | OUT  | `pid_controller`   | 現在の角度（単位：deg）       |
| `angle_error` | 16bit | OUT  | `fsm_engine`       | 目標角との誤差（deg）         |

---

## 📘 信号バス命名規約（例）

| 項目 | 命名例         | 説明               |
|------|----------------|--------------------|
| 状態出力信号 | `fsm_state`     | FSMの現在状態コード |
| PWM制御信号 | `control_pwm`  | PID出力のPWM値      |
| LLM命令入力 | `uart_cmd`     | UART経由の文字列    |

---

## 🔗 関連ファイル

- [`fsm_state_table.md`](./fsm_state_table.md)：状態と出力定義
- [`pid_design_spec.md`](./pid_design_spec.md)：PID制御目標と設計仕様（次ステップで作成）
- [`system_block_diagram.svg`](./system_block_diagram.svg)：構成図（作図予定）
