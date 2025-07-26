# 🤖 **AITL-H：Hybrid型構造制御フレームワーク**

**AITL-H（All-in-Theory Logic - Hybrid）** は、人型ロボットや適応型システムに向けて設計された **階層型知能制御アーキテクチャ** です。  
**FSM（本能） × PID（理性） × LLM（知性）** の三層構造により、**瞬時性・安定性・柔軟性** を兼ね備えた制御を実現します。

---

🇺🇸 [**English README here**](./README_en.md)

---

## 🧭 **概要**

| 項目 | 内容 |
|------|------|
| **名称** | **AITL-H（Hybrid）** |
| **目的** | **構造的AI制御による人型ロボット制御手法の確立** |
| **中核原理** | - **FSM**：状態遷移による本能的行動制御<br>- **PID**：物理量（角度・速度）の連続制御<br>- **LLM**：高度な判断・対話・学習による知能化 |

---

## 🧘 **三層アーキテクチャ構成**

| 層 | 機能 | 実装例 |
|----|------|--------|
| **FSM層** | 状態遷移に基づくロジック制御 | `fsm_engine.py`, `fsm_state_def.yaml` |
| **PID層** | 各関節・移動量の物理制御 | `pid_controller.py`, `pid_module.py` |
| **LLM層** | 状況判断、異常検出、言語応答 | `llm_interface.py`, `llm_logger.py` |

> 各層は **疎結合・協調的** に設計されており、**独立した開発・段階的統合が可能** です。

---

## 📘 **PoC設計マニュアル**

FSM×PID×LLM統合に基づいた **人型ロボットPoC設計マニュアル（全16章）** を公開中  
▶︎ [📖 マニュアルを読む](docs/index.md)

---

## 🧪 **PoC一覧**

| タイトル | 概要 | パス |
|----------|------|------|
| 🧭 **ジンバル制御（FSM + PID + LLM）** | ハイブリッド閉ループ制御 | [`PoC/gimbal_control`](./PoC/gimbal_control) |
| ⚙️ **Verilog自動生成（FSM + PID）** | YAML → C → Verilog生成＋検証 | [`PoC/verilog_demo`](./PoC/verilog_demo) |

---

## 🧪 **PoC例：FSM × PID × LLMによる3軸ジンバル制御**

> **自然言語指令 → 状態遷移（FSM） → PID安定制御 → アクチュエータ** という閉ループ構成。  
> 教育・応用に最適な **AITL-HXアーキテクチャ** の基本実装。

📂 ディレクトリ：[`PoC/gimbal_control/`](./PoC/gimbal_control/)  
📘 詳細：[`READMEはこちら`](./PoC/gimbal_control/README.md)

---

## 🧪 **Verilog自動生成PoC（FSM×PID）**

> FSM／PIDの **動作仕様（YAML）** から  
> **Cコード → 統合C → Verilog** を **ChatGPTと連携** して生成・検証

📂 ディレクトリ：[`PoC/verilog_demo/`](./PoC/verilog_demo/)  
📘 詳細：[`READMEはこちら`](./PoC/verilog_demo/README.md)

---

## 🤖 **ChatGPT支援ツール群**

`accelerated_design/` にて **ChatGPTを用いた設計支援ツール** を提供：

- 状態遷移設計支援（プロンプト → FSM YAML自動化）
- テストシナリオ／ログ可視化
- 設計ドキュメントの自動生成

> 人とAIの **協調設計フレームワーク** を実現するツール群です。

---

## 📂 **ディレクトリ構成**

```
AITL-H/
├── theory/                # 構造設計思想・アーキテクチャ解説
├── PoC/                   # 制御PoCコード・シナリオログ
├── implementary/          # FSM/PID/LLMのPythonモジュール実装
└── accelerated_design/    # GPT連携の設計支援ツール
```

---

## 🚀 **応用領域**

- 🧓 **介護支援ロボット**（感情認識×制御）
- 🛠 **自己進化制御**（異常検知×自己更新）
- 🌏 **災害対応ロボット**（定型＋推論）
- 🎓 **教育教材**（AI×制御の融合訓練）

---

## 🎓 **EduControllerとの接続**

**AITL-H** は、教育教材 **EduController** の第9章（FSM × PID × LLMハイブリッド制御）と**完全に統合**されています。

| 章 | 内容 | AITL-Hとの関係 |
|----|------|----------------|
| Part 01〜05 | 古典〜現代制御理論（PID、状態空間など） | **PID層の理論的基盤** |
| Part 06〜08 | AI制御（NN制御、強化学習、データ駆動） | **AI応用設計の補完知識** |
| **Part 09** | FSM × PID × LLM 統合制御 | **AITL-Hのアーキテクチャを教材として実装** |

🔗 [**EduControllerリポジトリを見る**](https://github.com/Samizo-AITL/EduController)

---

### 🔧 **実装支援モジュール（EduController内）**

以下のモジュールにより、**教材・シミュレーション・実装設計**をシームレスに連携できます。

🔹 **[matlab_tools](https://github.com/Samizo-AITL/EduController/tree/main/matlab_tools)**  
- **SimulinkによるPID・状態空間制御の可視化**
- **Simulink CoderによるCコード生成**
- HDL実装への展開に向けた中間出力（Cコード → `c_to_hdl/` 連携）

🔹 **[SoC_DesignKit_by_ChatGPT](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT)**  
- **FSM、PID、LLM制御構成のテンプレート群**
- **ChatGPTプロンプトによるVerilog自動生成支援**
- `testbench/` によるHDL動作検証・波形解析も提供

> 💡 教材（理論）と実装支援（設計）をつなぐ「**教育 × 実装 × AI**」の**統合フレームワーク**です。

---

## 🧩 **Edusemiとの統合設計展開**

**SoC/RTL設計まで発展**させたい場合は、  
**[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** の「特別編」にて、以下を提供：

- FSM×PID×LLM構成のSoC設計（第3章）
- OpenLaneによるレイアウト自動化（第4章）
- DRC/LVS/DFMの物理設計検証（第5章）

---

## 📚 **関連プロジェクト一覧**

- [**Edusemi-v4x**](https://github.com/Samizo-AITL/Edusemi-v4x)：半導体／SoC設計教材
- [**EduController**](https://github.com/Samizo-AITL/EduController)：制御理論×AI制御教材

---

## 👤 **執筆者情報 / Author**

**三溝 真一（Shinichi Samizo）**  
- **信州大学大学院 電気電子工学 修了**  
- 元 **セイコーエプソン** 技術者（1997年〜）

📌 **経験領域**：  
- **0.35〜0.18um ロジック／メモリ／高耐圧混載デバイス**  
- **薄膜ピエゾアクチュエータ**  
- **PrecisionCoreプリントヘッド製品化・技術教育**

📬 **連絡先**  
- ✉️ Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 X (Twitter): [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 GitHub: [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 🔖 **ライセンス / License**

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
教育・研究・個人利用の目的で自由に利用可能です。

---

💬 ご意見・議論は [**Discussionページ**](https://github.com/Samizo-AITL/AITL-H/discussions) へどうぞ。

---
