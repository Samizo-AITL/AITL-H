---
layout: clean
permalink: /docs/chapter05_uart_control.html
title: ""
show_title: false   # ← これで上部の自動H1バーを非表示
---

---

# 🔌 第05章：UART制御と通信管理 / Chapter 05: UART Control and Communication Management

本章では、AITL-H PoCにおける**UART（Universal Asynchronous Receiver/Transmitter）**通信の設計方針を説明します。  
This chapter explains the **UART (Universal Asynchronous Receiver/Transmitter)** communication design policy in AITL-H PoC.

UARTは、LLMや上位制御系とPoCデバイス間のデータ授受に用いられ、**コマンド伝達**および**センサデータ送信**を担います。  
UART is used for data exchange between the LLM or upper control system and the PoC device, handling **command transmission** and **sensor data sending**.

---

## 1. 📡 UART通信の役割 / Role of UART Communication

- **コマンド受信**（LLMや外部PCからの操作命令）  
  **Command Reception** (operation instructions from LLM or external PC)
- **状態送信**（センサ値・FSM状態・PID情報）  
  **Status Transmission** (sensor values, FSM states, PID information)
- **デバッグ出力**（開発時の動作確認）  
  **Debug Output** (behavior verification during development)

---

## 2. 🧩 UARTインターフェース構造 / UART Interface Structure

PoCでは、UART通信処理を `uart_interface.py` にまとめています：  
In PoC, UART communication processing is consolidated in `uart_interface.py`:

```python
import serial

class UARTInterface:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def send(self, message: str):
        # メッセージ送信 / Send message
        self.ser.write((message + "\n").encode())

    def receive(self) -> str:
        # メッセージ受信 / Receive message
        if self.ser.in_waiting > 0:
            return self.ser.readline().decode().strip()
        return ""
```

> UARTポート・ボーレートはデバイス構成に応じて設定します。  
> UART port and baudrate are configured according to the device setup.

---

## 3. 🔁 制御ループでの利用例 / Usage in Control Loop

```python
uart = UARTInterface()

while True:
    cmd = uart.receive()
    if cmd:
        fsm.handle_event(cmd)

    speed, angle = fsm.get_output()
    pwm = pid.compute(speed, sensor.read_distance())
    uart.send(f"Speed:{speed}, Angle:{angle}, PWM:{pwm}")
```

---

## 4. 🔄 拡張設計の方向性 / Extension Design Directions

| 項目 / Item | 設計方針 / Design Policy |
|-------------|--------------------------|
| **コマンドプロトコル化 / Command Protocol** | JSONやバイナリでコマンド体系化 / Structure commands in JSON or binary |
| **双方向同期 / Bi-Directional Sync** | 状態同期とコマンド適用のタイムスタンプ化 / Timestamp synchronization |
| **エラーハンドリング / Error Handling** | 再送・CRCチェックによる信頼性確保 / Ensure reliability via retransmission and CRC |

---

## 🔚 まとめ / Summary

UART通信は、AITL-H PoCにおける**上位系と制御系の橋渡し**として機能します。  
UART communication functions as the **bridge between upper-level systems and the control system** in AITL-H PoC.

適切なプロトコル化とエラー対策により、堅牢で拡張可能な通信基盤を実現します。  
Proper protocol structuring and error handling ensure a robust and extensible communication infrastructure.

---

### 🔗 **ナビゲーション / Navigation**
- ⏮ [第04章：センサ・アクチュエータ制御 / Sensor & Actuator Control](https://samizo-aitl.github.io/AITL-H/docs/chapter04_sensor_interface.html)  
- ▶️ [第06章：制御アーキテクチャ実装 / Control Architecture](https://samizo-aitl.github.io/AITL-H/docs/chapter06_run_main_arch.html)  

[← AITL-H PoC マニュアル README / Back to AITL-H PoC Manual README](https://samizo-aitl.github.io/AITL-H/docs/)

---

### 📝 **ライセンス / License**
- **Code:** MIT  
- **Text:** CC BY 4.0  
- **Figures:** CC BY-NC 4.0  
（詳細は [Docs Index のライセンス表 / License Table in Docs Index](https://samizo-aitl.github.io/AITL-H/docs/#-ライセンス--license) を参照）
