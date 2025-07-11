# 🤖 ジンバル制御PoC：FSM + MIMO PID + LLM（AITL-HX構成）

このディレクトリは、3軸ジンバルの安定化制御を対象とした、  
**FSM（状態機械）＋ MIMO PID制御 ＋ LLM（大規模言語モデル）**による  
**ハイブリッド制御アーキテクチャ（AITL-HX）**のPoC実装です。

---

## 🧭 システム構成図

![Hybrid Control Architecture](../../docs/architecture_gimbal_fsm_pid_llm.svg)

> 上位知能（LLM） → 状態遷移（FSM） → 安定制御（PID） → アクチュエータ  
> ← IMUセンサ・知覚ループにより、制御フィードバックが完結します。

---

## 🔩 構成要素

| 層 | モジュール | 説明 |
|----|------------|------|
| LLM層 | `llm_goal_agent.py` | 目的推論・対話ベースの指令生成 |
| FSM層 | `control_fsm_pid_llm.py` | 状態遷移ロジック：待機・追従・復帰など |
| PID層 | `control_fsm_pid_llm.py` | Roll・Pitch・Yaw に対する3軸MIMO PID制御 |
| センサ | `imu_sensor_model.py` | 3軸IMU（角速度・加速度）の簡易モデル |
| アクチュエータ | `motor_pwm_driver.py` | PWM出力 → ブラシレスモータ制御（3軸） |

---

## 🧪 ファイル一覧

| ファイル名 | 内容 |
|------------|------|
| `control_fsm_pid_llm.py` | 制御本体（FSM + PID + LLM接続） |
| `imu_sensor_model.py` | IMUセンサモデル（3軸角度・速度） |
| `motor_pwm_driver.py` | モータ駆動用PWM出力（模擬） |
| `llm_goal_agent.py` | 目的設定・状況判断のLLMインターフェース |
| `config_gimbal.json` | PIDゲイン・システム設定 |
| `gimbal_sim_demo.ipynb` | 統合制御の可視化・Notebook実行用 |

---

## 🎯 学習目標

- FSM（行動切替）＋PID（物理安定）＋LLM（意図判断）の協調制御を学ぶ
- 自然言語指令に応じた目標設定と適応的制御を設計する
- 外乱下での3軸ジンバル制御をシミュレーションする
- エッジAI／ロボティクス実装に向けた統合設計を体験する

---

## 🚀 今後の拡張

- 実機IMU＋ESC＋Jetson/Raspberry Pi への接続実験
- ChatGPT APIとのリアルタイム連携
- カメラ画像ベースの追従制御・サーボ制御との融合
- ドローン／視線制御ロボットなどへの応用展開

---

## 📎 参考

- 本PoCは [AITL-H](https://github.com/Samizo-AITL/AITL-H) フレームワークの一部です  
- 教材連携先： [EduController - Part09](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid)
