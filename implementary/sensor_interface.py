"""
sensor_interface.py — センサ入力模擬モジュール（AITL-H PoC用）

距離センサや角度センサの値を模擬的に生成・取得する。
現段階では手動入力またはダミーデータを返す。
"""

import random

class SensorInterface:
    def __init__(self, mode='manual'):
        """
        mode: 'manual' または 'dummy'
        """
        self.mode = mode

    def get_distance(self):
        if self.mode == 'manual':
            return self._manual_input("distance (cm)")
        elif self.mode == 'dummy':
            return random.uniform(10.0, 50.0)

    def get_angle(self):
        if self.mode == 'manual':
            return self._manual_input("angle (deg)")
        elif self.mode == 'dummy':
            return random.uniform(-30.0, 30.0)

    def _manual_input(self, label):
        try:
            val = float(input(f"Sensor input [{label}]: "))
            return val
        except ValueError:
            print("Invalid input. Defaulting to 0.0")
            return 0.0

# 動作確認（テスト用）
if __name__ == "__main__":
    sensor = SensorInterface(mode='manual')
    d = sensor.get_distance()
    a = sensor.get_angle()
    print(f"Distance: {d} cm, Angle: {a} deg")
