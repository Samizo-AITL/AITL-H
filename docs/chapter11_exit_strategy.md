---
layout: clean
permalink: /docs/chapter11_exit_strategy.html
---

---

# 🚪 第11章：PoC出口戦略とSystemDKへの接続展望

本章では、AITL-H PoCで構築した制御系設計を、**ハードウェア実装やSoC統合へ橋渡しする戦略**を示します。  
ここでの出口戦略とは、PoCで設計・検証された構成を、RTL設計やPDKベースの実装に展開するための考え方です。

---

## 1. 🧭 PoCでどこまで設計したか

PoCで実現する範囲は以下の通りです：

- FSM・PID・LLMによる**統合制御設計**
- UART/PWM/Sensor制御の**Pythonレベルでの模擬運用**
- 状態遷移・制御パラメータの明示的な設計構造（yaml/python）

一方で、RTL記述・シリコン実装・レイアウト設計などは**範囲外**です。

---

## 2. 🛣 RTL/PDK展開への接続

PoC成果をRTL・PDKへ展開するには：

| PoC成果物 | 展開先 | コメント |
|-----------|--------|----------|
| `fsm_config.yaml` | FSM HDL記述 | ステートと遷移をVerilogに変換可能 |
| `pid_controller.py` | PID RTL記述 | 浮動小数点 → 固定小数点変換と精度検討が必要 |
| `sensor_interface.py` | I/F RTL記述 | センサプロトコルとの整合性確認が必要 |
| `run_main.py` | SoC統合設計 | 各ブロック統合の仕様書に変換 |

> これらはEdusemi教材（特別編）にて展開を予定

---

## 3. 🧩 SystemDKとの関係性

SystemDK（System Design Kit）は、複数の知能要素と制御要素をSoC/FPGA上に統合する設計キット構想です。

PoCは以下の点でSystemDKのプロトタイプと見なせます：

- 三層構造（FSM/PID/LLM）を**明示的にモジュール化**
- 状態・命令・信号の構造が**記述可能な形式で分離**
- **PoCで設計したものをブロック単位でRTL化**して持ち込める

---

## 4. 🔄 展開シナリオとフェーズ

| フェーズ | 内容 | 参考 |
|---------|------|------|
| Phase 0 | AITL-H PoC設計完了 | 現在地点 |
| Phase 1 | RTL記述への変換 | Edusemi特別編で対応 |
| Phase 2 | OpenLaneによる論理合成 | Edusemi実践編と連携 |
| Phase 3 | SoC統合とSystemDK化 | AITL構想の最終展開 |

---

## 🔚 まとめ

AITL-H PoCは、**実用制御アーキテクチャの理論設計をRTLに接続可能な形で提示**したものです。  
今後の展開はEdusemi特別編との連携を通じて、**実機ハードウェアへの接続と知的制御の実装**へ進んでいきます。

---
