# 🧩 AITL-H / implementary

AITL-Hプロジェクトにおける**制御モジュール実装群**を格納するディレクトリです。  
本リポジトリでは、人型ロボットPoCに必要な**FSM制御、PID制御、UART通信、センサ制御、LLM連携**などのコードを提供します。

---

## 📁 ファイル構成

| ファイル名 | 内容 |
|------------|------|
| `fsm_engine.py`        | FSM（有限状態機械）による状態遷移ロジック |
| `pid_controller.py`    | PID制御アルゴリズム（目標値追従・補正） |
| `uart_driver.py`       | UART通信モジュール（センサ・アクチュエータ連携） |
| `sensor_interface.py`  | センサ制御・データ取得・異常検知処理 |
| `llm_interface.py`     | LLM（大規模言語モデル）とのインタフェース処理 |
| `README.md`            | 本ディレクトリの概要と構成説明 |

---

## 🔧 技術要素と役割

### ✅ FSM制御：`fsm_engine.py`
- 状態遷移テーブルとイベント駆動制御の実装
- YAML外部定義との連携も可能（`fsm_state_def.yaml`など）

### ✅ PID制御：`pid_controller.py`
- PIDアルゴリズムの基本実装
- ゲイン調整／サンプリング周期対応
- 実機アクチュエータへの適用前提

### ✅ UART通信：`uart_driver.py`
- PythonによるUART送受信制御
- デバイス間の双方向通信、エラーチェック機能付き

### ✅ センサ制御：`sensor_interface.py`
- センサ値の読み出し、スケーリング、フィルタ処理
- 異常検知、データロギングとの連携設計

### ✅ LLMインタフェース：`llm_interface.py`
- FSMやセンサ状態に対して自然言語で応答
- 状況説明、異常理由の対話的提示
- ChatGPTなどとのAPI連携を想定

---

## 💡 使用環境とライブラリ

- 言語：Python 3.9+
- ライブラリ：`pyserial`, `numpy`, `scipy`, `yaml`, `requests`, `time`, `logging`
- 動作環境例：Jetson Nano / Raspberry Pi / Linux組込み環境

---

## 📬 連絡先

技術監修・実装：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com
