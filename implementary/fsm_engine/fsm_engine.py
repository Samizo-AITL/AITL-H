# fsm_engine.py

class FSMEngine:
    def __init__(self, config):
        self.states = config.get("states", {})
        self.initial_state = config.get("initial_state")
        self.current_state = self.initial_state
        self.pending_event = None  # 外部からのイベントを一時保持
        self.last_action = []  # 現在の on_enter アクションリストを保持

        if self.current_state not in self.states:
            raise ValueError(f"Invalid initial state: {self.current_state}")

    def get_current_state(self):
        return self.current_state

    def get_action(self, state=None):
        """現在状態の on_enter アクションを返す（初回のみ）"""
        if state is None:
            state = self.current_state
        actions = self.states[state].get("on_enter", [])
        self.last_action = actions
        return actions

    def inject_event(self, event):
        """外部からのイベントを注入（LLM応答など）"""
        self.pending_event = event

    def next_state(self):
        """遷移条件に基づいて状態を更新"""
        state_def = self.states.get(self.current_state, {})
        transitions = state_def.get("transitions", [])

        # 優先：外部注入イベント
        if self.pending_event:
            for t in transitions:
                if t["event"] == self.pending_event:
                    print(f"[FSM] {self.current_state} → {t['next_state']} on {self.pending_event}")
                    self.current_state = t["next_state"]
                    self.pending_event = None
                    return
            print(f"[FSM] No matching transition for injected event: {self.pending_event}")
            self.pending_event = None

        # 次のイベント未指定の場合、何もしない
        else:
            print(f"[FSM] Waiting for external event in state: {self.current_state}")

    def is_finished(self):
        """状態が idle に戻れば終了と仮定"""
        return self.current_state == "idle" and self.last_action == []
