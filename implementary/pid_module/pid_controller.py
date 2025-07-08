
"""
pid_controller.py — PID制御器（AITL-H PoC用）

FSMから渡された制御目標値（target_speed, target_angle）と、
センサからの実測値に基づいて、PWM出力値を計算する。
"""

class PIDController:
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, dt=0.05):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt

        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, target, measured):
        """ PID制御出力を計算（target:目標値, measured:実測値）"""
        error = target - measured
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt

        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.prev_error = error

        # 0〜255 にクリップ（PWM用）
        pwm_value = max(0, min(255, int(output)))
        return pwm_value

# 動作確認（テスト用）
if __name__ == "__main__":
    pid = PIDController(kp=2.0, ki=0.5, kd=0.1)
    target = 5.0
    measured = 3.2
    pwm = pid.compute(target, measured)
    print(f"PID出力(PWM): {pwm}")
