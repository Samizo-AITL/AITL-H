# 🧪 uart_test_sim.py
# UARTControllerの簡易動作確認スクリプト

from uart_controller import UARTController
import time

def main():
    uart = UARTController(port="/dev/ttyUSB0", baudrate=115200)

    try:
        # コマンドID 0x01 に任意ペイロード [0x10, 0x20]
        print("[Test] Sending test command...")
        uart.send_command(command_id=0x01, payload=[0x10, 0x20])

        # 受信待機（タイムアウトまで）
        print("[Test] Waiting for response...")
        start_time = time.time()
        while time.time() - start_time < 3:  # 3秒待機
            response = uart.read_frame()
            if response:
                print(f"[Test] Received: {response}")
                break
        else:
            print("[Test] No response received.")
    finally:
        uart.close()

if __name__ == "__main__":
    main()
