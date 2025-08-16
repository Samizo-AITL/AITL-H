---
layout: clean
title: "AITL-H PoC Manual"
permalink: /docs/
---

---

# 📘 **AITL-H PoC Manual**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

本サイトは、**AITL-H（All-in-Theory Logic - Hybrid）** のPoC実装に関するマニュアルページです。  
**PID・FSM・LLM** の三層構造に基づいた制御設計と、PoC仕様への落とし込み方を解説します。  
_This site serves as the manual page for the PoC implementation of AITL-H (All-in-Theory Logic - Hybrid). It explains the control design based on the three-layer architecture of **PID**, **FSM**, and **LLM**, and how to realize them in PoC specifications._

---

## 📂 **Chapter Structure** _(Absolute URLs with Description)_

| Ch. | タイトル / Title | 説明 / Description | Links |
|-----|------------------|--------------------|-------|
| **1** | **PoC仕様策定と要件定義**<br>_PoC Specification & Requirements_ | AITL視点でのPoC構想と全体設計 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter01_aitl_architecture.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter01_aitl_architecture.md) |
| **2** | **PID制御設計と応答チューニング**<br>_PID Design & Tuning_ | Reason層のPIDゲイン設計と誤差補正 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter02_pid_design.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter02_pid_design.md) |
| **3** | **FSMとRTL制御実装**<br>_FSM & RTL Implementation_ | Instinct層の状態設計と制御フロー | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter03_fsm_design.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter03_fsm_design.md) |
| **4** | **センサ・アクチュエータ制御**<br>_Sensor & Actuator Control_ | ADC・PWM・I/Oの物理層インタフェース | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter04_sensor_interface.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter04_sensor_interface.md) |
| **5** | **UART通信制御**<br>_UART Communication_ | PoCのUART設計とホスト連携 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter05_uart_control.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter05_uart_control.md) |
| **6** | **制御アーキテクチャ実装**<br>_Control Architecture_ | `run_main()` 中心の統合制御 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter06_run_main_arch.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter06_run_main_arch.md) |
| **7** | **ログ出力とモニタリング**<br>_Logging & Monitoring_ | 制御ログ構成と可視化 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter07_log_monitoring.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter07_log_monitoring.md) |
| **8** | **LLM連携と意図推定**<br>_LLM Integration_ | 知性層との連携構造と推論接続 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter08_llm_integration.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter08_llm_integration.md) |
| **11** | **出口戦略とSystemDK接続**<br>_Exit Strategy_ | RTL/PDK展開とSystemDK連携構想 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/chapter11_exit_strategy.html) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter11_exit_strategy.md) |

---

## 🧩 **Planned Future Chapters (Placeholders)**

| 章番号 / Chapter | タイトル（仮） / Tentative Title | ステータス / Status |
|------------------|----------------------------------|----------------------|
| **第9章 / Ch.9** | 評価と検証方法 _Evaluation & Testing_ | 🔧 作成予定 / Planned |
| **第10章 / Ch.10** | 応用事例（人型ロボット） _Humanoid Use Cases_ | 🔧 作成予定 / Planned |
| **第12章 / Ch.12** | モデル予測制御との融合 _Fusion with MPC_ | 🔧 構想中 / In Concept |
| **第13章 / Ch.13** | ROS連携と自律移動 _ROS & Autonomous Navigation_ | 🔧 準備中 / In Preparation |
| **第14章 / Ch.14** | 強化学習との連動 _Reinforcement Learning_ | 🔧 未着手 / Not Started |
| **第15章 / Ch.15** | ハードウェア実装支援ツール群 _HW Implementation Tools_ | 🔧 予定 / Planned |
| **第16章 / Ch.16** | 実機動作・展示事例集 _Demonstrations_ | 🔧 予定 / Planned |

---

## 📄 **ライセンス / License**

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

| **📌 項目 / Item** | **ライセンス / License** | **説明 / Description** |
|--------------------|--------------------------|------------------------|
| **コード（Code）** | **[MIT License](https://opensource.org/licenses/MIT)** | 自由に使用・改変・再配布可 |
| **教材テキスト（Text materials）** | **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** | 著者表示必須 |
| **図表・イラスト（Figures & diagrams）** | **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** | 非商用利用のみ可 |
| **外部引用（External references）** | 元ライセンスに従う | 引用元を明記 |

---

## 🔗 **AITL-H Top**

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)  
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

---

📅 **最終更新 / Last Updated**: July 2025  
✍️ **著者 / Author**: 三溝 真一（Shinichi Samizo）

