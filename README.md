# 🤖 AITL-H：Hybrid型構造制御フレームワーク

AITL-H（All-in-Theory Logic - Hybrid）は、人型ロボットや適応型システムに向けて設計された**階層型知能制御アーキテクチャ**です。  
**FSM（本能）＋ PID（理性）＋ LLM（知性）**の三層構造により、**瞬時性・安定性・柔軟性**を兼ね備えた制御を実現します。

---

## 🧭 プロジェクト概要

- **名称**：AITL-H（Hybrid）
- **目的**：人型ロボット制御における構造的AI制御の実証と設計手法の確立
- **中核原理**：
  - 本能的行動（FSM）
  - 物理駆動制御（PID）
  - 意図推定・対話・学習（LLM）

---

## 🧘 三層アーキテクチャ

| 層     | 内容                             | 実装ファイル例                       |
|--------|----------------------------------|--------------------------------------|
| FSM層 | 状態遷移によるロジック制御        | `fsm_engine.py`, `fsm_state_def.yaml` |
| PID層 | 関節角・移動量などの連続量制御    | `pid_controller.py`, `pid_module.py` |
| LLM層 | 状況判断・異常検出・言語応答       | `llm_interface.py`, `llm_logger.py`   |

> 各層は**疎結合かつ協調的**に構成されており、段階的な開発と柔軟な拡張が可能です。

<img src="theory/aitl_h_architecture.png" alt="AITL-H構造図" width="300">

---

## 📘 AITL-H PoC 設計マニュアル

FSM＋PID＋LLMの三層構造をベースにした人型ロボットPoC設計マニュアル（全16章）を公開中：  
▶︎ [📖 PoC設計マニュアル](docs/README.md)

---

## 🤖 ChatGPT支援による設計・状態定義

`accelerated_design/` フォルダでは、ChatGPTを活用した設計支援ツール群を展開しています：

- 状態遷移の自動提案（プロンプト → FSM yaml）
- テストシナリオやPoCログの整形・可視化
- ドキュメント生成や設計検証補助（GPT連携）

> 💡 人とAIの**協調設計環境**を具現化する実験的開発です。

---

## 📂 ディレクトリ構成

```
AITL-H/
├── theory/                # アーキテクチャの理論構造と設計思想
├── PoC/                   # 人型ロボット制御の実証実験（FSM/PID/LLM統合）
├── implementary/          # 制御ブロックのPython実装コード群
└── accelerated_design/    # ChatGPT支援による状態提案・設計支援ツール
```

| ディレクトリ | 内容 |
|--------------|------|
| [`theory/`](theory/) | FSM・PID・LLMによる三層アーキテクチャの構造と設計意図を記述 |
| [`PoC/`](PoC/) | 実験シナリオ、状態制御、実験ログを含む統合PoC環境 |
| [`implementary/`](implementary/) | FSM・PID・通信などの制御モジュール群（Python実装） |
| [`accelerated_design/`](accelerated_design/) | 状態定義やテスト生成を補助するChatGPTツール集 |

---

## 🚀 応用可能性

- 🧓 **介護支援ロボット**：感情的反応＋物理制御の複合動作
- 🛠 **自己改善型制御**：LLMによる異常推定と行動修正提案
- 🌏 **災害対応ロボット**：事前定義＋現場推論の組合せ行動
- 🎓 **教育・研究用教材**：制御・AI・設計論を統合的に学ぶ

---

## 🧩 RTL以降のSoC実装・物理設計について

本リポジトリ「AITL-H」では、FSM＋PID＋LLMによる統合制御アーキテクチャとPoC設計を対象としています。  
一方、**RTL実装以降（Verilog設計〜OpenLaneによるGDSII生成）**に関しては、  
別途公開している教材プロジェクト「[Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)」の**特別編**にて扱っています。

### 🔗 関連教材リンク（Edusemi 特別編）

| 章 | タイトル |
|----|----------|
| [第3章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | FSM×PID×LLMによる統合制御システムのSoC実装手法 |
| [第4章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装 |
| [第5章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | PDKとレイアウト検証による物理整合とDFM設計指針 |

> 💡 「PoC制御」から「実チップ設計」への展開にご関心のある方は、上記教材をご覧ください。

---

## 📚 関連プロジェクト

- [`Edusemi`](https://github.com/Samizo-AITL/Edusemi-v4x)：半導体・SoC設計教材
- `AITL Architecture`：FSM/制御理論に基づく構造的AI設計の基礎理論（現在 AITL-H に統合）
- `TechScape（構想中）`：構造知に基づく技術アーキテクチャ全体の統合構想

---

## 👨‍💻 開発・設計者

**三溝 真一（Shinichi Samizo）**  
元セイコーエプソン株式会社 / 信州大学大学院 電気電子工学修士課程修了  
専門：半導体デバイス技術、ロボット制御、AI応用設計  

- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
- お問い合わせ：`shin3t72@gmail.com`  

> 💬 ご意見・ご質問は Issue または Discussions にてお寄せください。

---

© 2025 Shinichi Samizo — MIT License  
教材・構想・コード・図版等は、MITライセンスのもとで自由に再利用可能です。
