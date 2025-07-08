# 📡 UART通信プロトコル仕様 – AITL-H用カスタム定義

本ドキュメントでは、AITL-HプロジェクトにおけるUART通信に用いる**データフレーム構造**と**コマンド定義**を示します。  
FSM制御層やセンサ制御系と**高信頼かつシンプルに連携**することを目的としています。

---

## 🔧 フレーム構造（基本フォーマット）

[Header][CommandID][PayloadLen][Payload][Checksum]

| フィールド     | バイト数 | 内容 |
|----------------|----------|------|
| Header         | 1Byte    | 固定値 `0xAA`（開始識別子） |
| CommandID      | 1Byte    | コマンド識別（例：0x01 = 起動） |
| PayloadLen     | 1Byte    | ペイロード長（バイト数） |
| Payload        | NByte    | 任意のデータ（状態、指令、センサ値など） |
| Checksum       | 1Byte    | 簡易XORチェックまたは加算による整合確認 |

---

## 🧩 コマンドID一覧（例）

| コマンド名 | CommandID | 説明 |
|------------|-----------|------|
| 起動要求   | `0x01`    | 起動トリガの送信 |
| 状態報告   | `0x10`    | FSM状態の報告（Payload = 状態ID） |
| センサ値送信 | `0x20`  | センサデータ（温度、加速度など） |
| 動作指令   | `0x30`    | ロボットの行動選択指示（歩行・停止など） |
| エラー通知 | `0xFF`    | 通信異常、デコードエラー等の報告用 |

---

## 📐 チェックサム計算方式（例）

```python
def calculate_checksum(byte_list):
    return sum(byte_list) & 0xFF  # 下位8bitのみ抽出
```
または XOR方式：
```
def xor_checksum(byte_list):
    result = 0
    for b in byte_list:
        result ^= b
    return result

def xor_checksum(byte_list):
    result = 0
    for b in byte_list:
        result ^= b
    return result
```

## 🔁 送受信の流れ（例）
	1.	FSMが 状態報告 を送信：

0xAA 0x10 0x01 0x02 0xBD

•	Header: 0xAA
	•	CommandID: 0x10（状態報告）
	•	PayloadLen: 0x01
	•	Payload: 状態ID = 0x02
	•	Checksum = XOR(0x10, 0x01, 0x02) = 0xBD

	2.	LLMやPC側で受信・応答処理を行う。

---

## 📚 応用と拡張ポイント
	•	拡張ヘッダによる同期確保（例：0xAA 0x55）
	•	暗号化や署名によるセキュリティ強化
	•	応答ACKの追加で冗長化

---

## ✍️ 制作者より

AITL-HにおけるUART通信は、状態管理・センサ接続・制御切り替えにおいて中心的な役割を果たします。
プロトコル設計では「簡潔さ・明確さ・拡張性」を重視し、FSMやLLM層との連携を前提とした仕様としています。

