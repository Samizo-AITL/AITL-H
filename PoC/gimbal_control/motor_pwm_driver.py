# motor_pwm_driver.py
"""
PWM制御モータドライバ（模擬）
"""

class MotorPWMDriver:
    def __init__(self):
        self.output = {"roll": 0, "pitch": 0, "yaw": 0}

    def apply_pwm(self, pwm_values):
        self.output = pwm_values
        print(f"PWM output applied: {pwm_values}")
