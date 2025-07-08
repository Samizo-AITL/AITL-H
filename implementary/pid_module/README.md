# ⚙️ PIDモジュール – AITL-H物理層制御の実装

本フォルダでは、AITL-H構想における**物理層制御（第1層）**の中核である **PID制御の実装コード**を提供します。  
人型ロボットやアクチュエータの角度・速度制御、ファン回転数制御など、**安定かつ応答性の高い制御**を担います。

---

## 🧠 構成概要

| ファイル名 | 役割 |
|------------|------|
| `pid_controller.py` | PID制御の基本クラス（P, I, D項、履歴、出力計算） |
| `simulation_notebook.ipynb` | 応答シミュレーション用のJupyter Notebook |
| `docs/pid_usage_notes.md` | パラメータ設計とチューニングの実践ノート |

---

## 🔧 機能ハイライト

- **制御パラメータ設定（Kp, Ki, Kd）**
- **サンプリング周期指定**
- **出力制限（min/max）による飽和対策**
- **積分飽和防止（アンチワインドアップ）**
- **オフセット補正や初期化処理**

---

## 🚀 実装例（抜粋）

```python
pid = PIDController(Kp=1.2, Ki=0.8, Kd=0.05)
pid.set_target(30.0)  # 目標角度 [deg]

for t in time_steps:
    current = get_current_angle()
    control = pid.update(current)
    apply_motor_pwm(control)
```

## 📘 関連ドキュメント
	•	docs/pid_usage_notes.md にて以下を解説：
	•	PID各項の設計指針（応答性、安定性、制御対象に応じた調整）
	•	Ziegler-Nichols法などのチューニング法
	•	MIMO制御やH∞制御との住み分け

---

## 🔬 今後の拡張
	•	モデル予測制御（MPC）への拡張
	•	ノイズ対応（ローパスフィルタ内蔵）
	•	LLMからの動的ゲイン更新インタフェース

---

## ✍️ 制作者より

PID制御は、すべての制御の基盤です。
AITL-Hにおいても、LLMによる判断、FSMによる状態遷移の最終出力を物理的に実行する層として、PIDの正確さ・滑らかさは不可欠です。PoC段階から意識的に「物理応答の設計」を行うことが、高品質な全体設計につながります。

---
