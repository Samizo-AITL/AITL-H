---
layout: clean
permalink: /
show_title: false
---

------------------------------------------------------------------------

# 🤖 **AITL-H：Hybrid型構造制御フレームワーク**

*🤖 AITL-H: Hybrid Structural Control Framework*

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)
[![Hybrid
License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

> ⚠️ **開発・検証中 / Under Development**\
> 本プロジェクトは現在も **発展途上**
> にあり、構成・仕様・実装内容は今後変更される可能性があります。\
> 利用・参照の際は、最新のリポジトリ内容をご確認ください。\
> *⚠️ **Under development/testing.** This project is still evolving, and
> its structure, specifications, and implementation may change. Please
> check the latest repository contents when using or referencing it.*

------------------------------------------------------------------------

## 🆕 最新情報 / Update Log

  ------------------------------------------------------------------------------------------------------------
  日付                    更新内容 / Update             参照
  ----------------------- ----------------------------- ------------------------------------------------------
  2025-08-25              🚩 Humanoid Robot             [PoCページ](./PoC/humanoid/)
                          PoC（集大成）をトップに追加   

  2025-08-25              📑 PoCレポート3本（PWM Ripple [Docs Index](./PoC/humanoid/docs/)
                          / Thermal / Mission           
                          Energy）公開                  

  2025-08-25              🎤 発表用スライド雛形を追加   [Slides](./PoC/humanoid/docs/flagship_poc_slides.md)
  ------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🔗 公式リンク / Official Links

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  言語 / Language         GitHub Pages 🌐                                                                                                               GitHub 💻
  ----------------------- ----------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------
  🇯🇵 Japanese             [![GitHub Pages                                                                                                               [![GitHub Repo
                          JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)     JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)

  🇺🇸 English              [![GitHub Pages                                                                                                               [![GitHub Repo
                          EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/)   EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/en)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧭 概要 / Overview

  ----------------------------------------------------------------------------------------------------------------
  項目                                内容
  ----------------------------------- ----------------------------------------------------------------------------
  **名称**                            **AITL-H（Hybrid）**`<br>`{=html}*AITL-H (Hybrid)*

  **目的**                            **構造的AI制御による人型ロボット制御手法の確立**`<br>`{=html}*Establishing
                                      humanoid robot control methods using structural AI control*

  **中核原理**                        \- **FSM**：状態遷移による本能的行動制御`<br>`{=html}-
                                      **PID**：物理量（角度・速度）の連続制御`<br>`{=html}-
                                      **LLM**：高度な判断・対話・学習による知能化`<br>`{=html}*- **FSM**:
                                      instinctive behavior control through state transitions`<br>`{=html}-
                                      **PID**: continuous control of physical quantities (angle,
                                      velocity)`<br>`{=html}- **LLM**: intelligence through advanced
                                      decision-making, dialogue, and learning*
  ----------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧘 三層アーキテクチャ構成 / Three-Layer Architecture

  -----------------------------------------------------------------------------------------------------
  層                      機能                                                  実装例
  ----------------------- ----------------------------------------------------- -----------------------
  **FSM層**               状態遷移に基づくロジック制御`<br>`{=html}*Logic       `fsm_engine.py`,
                          control based on state transitions*                   `fsm_state_def.yaml`

  **PID層**               各関節・移動量の物理制御`<br>`{=html}*Physical        `pid_controller.py`,
                          control of joints and motion quantities*              `pid_module.py`

  **LLM層**               状況判断、異常検出、言語応答`<br>`{=html}*Situation   `llm_interface.py`,
                          assessment, anomaly detection, and language response* `llm_logger.py`
  -----------------------------------------------------------------------------------------------------

> 各層は **疎結合・協調的**
> に設計されており、**独立した開発・段階的統合が可能** です。\
> *Each layer is designed to be **loosely coupled yet cooperative**,
> allowing **independent development and step-by-step integration**.*

------------------------------------------------------------------------

## 🌏 戦略的重要性 / Strategic Significance

AITL-Hは、単なる制御アーキテクチャではなく、\
**状態フィードバック制御**と**状態遷移制御**を統合し、さらに**LLM（大規模言語モデル）**と**SystemDK**を組み合わせることで、\
**リアルタイムかつ物理制約を考慮した最適設計**を実現します。\
*AITL-H is not just a control architecture. By integrating **state
feedback control** and **state transition control**, and further
combining **LLMs** with **SystemDK**, it achieves **real-time optimal
design under physical constraints**.*

-   **産業的効果**
    -   故障対応時間の大幅短縮（PoC評価値：94%削減）\
    -   生産ライン再構成時間を8倍短縮\
    -   設計変更対応コストを40%削減
-   **Industrial effects**
    -   Significantly reduced fault response time (PoC evaluation: 94%
        reduction)\
    -   8× faster reconfiguration of production lines\
    -   40% reduction in design change costs
-   **国家的意義**
    -   先端ノード半導体や産業用自律システムの競争力確保\
    -   国際標準化における主導権獲得
-   **National significance**
    -   Securing competitiveness in advanced-node semiconductors and
        industrial autonomous systems\
    -   Gaining leadership in international standardization

> **この技術は「今」統合しなければならない。**\
> *This technology must be integrated **now**.*\
> 特にSystemDKはAITL-H固有ではなく、**全ての先端ノード半導体設計に必須の基盤技術**です。\
> *In particular, SystemDK is not unique to AITL-H but is an **essential
> foundational technology for all advanced-node semiconductor
> designs**.*

------------------------------------------------------------------------

## 🧪 PoC関連 / PoC Related

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  タイトル                   概要                                  パス
  -------------------------- ------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------
  🚩 **Humanoid Robot        FSM × PID × LLM × 状態空間 ×          [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](./PoC/humanoid/) [![View
  PoC（集大成）**            自己発電を統合したフラグシップ        Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid)

  🧭 **ジンバル制御（FSM +   ハイブリッド閉ループ制御の教育用PoC   [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](./PoC/gimbal_control/) [![View
  PID + LLM）**                                                    Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control)

  ⚙️                         YAML → C → Verilog 自動生成＋検証     [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](./PoC/verilog_demo/) [![View
  **Verilog自動生成（FSM +                                         Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/verilog_demo)
  PID）**                                                          

  🛠 **Auto Generator**       FSM・PID構成の自動生成ツール群        [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](./PoC/auto_generator/) [![View
                                                                   Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/auto_generator)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> 🚩 **フラグシップPoC：人型ロボット** --- クロスノード（22nm SoC /
> 0.18µm AMS / 0.35µm LDMOS / 自己発電）を SystemDK で統合。

------------------------------------------------------------------------

## 🗺️ プロジェクト関係図 / Project Relationship Map

``` mermaid
flowchart TB
  EC["EduController
(制御理論〜AI制御)"]
  AITLH["AITL-H
Hybrid Control & SystemDK"]
  ESV["Edusemi-v4x
(SoC/RTL/レイアウト)"]

  EC -- 教材フィード / Teaching Feed --> AITLH
  AITLH -- 設計手法・PoC成果 / Methods & PoC Results --> ESV
  EC -- 参照リンク / Cross Reference --> ESV
```

*EduController ⇔ AITL-H ⇔ Edusemi-v4x の相互参照関係を示す簡易図。*

------------------------------------------------------------------------

## 📚 関連プロジェクト一覧 / Related Project List

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  プロジェクト                 説明                     リンク
  ---------------------------- ------------------------ -------------------------------------------------------------------------------------------------------------------------------
  **Edusemi-v4x**              半導体／SoC設計教材      [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/)
                                                        [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x)

  **EduController**            制御理論×AI制御教材      [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/)
                                                        [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController)

  **SamizoGPT**                Project Design           [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/)
                               Hubガイド管理            [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT)

  **AITL-Strategy-Proposal**   AITL戦略提言・政策提案   [![🌐 View
                                                        Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-Strategy-Proposal/)
                                                        [![💻 View
                                                        Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-Strategy-Proposal)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 👤 執筆者 / Author

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  項目                                内容
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  **著者 / Author**                   三溝 真一（Shinichi Samizo）

  **Email**                           [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com)

  **X**                               [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72)

  **GitHub**                          [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📄 ライセンス / License

  ------------------------------------------------------------------------------------------------------------
  項目                    ライセンス                                              説明
  ----------------------- ------------------------------------------------------- ----------------------------
  **コード**              [MIT](https://opensource.org/licenses/MIT)              自由に使用・改変・再配布可

  **教材テキスト**        [CC BY                                                  著者表示必須
                          4.0](https://creativecommons.org/licenses/by/4.0/)      

  **図表**                [CC BY-NC                                               非商用利用のみ
                          4.0](https://creativecommons.org/licenses/by-nc/4.0/)   

  **外部引用**            元ライセンスに従う                                      引用元を明記
  ------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 💬 フィードバック / Feedback

[![💬 GitHub
Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/AITL-H/discussions)
