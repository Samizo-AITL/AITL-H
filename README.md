# 🤖 AITL-H：Hybrid型構造制御フレームワーク

**AITL-H（All-in-Theory Logic - Hybrid）**は、人型ロボットや適応型システムに向けて設計された**階層型知能制御アーキテクチャ**です。  
**FSM（本能）× PID（理性）× LLM（知性）**の三層構造により、**瞬時性・安定性・柔軟性**を兼ね備えた制御を実現します。

---

- 🇺🇸 [English README here](./README_en.md)  
　→ AITL-H: Hybrid Intelligent Control Architecture for Humanoid Systems using FSM × PID × LLM

---

## 🧭 概要

| 項目       | 内容 |
|------------|------|
| **名称**   | AITL-H（Hybrid） |
| **目的**   | 構造的AI制御による人型ロボット制御手法の確立 |
| **中核原理** | - FSM：状態遷移による本能的行動制御<br>- PID：物理量（角度・速度）の連続制御<br>- LLM：高度な判断・対話・学習による知能化 |

---

## 🧘 三層アーキテクチャ構成

| 層     | 機能                           | 実装例                                   |
|--------|--------------------------------|------------------------------------------|
| FSM層 | 状態遷移に基づくロジック制御   | `fsm_engine.py`, `fsm_state_def.yaml`    |
| PID層 | 各関節・移動量の物理制御       | `pid_controller.py`, `pid_module.py`     |
| LLM層 | 状況判断、異常検出、言語応答   | `llm_interface.py`, `llm_logger.py`      |

> 各層は**疎結合・協調的**に設計されており、独立した開発・段階的統合が可能です。

<div align="center"><img src="theory/aitl_h_architecture.png" alt="AITL-H構造図" width="400"></div>

---

## 📘 PoC設計マニュアル（全16章）

FSM×PID×LLM統合に基づいた**人型ロボットPoC設計マニュアル**を公開しています。  
▶︎ [📖 マニュアルを読む](docs/README.md)

---

## 🧪 PoC一覧

| タイトル | 概要 | パス |
|----------|------|------|
| 🧭 ジンバル制御（FSM + PID + LLM） | ハイブリッド閉ループ制御 | [`PoC/gimbal_control`](./PoC/gimbal_control) |
| ⚙️ Verilog自動生成（FSM + PID） | YAML → C → Verilog生成＋検証 | [`PoC/verilog_demo`](./PoC/verilog_demo) |
| 🔍 その他PoC | ※今後追加 | - |


---

## 🧪 実装例：FSM × PID × LLMによる3軸ジンバル制御（AITL-HX）

> **AITL-HXアーキテクチャ**によるジンバル制御のPoC実装。  
> 自然言語指令 → 状態遷移（FSM） → PID安定制御 → アクチュエータ という閉ループ構成。

📂 ディレクトリ：[`PoC/gimbal_control/`](./PoC/gimbal_control/)  
📘 詳細：[`READMEはこちら`](./PoC/gimbal_control/README.md)

![gimbal_architecture](./docs/images/figure9_1_gimbal_control_architecture.svg)

| 構成要素 | 説明 |
|----------|------|
| LLM層 | 自然言語指令からの目標生成・意図判断 |
| FSM層 | 状態切替（待機・追従・異常復帰） |
| PID層 | Roll・Pitch・Yawの3軸PID制御 |
| センサ層 | 3軸IMUセンサモデル（姿勢推定） |
| アクチュエータ層 | PWM制御によるモータ出力（模擬） |

🧭 学習ポイント：
- FSM + PID + LLMによるハイブリッド制御の全体設計
- 自然言語 → 制御目標への変換と適応
- MIMO制御と状態管理の連携による閉ループ知能制御の実装

---

## 🤖 ChatGPT支援：協調型設計ツール群

`accelerated_design/`では、ChatGPTを活用した設計支援ツールを提供：

- 状態遷移自動提案（プロンプト → FSM YAML）
- テストシナリオ生成／ログ可視化支援
- ドキュメント自動生成・設計レビュー支援

> 🧠 人とAIの**協調設計環境**構築を目的とした実験的開発群です。

---

## 📂 ディレクトリ構成

```
AITL-H/
├── theory/                # 構造設計思想・アーキテクチャ解説
├── PoC/                   # 人型ロボット用統合制御の実証コード・ログ
├── implementary/          # 各制御モジュール（FSM/PID/LLM）のPython実装
└── accelerated_design/    # GPT連携による状態設計・支援ツール
```

| ディレクトリ | 内容 |
|--------------|------|
| [`theory/`](theory/) | 設計思想・三層構造の理論背景 |
| [`PoC/`](PoC/) | 制御シナリオ・ロギング・評価 |
| [`implementary/`](implementary/) | FSM・PID・通信・LLM連携コード |
| [`accelerated_design/`](accelerated_design/) | 設計提案支援ツール・ログ整形支援 |

---

## 🚀 応用領域

- 🧓 **介護支援ロボット**：感情認識＋物理制御
- 🛠 **自己進化型制御**：LLMによる異常検知とフィードバック改善
- 🌏 **災害対応ロボット**：定型動作と推論行動の組合せ
- 🎓 **教育・研究用途**：AI×制御の融合教材として最適

---
## 🎓 教育教材：EduControllerとの連携

AITL-Hの制御理論基盤は、**教育教材「EduController」**の第9章に完全対応しています。

| 章 | 内容 | AITL-Hとの関係 |
|----|------|----------------|
| [Part 1〜5](https://github.com/Samizo-AITL/EduController#制御理論系) | 古典〜現代制御理論 | PID層の理論的基盤 |
| [Part 6〜8](https://github.com/Samizo-AITL/EduController#ai制御系) | NN制御・強化学習 | AI応用制御への展開 |
| [Part 9](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | FSM×PID×LLM統合制御 | AITL-Hの構造と実装を教材化 |

> 🔗 [EduController リポジトリを見る](https://github.com/Samizo-AITL/EduController)

---

## 🧩 実チップ設計への展開：Edusemiとの接続

PoCレベルを超えて**SoC設計・RTL実装・物理設計**まで扱いたい場合は、  
関連プロジェクト **[Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)** の「特別編」が対応しています。

| 章 | 内容 |
|----|------|
| [第3章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | FSM×PID×LLM統合制御のSoC設計 |
| [第4章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | OpenLaneによるRTL〜GDSII変換 |
| [第5章](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | DRC/LVS/DFM設計指針と物理整合 |

---

## 📚 関連プロジェクト一覧

- [Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)：半導体／SoC設計教材（実装対応）
- [EduController](https://github.com/Samizo-AITL/EduController)：制御理論〜AI制御の教育教材
- [Rekiden](https://github.com/Samizo-AITL/Rekiden)：歴史シミュレーション教材（FSM応用）

---

## 👤 執筆者情報 / Author

**三溝 真一（Shinichi Samizo）**  
- 信州大学大学院 電気電子工学 修了  
- 元 セイコーエプソン株式会社 技術者（1997年〜）  

📌 **経験領域**：  
- 半導体デバイス（ロジック／メモリ／高耐圧混載）  
- 薄膜ピエゾアクチュエータ
- PrecisionCoreプリントヘッド製品化

📫 [GitHub: Samizo-AITL](https://github.com/Samizo-AITL)  
📩 Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

© 2025 Shinichi Samizo — MIT License  
教材・ソースコード・構造図等はMITライセンスにて自由に利用可能です。

---

💬 ご意見・議論は [Discussionページ](https://github.com/Samizo-AITL/AITL-H/discussions) へどうぞ。

---
