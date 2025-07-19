# 🧠 AITL-H Auto Generator GUI 操作マニュアル

このGUIツールは、FSM・PIDの制御構成を  
YAML形式で記述し、Cコードおよび統合コードを自動生成する支援ツールです。

---

## ✅ 準備

### 必要なパッケージ：

```bash
pip install streamlit pyyaml
```

### 実行コマンド：

```bash
streamlit run streamlit_gui.py
```

---

## 📥 操作手順

1. `test_config.yaml` を用意（FSM＋PID定義を含むYAML）
2. 画面上で YAML ファイルをアップロード
3. FSMコード、PIDコード、統合Cコードが順に表示されます
4. コードはコピー＆ChatGPT活用 or Verilog変換に使用可能

---

## 🧩 ファイル構成例

```
auto_generator/
├── streamlit_gui.py
├── test_config.yaml
└── streamlit_gui_manual.md  ← 本マニュアル
```

---

## 📦 YAML記述例（抜粋）

```yaml
fsm:
  states: [idle, track, recovery]
  initial_state: idle
  transitions:
    - { from: idle, to: track, condition: start_signal }
    - { from: track, to: recovery, condition: lost_target }
    - { from: recovery, to: idle, condition: recovered }

pid:
  kp: 1.2
  ki: 0.4
  kd: 0.1
  setpoint: 90
  output_limits: [-100, 100]
```

---

## 📜 ライセンス

MIT License  
教育・開発目的での再利用を歓迎します。
