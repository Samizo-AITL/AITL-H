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

> **本PoCは Samizo-AITL プロジェクトの「集大成」として位置づけられます。**  
> AITL-Hの三層アーキテクチャ（FSM × PID × LLM）を基盤に、**頭脳（22nm SoC）／感覚（0.18µm AMS）／筋肉（0.35µm LDMOS）**を跨いだクロスノード設計をSystemDKで統合検証します。  

---

## 🧩 クロスノード・チップセット
| ブロック | ノード | 役割 / 主要IF |
|---|---|---|
| **Brain SoC** | **22 nm** | LLM推論・FSM管理・状態空間制御（LQR/LQG）IP / **UART・SPI・I²C・MIPI-CSI2** |
| **Sensor Hub** | **0.18 µm AMS** | CMOSカメラ, IMU, エンコーダ, 力覚/圧力, MEMSマイク / **I²C・SPI・DVP・CSI2** |
| **Power Drive** | **0.35 µm LDMOS** | サーボ・BLDC駆動, PWM/Hブリッジ, ゲートドライバ, 温度/電流モニタ |

---

## ⚙️ 制御アーキテクチャ
| 層 | 実装 | 役割 |
|---|---|---|
| **LLM層** | SoC上アプリ/RTOS | 目標生成・異常解釈・学習 |
| **FSM層** | `fsm_engine.py` / YAML→C→Verilog | 行動モード切替（立位・歩行・旋回・転倒回避） |
| **物理制御層** | PID＋状態空間（LQR/LQG） | 局所SISO安定化＋全身MIMO協調制御 |
| **駆動層** | LDMOS PWM/Hブリッジ | トルク出力・安全監視 |

---

## 📷 代表センサ構成
- **CMOSイメージセンサ**（MIPI-CSI2 / DVP）  
- **IMU（6/9軸）＋エンコーダ**  
- **力覚/圧力センサ**（グリップ・足裏）  
- **MEMSマイク**（音声）  
- **温度センサ**（駆動系/SoCサーマル）  

---

## 🧭 SystemDK統合設計フロー
```mermaid
flowchart TB
  Spec[Use-Case Spec] --> Model[SystemDK Multi-physics Model]
  Model --> Ctrl[PID + State-Space Design]
  Ctrl --> RTL[22nm SoC]
  Model --> AMS[0.18µm AMS AFE/ADC]
  Model --> PWR[0.35µm LDMOS Drive]
  RTL -->|UART/SPI/I2C/CSI2| AMS
  RTL -->|PWM/Telemetry| PWR
  PWR -.Heat/Noise/Stress.-> Model
  AMS -.Noise/Coupling.-> Model
```

---

## 🎯 成功指標（KPI）
- **姿勢回復時間** ≤ 200 ms  
- **歩容安定度**（CoM偏差RMS）**30%改善**（PID単独比）  
- **エネルギー効率** 15%改善（協調制御導入）  
- **異常検知誤差率**（LLM+FSM） < 2%  

---

## 📂 ディレクトリ構成（予定）
```
humanoid/
 ├─ README.md
 ├─ hw/            # SoC, AMS, LDMOS 設計
 ├─ control/       # FSM, PID, 状態空間, LLM
 ├─ systemdk/      # モデル & シミュレーション
 ├─ docs/          # マニュアル・テスト仕様
 └─ logs/          # 実験ログ
```

---

## 🔗 関連リンク
- [EduController Part09](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)  
- [Edusemi-v4x 特別編](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/)  
- [AITL-Strategy-Proposal](https://samizo-aitl.github.io/AITL-Strategy-Proposal/)  
