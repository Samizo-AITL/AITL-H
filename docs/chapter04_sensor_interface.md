---
layout: clean
permalink: /docs/chapter04_sensor_interface.html
title: ""
show_title: false   # ← これで上部の自動H1バーを非表示
---

---

# 📡 第04章：センサ連動と環境反応性の設計  
**Chapter 04: Sensor Integration and Environmental Responsiveness**

本章では、AITL-H PoCにおける**センサインターフェースの設計方針**と、  
FSM・PIDへのデータ供給の役割、拡張可能なインターフェース設計について説明します。  

---

## 1. 🎯 センサの役割 / **Role of Sensors**

センサは、以下の2つの主要な制御層において重要な役割を果たします：

- **FSM**：環境イベントのトリガ（例：障害物検出 → `obstacle_detected`）  
- **PID**：制御対象の実測値（例：目標速度との差分）  

これにより、環境との**リアクティブな応答**と**フィードバック制御**が成立します。

---

## 2. 🧩 センサインターフェース構造 / **Sensor Interface Structure**

PoCでは、センサ読み出しと抽象化を `sensor_interface.py` により統一します：

```python
class SensorInterface:
    def __init__(self):
        self.distance = 0.0
        self.angle = 0.0

    def read_distance(self):
        # センサデバイスから距離（cm）を取得
        return self.distance

    def read_angle(self):
        # IMU等から角度（度）を取得
        return self.angle

    def update(self):
        # センサ値を一括更新（バッファ同期）
        self.distance = self._read_ultrasonic()
        self.angle = self._read_imu()
```

> センサ読み出しロジックは、仮想実装または物理デバイスに応じて差し替え可能です。

---

## 3. 🔁 FSM/PIDへの接続例 / **Example Connections to FSM & PID**

- FSMで使用：  

```python
if sensor.read_distance() < 10.0:
    fsm.handle_event("obstacle_detected")
```

- PIDで使用：  

```python
measured_speed = sensor.read_distance()
pwm = pid.compute(target_speed, measured_speed)
```

---

## 4. 🔄 拡張設計の方向性 / **Future Expansion Strategies**

| 項目 / Item       | 設計方針 / Design Policy |
|-------------------|-------------------------|
| センサの増加 / Sensor Addition | `read_xyz()` をインターフェースとして追加 |
| デバイス抽象 / Device Abstraction | 実装クラスを切替可能に（e.g. `MockSensor`, `RealSensor`） |
| LLM通知 / LLM Notification | センサ異常や外乱イベントをLLMに送信して判断委譲 |

---

## 🔚 まとめ / **Summary**

センサインターフェースは、FSM/PID/LLM間の共通データ基盤として、柔軟かつ拡張性ある構造が求められます。  
PoC設計においては、`sensor_interface.py` を用いてシンプルなAPIで統合しています。

---

[← PoCマニュアルのREADMEに戻る / Back to AITL-H PoC Manual README](README.md)
