# 🧠 AITLロジックテンプレート（Verilog）

このフォルダは、FSM・PID・LLMをベースとした制御構造を  
**Verilogで理論的に提供**するテンプレート集です。

## 含まれるモジュール

- `fsm_core.v`：基本的なMoore型の状態機械
- `pid_controller.v`：離散時間のPID制御器（整数演算）
- `llm_interface_stub.v`：外部命令入力（LLM想定）のスタブ
- `aitl_top.v`：FSM・PID・LLMを統合したトップモジュール
- `testbench/`：FSM・PIDの簡易テストベンチ

> ⚠️ 注意：このテンプレートは**物理実装のための回路ではなく、  
> 「構造としての理屈」を形式化して提供**するものです。
