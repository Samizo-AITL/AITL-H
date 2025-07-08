# 第10章：PoCプロジェクトの管理と評価（AITL評価体系）

## 🎯 本章の目的

PoC開発では、短期間での検証・反復が求められます。本章では、AITL構造に基づいたPoC評価指標と、プロジェクト全体を俯瞰するための管理項目について整理します。

---

## 📈 AITLに基づくPoC評価軸

| 層構造     | 評価軸                          | 評価例                              |
|------------|----------------------------------|-------------------------------------|
| 知性層（LLM） | 状況判断の正確性、応答の適切性         | LLMによる提案とログ解析結果の比較     |
| 理性層（PID） | 安定性、過渡応答、パラメータ調整適応性 | ゲインスイープテスト、定常誤差計測     |
| 本能層（FSM） | 状態遷移の正当性、遷移網羅率            | シナリオ駆動によるカバレッジ評価       |

→ 評価は単一指標でなく、動作ログと設計意図の整合性で確認

---

## 🛠 プロジェクト管理の要点（PoC特有）

| 管理項目         | 内容                                         |
|------------------|----------------------------------------------|
| 要件トレーサビリティ | PoC目的→仕様→実装→評価の一貫性確認             |
| バージョン管理     | コード／仕様／FSM定義などをGitで一元管理         |
| 評価ログの収集     | `log/`ディレクトリに日付・セッション別に保存     |
| 修復判断の記録     | LLM介在時の判断・根拠・対処ログを必ず残す         |
| ドキュメント管理   | `docs/`配下に章別READMEと補足資料を明示的配置   |

---

## 🧪 評価ログ構造の一例（YAML）

```yaml
session: 2025-07-08_AM
fsm_trace:
  - idle → detect_target
  - detect_target → approach
anomaly_detected: true
llm_response:
  - reason: "左前輪センサ不感"
  - action: "旋回モードに切替"
pid_response: "ゲイン調整により過渡応答改善"
```
→ このログをベースに、自動評価やレポート生成が可能

---

## 📊 管理ツールの推奨構成
```
management/
├── evaluation_metrics.xlsx   # AITL対応の評価指標一覧
├── log_templates/
│   └── sample_log.yaml
├── report_templates/
│   └── daily_report.md
├── doc_register.csv          # 各ドキュメントの改訂・管理履歴
└── version_history.md        # 実装ごとのリリース記録
```
---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---


