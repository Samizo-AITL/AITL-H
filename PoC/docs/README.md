# 📘 AITL-H PoC 設計マニュアル

本ディレクトリでは、AITL-Hアーキテクチャに基づいた**人型ロボットPoCの制御設計手法**を、章ごとに整理しています。  
FSM（本能）・PID（理性）・LLM（知性）の三層構造を起点に、実験設計、統合制御、自己修復までの展開を明示します。

---

## 🧭 章構成一覧

| 章番号 | タイトル | 内容概要 |
|--------|----------|-----------|
| [第00章](chapter00_overview.md) | PoC設計全体像 | 三層モデルの設計思想とPoC全体構成 |
| [第01章](chapter01_aitl_architecture.md) | AITLの統合アーキテクチャ設計 | FSM / PID / LLM の分離と役割、制御階層の構成 |
| [第02章](chapter02_pid_design.md) | PID制御器の設計と応答チューニング | ゲイン設計・シミュレーション・安定性評価 |
| [第03章](chapter03_fsm_design.md) | FSM状態設計と遷移戦略 | 状態定義・トリガ設計・遷移表と行動生成の論理 |
| [第04章](chapter04_sensor_interface.md) | センサ連動と環境反応性 | 距離・角度センサを用いた動的制御反応の設計 |
| [第08章](chapter08_llm_integration.md) | LLM統合と自己修復設計 | LLMによるFSM/制御補正のPoC試行と課題 |
| [第11章](chapter11_exit_strategy.md) | 出口戦略とSystemDK連携 | RTL展開・Edusemi特別編との連携戦略 |

---

## 🛠 対象ディレクトリ構成

```
PoC/
├── docs/
│   ├── chapter00_overview.md
│   ├── chapter01_aitl_architecture.md
│   ├── chapter02_pid_design.md
│   ├── chapter03_fsm_design.md
│   ├── chapter04_sensor_interface.md
│   ├── chapter08_llm_integration.md
│   ├── chapter11_exit_strategy.md
│   └── README.md   ← 本ファイル
```

---

## 🧑‍💻 本設計マニュアルの目的

AITL-H制御PoCの構造・設計方針を体系的に整理し、各構成要素がどのように連携し、知性・理性・本能の分離実装が成立するかを明示します。  
PoC設計者、評価者、ハード展開の引き継ぎ者に向けて設計思想を伝達する**技術ブリーフィング資料**としての役割を担います。
