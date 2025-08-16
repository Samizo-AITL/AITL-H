---
layout: clean
title: AITL-H/docs/toc.md
---

---

# 📘 AITL-H PoC 設計マニュアル：章構成一覧

このページでは、AITL-H構想に基づいたPoC設計マニュアルの章リンクを一覧化しています。

| 章番号 | タイトル | 説明 |
|--------|----------|------|
| [第0章](chapter00_overview.md) | PoC設計の全体像 | AITL-Hの設計目的と全体構成 |
| [第1章](chapter01_aitl_architecture.md) | 三層構造と設計視点 | FSM（本能）＋PID（理性）＋LLM（知性）の役割整理 |
| [第2章](chapter02_pid_design.md) | PID制御設計 | PID制御の基本構成・パラメータ調整 |
| [第3章](chapter03_fsm_design.md) | FSM設計 | 状態遷移の設計とシナリオ連携 |
| [第4章](chapter04_sensor_interface.md) | センサ・アクチュエータ制御 | I/O制御・ADC/PWM/デバイス連携の設計手法 |
| [第5章](chapter05_uart_control.md) | UART通信の構成 | UARTによる命令送信とPoC連携 |
| [第6章](chapter06_run_main_arch.md) | PoC統合実行構成 | run_mainによる制御統合と構成図 |
| [第7章](chapter07_log_monitoring.md) | ログ構成と記録設計 | 各制御モジュールからのログ出力 |
| [第8章](chapter08_llm_integration.md) | LLM拡張設計（構想） | LLMによる自己修復・強化学習展開 |
| 第9章 | （未定） | – |
| 第10章 | （未定） | – |
| [第11章](chapter11_exit_strategy.md) | 出口戦略とSystemDK接続 | SystemDKやハード実装への連携方針 |

---

※ 一部章は構想・ドラフト段階です。順次追加・改訂されていきます。
