# 🧠 AITL-H PoC設計マニュアル（構造化ドキュメント）

本マニュアルは、AITL構想に基づくPoC（Proof of Concept）設計において、FSM・PID・LLM・SoC統合などの観点から、人型ロボットや自律システムのPoCを体系的に記録・再利用することを目的としています。

---

## 📚 章構成一覧

| 区分     | 章番号 | タイトル | ファイル名 |
|----------|--------|----------|------------|
| 緒言     | 第0章  | PoC設計全体像・AITL対応マニュアル概要 | [chapter00_intro.md](chapter00_intro.md) |
| 基本技術 | 第1章  | PoC仕様策定と要件定義（AITL視点） | [chapter01_spec.md](chapter01_spec.md) |
|          | 第2章  | 制御系設計の実務ポイント | [chapter02_control.md](chapter02_control.md) |
|          | 第3章  | RTL設計のAITL対応実務ポイント | [chapter03_rtl.md](chapter03_rtl.md) |
|          | 第4章  | PDKとファウンドリ選定 | [chapter04_pdk.md](chapter04_pdk.md) |
|          | 第5章  | ソフト制御との連携設計 | [chapter05_sw_control.md](chapter05_sw_control.md) |
| 応用展開 | 第6章  | センサ混載技術とアナログIF設計 | [chapter06_sensor_if.md](chapter06_sensor_if.md) |
|          | 第7章  | DFT設計とテスト容易化 | [chapter07_dft.md](chapter07_dft.md) |
|          | 第8章  | AI自己修復PoC設計手法 | [chapter08_self_repair.md](chapter08_self_repair.md) |
|          | 第9章  | SoC統合と協調設計 | [chapter09_soc_integration.md](chapter09_soc_integration.md) |
|          | 第10章 | PoCプロジェクトの管理と評価 | [chapter10_project_management.md](chapter10_project_management.md) |
|          | 第11章 | 出口戦略とSystemDK移行設計 | [chapter11_exit_strategy.md](chapter11_exit_strategy.md) |
| 実装検証 | 第12章 | PoC評価の指標とプロジェクト管理 | [chapter12_evaluation_management.md](chapter12_evaluation_management.md) |
| 出口展開 | 第13章 | 製品化に向けた物理・実装検証 | [chapter13_physical_verification.md](chapter13_physical_verification.md) |
|          | 第14章 | 外付け・混載デバイスとのインタフェース設計 | [chapter14_mixed_device_interface.md](chapter14_mixed_device_interface.md) |
|          | 第15章 | SystemDK移行設計とIP再構成戦略 | [chapter15_systemdk_transition.md](chapter15_systemdk_transition.md) |
|          | 第16章 | 出口戦略別SystemDK開発方針 | [chapter16_exit_policy.md](chapter16_exit_policy.md) |

---

## 📎 付録資料

| 付録 | 内容 | ファイル名 |
|------|------|------------|
| A    | 設計テンプレート・PoC成果記録フォーマット | [appendix_a_templates.md](appendix_a_templates.md) |
| B    | 出口戦略別チェックリスト | [appendix_b_exit_checklist.md](appendix_b_exit_checklist.md) |
| C    | PoCDK→SystemDK変換事例集 | [appendix_c_conversion_cases.md](appendix_c_conversion_cases.md) |

---

## 🗂 関連ディレクトリ構成

```text
PoC/
├── docs/                 # 本マニュアル（このフォルダ）
├── scenario/             # 状態遷移・行動シナリオ（YAML/Markdown）
│   └── interaction_scenario.md
├── data/                 # 実行ログ・記録データ
│   └── .gitkeep（または README.md）
├── run_main.py           # 実行制御スクリプト（PoC起動エントリ）
└── fsm_config.yaml       # 状態遷移構成（FSM制御YAML）
```

## 🧑‍🔬 執筆・構成

三溝 真一（Shinichi Samizo）
GitHub: https://github.com/Samizo-AITL
Email: shin3t72@gmail.com

---
