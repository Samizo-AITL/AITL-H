# llm_interface.py
# AITL-H プロジェクト用 LLMインタフェース（スタブ実装）

import random

class LLMInterface:
    def __init__(self):
        print("[LLM] Interface initialized.")

    def judge(self, prompt):
        """
        LLMによる判断を模倣する簡易ダミー関数。
        :param prompt: 質問内容（例："Is it safe to interact?"）
        :return: 'llm_yes' または 'llm_no'
        """
        print(f"[LLM] Prompt received: {prompt}")
        
        # 仮の条件付き応答（ランダム／固定でも可）
        if "safe" in prompt.lower():
            response = random.choice(["llm_yes", "llm_no"])
        else:
            response = "llm_yes"

        print(f"[LLM] → Response: {response}")
        return response
