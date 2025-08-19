---
layout: clean
permalink: /docs/
title: "AITL-H PoC Manual | Project Design Hub"
description: "AITL-HのPoC実装マニュアル。PID・FSM・LLM三層構造の制御設計とPoC仕様を解説。"
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

> マウスオーバーで各章の詳細ツールチップが表示されます。

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

## 📚 **関連資料 / Related Resources**

### 🏠 **AITL-H トップ / AITL-H Top**
[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)  
[![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

### 🎛️ **EduControllerとの接続 / Connection with EduController**

**AITL-H** は、教育教材 **EduController** の第9章（FSM × PID × LLMハイブリッド制御）と**完全に統合**されています。  

| 章 | 内容 | AITL-Hとの関係 |
|----|------|----------------|
| **Part 01〜05**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#制御理論系) | 古典〜現代制御理論（PID、状態空間など） | **PID層の理論的基盤** |
| **Part 06〜08**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#ai制御系) | AI制御（NN制御、強化学習、データ駆動） | **AI応用設計の補完知識** |
| **Part 09**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)&nbsp;[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | FSM × PID × LLM 統合制御 | **AITL-Hのアーキテクチャを教材として実装** |

### 🎓 **Edusemi-v4xとの統合設計展開 / Integration with Edusemi-v4x**

**SoC/RTL設計まで発展**させたい場合は、**[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** の「特別編」にて、以下の内容が提供されています：

| 章 | 内容 | リンク |
|----|------|--------|
| 第3章 | FSM × PID × LLM 統合制御による SoC設計 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |
| 第4章 | OpenLaneによるRTL 〜 GDSII レイアウト自動化 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) |
| 第5章 | DRC / LVS / DFM による物理検証と整合性確認 | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) |

📌 **さらに物理制約を深く学びたい場合**  
SoC設計〜物理検証の流れを理解したら、**特別編 第2a章：SystemDKにおける熱・応力・ノイズ制約の設計対応**へ進んでください。  

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)  
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk)

### 📂 **関連プロジェクト一覧 / Related Projects**

| プロジェクト | 説明 | リンク |
|--------------|------|--------|
| **AITL-H** | ハイブリッド制御PoCマニュアル | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| **Edusemi-v4x** | 半導体／SoC設計教材 | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| **EduController** | 制御理論×AI制御教材 | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| **SamizoGPT** | Project Design Hubガイド管理 | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT) |
| **AITL-Strategy-Proposal** | AITL戦略提言・政策提案 | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-Strategy-Proposal/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-Strategy-Proposal) |

---

📅 **最終更新 / Last Updated**:
{% if page.last_modified_at %}
  {{ page.last_modified_at | date: "%Y-%m-%d" }}
{% elsif page.date %}
  {{ page.date | date: "%Y-%m-%d" }}
{% else %}
  August 2025
{% endif %}

✍️ **著者 / Author**: 三溝 真一（Shinichi Samizo）
