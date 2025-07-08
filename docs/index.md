---
title: AITL-H PoC マニュアル
---

# 📘 AITL-H PoC マニュアル

本サイトは、AITL-H（All-in-Theory Logic - Hybrid）のPoC実装に関するマニュアルページです。  
PID・FSM・LLM などの三層構造に基づいた制御設計と、PoC仕様への落とし込み方を解説します。

---

## 📂 章構成一覧（第1〜11章）

| 章番号 | タイトル | 説明 |
|--------|----------|------|
| [第1章](chapter01_spec_definition.md) | PoC仕様策定と要件定義 | AITLの視点に基づくPoC設計の基本方針と要件定義 |
| [第2章](chapter02_pid_design.md) | PID制御設計と応答チューニング | Reason層としてのPIDゲイン設計と誤差補正の基本戦略 |
| [第3章](chapter03_rtl_fsm.md) | FSMとRTL制御の実装 | FSMを中心とした本能層の状態設計とRTL制御方針 |
| [第4章](chapter04_pdk_foundry.md) | PDKとファウンドリ選定 | AITL制御構造と整合するPDK・ファウンドリの選定基準 |
| [第5章](chapter05_software_riscv.md) | RISC-Vソフト連携設計 | ソフト層での外部制御連携とLLMインタフェース |
| [第6章](chapter06_interface_control.md) | センサ・アクチュエータ制御 | 物理層とのI/O制御・UART/ADC/PWM等の実装 |
| [第7章](chapter07_debug_strategy.md) | 実装とデバッグ戦略 | PoC開発における分割テストと段階検証の設計手法 |
| [第8章](chapter08_llm_integration.md) | LLM連携と意図推定処理 | 高次推論を活用した知性層（LLM）との連携設計 |
| [第9章](chapter09_eval_validation.md) | 評価と検証方法 | 実験・検証フロー、AITL制御の安定性/柔軟性評価 |
| [第10章](chapter10_usecase_robotics.md) | 応用事例（人型ロボット） | AITL-Hを用いたロボットPoCへの実装と動作例 |
| [第11章](chapter11_summary_future.md) | 総括と今後の展望 | AITL-H設計の総まとめと今後の研究展開方針 |

---

## 🧩 今後追加予定の章（プレースホルダ）

| 章番号 | タイトル（仮） | ステータス |
|--------|----------------|------------|
| 第12章 | モデル予測制御との融合 | 🔧 構想中 |
| 第13章 | ROS連携と自律移動 | 🔧 準備中 |
| 第14章 | AI学習との連動（強化学習） | 🔧 未着手 |
| 第15章 | ハードウェア実装支援ツール群 | 🔧 予定 |
| 第16章 | 実機動作・展示事例集 | 🔧 予定 |

---

## 🔗 関連リンク

- [AITL-H GitHubリポジトリ](https://github.com/Samizo-AITL/AITL-H)

---

📅 最終更新：2025年7月  
✍️ 著者：三溝真一（Shinichi Samizo）
