---
layout: clean
title: AITL-H / PoC - 人型ロボット制御（集大成）
nav_order: 2
description: FSM + PID + 状態空間制御 + LLM による三層アーキテクチャを用いた人型ロボット制御の概念実証
permalink: /PoC/humanoid/
last_updated: 2025-08-25
---

---

# 🚩 フラグシップPoC：人型ロボット（Samizo-AITL集大成）
*🚩 Flagship PoC: Humanoid Robot (Culmination of Samizo-AITL)*

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

---

> **本PoCは Samizo-AITL プロジェクトの「集大成」**。<br/>
> *This PoC is positioned as the "culmination" of the Samizo-AITL project.*<br/>
> AITL-Hの三層アーキテクチャ（FSM × PID × LLM）を基盤に、**頭脳（22 nm SoC）／感覚（0.18 µm AMS）／筋肉（0.35 µm LDMOS）／自己発電ブロック**を跨いだクロスノード設計を、SystemDKで統合検証します。<br/>
> *Based on AITL-H (FSM × PID × LLM), cross-node design spanning Brain (22 nm SoC), Sensing (0.18 µm AMS), Muscles (0.35 µm LDMOS), and Energy Harvesting is integrated and verified with SystemDK.*

---

## 🔗 公式リンク / Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/humanoid/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid) |

---

## 🧩 クロスノード・チップセット / Cross-Node Chipset

| ブロック / Block | ノード / Node | 役割・IF / Role & Interface |
|---|---|---|
| **Brain SoC** | **22 nm** | **LLM推論・FSM管理・状態空間制御（LQR/LQG IP）**<br/>*LLM inference, FSM management, state-space control (LQR/LQG IP)*<br/>UART / SPI / I²C / MIPI-CSI2 |
| **Sensor Hub** | **0.18 µm AMS** | **CMOSカメラ・IMU・エンコーダ・力覚/圧力・MEMSマイク**<br/>*CMOS camera, IMU, encoders, force/pressure, MEMS microphone*<br/>I²C / SPI / DVP / CSI2 |
| **Power Drive** | **0.35 µm LDMOS** | **PWM/Hブリッジ・サーボ/BLDC駆動・温度/電流モニタ**<br/>*PWM/H-bridge, servo/BLDC drive, temp/current monitor* |
| **Energy Harvest** | **Piezo / PV / Regen** | **発電・蓄電・DC-DC電源供給**<br/>*Energy harvesting, storage, DC-DC power* |

---

## ⚙️ 制御アーキテクチャ / Control Architecture

| 層 / Layer | 実装 / Implementation | 役割 / Role |
|---|---|---|
| **LLM層** | SoCアプリ / RTOS | **目標生成・異常解釈・学習**<br/>*Goal generation, anomaly interpretation, learning* |
| **FSM層** | `fsm_engine.py` ・ YAML→C→Verilog | **行動モード切替（立位/歩行/旋回/転倒回避/省エネ）**<br/>*Behavior mode switching* |
| **物理制御層** | PID＋状態空間（LQR/LQG） | **関節SISO安定化＋全身MIMO協調制御**<br/>*Joint SISO stabilization + whole-body MIMO control* |
| **駆動層** | LDMOS PWM/Hブリッジ | **トルク出力・安全監視**<br/>*Torque output, safety monitoring* |
| **エネルギー層** | 圧電 / PV / 回生制御 | **発電・蓄電・電力マネジメント**<br/>*Energy harvesting, storage, power management* |

---

## 📷 代表センサ構成 / Representative Sensors
- **CMOSイメージセンサ**（MIPI-CSI2 / DVP）<br/>*CMOS image sensor (MIPI-CSI2 / DVP)*
- **IMU（6/9軸）＋エンコーダ**<br/>*IMU (6/9-axis) + encoders*
- **力覚／圧力センサ**（グリップ・足裏）<br/>*Force/pressure sensors (grip, foot sole)*
- **MEMSマイク**（音声入力）<br/>*MEMS microphone (audio input)*
- **温度センサ**（駆動系／SoCサーマル管理）<br/>*Temperature sensors (drive/SoC thermal)*
- **圧電素子アレイ**（歩行衝撃からのエネルギー回収）<br/>*Piezo array (harvesting walking impact)*
- **薄膜PVセル**（外装からの光発電）<br/>*Thin-film PV cells (exterior light harvesting)*

---

## 🧭 SystemDK統合設計フロー / SystemDK Integrated Design Flow
```mermaid
flowchart TB
  Spec[Use-Case Spec] --> Model[SystemDK Multi-physics Model]
  Model --> Ctrl[PID + State-Space Design]
  Ctrl --> RTL[22nm SoC]
  Model --> AMS[0.18µm AMS AFE/ADC]
  Model --> PWR[0.35µm LDMOS Drive]
  Model --> Harvest[Energy Harvest: Regen / Piezo / PV]
  RTL -->|UART/SPI/I2C/CSI2| AMS
  RTL -->|PWM/Telemetry| PWR
  Harvest --> PWR
  Harvest --> RTL
  PWR -.Heat/Noise/Stress.-> Model
  AMS -.Noise/Coupling.-> Model
  Harvest -.Heat/Stress/Noise.-> Model
```

---

## 🎯 成功指標（KPI） / Key Performance Indicators
- **姿勢回復時間** ≤ 200 ms<br/>*Posture recovery time ≤ 200 ms*
- **歩容安定度**（CoM偏差RMS）**+30%**（PID単独比）<br/>*Gait stability +30% vs. PID-only*
- **エネルギー効率** **+15%**（協調制御＋ハーベスト）<br/>*Energy efficiency +15% (hybrid + harvesting)*
- **異常検知誤差率**（LLM+FSM） < 2%<br/>*Anomaly detection error < 2%*
- **自己発電寄与率**：消費電力量の最大 **20%補填**<br/>*Self-powering contribution up to 20%*

---

## 📂 ディレクトリ構成（予定） / Planned Directory Structure
```
humanoid/
 ├─ README.md
 ├─ hw/            # SoC, AMS, LDMOS 設計 / SoC, AMS, LDMOS design
 ├─ control/       # FSM, PID, 状態空間, LLM / FSM, PID, state-space, LLM
 ├─ systemdk/      # モデル & シミュレーション / Models & simulation
 ├─ energy/        # 自己発電・電力回生モデル / Energy harvesting & regen models
 ├─ docs/          # マニュアル・テスト仕様 / Manuals & test specs
 └─ logs/          # 実験ログ / Experiment logs
```

---

## 📚 関連プロジェクト・教材 / Related Projects & Materials

| プロジェクト / Project | 説明 / Description | リンク / Links |
|---|---|---|
| **EduController Part09** | FSM × PID × LLM統合制御教材<br/>*Integrated control (FSM × PID × LLM)* | [![🌐 Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/) [![💻 Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) |
| **Edusemi-v4x Chapter3** | FSM × PID × LLMによるSoC設計教材<br/>*SoC design with FSM × PID × LLM* | [![🌐 Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/) [![💻 Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |
| **AITL-Strategy-Proposal** | AITL戦略提言・政策提案<br/>*Strategy proposals & policy* | [![🌐 Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-Strategy-Proposal/) [![💻 Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-Strategy-Proposal) |

---

## 📑 詳細資料リンク / Reference Links

| 資料 / Material | 内容 / Description | リンク / Links |
|-----------------|--------------------|----------------|
| **Humanoid PoC Reports** | PWM Ripple / Thermal Derating / Mission Energy | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./docs/index.md) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid/docs) |
| **Flagship PoC Slides** | 発表用スライド雛形 / *Presentation draft slides* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./docs/flagship_poc_slides.md) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/PoC/humanoid/docs/flagship_poc_slides.md) |

---

## 👤 執筆者 / Author

| 項目 / Item | 内容 / Details |
|---|---|
| **著者 / Author** | 三溝 真一（Shinichi Samizo）<br/>*Shinichi Samizo* |
| **Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **X** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 ライセンス / License
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

| 項目 / Item | ライセンス / License | 説明 / Description |
|-------------|----------------------|--------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br/>*Free to use, modify, and redistribute* |
| **教材テキスト（Text）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br/>*Attribution required* |
| **図表・イラスト（Figures）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br/>*Non-commercial use only* |
| **外部引用（External refs）** | 元ライセンスに従う | 引用元を明記<br/>*Follow original license & cite* |

---

## 🔝 トップに戻る / Back to Top
[![🌐 Back to Site](https://img.shields.io/badge/Back_to-Site-brightgreen?logo=github)](../../) [![💻 Back to Repo](https://img.shields.io/badge/Back_to-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)
