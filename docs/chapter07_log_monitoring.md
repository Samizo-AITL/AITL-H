---
layout: clean
permalink: /docs/chapter07_log_monitoring.html
title: ""
show_title: false   # ← これで上部の自動H1バーを非表示
---

---

# 📊 第07章：PoCログ記録とモニタリング設計

本章では、AITL-H PoCにおける**センサ値・FSM状態・PID出力などのログ記録と可視化戦略**について解説します。  
動作中のデータを蓄積・解析・グラフ表示することで、制御挙動の評価と改善が可能になります。

---

## 1. 🗂 ログ記録の目的

- FSM状態の遷移履歴を記録し、**行動パターンを分析**
- センサデータ（距離・角度）を記録し、**外界変化との関係性を把握**
- PID出力（PWM）を記録し、**誤差推移や応答性を評価**

---

## 2. 🧩 ログ保存構造（例）

PoCでは `data/` ディレクトリにCSV形式で保存：

```bash
PoC/data/
├── fsm_log.csv         # 状態遷移ログ
├── sensor_log.csv      # 距離・角度のセンサ値履歴
└── pid_log.csv         # 目標値・実測値・出力PWM
```

---

## 3. 📝 ログ記録のコード例

```python
# ログファイル初期化
with open("data/pid_log.csv", "w") as f:
    f.write("time,target,measured,pwm\n")

# 制御ループ内で追記
timestamp = time.time()
with open("data/pid_log.csv", "a") as f:
    f.write(f"{timestamp},{target},{measured},{pwm}\n")
```

---

## 4. 📈 可視化例（Python + matplotlib）

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/pid_log.csv")
plt.plot(df["time"], df["target"], label="Target")
plt.plot(df["time"], df["measured"], label="Measured")
plt.plot(df["time"], df["pwm"], label="PWM")
plt.legend()
plt.show()
```

---

## 5. 📡 FSM状態の可視化アイデア

- 状態ごとに色分けされた時系列プロット
- 状態遷移を時間軸上でマッピングする**状態チャート**
- 自動レポート生成（PDF/HTML）での評価支援

---

## 🔚 まとめ

ログ記録と可視化は、PoC制御の**挙動検証・最適化・トラブルシュート**に不可欠な要素です。  
FSM・PID・センサの出力を統合記録し、**PoC設計の品質を客観的に評価**するための土台となります。

---

## 図7-1：ログ出力構成図（Mermaid）

```mermaid
flowchart LR
    subgraph Modules
        FSM["FSM Engine\n(状態制御)"]
        Sensor["Sensor Interface\n(センサ取得)"]
        PID["PID Controller\n(制御演算)"]
    end

    subgraph Logs
        FSMLog["fsm_log.csv"]
        SensorLog["sensor_log.csv"]
        PIDLog["pid_log.csv"]
    end

    FSM --> FSMLog
    Sensor --> SensorLog
    PID --> PIDLog

    FSMLog -.-> Visualization["可視化/解析"]
    SensorLog -.-> Visualization
    PIDLog -.-> Visualization
```

- **FSM Engine** → `fsm_log.csv`：状態遷移ログ  
- **Sensor Interface** → `sensor_log.csv`：実測値（距離・角度など）  
- **PID Controller** → `pid_log.csv`：制御応答ログ（目標 vs 実測 vs 出力）  

> この構成により、制御挙動を時系列でトレースでき、システム全体の評価とデバッグが容易になります。

---

### 📝 **ライセンス / License**
- **Code:** MIT  
- **Text:** CC BY 4.0  
- **Figures:** CC BY-NC 4.0  
（詳細は [Docs Index のライセンス表 / License Table in Docs Index](https://samizo-aitl.github.io/AITL-H/docs/#-ライセンス--license) を参照）

---

### 🔗 **ナビゲーション / Navigation**
- ⏮ [第06章：制御アーキテクチャ実装 / Control Architecture](https://samizo-aitl.github.io/AITL-H/docs/chapter06_run_main_arch.html)  
- ▶️ [第08章：LLM連携と意図推定 / LLM Integration](https://samizo-aitl.github.io/AITL-H/docs/chapter08_llm_integration.html)  

[![📄 READMEに戻る / Back to README](https://img.shields.io/badge/Back%20to-README-blue?logo=readme)](https://samizo-aitl.github.io/AITL-H/docs/)  
[![🏠 AITL-Hトップ / AITL-H Top](https://img.shields.io/badge/AITL--H-Top-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)

