# 📘 UART使用ガイド – AITL-H向け通信モジュール解説

このドキュメントでは、`uart_controller.py` を中心とした UART 通信モジュールの使い方、接続方法、テスト方法について解説します。  
AITL-Hプロジェクトにおける FSM 制御、センサ連携、PC通信等に使用される**シリアル通信の基本構成**として位置づけられます。

---

## 🔌 1. UARTとは？

UART（Universal Asynchronous Receiver/Transmitter）は、非同期シリアル通信方式の一つであり、以下の特徴があります：

- **1本のTx（送信）線**と**1本のRx（受信）線**によるデータ伝送
- クロック非共有（非同期）のため簡素なハード構成
- マイコン、センサモジュール、PC間通信で広く用いられる

---

## 🛠 2. 使用ファイル構成
```
uart_controller/
├── uart_controller.py         # UART通信の基本クラス（送受信）
├── uart_test_sim.py           # 送受信テストスクリプト
└── docs/
└── uart_usage.md          # ← 本ドキュメント
```
---

## 🧩 3. UART制御クラスの使い方

### ✅ 初期化例

```python
from uart_controller import UARTController

uart = UARTController(port='/dev/ttyUSB0', baudrate=115200)
```

---

## ✅ 4. 基本的な使用例

```python
from uart_controller import UARTController

uart = UARTController(port='/dev/ttyUSB0', baudrate=115200)

uart.send("Hello AITL-H\n")
data = uart.receive()
print("受信：", data)
```

---

## 🔍 5. テスト実行方法

`uart_test_sim.py` を実行して、送受信の動作確認が可能です：

```bash
python uart_test_sim.py
```
•	実行前に port を実際の接続先（例：COM3 や /dev/ttyUSB1）に合わせてください。


---

## 📦 6. AITL-Hにおける応用例

UART通信は、AITL-Hアーキテクチャにおいて以下のような役割で活用されます：

| 応用先         | 具体的な内容 |
|----------------|--------------|
| FSM入力         | LLMまたは外部GUIからの制御コマンド（例：「start」「sit」など）をFSMの状態遷移トリガとして受信 |
| LLM連携         | 状況応答の自然言語コマンドを受信・送信（例：音声入力→文字列→FSM連携） |
| センサ接続      | 外部の距離センサ、IMU、温度センサなどからのリアルタイムデータ受信 |
| ロギング         | モータ応答やセンサ値をログ形式で外部PCへ送信（シリアルロガーとして活用） |
| デバッグ・状態監視 | FSMの現在状態、PIDゲイン、センサ値などの動的モニタリング |

---

## 🧠 7. 注意点と拡張

- 改行（`\n`）や区切り文字（`,`）によるパース処理が必要
- シリアルポートのバッファは環境により溢れやすいため、定期フラッシュや時間制御を実装
- 今後の拡張として、以下も視野に入れています：
  - JSONベースの構造化通信
  - 複数ポート接続の管理（センサ／LLM用ポート分離）
  - ROSなど他ミドルウェアとのブリッジ連携

---

## ✍️ 制作者より

UART通信は、LLMからFSM、FSMからPIDへの命令系、また外界とのセンサフィードバックをつなぐ「神経ネットワーク」のような存在です。  
PoC開発ではまずUARTから始めることで、全体設計の可視化とデバッグが容易になります。AITL-H制御系の中でも、最も基本でありながら深い役割を果たします。

---

