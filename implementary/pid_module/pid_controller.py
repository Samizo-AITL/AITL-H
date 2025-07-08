# pid_controller.py
# AITL-H プロジェクト用 PID制御クラス
# FSMやLLM層からの目標値指示に対し、物理層での応答制御を担う

class PIDController:
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=0.0):
        """
        PID制御器の初期化
        :param kp: 比例ゲイン
        :param ki: 積分ゲイン
        :param kd: 微分ゲイン
        :param setpoint: 目標値
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint

        self.integral = 0.0
        self.prev_error = 0.0
        self.last_output = 0.0

    def reset(self):
        """内部状態をリセット（積分項・前回誤差）"""
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, measurement, dt=0.01):
        """
        現在の計測値から制御出力を計算する
        :param measurement: 実測値（センサ値など）
        :param dt: サンプリング周期（秒）
        :return: 制御出力（u）
        """
        error = self.setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0

        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )

        self.prev_error = error
        self.last_output = output
        return output

    def set_setpoint(self, new_setpoint):
        """目標値を更新"""
        self.setpoint = new_setpoint
