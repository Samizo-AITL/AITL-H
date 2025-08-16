---
layout: default
title: Verilog Demo（AITL-H統合制御モジュール動作検証）
nav_order: 10
description: AITL-HアーキテクチャにおけるFSM × PID × LLM統合制御モジュールのVerilog動作検証環境。
permalink: /AITL-H/PoC/verilog_demo/
---

---

# 🧪 verilog_demo/README.md

このディレクトリは、AITL-Hアーキテクチャにおける  
統合制御モジュール（FSM × PID × LLM）の **Verilog動作検証** を行うためのテスト環境です。  
_This directory provides a test environment for **Verilog-based functional verification** of the unified control module (FSM × PID × LLM) in the AITL-H architecture._

---

## 🧩 構成ファイル一覧  
### List of Files

| ファイル名 / File Name      | 内容 / Description |
|----------------------------|--------------------|
| `fsm_core.v`               | Moore型FSM制御ロジック<br>_Moore-type FSM control logic_ |
| `pid_controller.v`         | 離散時間PID制御器<br>_Discrete-time PID controller_ |
| `llm_interface_stub.v`     | 外部命令入力スタブ<br>_Stub for external LLM command input_ |
| `aitl_top.v`               | 上記3要素の統合モジュール<br>_Top module integrating the above three components_ |
| `tb_aitl_top.v`            | テストベンチ（FSM入力・PID反応を模擬）<br>_Testbench simulating FSM inputs and PID responses_ |

---

## 🧪 動作検証の手順（iverilog）  
### How to Run Simulation (with iverilog)

以下のコマンドでコンパイルと実行が可能です：  
_Use the following commands to compile and run the simulation:_

```bash
iverilog -o sim_tb tb_aitl_top.v aitl_top.v fsm_core.v pid_controller.v
vvp sim_tb
```

波形出力を含む場合：  
_To view waveform output:_

```bash
gtkwave aitl_top.vcd
```

---

## 💬 `$display` 出力例  
### Sample `$display` Output

実行時のコンソール出力例：  
_Example console output during simulation:_

```
=== AITL Unified Test Start ===
FSM=01, PID_OUT=132
FSM=10, PID_OUT=98
FSM=00, PID_OUT=142
=== AITL Unified Test Done ===
```

FSM状態とPID出力が段階的に変化することが確認できます。  
_You can observe stepwise transitions in FSM states and PID outputs._

---

## 📚 参考リンク  
### Related Links

- [`../auto_generator/`](../auto_generator/)：YAML→Cコード→Verilog変換の自動設計フロー  
  _Automatic design flow from YAML → C code → Verilog_

- [`../logic_templates/`](../logic_templates/)：Verilog雛形・ChatGPT用プロンプトテンプレート集  
  _Verilog templates and prompt collections for ChatGPT usage_

---

## 📜 ライセンス  
### License

MIT License  
技術者・研究者・教育者による自由利用・拡張を歓迎します。  
_Freely available and extensible for engineers, researchers, and educators._
