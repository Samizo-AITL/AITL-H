# 📚 AITL-H PoC設計マニュアル

本ディレクトリは、AITL-H構想に基づく**三層制御アーキテクチャ（FSM / PID / LLM）**のPoC設計に関する文書群です。  
FSM（本能）・PID（理性）・LLM（知性）を分離し、それぞれの責任領域と統合戦略を体系的に整理します。

---

## 🗂 章構成一覧（v1.0）

| 章番号 | ファイル | 内容概要 |
|--------|----------|----------|
| 第0章 | [chapter00_overview.md](chapter00_overview.md) | PoC設計全体像と構成方針 |
| 第1章 | [chapter01_aitl_architecture.md](chapter01_aitl_architecture.md) | AITL三層構造の設計思想 |
| 第2章 | [chapter02_pid_design.md](chapter02_pid_design.md) | PID制御の基本構成とゲイン設計 |
| 第3章 | [chapter03_fsm_design.md](chapter03_fsm_design.md) | FSMによる状態管理と遷移戦略 |
| 第4章 | [chapter04_sensor_interface.md](chapter04_sensor_interface.md) | センサ連携と環境応答性設計 |
| 第5章 | [chapter05_uart_control.md](chapter05_uart_control.md) | UART通信による命令受信とFSM接続 |
| 第6章 | [chapter06_run_main_arch.md](chapter06_run_main_arch.md) | `run_main.py` による統合制御構成 |
| 第7章 | [chapter07_log_monitoring.md](chapter07_log_monitoring.md) | ログ記録とPoC可視化設計 |
| 第8章 | [chapter08_llm_integration.md](chapter08_llm_integration.md) | LLMとの統合と自己修復設計 |
| 第11章 | [chapter11_exit_strategy.md](chapter11_exit_strategy.md) | RTL/PDK展開とSystemDK接続戦略 |

---

## 📌 備考

- 各章は `PoC/docs/` 以下に整理
- 実装コードは `implementary/` に格納
- 実験構成・統合実行スクリプトは `PoC/` 直下に配置

---

## 📬 連絡先

技術監修・執筆：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---
