# 第2章：制御系設計の実務ポイント

---

## 🎯 本章の目的

本章では、PoCにおける制御系設計の構造と実装ポイントを示します。  
AITL構想における「本能（FSM）＋理性（PID）」を軸とし、**状態管理・目標追従・実行制御**の3要素を構造的に連携させます。

---

## 🧠 三層制御モデルの中核：FSMとPIDの連携

| 層 | 担当機能 | 実装対象 | 備考 |
|----|----------|----------|------|
| FSM（本能） | 状態選択／アクション管理 | `fsm_config.yaml`, `fsm_engine.py` | 状態定義はYAML形式で柔軟に記述 |
| PID（理性） | 位置制御／姿勢制御 | `pid_controller.py` | 移動・停止・回転などの基本制御 |
| 実行制御 | 統合制御・ログ記録 | `run_main.py` | FSMとPIDを呼び出してPoCを統合運用 |

---

## 📋 状態遷移の定義（FSM構造）

```yaml
initial_state: idle

states:
  idle:
    on_enter:
      - control: stop
    transitions:
      - event: start_command
        next_state: approach_target

  approach_target:
    on_enter:
      - control: move
        target: [1.0, 0.5]
    transitions:
      - event: reached_target
        next_state: check_condition

  check_condition:
    on_enter:
      - control: llm_decide
        input: "Is it safe to interact?"
    transitions:
      - event: llm_yes
        next_state: interact
      - event: llm_no
        next_state: abort

  interact:
    on_enter:
      - control: move
        target: [0.0, 0.0]
    transitions:
      - event: interaction_done
        next_state: idle

  abort:
    on_enter:
      - control: stop
    transitions:
      - event: reset
        next_state: idle
```
	•	状態ごとの行動記述（例：move, stop, llm_decide）はFSM内で完結
	•	YAMLにより状態追加・修正が容易で、構造的制御に適する

## 🔧 PID制御の役割と構成例

PoCでは以下のような単純な目標追従型PID制御を仮定します：

```python
def move_to(self, target):
    while not self.reached_target(target):
        error = target - self.get_current_position()
        control_signal = self.kp * error
        self.apply_motor_signal(control_signal)
```

　 •	move_to(target)：FSMから命令されて位置制御を開始
	•	stop()：即時停止制御（PWM=0）を想定

## 🔗 統合制御の流れ（run_main.py）

```
current_state = fsm.get_current_state()
action = fsm.get_action(current_state)

if action["control"] == "move":
    pid.move_to(action["target"])
elif action["control"] == "stop":
    pid.stop()
elif action["control"] == "llm_decide":
    result = llm.judge(action["input"])
    fsm.feed_event("llm_" + result)
```

	•	FSMが行動を選択し、PID・LLMへ制御命令を発行
	•	LLMの判断結果をFSMへフィードバック（イベント入力）

## 📌 制御設計上の注意点

- FSM構成は「人が読める・修正できる」構造にすること  
- PID制御は実装の簡便さより、現場のセンサ・遅延特性への適応性を重視  
- 状態遷移ログを残すことでPoC評価と再設計が容易になる

---

## 📈 制御の評価指標（PoC段階）

| 項目             | 評価方法       | 成功基準例                     |
|------------------|----------------|--------------------------------|
| 状態遷移の妥当性 | ログ検証       | 意図通りの状態順で遷移する     |
| 追従精度（PID）  | センサ vs 目標 | 誤差 ±10cm 以内                 |
| LLM判断分岐      | 応答ログ確認   | yes/no 分岐が正しく反映される |

---

## 🔗 関連ファイル

- `fsm_config.yaml`：状態定義ファイル  
- `run_main.py`：PoC統合実行スクリプト  
- `implementary/pid_controller.py`：PID制御ロジック  
- `implementary/fsm_engine.py`：FSMエンジン（YAML解析＋遷移）

---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com


