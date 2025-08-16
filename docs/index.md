---
layout: clean
# title: AITL-H/docs/index.md
---

---

# 📘 **AITL-H PoC Manual**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

本サイトは、**AITL-H（All-in-Theory Logic - Hybrid）** のPoC実装マニュアルです。  
**PID・FSM・LLM** の三層構造に基づく制御設計と、そのPoC仕様への落とし込みを解説します。  
_This site serves as the PoC manual for AITL-H, explaining the control design based on the three-layer architecture of **PID**, **FSM**, and **LLM**, and how to realize them in PoC specifications._

---

## 📂 **Chapter Structure** _(Ch.1–8, 11)_

| Ch. | タイトル / Title | 説明 / Description |
|-----|------------------|---------------------|
| **1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter01_aitl_architecture.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter01_aitl_architecture.md) | **PoC仕様策定と要件定義**<br>_PoC Specification & Requirements_ | AITL視点でのPoC構想と全体設計 |
| **2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter02_pid_design.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter02_pid_design.md) | **PID制御設計と応答チューニング**<br>_PID Design & Tuning_ | Reason層のPIDゲイン設計と誤差補正 |
| **3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter03_fsm_design.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter03_fsm_design.md) | **FSMとRTL制御実装**<br>_FSM & RTL Implementation_ | Instinct層の状態設計と制御フロー |
| **4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter04_sensor_interface.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter04_sensor_interface.md) | **センサ・アクチュエータ制御**<br>_Sensor & Actuator Control_ | ADC・PWM・I/Oの物理層インタフェース |
| **5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter05_uart_control.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter05_uart_control.md) | **UART通信制御**<br>_UART Communication_ | PoCのUART設計とホスト連携 |
| **6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter06_run_main_arch.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter06_run_main_arch.md) | **制御アーキテクチャ実装**<br>_Control Architecture_ | `run_main()`中心の統合制御 |
| **7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter07_log_monitoring.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter07_log_monitoring.md) | **ログ出力とモニタリング**<br>_Logging & Monitoring_ | 制御ログ構成と可視化 |
| **8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter08_llm_integration.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter08_llm_integration.md) | **LLM連携と意図推定**<br>_LLM Integration_ | 知性層との連携構造と推論接続 |
| **11**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](/AITL-H/chapter11_exit_strategy.md) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter11_exit_strategy.md) | **出口戦略とSystemDK接続**<br>_Exit Strategy_ | RTL/PDK展開とSystemDK連携構想 |

---

## 🧩 **Planned Future Chapters**

| Ch. | タイトル / Title | ステータス / Status |
|-----|------------------|----------------------|
| 9 | 評価と検証方法<br>_Evaluation & Testing_ | 🔧 Planned |
| 10 | 応用事例（人型ロボット）<br>_Use Case: Humanoid Robot_ | 🔧 Planned |
| 12 | モデル予測制御との融合<br>_Fusion with MPC_ | 🔧 Concept |
| 13 | ROS連携と自律移動<br>_ROS Integration_ | 🔧 Preparation |
| 14 | AI学習との連動（強化学習）<br>_RL Integration_ | 🔧 Not Started |
| 15 | ハードウェア実装支援ツール群<br>_HW Tools_ | 🔧 Planned |
| 16 | 実機動作・展示事例集<br>_Demonstrations_ | 🔧 Planned |

---

## 📄 **ライセンス / License**

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> **本プロジェクトはハイブリッドライセンス**を採用。教材・コード・図表の性質に応じて以下を適用。

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|---------------|----------------------|--------------------|
| **コード** | [MIT](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可 |
| **教材テキスト** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須 |
| **図表・イラスト** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可 |
| **外部引用** | 元ライセンスに従う | 引用元を明記 |

---

## 🔗 **AITL-H Top**

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

---

📅 **最終更新 / Last Updated**: July 2025  
✍️ **著者 / Author**: 三溝 真一（Shinichi Samizo）
