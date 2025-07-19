
# 🧪 verilog_demo/README.md

このディレクトリは、AITL-Hアーキテクチャにおける  
統合制御モジュール（FSM × PID × LLM）の **Verilog動作検証** を行うためのテスト環境です。

---

## 🧩 構成ファイル一覧

| ファイル名         | 内容 |
|--------------------|------|
| `fsm_core.v`       | Moore型FSM制御ロジック |
| `pid_controller.v` | 離散時間PID制御器 |
| `llm_interface_stub.v` | 外部命令入力スタブ |
| `aitl_top.v`       | 上記3要素の統合モジュール |
| `tb_aitl_top.v`    | テストベンチ（FSM入力・PID反応を模擬） |

---

## 🧪 動作検証の手順（iverilog）

以下のコマンドでコンパイルと実行が可能です：

```sh
iverilog -o sim_tb tb_aitl_top.v aitl_top.v fsm_core.v pid_controller.v
vvp sim_tb
```

波形出力を含む場合：

```sh
gtkwave aitl_top.vcd
```

---

## 💬 `$display` 出力例

実行時のコンソール出力例：

```
=== AITL Unified Test Start ===
FSM=01, PID_OUT=132
FSM=10, PID_OUT=98
FSM=00, PID_OUT=142
=== AITL Unified Test Done ===
```

FSM状態とPID出力が段階的に変化することが確認できます。

---

## 📚 参考リンク

- [`../auto_generator/`](../auto_generator/)：YAML→Cコード→Verilog変換の自動設計フロー
- [`../logic_templates/`](../logic_templates/)：Verilog雛形・ChatGPT用プロンプトテンプレート集

---

## 📜 ライセンス

MIT License  
技術者・研究者・教育者による自由利用・拡張を歓迎します。
