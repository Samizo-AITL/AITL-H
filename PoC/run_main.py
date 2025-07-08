
"""
run_main.py — AITL-H PoC 統合制御エントリスクリプト

UART → FSM → PID → PWM という統合制御フローを実行。
"""

from fsm_engine import FSMEngine
from pid_controller import PIDController
from uart_driver import UARTDriver

def get_sensor_input():
    """ センサ値（仮に手動入力）を取得 """
    try:
        val = float(input("Sensor (measured speed): "))
        return val
    except ValueError:
        print("Invalid input. Defaulting to 0.0")
        return 0.0

def main():
    # 初期化
    fsm = FSMEngine("fsm_config.yaml")
    pid = PIDController(kp=2.0, ki=0.5, kd=0.1)
    uart = UARTDriver()

    print("=== AITL-H PoC 制御開始 ===")

    while True:
        cmd = uart.receive_command()
        if not cmd:
            continue

        fsm.update(cmd)
        targets = fsm.get_output()

        if not targets:
            print("[FSM] 現在状態に対応する出力なし")
            continue

        target_speed = targets.get("target_speed", 0.0)
        measured_speed = get_sensor_input()

        pwm = pid.compute(target_speed, measured_speed)
        print(f"[PID] Target: {target_speed}, Measured: {measured_speed} → PWM: {pwm}")

if __name__ == "__main__":
    main()
