---
layout: clean
title: "Ch.6 — 制御アーキテクチャ実装（run_main中心）"
permalink: /AITL-H/docs/chapter06_run_main_arch.html
---

---

# 🧩 第06章：PoC統合制御構成と run_main.py

本章では、AITL-H PoCにおける**統合制御スクリプト `run_main.py` の構成と制御ループ設計**を説明します。  
FSM・PID・UART・センサの各モジュールを接続し、PoCとしての一貫した動作を実現します。

---

## 1. ⚙️ 統合制御の目的

- 各制御モジュール（FSM/PID/UART/Sensor）を**統合的に連携**
- 外部命令（UART）を受信し、状態制御・出力制御を連動実行
- センサ値に応じて**動的に出力制御量を変化**

---

## 2. 🧾 run_main.py の基本構成

```python
from uart_driver import UARTDriver
from fsm_engine import FSMEngine
from pid_controller import PIDController
from sensor_interface import SensorInterface

# 初期化
uart = UARTDriver()
fsm = FSMEngine(config_path="fsm_config.yaml")
pid = PIDController(kp=1.2, ki=0.5, kd=0.1)
sensor = SensorInterface()

# 制御ループ
while True:
    # 1. 外部命令を取得（UART）
    command = uart.receive()
    if command:
        fsm.handle_event(command)

    # 2. センサ更新
    sensor.update()

    # 3. FSMの出力目標値を取得
    target_speed = fsm.get_output()

    # 4. 実測値を取得して制御量生成（PID）
    measured_speed = sensor.read_distance()
    pwm = pid.compute(target_speed, measured_speed)

    # 5. PWM制御量を出力（仮想）
    print(f"PWM output: {pwm}")
```

---

## 3. 📡 情報の流れと各層の役割

```
UART（知性）
   ↓ command
FSM（本能）---→ target_speed
                      ↓
Sensor（現実）       measured_speed
                      ↓
PID（理性）---→ PWM信号出力
```

このように、FSMとPIDを軸にした**データフロー制御**が成立しています。

---

## 4. 🔄 テストとデバッグの観点

- UART命令を `inject_command()` でテスト送信可能
- PIDの出力ログやFSM状態ログを print で確認
- センサ値は `sensor.update()` で動的更新可能

---

## 🔚 まとめ

PoC制御の中心は `run_main.py` にあり、FSM・PID・UART・センサを一体化して動作検証を可能にしています。  
この構造をもとに、将来的にはFSMの再構成やPIDの自動調整などの拡張が見込まれます。

---

<h3>図6-1：PoC統合制御ブロック図</h3>
<img src="./images/figure6_1_system_block_diagram.png" alt="System Block Diagram" width="500"/>

---

