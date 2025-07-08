---
title: AITL-H PoC マニュアル
---

# 📘 AITL-H PoC マニュアル

本サイトは、AITL-H（All-in-Theory Logic - Hybrid）のPoC実装に関するマニュアルページです。  
PID・FSM・LLM などの三層構造に基づいた制御設計と、PoC仕様への落とし込み方を解説します。

---

## 📂 章構成一覧（第1〜8章・第11章）

| 章番号 | タイトル | 説明 |
|--------|----------|------|
| [第1章](chapter01_aitl_architecture.md) | PoC仕様策定と要件定義 | AITLの視点に基づくPoC構想・全体設計アーキテクチャ |
| [第2章](chapter02_pid_design.md) | PID制御設計と応答チューニング | Reason層としてのPIDゲイン設計と誤差補正の基本戦略 |
| [第3章](chapter03_fsm_design.md) | FSMとRTL制御の実装 | FSMを中心とした本能層の状態設計と制御フロー構成 |
| [第4章](chapter04_sensor_interface.md) | センサ・アクチュエータ制御 | 物理層インタフェース（ADC, PWM, I/O）の設計 |
| [第5章](chapter05_uart_control.md) | UART通信制御 | PoCにおけるUART通信設計とホスト連携制御方式 |
| [第6章](chapter06_run_main_arch.md) | 制御アーキテクチャ実装 | `run_main()` を中心とした統合制御構造と設計手法 |
| [第7章](chapter07_log_monitoring.md) | ログ出力とモニタリング戦略 | PoC制御ログ出力構成、評価用可視化手法の導入 |
| [第8章](chapter08_llm_integration.md) | LLM連携と意図推定処理 | 知性層（LLM）との接続方式と推論連携構造 |
| [第11章](chapter11_exit_strategy.md) | 総括と出口戦略 | AITL-H設計の成果まとめと今後の展望 |

---

## 🧩 今後追加予定の章（プレースホルダ）

| 章番号 | タイトル（仮） | ステータス |
|--------|----------------|------------|
| 第9章 | 評価と検証方法 | 🔧 作成予定（評価指標とテスト設計） |
| 第10章 | 応用事例（人型ロボット） | 🔧 作成予定（ロボット実装とユースケース） |
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
