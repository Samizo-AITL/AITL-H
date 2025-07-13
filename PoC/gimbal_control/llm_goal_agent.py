# llm_goal_agent.py
"""
自然言語命令 → 意図推論 → 目標指令（LLM）
"""

class LLMGoalAgent:
    def __init__(self):
        pass

    def generate_goal(self, user_prompt):
        # 簡易モック
        if "track" in user_prompt:
            return {"target_angle": 30}
        return {"target_angle": 0}
