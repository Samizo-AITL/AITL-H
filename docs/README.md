# 📚 AITL-H PoC Design Manual

本ディレクトリは、AITL-H構想に基づく**三層制御アーキテクチャ（FSM / PID / LLM）**のPoC設計に関する文書群です。  
FSM（本能）・PID（理性）・LLM（知性）を分離し、それぞれの責任領域と統合戦略を体系的に整理します。  
_This directory contains documentation for the PoC design of the **three-layer control architecture (FSM / PID / LLM)** based on the AITL-H concept. FSM (instinct), PID (logic), and LLM (intelligence) are separated and systematically integrated._

---

## 🗂 Chapter List (v1.0)

| 章番号 / Chapter | ファイル / File | 内容概要 / Description |
|------------------|------------------|--------------------------|
| 第0章 / Ch.0     | [chapter00_overview.md](chapter00_overview.md) | PoC設計全体像と構成方針<br>_Overview and structural policy of PoC design_ |
| 第1章 / Ch.1     | [chapter01_aitl_architecture.md](chapter01_aitl_architecture.md) | AITL三層構造の設計思想<br>_Design philosophy of the AITL three-layer structure_ |
| 第2章 / Ch.2     | [chapter02_pid_design.md](chapter02_pid_design.md) | PID制御の基本構成とゲイン設計<br>_PID structure and gain design_ |
| 第3章 / Ch.3     | [chapter03_fsm_design.md](chapter03_fsm_design.md) | FSMによる状態管理と遷移戦略<br>_FSM-based state management and transition strategy_ |
| 第4章 / Ch.4     | [chapter04_sensor_interface.md](chapter04_sensor_interface.md) | センサ連携と環境応答性設計<br>_Sensor integration and environmental responsiveness_ |
| 第5章 / Ch.5     | [chapter05_uart_control.md](chapter05_uart_control.md) | UART通信による命令受信とFSM接続<br>_Receiving commands via UART and FSM integration_ |
| 第6章 / Ch.6     | [chapter06_run_main_arch.md](chapter06_run_main_arch.md) | `run_main.py` による統合制御構成<br>_Integrated control configuration using `run_main.py`_ |
| 第7章 / Ch.7     | [chapter07_log_monitoring.md](chapter07_log_monitoring.md) | ログ記録とPoC可視化設計<br>_Logging and PoC visualization design_ |
| 第8章 / Ch.8     | [chapter08_llm_integration.md](chapter08_llm_integration.md) | LLMとの統合と自己修復設計<br>_LLM integration and self-recovery design_ |
| 第11章 / Ch.11   | [chapter11_exit_strategy.md](chapter11_exit_strategy.md) | RTL/PDK展開とSystemDK接続戦略<br>_Strategy for RTL/PDK deployment and SystemDK integration_ |

---

## 📌 Notes

- 各章は `docs/` 以下に整理  
  _Each chapter is organized under the `docs/` directory_

- 実装コードは `implementary/` に格納  
  _Implementation code is stored in the `implementary/` directory_

- 実験構成・統合実行スクリプトは `PoC/` 直下に配置  
  _Experimental setups and integration scripts are placed directly under the `PoC/` directory_

---

## 📬 Contact

技術監修・執筆：**三溝 真一（Shinichi Samizo）**  
_Editor and Technical Supervisor: **Shinichi Samizo**_  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---
 
## 📜 License

MIT License  
教育・研究・個人開発での自由な利用・拡張を歓迎します。  
_Freely usable and extensible for educational, research, and personal development purposes._

---
