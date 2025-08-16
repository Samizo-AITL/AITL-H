---
layout: clean
permalink: /docs/
title: "AITL-H PoC Manual | Project Design Hub"
show_title: false
description: "AITL-H (All-in-Theory Logic - Hybrid) のPoC実装マニュアル。PID・FSM・LLM三層構造の制御設計とPoC仕様を解説。"
---

<!-- Structured Data (SEO) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "AITL-H PoC Manual",
  "about": ["PID", "FSM", "LLM", "Control Architecture", "PoC"],
  "author": {"@type": "Person","name": "Shinichi Samizo"},
  "inLanguage": "ja",
  "url": "https://samizo-aitl.github.io/AITL-H/docs/",
  "license": "https://opensource.org/licenses/MIT",
  "isPartOf": {"@type": "CreativeWorkSeries","name": "Project Design Hub"}
}
</script>

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

| Ch. | タイトル / Title | 説明 / Description | Links |
|-----|------------------|--------------------|-------|
| **0** | **序章：PoC概要と背景**<br>_Introduction & Background_ | <abbr title="AITL-H PoCの目的、背景、全体像、および本マニュアルの使い方を解説">目的と背景説明</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter00_introduction.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter00_introduction.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **1** | **PoC仕様策定と要件定義**<br>_PoC Specification & Requirements_ | <abbr title="AITL視点でのPoC構想・目的・非機能要件・全体ブロック図を定義">PoC構想と全体設計</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter01_aitl_architecture.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter01_aitl_architecture.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **2** | **PID制御設計と応答チューニング**<br>_PID Design & Tuning_ | <abbr title="Reason層のPIDゲイン設計・整定時間/オーバーシュート・ロバスト化">PIDゲイン設計と誤差補正</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter02_pid_design.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter02_pid_design.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **3** | **FSMとRTL制御実装**<br>_FSM & RTL Implementation_ | <abbr title="Instinct層の状態設計・遷移論理・安全設計（フェイルセーフ/ウォッチドッグ）">状態設計と制御フロー</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter03_fsm_design.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter03_fsm_design.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **4** | **センサ・アクチュエータ制御**<br>_Sensor & Actuator Control_ | <abbr title="ADC／PWM／GPIO等の物理I/F、スケーリングとキャリブレーション">物理層インタフェース</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter04_sensor_interface.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter04_sensor_interface.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **5** | **UART通信制御**<br>_UART Communication_ | <abbr title="PoCのUARTプロトコル、ホスト連携、ログ/テレメトリ設計">UART設計とホスト連携</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter05_uart_control.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter05_uart_control.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **6** | **制御アーキテクチャ実装**<br>_Control Architecture_ | <abbr title="run_main()中心の制御統合、割込み/スレッド指針、例外処理">統合制御</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter06_run_main_arch.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter06_run_main_arch.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **7** | **ログ出力とモニタリング**<br>_Logging & Monitoring_ | <abbr title="観測項目・ログレベル・収集周期・可視化・健全性監視">ログ構成と可視化</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter07_log_monitoring.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter07_log_monitoring.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **8** | **LLM連携と意図推定**<br>_LLM Integration_ | <abbr title="知性層とのAPI設計・プロンプト方針・安全枠組・出力検証">連携構造と推論接続</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter08_llm_integration.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter08_llm_integration.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |
| **11** | **出口戦略とSystemDK接続**<br>_Exit Strategy_ | <abbr title="RTL/PDK展開、SystemDK連携のロードマップと移行ガイド">RTL/PDK展開とSystemDK連携</abbr> | <div class="docs-links"><a href="https://samizo-aitl.github.io/AITL-H/docs/chapter11_exit_strategy.html"><img alt="View Site" src="https://img.shields.io/badge/View-Site-brightgreen?logo=github"></a><a href="https://github.com/Samizo-AITL/AITL-H/blob/main/docs/chapter11_exit_strategy.md"><img alt="View Repo" src="https://img.shields.io/badge/View-Repo-blue?logo=github"></a></div> |

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

📅 **最終更新 / Last Updated**:
{% if page.last_modified_at %}
  {{ page.last_modified_at | date: "%Y-%m-%d" }}
{% elsif page.date %}
  {{ page.date | date: "%Y-%m-%d" }}
{% else %}
  August 2025
{% endif %}

✍️ **著者 / Author**: 三溝 真一（Shinichi Samizo）
