---
layout: default
title: FSM状態遷移表（PoC設計仕様）
nav_order: 1
description: AITL-H 三層制御構造（FSM–PID–LLM）のうち、FSM（行動制御）のPoC設計仕様。
permalink: /AITL-H/fsm_state_table/
---

---

# 🧠 FSM状態遷移表（PoC設計仕様）

AITL-Hプロジェクトにおける「三層制御構造（FSM–PID–LLM）」のうち、FSM（行動制御）の設計仕様です。  
本状態遷移表は、FSMを**設計起点**として定義し、PID制御・PWM出力・UART/センサ入力との**構造的な接続**を行うための基礎設計ドキュメントです。

---

## 🎯 制御対象の概要

| 項目         | 内容                                                         |
|--------------|--------------------------------------------------------------|
| 制御対象     | 人型ロボットの基本行動（待機・前進・停止・方向転換）       |
| 入力イベント | UART命令（LLM経由）、センサ信号（距離センサ、角度センサ） |
| 出力信号     | PWM制御、PID目標値、UART応答メッセージ                      |
| 実装対象     | Python (`fsm_engine.py`)、将来はVerilogへの展開を想定      |

---

## 🗂 状態一覧（State Definitions）

| 状態名     | 説明                        |
|------------|-----------------------------|
| `IDLE`     | 初期待機状態、センサ監視中 |
| `WALK`     | 前進移動制御中              |
| `TURN`     | 方向転換制御中              |
| `STOP`     | 強制停止状態                |
| `LLM_WAIT` | LLM命令待ちの受付状態       |

---

## 🔁 状態遷移ルール（State Transitions）

| 現在の状態 | イベント                   | 次の状態 | 条件例                  |
|------------|----------------------------|----------|-------------------------|
| `IDLE`     | UARTで "walk"              | `WALK`   | `uart_cmd == "walk"`    |
| `IDLE`     | UARTで "wait_llm"          | `LLM_WAIT`| `uart_cmd == "wait_llm"`|
| `WALK`     | UARTで "stop"              | `STOP`   | `uart_cmd == "stop"`    |
| `WALK`     | 距離センサ値が閾値超過     | `STOP`   | `distance > 100`        |
| `STOP`     | UARTで "turn"              | `TURN`   | `uart_cmd == "turn"`    |
| `TURN`     | 回転完了（角度誤差が0）     | `IDLE`   | `angle_error < 1`       |
| `LLM_WAIT` | LLMから新しい指示受信       | `IDLE`   | `uart_ready == True`    |

---

## 🧾 各状態の出力制御信号（Output Mapping）

| 状態名     | PWM出力 | PID目標値     | UART応答           |
|------------|----------|----------------|----------------------|
| `IDLE`     | OFF      | None           | "Waiting for command"|
| `WALK`     | ON       | speed = 5.0    | "Walking forward"    |
| `TURN`     | ON       | angle = 90.0   | "Turning right"      |
| `STOP`     | OFF      | None           | "Stopped"            |
| `LLM_WAIT` | OFF      | None           | "Awaiting instruction"|

---

## 🔗 接続先ブロックとの関係

- 各状態の出力は `pid_controller.py`, `pwm_driver.py`, `uart_driver.py` に信号を送る。
- 本状態遷移表に対応する信号仕様は [`interface_spec.md`](./interface_spec.md) に記述予定。
- FSM状態は `fsm_engine.py` にてクラスまたは状態辞書により実装予定。

---

## 📝 備考

- 状態名・出力信号・イベント名は、RTL化を意識してプレフィクスや命名規則を後述する。
- 今後、状態遷移にタイマトリガやセンサ連携を追加可能。
- FSMはPoCにおいて**制御設計の起点**であり、すべての下位制御がこの定義に従う。
