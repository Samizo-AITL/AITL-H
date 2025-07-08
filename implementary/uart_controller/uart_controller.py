# 📡 uart_controller.py
# AITL-H用 UART通信制御クラス

import serial
import time

class UARTController:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        if self.ser.is_open:
            print(f"[UART] Opened port: {port} @ {baudrate}bps")

    def build_frame(self, command_id, payload):
        header = 0xAA
        payload_len = len(payload)
        frame = [header, command_id, payload_len] + payload
        checksum = self.calculate_checksum(frame[1:])  # exclude header
        frame.append(checksum)
        return bytes(frame)

    def calculate_checksum(self, data_bytes):
        # XOR方式
        checksum = 0
        for b in data_bytes:
            checksum ^= b
        return checksum

    def send_command(self, command_id, payload=[]):
        frame = self.build_frame(command_id, payload)
        self.ser.write(frame)
        print(f"[UART] Sent: {frame.hex()}")

    def read_frame(self):
        if self.ser.in_waiting >= 4:
            header = self.ser.read(1)
            if header != b'\xAA':
                print("[UART] Invalid header.")
                return None
            command_id = int.from_bytes(self.ser.read(1), "big")
            payload_len = int.from_bytes(self.ser.read(1), "big")
            payload = list(self.ser.read(payload_len))
            checksum = int.from_bytes(self.ser.read(1), "big")
            if checksum != self.calculate_checksum([command_id, payload_len] + payload):
                print("[UART] Checksum error.")
                return None
            return {
                "command_id": command_id,
                "payload": payload
            }

    def close(self):
        self.ser.close()
        print("[UART] Port closed.")
