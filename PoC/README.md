# 🤖 AITL-H / PoC – 実装コードと実験構成

本ディレクトリは、AITL-H構想に基づく人型ロボットPoCの**実装コードおよび制御構成**を格納しています。  
FSM（本能）＋PID（理性）＋LLM（知性）という三層アーキテクチャにより、ロボットの行動制御・判断・改善を統合的に実現するためのPoC設計を支援します。

---

## 📁 ディレクトリ構成（PoC）
```
PoC/
├── fsm_engine.py             # FSMエンジン（状態遷移制御）
├── pid_controller.py         # PID制御ロジック（追従・姿勢制御）
├── llm_interface.py          # LLMと連携する知的判断モジュール
├── fsm_state_def.yaml        # 状態遷移定義ファイル（人間可読）
├── interaction_scenario.md   # 対話・実験シナリオ定義
├── data/                     # 実験ログ・センサデータ
├── docs/                     # 設計マニュアル（PoC全体の章構成）
│   └── README.md             # → PoC設計マニュアルのトップ
└── README.md                 # ← 本ドキュメント
```
---

## 🎯 このディレクトリの目的

- 実際のPoC制御・実験を担う**コードベースの中心**
- FSM/PID/LLMの統合実装に基づくロボット動作の**実証**
- `fsm_state_def.yaml` による**行動パターンの柔軟定義**
- 実験シナリオや結果を `data/`, `interaction_scenario.md` に蓄積

---

## 📘 設計マニュアル（PoC/docs/）

PoC設計の背景・構成方針・章構成に関するマニュアルは、以下のディレクトリに整理しています：

▶︎ [📚 PoC設計マニュアルへ](docs/README.md)

マニュアルには、次のような内容が含まれています：

- 第0章：PoC設計全体像とAITL構造の位置づけ
- 第1章：PoC仕様策定と要件定義
- 第2章以降：制御設計、RTL連携、PDK選定、SystemDK移行まで
- 付録：設計テンプレート、評価指標、変換事例集

---

## 🔧 今後の開発項目（予定）

- FSM状態のグラフィカル表示ツール
- LLMによる異常推論と自己修復判断（第8章参照）
- 制御ログの解析可視化スクリプト
- PoC成果をSystemDKに移行する変換ツール

---

## 📬 連絡先

技術監修・設計構成：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---
