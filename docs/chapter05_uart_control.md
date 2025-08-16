---
layout: clean
# title: 
---

---

# 🔌 第05章：UART通信制御とFSM接続

本章では、AITL-H PoCにおける**UART（シリアル通信）による命令受信とFSM制御の接続構造**を解説します。  
UARTは、LLMや外部ユーザからの制御命令をFSMへ伝達する「入力インターフェース」として機能します。

---

## 1. 📬 UART通信の役割

UARTはPoC内で次のような役割を担います：

- LLMから生成された**自然言語命令をFSM用イベントに変換して送信**
- FSMはUARTから受信したイベント文字列をもとに**状態遷移を実行**
- 双方向通信により、FSMの状態やセンサデータを**外部に送信**することも可能

---

## 2. 🧩 `uart_driver.py` の構成例

PoC内での仮想UART実装は次のような簡易構成です：

```python
class UARTDriver:
    def __init__(self):
        self.rx_buffer = []

    def receive(self):
        if self.rx_buffer:
            return self.rx_buffer.pop(0)
        return None

    def send(self, data):
        print(f"UART Send: {data}")

    def inject_command(self, command):
        self.rx_buffer.append(command)
```

- `inject_command()`：LLMやユーザが命令を挿入する仮想メソッド
- `receive()`：FSMがポーリング的に命令を取得

---

## 3. 📄 コマンド形式とFSMイベント対応

| UART文字列 | 対応するFSMイベント |
|------------|----------------------|
| `"start"` | `start` |
| `"stop"` | `stop` |
| `"turn_left"` | `turn_left` |
| `"obstacle_detected"` | `obstacle_detected` |
| `"cleared"` | `cleared` |

UARTコマンドはFSM構成（`fsm_config.yaml`）に対応している必要があります。

---

## 4. 🔄 応用通信方式と今後の展開

将来的には、以下のような通信方式への拡張が可能です：

| 通信方式 | 特徴 | 用途 |
|----------|------|------|
| USB-C仮想COM | 高速・安定 | PC ⇔ マイコン連携 |
| Bluetooth (BLE) | 無線・省電力 | モバイル制御・ウェアラブル連携 |
| WiFi (UDP/TCP) | 長距離・ネット統合 | リモート制御・クラウド制御 |

---

## 🔚 まとめ

UART通信は、AITL-H構成における**知性層（LLM）と本能層（FSM）を接続する重要インターフェース**です。  
本章では、UARTによる命令伝達とFSM接続の実装例を示し、今後の通信拡張への布石を整理しました。
