---
layout: clean
permalink: /
title: ""
show_title: false   # ← これで上部の自動H1バーを非表示
---

---

# 🤖 **AITL-H：Hybrid型構造制御フレームワーク**
*🤖 AITL-H: Hybrid Structural Control Framework*

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

> ⚠️ **開発・検証中 / Under Development**  
> 本プロジェクトは現在も **発展途上** にあり、構成・仕様・実装内容は今後変更される可能性があります。  
> 利用・参照の際は、最新のリポジトリ内容をご確認ください。  
> *⚠️ **Under development/testing.** This project is still evolving, and its structure, specifications, and implementation may change. Please check the latest repository contents when using or referencing it.*

---

## 🆕 最新情報 / Update Log
| 日付 | 更新内容 / Update | 参照 |
|-----|-------------------|------|
| 2025-08-25 | 🚩 **Humanoid Robot PoC（集大成）** をトップに追加 | [PoCページ](./PoC/humanoid/) |
| 2025-08-25 | 📑 PoCレポート3本（PWM Ripple / Thermal / Mission Energy）公開 | [Docs Index](./PoC/humanoid/docs/) |
| 2025-08-25 | 🎤 発表用スライド雛形を追加 | [Slides](./PoC/humanoid/docs/flagship_poc_slides.md) |

---

## 🔗 公式リンク / Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/en) |

---

## 🧭 概要　/　Overview

| 項目 | 内容 |
|------|------|
| **名称** | **AITL-H（Hybrid）**<br>*AITL-H (Hybrid)* |
| **目的** | **構造的AI制御による人型ロボット制御手法の確立**<br>*Establishing humanoid robot control methods using structural AI control* |
| **中核原理** | - **FSM**：状態遷移による本能的行動制御<br>- **PID**：物理量（角度・速度）の連続制御<br>- **LLM**：高度な判断・対話・学習による知能化<br>*- **FSM**: instinctive behavior control through state transitions<br>- **PID**: continuous control of physical quantities (angle, velocity)<br>- **LLM**: intelligence through advanced decision-making, dialogue, and learning* |

---

## 🧘 三層アーキテクチャ構成　/　Three-Layer Architecture

| 層 | 機能 | 実装例 |
|----|------|--------|
| **FSM層** | 状態遷移に基づくロジック制御<br>*Logic control based on state transitions* | `fsm_engine.py`, `fsm_state_def.yaml` |
| **PID層** | 各関節・移動量の物理制御<br>*Physical control of joints and motion quantities* | `pid_controller.py`, `pid_module.py` |
| **LLM層** | 状況判断、異常検出、言語応答<br>*Situation assessment, anomaly detection, and language response* | `llm_interface.py`, `llm_logger.py` |

> 各層は **疎結合・協調的** に設計されており、**独立した開発・段階的統合が可能** です。  
> *Each layer is designed to be **loosely coupled yet cooperative**, allowing **independent development and step-by-step integration**.*

### AITL-H: Hybrid Architecture

> 📌 This diagram is **displayed on GitHub**. On the site, use the button below to view the GitHub version.  
> [![View on GitHub](https://img.shields.io/badge/View_on-GitHub-black?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/README.md#aitl-h-hybrid-architecture)

```mermaid
flowchart TB
  subgraph LLM["LLM Layer"]
    L1[Decision-Making]
    L2[Anomaly Detection]
    L3[Language Response]
  end
  subgraph PID["PID Layer"]
    P1[Continuous Control]
    P2[Joint Angles / MIMO]
  end
  subgraph FSM["FSM Layer"]
    F1[Logic Control]
    F2[State Transitions]
  end

  LLM -->|Scenario / Commands| FSM
  FSM -->|Mode Control / Gain Select| PID
  PID -->|PWM / Control Signals| ACT["Actuators"]
  ACT -->|Motion Response| SEN["Sensors (IMU, etc.)"]
  SEN -->|Perception Feedback| LLM

  classDef box fill:#eaf5ff,stroke:#6ca7ff,stroke-width:1px,rx:6,ry:6;
  class LLM,PID,FSM,ACT,SEN box

  click F1 "https://github.com/Samizo-AITL/AITL-H/search?q=fsm_engine.py" "FSM Implementation"
  click P1 "https://github.com/Samizo-AITL/AITL-H/search?q=pid_controller.py" "PID Implementation"
  click L1 "https://github.com/Samizo-AITL/AITL-H/search?q=llm_interface.py" "LLM Interface"
```

---

## 🌏 戦略的重要性　/  Strategic Significance

AITL-Hは、単なる制御アーキテクチャではなく、  
**状態フィードバック制御**と**状態遷移制御**を統合し、さらに**LLM（大規模言語モデル）**と**SystemDK**を組み合わせることで、  
**リアルタイムかつ物理制約を考慮した最適設計**を実現します。  
*AITL-H is not just a control architecture. By integrating **state feedback control** and **state transition control**, and further combining **LLMs** with **SystemDK**, it achieves **real-time optimal design under physical constraints**.*

- **産業的効果**  
  - 故障対応時間の大幅短縮（PoC評価値：94%削減）  
  - 生産ライン再構成時間を8倍短縮  
  - 設計変更対応コストを40%削減  
- **Industrial effects**  
  - Significantly reduced fault response time (PoC evaluation: 94% reduction)  
  - 8× faster reconfiguration of production lines  
  - 40% reduction in design change costs*  

- **国家的意義**  
  - 先端ノード半導体や産業用自律システムの競争力確保  
  - 国際標準化における主導権獲得  
- **National significance**  
  - Securing competitiveness in advanced-node semiconductors and industrial autonomous systems  
  - Gaining leadership in international standardization*  

> **この技術は「今」統合しなければならない。**  
> 特にSystemDKはAITL-H固有ではなく、**全ての先端ノード半導体設計に必須の基盤技術**です。  
> *This technology must be integrated **now**. In particular, SystemDK is not unique to AITL-H but is an **essential foundational technology for all advanced-node semiconductor designs**.*

---

## 🧪 PoC関連　/  PoC Related

| タイトル | 概要 | パス |
|----------|------|------|
| 📘 **PoC設計マニュアル** | FSM×PID×LLM統合に基づいた人型ロボットPoC設計マニュアル（全16章）<br>*Humanoid robot PoC design manual (16 chapters) based on FSM × PID × LLM integration.* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/docs) |
| 🤖 **PoC統合実行環境** | FSM＋PID＋LLMの三層アーキテクチャを用いたAITL-H PoC（人型ロボット制御）の実験構成・実行環境<br>*Experimental setup and execution environment for AITL-H PoC (humanoid robot control) using the three-layer architecture of FSM + PID + LLM.* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC) |
| 🧭 **ジンバル制御（FSM + PID + LLM）** | ハイブリッド閉ループ制御<br>*Hybrid closed-loop control.* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/gimbal_control/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control) |
| ⚙️ **Verilog自動生成（FSM + PID）** | YAML → C → Verilog生成＋検証<br>*Automatic conversion from YAML → C → Verilog with verification.* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/verilog_demo/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/verilog_demo) |
| 🛠 **Auto Generator（FSM・PID自動生成ツール）** | AITL-Hアーキテクチャに基づくFSM・PID構成をYAML→C→Verilog変換する自動生成支援ツール群<br>*Auto-generation support toolset for converting FSM/PID configurations based on the AITL-H architecture from YAML → C → Verilog.* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/auto_generator/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/auto_generator) |
| 🚩 **Humanoid Robot PoC（集大成）** | FSM × PID × LLM × 状態空間 × 自己発電を統合したフラグシップPoC<br>*Flagship PoC integrating FSM × PID × LLM × State-Space × Energy Harvesting* | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/humanoid/) <br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid) |

---

> 🚩 **フラグシップPoC：人型ロボット**  
> *Flagship PoC: Humanoid Robot*  
> Samizo-AITLの集大成として、クロスノード設計（22nm SoC / 0.18µm AMS / 0.35µm LDMOS / 自己発電）をSystemDKで統合。  
> 教育・産業・政策の三領域で優位性を発揮できるテーマです。

---

### ​ PoC例：FSM × PID × LLMによる3軸ジンバル制御
*PoC Example: 3-Axis Gimbal Control with FSM × PID × LLM*

> **自然言語指令 → 状態遷移（FSM） → PID安定制御 → アクチュエータ** の閉ループ構成。  
> 教育・応用に最適な **AITL-HXアーキテクチャ** の基本実装。  
> *Closed-loop structure: **Natural language commands → State transitions (FSM) → PID stabilization → Actuators**.  
> A basic implementation of the **AITL-HX architecture**, ideal for education and applications.*

📂 ディレクトリ：[**`PoC/gimbal_control/`**]  [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control)  
*📂 Directory: [**`PoC/gimbal_control/`**](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control)*  

📘 詳細：[**`READMEはこちら`**](https://samizo-aitl.github.io/AITL-H/PoC/gimbal_control/)  
*📘 Details: [**`README here`**](https://samizo-aitl.github.io/AITL-H/PoC/gimbal_control/)*  

```mermaid
flowchart TB
    subgraph LLM["LLM層 / *LLM Layer*"]
        direction TB
        LLM_desc["自然言語による指令生成・意図推論 / *Command generation & intent inference from natural language*"]
    end

    subgraph FSM["FSM層 / *FSM Layer*"]
        FSM_desc["行動切替（待機・追従・復帰 など） / *Behavior switching (standby, tracking, recovery, etc.)*"]
    end

    subgraph PID["PID層 / *PID Layer*"]
        PID_desc["Roll / Pitch / Yaw の MIMO PID制御 / *MIMO PID control of roll, pitch, yaw*"]
    end

    subgraph ACT["アクチュエータ層 / *Actuator Layer*"]
        ACT_desc["モータ駆動（PWM制御） / *Motor drive (PWM control)*"]
    end

    subgraph SENSOR["IMUセンサ層 / *IMU Sensor Layer*"]
        SENSOR_desc["姿勢センサ（角速度・加速度） / *Attitude sensors (angular velocity, acceleration)*"]
    end

    LLM --> FSM --> PID --> ACT
    ACT <--> SENSOR
    SENSOR --> LLM
```

---

## 🤖 ChatGPT支援ツール　/  ChatGPT-Assisted Toolset

`accelerated_design/` にて **ChatGPTを用いた設計支援ツール** を提供：  
*The directory `accelerated_design/` provides **design support tools using ChatGPT***:

- 状態遷移設計支援（プロンプト → FSM YAML自動化）  
  *State transition design support (prompt → automatic FSM YAML generation)*  
- テストシナリオ／ログ可視化  
  *Test scenario and log visualization*  
- 設計ドキュメントの自動生成  
  *Automatic generation of design documents*  

> 人とAIの **協調設計フレームワーク** を実現するツール群です。  
> *A toolset to realize a **collaborative design framework between humans and AI**.*

---

## 🎛️ EduControllerとの接続　　/  Connection with EduController

**AITL-H** は、教育教材 **EduController** の第9章（FSM × PID × LLMハイブリッド制御）と**完全に統合**されています。  
*AITL-H is **fully integrated** with Chapter 9 of the educational material **EduController** (FSM × PID × LLM hybrid control).*

| 章 | 内容 | AITL-Hとの関係 |
|----|------|----------------|
| **Part 01〜05**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#制御理論系) | 古典〜現代制御理論（PID、状態空間など）<br>*Classical to modern control theory (PID, state-space, etc.)* | **PID層の理論的基盤**<br>*Theoretical foundation of the PID layer* |
| **Part 06〜08**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#ai制御系) | AI制御（NN制御、強化学習、データ駆動）<br>*AI control (neural networks, reinforcement learning, data-driven)* | **AI応用設計の補完知識**<br>*Complementary knowledge for AI-based design* |
| **Part 09**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)&nbsp;[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | FSM × PID × LLM 統合制御<br>*Integrated control of FSM × PID × LLM* | **AITL-Hのアーキテクチャを教材として実装**<br>*Implements the AITL-H architecture as teaching material* |

---

## 🎓 Edusemi-v4xとの統合設計展開
*🎓 Integrated Design Development with Edusemi-v4x*

**SoC/RTL設計まで発展**させたい場合は、**[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** の「特別編」にて、以下の内容が提供されています：  
*If you want to expand to **SoC/RTL design**, the “Special Editions” of **[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** provide the following:*

| 章 | 内容 | リンク |
|----|------|--------|
| 第3章 | FSM × PID × LLM 統合制御による SoC設計<br>*SoC design with integrated FSM × PID × LLM control* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |
| 第4章 | OpenLaneによるRTL 〜 GDSII レイアウト自動化<br>*RTL-to-GDSII layout automation using OpenLane* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) |
| 第5章 | DRC / LVS / DFM による物理検証と整合性確認<br>*Physical verification and consistency checks with DRC / LVS / DFM* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) |

### 📌 さらに物理制約を深く学びたい場合
*📌 For deeper study of physical constraints*

SoC設計〜物理検証の流れを理解したら、**特別編 第2a章：SystemDKにおける熱・応力・ノイズ制約の設計対応**へ進んでください。  
*After understanding the SoC design-to-physical verification flow, proceed to **Special Edition Chapter 2a: Design for thermal, stress, and noise constraints in SystemDK**.*

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)  
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk)

---

## 📚 関連プロジェクト一覧　　/  Related Project List

| プロジェクト | 説明 | リンク |
|--------------|------|--------|
| **Edusemi-v4x** | 半導体／SoC設計教材<br>*Semiconductor / SoC design learning material* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| **EduController** | 制御理論×AI制御教材<br>*Control theory × AI control learning material* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| **SamizoGPT** | Project Design Hubガイド管理<br>*Project Design Hub guide management* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT) |
| **AITL-Strategy-Proposal** | AITL戦略提言・政策提案<br>*AITL strategy proposals and policy recommendations* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-Strategy-Proposal/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-Strategy-Proposal) |

---

## 👤 執筆者情報 / Author

| **📌 項目 / Item** | **内容 / Details** |
|--------------------|--------------------|
| **氏名 / Name** | **三溝 真一（Shinichi Samizo）**<br>*Shinichi Samizo* |
| **学歴 / Education** | **信州大学大学院 電気電子工学 修了**<br>*M.S. in Electrical and Electronic Engineering, Shinshu University* |
| **経歴 / Career** | **元 セイコーエプソン株式会社 技術者（1997年〜）**<br>*Former Engineer at Seiko Epson Corporation (since 1997)* |
| **経験領域 / Expertise** | **半導体デバイス**（ロジック・メモリ・高耐圧混載）<br>*Semiconductor devices (logic, memory, high-voltage mixed integration)*<br>**インクジェット薄膜ピエゾアクチュエータ**<br>*Inkjet thin-film piezo actuators*<br>**PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**<br>*Productization of PrecisionCore printheads, BOM management, and ISO training* |
| **✉️ Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **🐦　X** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 ライセンス / License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> **本プロジェクトはハイブリッドライセンスを採用**  
> *This project adopts a Hybrid License*  
> 教材・コード・図表の性質に応じて以下のライセンスを適用します。  
> *Different licenses are applied depending on whether the content is code, text, or figures.*

| **📌 項目 / Item** | **ライセンス / License** | **説明 / Description** |
|--------------------|--------------------------|------------------------|
| **コード（Code）** | **[MIT License](https://opensource.org/licenses/MIT)** | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow original license* | 引用元を明記<br>*Cite the original source* |

---

## 💬 フィードバック / Feedback

> 改善提案や議論は **GitHub Discussions** からお願いします。  
> *Propose improvements or start discussions via **GitHub Discussions**.*

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/AITL-H/discussions)

