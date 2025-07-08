# 付録C：PoCDK→SystemDK変換事例集

## 📘 本付録の目的

本付録では、PoC設計キット（PoCDK）をSystem開発キット（SystemDK）へ変換した具体的事例を提示します。FSM/PID/LLM構成を保持したまま、再利用性や展開性を高めるための変換手順と成果例を示します。

---

## 🧪 ケース①：介護支援ロボットPoC

### 📝 変換前（PoCDK）

| 要素               | 内容                               |
|--------------------|------------------------------------|
| FSM構成            | `fsm_config.yaml`（状態数5）         |
| PID制御            | `pid_controller.v`（固定ゲイン）     |
| LLMインタフェース  | `llm_interface.py`（直接呼び出し）   |
| ログ               | `interaction_log/2025_02_10.txt`    |

### 🔄 変換後（SystemDK）

| 要素               | 内容                                      |
|--------------------|-------------------------------------------|
| FSMテンプレート化  | `base_fsm_template.yaml`（状態抽象化済）     |
| PID IP化           | `pid_core_module.v`（パラメトラブル対応）     |
| LLM抽象化          | `llm_prompt_base.json`（分類タグ付き）         |
| ログ整備           | `scenario_response_db.json`（JSON形式変換）   |

---

## 🤖 ケース②：視線追従型インタフェースPoC

### 📝 変換前（PoCDK）

| 要素               | 内容                                  |
|--------------------|---------------------------------------|
| アナログIF         | `eye_sensor_if.v`（ノイズ補正なし）      |
| FSM構成            | `gaze_fsm.yaml`（状態数3）              |
| LLM出力            | `llm_gaze_log.txt`                     |

### 🔄 変換後（SystemDK）

| 要素               | 内容                                           |
|--------------------|------------------------------------------------|
| アナログIF再設計   | `analog_if_core.v`（IR補正＋ゲイン調整対応）     |
| FSMテンプレート    | `gaze_control_template.yaml`                  |
| LLM応答整理        | `prompt_tuning_gaze.json`（時系列付き分類ログ）   |

---

## ✍️ 補足と留意点

- FSMとPIDは**テンプレート分離とパラメータ独立化**が鍵
- LLMはPoC依存性が高く、**プロンプトの階層構造化**が再利用性に寄与
- 変換成果物は `SystemDK/` 以下に集約し、再展開可能な構成に整備

---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com
