# fsm_engine.py

class FSMEngine:
    def __init__(self, state_def):
        """
        state_def: 状態定義（dict形式）
        """
        self.states = state_def.get("states", {})
        self.current_state = state_def.get("initial_state", None)

    def handle_input(self, input_signal):
        """
        入力に応じて状態を遷移させる
        """
        if self.current_state not in self.states:
            raise ValueError(f"未定義の状態: {self.current_state}")

        state_info = self.states[self.current_state]
        transitions = state_info.get("on_input", {})

        if input_signal in transitions:
            next_state = transitions[input_signal]
            print(f"[FSM] 状態遷移: {self.current_state} → {next_state}（入力: {input_signal}）")
            self.current_state = next_state
        else:
            print(f"[FSM] 入力 {input_signal} による遷移なし（状態: {self.current_state}）")

    def get_state(self):
        return self.current_state
