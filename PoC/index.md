---
layout: clean
title: AITL-H / PoC – 概要とリンク集
nav_order: 1
description: AITL-HにおけるPoCディレクトリ全体の概要とリンク集
permalink: /PoC/
last_updated: 2025-08-25
---

---

# 🤖 **AITL-H / PoC – 概要とリンク集**  
*🤖 AITL-H / PoC – Overview & Links*

---

このディレクトリは、AITL-H構想に基づく **各種Proof of Concept (PoC)** を格納しています。  
*This directory contains various **Proof of Concepts (PoC)** based on the AITL-H concept.*  

FSM（本能）＋ PID（理性）＋ LLM（知性）の三層アーキテクチャにより、**制御・推論・動作の統合検証**を行います。  
*Through a three-layer architecture of FSM (instinct) + PID (reason) + LLM (intelligence), integrated verification of control, inference, and motion is performed.*  

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC) |

---

## 📁 ディレクトリ構成 / *Directory Structure*

```
PoC/
├── humanoid/              # フラグシップPoC（人型ロボット制御） / Flagship PoC (Humanoid Robot Control)
├── gimbal_control/        # 教育用ジンバル制御PoC / Educational Gimbal Control PoC
├── verilog_demo/          # FSM+PID Verilog自動生成デモ / FSM+PID Verilog Auto-Generation Demo
├── auto_generator/        # FSM・PID自動生成ツール群 / FSM & PID Auto-Generation Tools
├── scenario/              # 対話・行動シナリオ定義 / Dialogue & Behavior Scenarios
├── data/                  # 実験ログ・センサデータ / Experiment Logs & Sensor Data
├── docs/                  # PoC設計マニュアル / PoC Design Manual
├── hw/                    # ハードウェア関連 / Hardware Related
├── run_main.py            # PoC統合実行エントリ / PoC Execution Entry
├── fsm_config.yaml        # FSM状態定義 / FSM State Definition
└── README.md              # ← 本ドキュメント / This Document
```

---

## 📚 PoC 一覧 / *PoC List*

| タイトル / Title | 概要 / Description | リンク / Links |
|---|---|---|
| 🚩 **Humanoid Robot PoC（集大成）**<br/>*Humanoid Robot PoC (Flagship)* | FSM × PID × LLM × 状態空間 × 自己発電を統合したフラグシップPoC<br/>*Flagship PoC integrating FSM × PID × LLM × State-Space × Energy Harvesting* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./humanoid/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid) |
| 🧭 **ジンバル制御（FSM + PID + LLM）**<br/>*Gimbal Control (FSM + PID + LLM)* | 教育用PoC。ハイブリッド閉ループ制御の基本例<br/>*Educational PoC. Basic hybrid closed-loop control example* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./gimbal_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control) |
| ⚙️ **Verilog自動生成（FSM + PID）**<br/>*Verilog Auto-Generation (FSM + PID)* | YAML → C → Verilog 自動生成＋検証<br/>*YAML → C → Verilog auto-generation & verification* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./verilog_demo/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/verilog_demo) |
| 🛠 **Auto Generator**<br/>*Auto Generator* | FSM・PID構成の自動生成ツール群<br/>*Automatic generation tools for FSM & PID* | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./auto_generator/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/auto_generator) |

---

## 📑 PoCマニュアル / *PoC Manual*

PoC全体の設計思想・章構成は **docs/** 以下に整理しています。  
*The overall design philosophy and chapter structure of the PoC are organized under **docs/**.*  

| ドキュメント / Document | 説明 / Description | リンク / Links |
|--------------|------|--------|
| 📘 **AITL-H PoC Manual** | PoC全体をカバーする実装マニュアル。PID・FSM・LLM三層構造の設計と仕様を解説。<br/>*Comprehensive manual covering PoC. Explains PID, FSM, and LLM three-layer design & specifications.* | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](../docs/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/docs) |

---

## ⚙️ 制御構成図 / *Control Structure*

```mermaid
graph TD
    UART[UART Driver] --> FSM[FSM Engine]
    FSM --> PID[PID Controller]
    PID --> PWM[PWM Driver]
    FSM -->|pwm_enable| PWM
    FSM -->|target_speed/angle| PID
    Sensor[Sensor Interface] --> FSM
    Sensor --> PID
```

- **UART Driver**：LLMからの命令をFSMに送信  
  *Sends commands from LLM to FSM*  
- **FSM Engine**：状態管理と制御目標出力（速度・角度）  
  *Manages states & outputs control targets (speed/angle)*  
- **PID Controller**：誤差に基づくPWM制御量生成  
  *Generates PWM control values based on error*  
- **PWM Driver**：最終出力信号（duty制御）  
  *Final output signal (duty control)*  
- **Sensor Interface**：FSMおよびPIDへ距離・角度センサ値を提供  
  *Provides distance & angle sensor values to FSM & PID*  

---

## 🚀 実行例 / *Execution Example*

```bash
# FSM定義・制御モジュールを統合してPoC制御を起動
# Launch PoC control by integrating FSM definition & control modules
python run_main.py --config fsm_config.yaml
```

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
[![🌐 Back to Site](https://img.shields.io/badge/Back_to-Site-brightgreen?logo=github)](./) [![💻 Back to Repo](https://img.shields.io/badge/Back_to-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

