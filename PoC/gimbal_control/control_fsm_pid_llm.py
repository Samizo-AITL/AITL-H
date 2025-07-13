# control_fsm_pid_llm.py
"""
FSM + MIMO PID + LLM統合制御本体
AITL-HX構成：状態管理・姿勢制御・知能連携を統括
"""

from imu_sensor_model import IMUSensorModel
from motor_pwm_driver import MotorPWMDriver
from llm_goal_agent import LLMGoalAgent

class GimbalController:
    def __init__(self, config):
        self.fsm_state = "idle"
        self.pid_gains = config["pid_gains"]
        self.imu = IMUSensorModel()
        self.motor = MotorPWMDriver()
        self.llm = LLMGoalAgent()
    
    def run_step(self, sensor_data):
        # FSM遷移ロジック（簡易版）
        if self.fsm_state == "idle" and sensor_data["trigger"]:
            self.fsm_state = "move"
        elif self.fsm_state == "move" and sensor_data["overload"]:
            self.fsm_state = "error"
        elif self.fsm_state == "error" and sensor_data["reset"]:
            self.fsm_state = "idle"
        
        # PID制御ロジック
        if self.fsm_state == "move":
            control_output = self.compute_pid(sensor_data)
            self.motor.apply_pwm(control_output)
    
    def compute_pid(self, sensor_data):
        # 簡易PID（1軸のみ例示）
        error = sensor_data["target_angle"] - sensor_data["current_angle"]
        pwm = self.pid_gains["P"] * error
        return pwm
