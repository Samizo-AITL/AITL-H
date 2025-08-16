---
layout: clean
# title: AITL-H/docs/index.md
---

---

# 📘 **AITL-H PoC Manual**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/) 

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

本サイトは、**AITL-H（All-in-Theory Logic - Hybrid）**のPoC実装に関するマニュアルページです。  
**PID・FSM・LLM**の三層構造に基づいた制御設計と、PoC仕様への落とし込み方を解説します。  
_This site serves as the manual page for the PoC implementation of AITL-H (All-in-Theory Logic - Hybrid)._  
_It explains the control design based on the three-layer architecture of **PID**, **FSM**, and **LLM**, and how to realize them in PoC specifications._

---

## 📂 **Chapter Structure (Chapters 1–8, 11)**

| 章番号 / Chapter | タイトル / Title | 説明 / Description |
|------------------|------------------|---------------------|
| **第1章 / Ch.1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter01_aitl_architecture.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter01_aitl_architecture.md) | **PoC仕様策定と要件定義**<br>_PoC Specification and Requirements_ | AITLの視点に基づくPoC構想とアーキテクチャ全体の設計<br>_AITL-based PoC concept and overall architecture_ |
| **第2章 / Ch.2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter02_pid_design.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter02_pid_design.md) | **PID制御設計と応答チューニング**<br>_PID Design and Response Tuning_ | Reason層としてのPIDゲイン設計と誤差補正の基本戦略<br>_PID gain tuning and error correction strategies_ |
| **第3章 / Ch.3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter03_fsm_design.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter03_fsm_design.md) | **FSMとRTL制御の実装**<br>_FSM and RTL Implementation_ | FSM中心の本能層の状態設計と制御フロー構成<br>_Instinct-layer state design and control flow via FSM_ |
| **第4章 / Ch.4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter04_sensor_interface.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter04_sensor_interface.md) | **センサ・アクチュエータ制御**<br>_Sensor and Actuator Control_ | ADC・PWM・I/Oなど物理層インタフェースの設計<br>_Design of physical interfaces (ADC, PWM, I/O)_ |
| **第5章 / Ch.5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter05_uart_control.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter05_uart_control.md) | **UART通信制御**<br>_UART Communication Control_ | PoCにおけるUART通信設計とホスト連携制御方式<br>_UART and host integration design in PoC_ |
| **第6章 / Ch.6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter06_run_main_arch.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter06_run_main_arch.md) | **制御アーキテクチャ実装**<br>_Control Architecture Implementation_ | `run_main()` を中心とした統合制御構造の設計<br>_Unified control architecture centered on `run_main()`_ |
| **第7章 / Ch.7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter07_log_monitoring.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter07_log_monitoring.md) | **ログ出力とモニタリング戦略**<br>_Logging and Monitoring Strategy_ | PoC制御ログ構成と可視化ツール導入<br>_Log output and visualization for evaluation_ |
| **第8章 / Ch.8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter08_llm_integration.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter08_llm_integration.md) | **LLM連携と意図推定処理**<br>_LLM Integration and Intent Estimation_ | 知性層（LLM）との連携構造と推論接続<br>_LLM interface and inference architecture_ |
| **第11章 / Ch.11**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](chapter11_exit_strategy.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter11_exit_strategy.md) | **出口戦略とSystemDKへの接続展望**<br>_Exit Strategy and SystemDK Expansion_ | RTL/PDK実装への展開、SystemDKとの接続構想の提示<br>_Transition to RTL/PDK implementation and SystemDK linkage_ |

---

## 🧩 **Planned Future Chapters (Placeholders)**

| 章番号 / Chapter | タイトル（仮） / Tentative Title | ステータス / Status |
|------------------|----------------------------------|----------------------|
| **第9章 / Ch.9** | 評価と検証方法<br>_Evaluation and Testing Methods_ | 🔧 作成予定 / Planned |
| **第10章 / Ch.10** | 応用事例（人型ロボット）<br>_Use Case: Humanoid Robot_ | 🔧 作成予定 / Planned |
| **第12章 / Ch.12** | モデル予測制御との融合<br>_Fusion with Model Predictive Control_ | 🔧 構想中 / In Concept |
| **第13章 / Ch.13** | ROS連携と自律移動<br>_ROS Integration and Autonomous Navigation_ | 🔧 準備中 / In Preparation |
| **第14章 / Ch.14** | AI学習との連動（強化学習）<br>_Reinforcement Learning Integration_ | 🔧 未着手 / Not Started |
| **第15章 / Ch.15** | ハードウェア実装支援ツール群<br>_Hardware Implementation Tools_ | 🔧 予定 / Planned |
| **第16章 / Ch.16** | 実機動作・展示事例集<br>_Demonstration and Exhibition Cases_ | 🔧 予定 / Planned |

---

## 📄 **ライセンス / License**

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> **本プロジェクトはハイブリッドライセンスを採用**  
> 教材・コード・図表の性質に応じて以下のライセンスを適用します。

| **📌 項目 / Item** | **ライセンス / License** | **説明 / Description** |
|--------------------|--------------------------|------------------------|
| **コード（Code）** | **[MIT License](https://opensource.org/licenses/MIT)** | 自由に使用・改変・再配布可 |
| **教材テキスト（Text materials）** | **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** | 著者表示必須 |
| **図表・イラスト（Figures & diagrams）** | **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** | 非商用利用のみ可 |
| **外部引用（External references）** | 元ライセンスに従う | 引用元を明記 |

---

## 🔗 **AITL-H Top**

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)  [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

---

📅 **最終更新 / Last Updated**: July 2025  
✍️ **著者 / Author**: 三溝 真一（Shinichi Samizo）
