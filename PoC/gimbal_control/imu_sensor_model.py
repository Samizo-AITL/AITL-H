# imu_sensor_model.py
"""
3軸IMUセンサモデル（角速度・加速度）
"""

import random

class IMUSensorModel:
    def __init__(self):
        self.angle = {"roll": 0.0, "pitch": 0.0, "yaw": 0.0}

    def read(self):
        # ノイズ付き角度出力
        return {
            "roll": self.angle["roll"] + random.gauss(0, 0.1),
            "pitch": self.angle["pitch"] + random.gauss(0, 0.1),
            "yaw": self.angle["yaw"] + random.gauss(0, 0.1)
        }
