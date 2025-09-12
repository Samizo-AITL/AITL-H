# AITL on Space (PoC Profile)

## 概要 / Overview
**AITL on Space** は、AITL-H アーキテクチャ（Robust Core × FSM × AI）を  
**宇宙機向けウルトラロバスト制御** に適用するためのプロファイルです。  

- 内層 (**Robust Core**) : H∞ / MPC / SMC を用いたリアルタイム制御  
- 中層 (**FSM Supervisor**) : Safe / Nominal / Recovery のモード管理と故障検知・隔離  
- 外層 (**AI Adaptor**) : 長期劣化・外乱データを学習し、パラメタや運用ルールを再設計  
- 記憶階層 (**NVM Layer**) : SRAM + 大容量MRAM + 補助FRAM による安全な記録と更新  

本PoCでは、姿勢制御リグ・電源サーマルリグを対象に、  
**放射線イベント・熱サイクル・長期ドリフト**を注入したときの  
**可用性・ロバスト性・自己回復性**を検証します。

---

## ディレクトリ構成 / Directory Structure

```
space/
├─ README.md              # この文書
├─ robust_core/           # H∞, MPC, SMC 実装（固定小数点対応）
├─ supervisor_fsm/        # Boot/Safe/Nominal FSM + FDI/FDII
├─ nvm_layer/             # SRAM+MRAM+FRAM 模擬, ECC, Scrub FSM, WAL
├─ space_digital_twin/    # 姿勢/熱/電力モデル + 放射線外乱注入
├─ scenarios/             # 日食, SEUバースト, 熱サイクル, TID劣化
└─ experiments/           # PoC検証スクリプト & ログ
```

---

## 評価指標 / Metrics
- **制御性能** : |S|∞, |T|∞, 整定時間, 制約違反率
- **可用性** : SEU注入時の機能可用性 ≥ 99.9%（2時間シナリオ）
- **NVM健全性** : ECC訂正率, スクラブ周期遵守率, 異常時ロールバック成功率
- **FSM応答** : Safeモード到達時間, Recovery成功率

---

## 実装ステップ / Implementation Steps
1. Robust Core (H∞, MPC, SMC) のJSON設計値を受け入れ  
2. Supervisor FSM (状態遷移・FDI/FDII) の実装と検証  
3. NVM Layer (ECC, Scrub, WAL) の模擬とPoC統合  
4. Space Digital Twin + Scenarios による外乱注入試験  
5. Experiments で自動レポート生成

---

## 関連仕様 / Related Specs
- [../fsm_state_table.md](../fsm_state_table.md)  
- [../interface_spec.md](../interface_spec.md)  
- [../pid_design_spec.md](../pid_design_spec.md)  

---

## ライセンス / License
MIT License (c) 2025 Shinichi Samizo
