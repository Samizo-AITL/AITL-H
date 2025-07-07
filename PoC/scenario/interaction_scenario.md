# 🤖 PoC行動シナリオ定義：interaction_scenario.md

このファイルは、人型ロボットPoCにおける**状態遷移と行動シナリオ**をテキストベースで記述するものです。  
FSMの状態構成や、各状態で実行されるアクション・判断内容などを、シンプルに記述して動作仕様を共有できます。

---

## 🎯 想定シナリオ：人型ロボットの基本動作フロー

1. **初期状態（idle）**  
   - 動作待機中
   - 外部からの開始コマンドを待つ

2. **ターゲットへの接近（approach_target）**  
   - FSMにより、対象物（例：人、物体）への移動指令を出す  
   - PID制御により移動を制御（target: [1.0, 0.5]）

3. **状況確認（check_condition）**  
   - LLMにより状況判断（例：安全性の確認）
   - 応答が `"yes"` なら次へ進む、`"no"` なら停止

4. **対話・インタラクション（interact）**  
   - 音声出力、握手動作などを行う

5. **終了処理または再待機（abort / idle）**  
   - 状況に応じて停止または初期状態に戻る

---

## 🔄 状態遷移イメージ
```
idle ── start_command ──▶ approach_target ── reached_target ──▶ check_condition
├── llm_yes ─▶ interact ─▶ idle
└── llm_no  ─▶ abort ─▶ idle
```
---

## 📌 備考

- 本シナリオは `fsm_config.yaml` と一致する構成が前提です
- 詳細動作は run_main.py と制御モジュールにより定義されます

---
