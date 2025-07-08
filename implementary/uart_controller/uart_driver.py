"""
uart_driver.py — UART受信ドライバ（AITL-H PoC用）

LLM（知性層）からの制御命令をUART経由で受信し、FSMに渡す。
PoC段階では、標準入力から模擬的にコマンドを受け取る形式で実装。
"""

class UARTDriver:
    def __init__(self):
        self.latest_command = None

    def receive_command(self):
        """ UART受信（ここでは入力模擬） """
        try:
            cmd = input("UART> ").strip()
            self.latest_command = cmd
            return cmd
        except KeyboardInterrupt:
            print("\n[UART] 中断されました。")
            return None

    def get_latest(self):
        return self.latest_command

# 動作確認（テスト用）
if __name__ == "__main__":
    uart = UARTDriver()
    while True:
        command = uart.receive_command()
        if command:
            print(f"[UART] 受信コマンド: {command}")
