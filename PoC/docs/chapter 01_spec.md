# 第1章：PoC仕様策定と要件定義（AITL視点）

---

## 🎯 本章の目的

この章では、人型ロボットPoCにおける**設計仕様と開発要件**を明確にします。  
AITL三層構造（LLM／FSM／PID）を踏まえ、構造的・実装的な観点から必要な設計目標を定義します。

---

## 🧠 設計の出発点：AITL三層構造の分離と連携

| 層 | 機能 | 設計対象 | 主要インターフェース |
|----|------|----------|----------------------|
| 知性層（LLM） | 状況判断／異常認識／対話 | LLM判断トリガ | `llm_interface.py` |
| 制御層（FSM） | 行動の状態管理／遷移制御 | 状態記述／遷移条件 | `fsm_config.yaml` + `fsm_engine.py` |
| 物理層（PID） | 実行制御／目標追従／安定化 | モータ制御・位置姿勢制御 | `pid_controller.py` |

---

## 📋 基本仕様（PoC V1）

| 項目 | 内容 |
|------|------|
| プラットフォーム | Raspberry Pi + DCモータ + 距離センサ + 加速度センサ |
| 動作対象 | 小型人型ロボット（二輪 or 四脚） |
| 操作体系 | 自律動作＋外部トリガ入力（start/reset） |
| 通信・接続 | UART / GPIO / LLM API（ローカル or クラウド） |

---

## 🔁 状態遷移仕様（例）
```
idle ── start_command ─▶ approach_target ─▶ check_condition
├── llm_yes ─▶ interact ─▶ idle
└── llm_no  ─▶ abort ─▶ idle
```
- 状態とアクションは `fsm_config.yaml` にて定義
- 各状態で実行する制御（PID）や判断（LLM）は `run_main.py` で統合

---

## 🔧 要件定義（機能要件＋非機能要件）

### ✅ 機能要件

- [ ] 状態遷移定義に基づく行動制御
- [ ] PIDによる目標位置への追従制御（単純なmove-to）
- [ ] LLMによる状況判断（yes/noによる状態分岐）

### ✅ 非機能要件

- [ ] FSM構成の変更が容易であること（YAML外部定義）
- [ ] LLMとの通信は抽象化されていること（モックでも動作）
- [ ] 実験ログ（状態・センサ・判断）が記録されること

---

## 📈 評価指標（PoC段階）

| 項目 | 評価方法 | 成功条件（例） |
|------|----------|----------------|
| 状態遷移制御 | ログ解析 | 期待通りの順序で遷移 |
| PID追従精度 | センサログ | ±10cm以内で到達 |
| LLM応答分岐 | 出力確認 | yes/noが想定通り反映される |

---

## 📌 今後の拡張

- 音声認識／音声合成との統合
- 複数ロボットのFSM連携
- ローカルLLMへの切り替えによるオフライン化

---

## 🔗 関連ファイル

- [`../fsm_config.yaml`](../fsm_config.yaml)：状態遷移定義
- [`../run_main.py`](../run_main.py)：統合実行スクリプト
- [`../scenario/interaction_scenario.md`](../scenario/interaction_scenario.md)：PoC動作シナリオ概要

---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---
