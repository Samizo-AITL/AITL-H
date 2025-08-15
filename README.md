---
layout: default
title: AITL-H/README.md
---

---

# 🤖 **AITL-H：Hybrid型構造制御フレームワーク**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

> ⚠️ **開発・検証中 / Under Development**  
> 本プロジェクトは現在も **発展途上** にあり、構成・仕様・実装内容は今後変更される可能性があります。  
> 利用・参照の際は、最新のリポジトリ内容をご確認ください。

---

## 🔗 公式リンク | Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/en) |

---

**AITL-H（All-in-Theory Logic - Hybrid）** は、人型ロボットや適応型システムに向けて設計された **階層型知能制御アーキテクチャ** です。  
**FSM（本能） × PID（理性） × LLM（知性）** の三層構造により、**瞬時性・安定性・柔軟性** を兼ね備えた制御を実現します。

---

## 🧭 **概要**

| 項目 | 内容 |
|------|------|
| **名称** | **AITL-H（Hybrid）** |
| **目的** | **構造的AI制御による人型ロボット制御手法の確立** |
| **中核原理** | - **FSM**：状態遷移による本能的行動制御<br>- **PID**：物理量（角度・速度）の連続制御<br>- **LLM**：高度な判断・対話・学習による知能化 |

---

## 🧘 **三層アーキテクチャ構成**

| 層 | 機能 | 実装例 |
|----|------|--------|
| **FSM層** | 状態遷移に基づくロジック制御 | `fsm_engine.py`, `fsm_state_def.yaml` |
| **PID層** | 各関節・移動量の物理制御 | `pid_controller.py`, `pid_module.py` |
| **LLM層** | 状況判断、異常検出、言語応答 | `llm_interface.py`, `llm_logger.py` |

> 各層は **疎結合・協調的** に設計されており、**独立した開発・段階的統合が可能** です。

<div align="center">
  <img src="theory/aitl_h_architecture.png" alt="AITL-H アーキテクチャ構成図" width="400">
</div>

---

## 📘 **PoC設計マニュアル**

📖 **FSM×PID×LLM統合に基づいた人型ロボットPoC設計マニュアル（全16章）**  
[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/docs)

---

## 🧪 **PoC一覧**

| タイトル | 概要 | パス |
|----------|------|------|
| 🧭 **ジンバル制御（FSM + PID + LLM）** | ハイブリッド閉ループ制御 | [`PoC/gimbal_control`](./PoC/gimbal_control) |
| ⚙️ **Verilog自動生成（FSM + PID）** | YAML → C → Verilog生成＋検証 | [`PoC/verilog_demo`](./PoC/verilog_demo) |

---

## 🧪 **PoC例：FSM × PID × LLMによる3軸ジンバル制御**

> **自然言語指令 → 状態遷移（FSM） → PID安定制御 → アクチュエータ** という閉ループ構成。  
> 教育・応用に最適な **AITL-HXアーキテクチャ** の基本実装。

📂 ディレクトリ：[`PoC/gimbal_control/`](./PoC/gimbal_control/)  
📘 詳細：[`READMEはこちら`](./PoC/gimbal_control/README.md)

<div align="center">
  <img src="./docs/images/figure9_1_gimbal_control_architecture.svg" alt="ジンバル制御アーキテクチャ" width="700">
</div>

---

## 🧪 **Verilog自動生成PoC（FSM×PID）**

> FSM／PIDの **動作仕様（YAML）** から  
> **Cコード → 統合C → Verilog** を **ChatGPTと連携** して生成・検証

📂 ディレクトリ：[`PoC/verilog_demo/`](./PoC/verilog_demo/)  
📘 詳細：[`READMEはこちら`](./PoC/verilog_demo/README.md)

---

## 🤖 **ChatGPT支援ツール群**

`accelerated_design/` にて **ChatGPTを用いた設計支援ツール** を提供：

- 状態遷移設計支援（プロンプト → FSM YAML自動化）
- テストシナリオ／ログ可視化
- 設計ドキュメントの自動生成

> 人とAIの **協調設計フレームワーク** を実現するツール群です。

---

## 📂 **ディレクトリ構成**

```
AITL-H/
├── theory/                # 構造設計思想・アーキテクチャ解説
├── PoC/                   # 制御PoCコード・シナリオログ
├── implementary/          # FSM/PID/LLMのPythonモジュール実装
└── accelerated_design/    # GPT連携の設計支援ツール
```

---

## 🎓 **EduControllerとの接続**

**AITL-H** は、教育教材 **[EduController](https://github.com/Samizo-AITL/EduController)** の第9章（FSM × PID × LLMハイブリッド制御）と**完全に統合**されています。

| 章 | 内容 | AITL-Hとの関係 |
|----|------|----------------|
| [**Part 01〜05**](https://github.com/Samizo-AITL/EduController#制御理論系) | 古典〜現代制御理論（PID、状態空間など） | **PID層の理論的基盤** |
| [**Part 06〜08**](https://github.com/Samizo-AITL/EduController#ai制御系) | AI制御（NN制御、強化学習、データ駆動） | **AI応用設計の補完知識** |
| [**Part 09**](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | FSM × PID × LLM 統合制御 | **AITL-Hのアーキテクチャを教材として実装** |

🔗 [**EduControllerリポジトリを見る**](https://github.com/Samizo-AITL/EduController)

---

## 🧩 **Edusemi-v4xとの統合設計展開**

**SoC/RTL設計まで発展**させたい場合は、  
**[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** の「特別編」にて、以下の内容が提供されています：

| 章 | 内容 | リンク |
|----|------|--------|
| 第3章 | FSM × PID × LLM 統合制御による SoC設計 | [🔗 第3章を見る](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |
| 第4章 | OpenLaneによるRTL 〜 GDSII レイアウト自動化 | [🔗 第4章を見る](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) |
| 第5章 | DRC / LVS / DFM による物理検証と整合性確認 | [🔗 第5章を見る](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) |

🔗 [**Edusemi-v4x リポジトリを見る**](https://github.com/Samizo-AITL/Edusemi-v4x)

---

## 📚 **関連プロジェクト一覧**

- [**Edusemi-v4x**](https://github.com/Samizo-AITL/Edusemi-v4x)：半導体／SoC設計教材  
- [**EduController**](https://github.com/Samizo-AITL/EduController)：制御理論×AI制御教材

---

## 👤 **執筆者情報 / Author**

| 項目 / Item | 詳細 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **学歴 / Education** | 信州大学大学院 電気電子工学 修了 |
| **職歴 / Career** | 元 セイコーエプソン株式会社 技術者（1997年〜） |
| **専門分野 / Expertise** | 半導体デバイス（ロジック・メモリ・高耐圧混載）、インクジェット薄膜ピエゾアクチュエータ、PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育 |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

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

💬 ご意見・議論は [**Discussionページ**](https://github.com/Samizo-AITL/AITL-H/discussions) へどうぞ。

