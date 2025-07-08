"""
fsm_engine.py — FSM制御エンジン（AITL-H PoC用）

本モジュールは、fsm_config.yaml に定義された状態遷移表を元に、
UARTやセンサからの入力に応じて、現在状態を管理し、PIDへの制御目標を出力する。
"""

import yaml

class FSMEngine:
    def __init__(self, config_path):
        self.state = None
        self.transitions = {}
        self.actions = {}
        self.load_config(config_path)

    def load_config(self, path):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        self.state = config.get('initial_state')
        self.transitions = config.get('transitions', {})
        self.actions = config.get('actions', {})

    def update(self, input_event):
        """ 入力イベント（uart_cmdやsensor_trigger）に基づいて状態遷移 """
        key = f"{self.state}:{input_event}"
        if key in self.transitions:
            new_state = self.transitions[key]
            print(f"[FSM] {self.state} → {new_state} (on '{input_event}')")
            self.state = new_state
        else:
            print(f"[FSM] 状態遷移なし: {self.state} + '{input_event}'")

    def get_output(self):
        """ 現在の状態に対応する制御目標（target_speed, target_angleなど）を返す """
        return self.actions.get(self.state, {})

# 動作確認（テスト用）
if __name__ == "__main__":
    fsm = FSMEngine("fsm_config.yaml")
    fsm.update("start")
    print(fsm.get_output())
