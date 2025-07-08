# 付録A：設計テンプレート・PoC成果記録フォーマット

## 📁 フォルダ構成例

```text
PoC_templates/
├── fsm_config_template.yaml       # 状態遷移テンプレート
├── pid_gain_config_template.txt   # PIDゲイン設定ファイル
├── llm_prompt_template.json       # LLM用プロンプトテンプレート
└── poc_log_template.md            # PoC記録用ログテンプレート
```

---

## 📄 PoC記録テンプレート（抜粋例）
# PoC記録ログ（テンプレート）

## 実行日：
2025年○月○日

## 実施者：
Samizo Shinichi

## 使用FSM構成：
- 状態数：4
- イベント数：3
- 使用YAML：fsm_config_v2.yaml

## PID設定：
- P：1.2
- I：0.4
- D：0.1

## LLM連携概要：
- モデル：GPT-4
- プロンプトファイル：llm_prompt_v1.json

## 実行結果ログ：
- 正常応答率：94%
- 異常応答（未遷移）：2件

---

## ✍️ 活用方法
	•	プロジェクト内での統一記録様式として活用
	•	チーム教育／評価報告時の標準化に貢献

---
