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

このディレクトリは、AITL-H構想に基づく **各種Proof of Concept (PoC)** を格納しています。  
FSM（本能）＋ PID（理性）＋ LLM（知性）の三層アーキテクチャにより、**制御・推論・動作の統合検証**を行います。  

---

## 🔗 公式リンク / Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/PoC/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC) |

---

## 📚 PoC 一覧 / PoC List

| タイトル | 概要 | リンク |
|---|---|---|
| 🚩 **Humanoid Robot PoC（集大成）** | FSM × PID × LLM × 状態空間 × 自己発電を統合したフラグシップPoC | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./humanoid/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid) |
| 🧭 **ジンバル制御（FSM + PID + LLM）** | 教育用PoC。ハイブリッド閉ループ制御の基本例 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./gimbal_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control) |
| ⚙️ **Verilog自動生成（FSM + PID）** | YAML → C → Verilog 自動生成＋検証 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./verilog_demo/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/verilog_demo) |
| 🛠 **Auto Generator** | FSM・PID構成の自動生成ツール群 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](./auto_generator/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/auto_generator) |

---

## 📁 ディレクトリ構成 / Directory Layout

```
PoC/
├── humanoid/         # 人型ロボット制御PoC（集大成）
├── gimbal_control/   # 教育用ジンバル制御PoC
├── verilog_demo/     # Verilog自動生成PoC
├── auto_generator/   # FSM・PID自動生成ツール群
├── data/             # 実験ログ・センサデータ
├── scenario/         # 対話・行動シナリオ
├── hw/               # ハードウェア仕様
├── run_main.py       # PoC実行エントリ
├── fsm_config.yaml   # FSM状態定義
└── README.md         # ← 本ページ
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
[![🌐 Back to Site](https://img.shields.io/badge/Back_to-Site-brightgreen?logo=github)](../../) [![💻 Back to Repo](https://img.shields.io/badge/Back_to-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)
