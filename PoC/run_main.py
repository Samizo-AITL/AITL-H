# run_main.py
import argparse
import yaml
from implementary.fsm_engine import FSMEngine
from implementary.pid_controller import PIDController
from implementary.llm_interface import LLMInterface

def load_fsm_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="AITL-H PoC 実行統合スクリプト")
    parser.add_argument('--config', type=str, default='fsm_config.yaml',
                        help='FSM設定ファイル（YAML形式）')
    args = parser.parse_args()

    # FSM設定読み込み
    fsm_def = load_fsm_config(args.config)

    # モジュール初期化
    fsm = FSMEngine(fsm_def)
    pid = PIDController()
    llm = LLMInterface()

    print("✅ AITL-H PoC 起動：FSM + PID + LLM 統合")

    # メイン制御ループ
    while not fsm.is_finished():
        current_state = fsm.get_current_state()
        action = fsm.get_action(current_state)

        print(f"▶ 現在状態: {current_state} / 実行アクション: {action}")

        # 状態に応じたPID制御（例：移動、回転、停止）
        if action.get("control") == "move":
            pid.move_to(action.get("target"))
        elif action.get("control") == "stop":
            pid.stop()
        elif action.get("control") == "llm_decide":
            response = llm.judge(action.get("input"))
            print(f"💬 LLM判断結果: {response}")

        # 次状態へ遷移
        fsm.next_state()

    print("🏁 PoC 実行完了")

if __name__ == "__main__":
    main()
