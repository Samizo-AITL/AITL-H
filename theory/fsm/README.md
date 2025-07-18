# 🔄 FSM 理論 – 制御層の中核ロジック

FSM（有限状態機械）は、**AITL-Hの第2層「制御層」**における中核ロジックです。  
人型ロボットにおける「行動の流れ」や「条件分岐」を構造的に記述・制御するために用いられます。

---

## 🧩 FSMとは

FSM（Finite State Machine）は、以下の要素から構成されます：

- **状態（State）**：システムが現在どの段階にあるか（例：立ち上がり中、歩行中、待機中）
- **入力（Input）**：外部または内部の条件（例：足裏センサ、時間、ユーザ命令）
- **遷移（Transition）**：入力に応じて状態がどのように変化するかを定義
- **出力（Output）**：現在の状態や遷移に応じた動作（例：モーター出力、音声発話）

FSMを用いることで、複雑なロジックを**視覚的かつ論理的に記述・管理**できます。

---

## 🔁 状態遷移の例

```text
[起動待機]
   │（起動コマンド）
   ↓
[立ち上がり動作]
   │（完了信号）
   ↓
[歩行状態]
   │（障害物検知）
   ↓
[停止状態]
```

---

## 🧠 AITL-H における役割

FSMは、LLM層からの**高次判断**を受けて、物理層（PID制御）に対して**具体的な動作指令**を出す中間制御層を担います：

| 上位 | LLM（推論層）→ FSMへ | 例：会話から「座って」命令を抽出 |
|------|----------------------|------------------------------|
| 中位 | FSM（制御層）        | 状態遷移：歩行中 → 停止 → 座る |
| 下位 | FSM → PID制御        | 各関節に目標角度を伝達           |

---

## 📂 構成ファイル（予定）

| ファイル名 | 役割 |
|------------|------|
| `fsm_engine.py` | FSMのコアエンジン（状態・遷移・入力管理） |
| `fsm_state_def.yaml` | 状態定義・遷移条件を記述する設定ファイル |
| `fsm_simulator.ipynb` | FSM動作の可視化とテスト用ノートブック |
| `docs/fsm_design_notes.md` | 設計方針・導入手順・使用例・LLM連携方法 |

---

## 📚 応用と拡張

- **階層FSM（HFSM）**による多段階行動制御
- **状態履歴ログ**による異常検知や自己改善ループ
- **LLMによる状態遷移定義の動的生成**（プロンプトベース）

---

## 🧠 FSM制御の教育的意義

FSMは、以下のような教育効果を持ちます：

- 制御構造の可視化
- LLMや物理制御との**橋渡し概念**の理解
- プログラムと論理設計の接続点の体得

---

## ✍️ 制作者より

FSMは単なる状態制御ではなく、**「知能と物理の橋渡し」**として重要な役割を果たします。  
AITL-Hでは、FSMを構造的制御の基盤として位置づけ、教育・PoC・実装の全てで活用していきます。

---
