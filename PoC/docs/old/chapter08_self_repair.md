# 第8章：AI自己修復PoC設計手法（AITL理論適用）

## 🎯 本章の目的

本章では、PoC設計にAI的要素（特にLLM・自己推論）を導入し、異常検知・自己修復機構を持つPoCアーキテクチャを構築する手法を解説します。AITLの知性層を中心とした応用実装です。

---

## 🧠 AITL理論における「自己修復」

| AITL層     | 自己修復の役割                            |
|------------|--------------------------------------------|
| FSM（本能） | 異常時の安全状態へ即座に遷移               |
| PID（理性） | パラメータ逸脱への補正・制限                |
| LLM（知性） | 状況の再解釈、原因推定、行動戦略の再構築     |

---

## 🔁 自己修復ループの例（異常→推論→再構成）

```text
[1] センサ異常 → [2] FSMが緊急停止 →
[3] LLMがログを解析 → [4] 故障要因を推定 →
[5] 回避策を提案（モード切替／ゲイン補正） →
[6] FSMが動作再開
```

	•	FSMは「止める」責任、LLMは「復元する」責任
	•	LLMはログ＋事前知識を使ってリアルタイム推論

---

## 💬 LLMによる推論・修復例（対話）
ログ解析：
[WARN] Motor feedback timeout
[INFO] Last state = moving_forward

LLM判断：
→ 推定：右輪センサ不感 or モータ応答不良
→ 提案：左輪のみで定位置保持に切替え

→ 処置：FSMに「hold_position」命令送信

---

## 🧪 PoC設計への実装方法

| 要素             | 実装例                                     |
|------------------|--------------------------------------------|
| ログ構造         | YAML/JSON 形式の状態・異常記録              |
| LLMインターフェース | `llm_interface.py` にてOpenAI APIなどと接続 |
| 修復命令発行     | FSMへUARTまたはローカルAPI経由でコマンド送信 |

> 🔧 異常ログ例（sample_anomaly1.yaml）

```yaml
timestamp: 2025-07-08T10:02:15
state: moving_forward
event: motor_feedback_timeout
sensor_status:
  left_motor: OK
  right_motor: NO_FEEDBACK
```

→ 上記に対し、repair_decision_engine.py が以下を生成：
```
{
  "decision": "hold_position",
  "reason": "右輪センサの応答喪失",
  "recommended_action": "FSMを hold_position 状態へ遷移させる"
}
```

---

## 🧩 実装モジュール構成例（self_repair/）
```
self_repair/
├── llm_interface.py              # LLMとの連携
├── anomaly_log_parser.py        # ログ解析ユーティリティ
├── repair_decision_engine.py    # 修復判断のコア
└── test_logs/
    ├── sample_anomaly1.yaml
    └── sample_anomaly2.yaml
```
---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---

