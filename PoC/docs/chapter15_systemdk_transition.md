# 第15章：SystemDK移行設計とIP再構成戦略（AITL設計資産化）

## 🎯 本章の目的

PoCで得られたFSM・PID・LLM構造を再利用可能な設計資産（IP）として体系化し、SystemDK（System Development Kit）への移行を支援します。AITLの三層構造を保ちつつ、再構成可能な形式で設計知識を移行する方法を解説します。

---

## 🧱 設計資産のIP再構成方針

| ブロック名   | 構成要素                     | 再構成時の形式                    |
|--------------|------------------------------|----------------------------------|
| FSM制御      | 状態遷移表、YAML定義、イベント構造 | `.yaml`, `.py`, `.v` モジュール  |
| PID制御      | ゲイン調整式、FPGA HDLコード     | パラメータ付きRTL、Cモデル        |
| LLM連携      | 質問応答ログ、プロンプト設計     | JSONテンプレート、REST I/F仕様書 |

→ 各ブロックを抽象化・ドキュメント化し、SystemDK開発者が容易に取り込める形へ整備

---

## 🔄 AITL三層の再構成マップ

```text
PoC成果物/
├── fsm/
│   ├── fsm_config.yaml
│   └── fsm_engine.py
├── pid/
│   ├── pid_controller.v
│   └── gain_config.txt
├── llm/
│   ├── scenario_prompt.json
│   └── llm_interface.py
└── integration_notes/
    └── systemdk_porting_guide.md
```

## 🛠 SystemDK移行のステップ例

1. **PoC整理**：構成図・FSM記述・各パラメータの棚卸し  
2. **ブロック分離**：FSM/PID/LLM各部を独立部品化  
3. **インタフェース仕様化**：API・信号線の入出力仕様をドキュメント化  
4. **SystemDKへ統合**：他IPとの結合検証とソフト制御層の調整  
5. **PoCDK → SystemDK化**：ドキュメント＋テンプレート形式で資産化

---

## 📚 PoCDKからSystemDKへの変換テンプレート例

```text
systemdk_templates/
├── base_fsm_template.yaml
├── pid_core_module.v
├── llm_prompt_base.json
├── integration_flowchart.svg
└── ip_porting_checklist.md
```

---

## 🧠 AITL設計資産化の意義
	•	設計の知的構造を保持したまま、別PoCへ再利用可能
	•	チーム間の構造共有・教育教材として展開可能
	•	IP化による開発効率の向上と外部連携の加速

---

## 📬 連絡先

執筆・設計：三溝 真一（Shinichi Samizo）
GitHub: https://github.com/Samizo-AITL
Email: shin3t72@gmail.com

---

---
