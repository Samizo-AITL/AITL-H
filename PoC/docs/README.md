# 📘 AITL-H / PoC設計マニュアル – ドキュメントトップ

本マニュアルは、AITL-H構想に基づく人型ロボット制御PoC（Proof of Concept）における**設計思想・構成・評価指針**を体系的に整理したものです。  
FSM（本能）＋ PID（理性）＋ LLM（知性）の三層構造を設計の軸に据え、PoC段階からSystemDKレベルへの展開を視野に設計します。

---

## 🧭 本マニュアルの目的

- 構造的制御のPoC（人型ロボット）を体系的に設計・記録する  
- AITLの三層モデル（推論／制御／物理）を設計・評価に組み込む  
- SystemDKや出口戦略を見据えたPoC展開を可能にする  

---

## 🧠 AITL三層構造との関係
```
      知性層（LLM）      ⇨ 状況判断・異常検知・対話
      ┃
      制御層（FSM）     ⇨ 状態遷移制御・行動選択
      ┃
      物理層（PID）     ⇨ モータ・センサ制御・ハード制御
```

- 各章はこの三層に対応する設計要素を明示的に区分して展開  
- 実装コードは [`PoC/`](../) および [`implementary/`](../../implementary/) に対応  

---

## 📚 章構成一覧

### 【0】緒言・導入

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第0章](chapter0_overview.md) | PoC設計全体像・AITL対応マニュアル概要 | 本マニュアルの目的と全体像紹介 |

---

### 【I】基本技術基盤

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第1章](chapter1_requirements.md) | PoC仕様策定と要件定義（AITL視点） | AITL視点によるPoC仕様と要件の策定 |
| [第2章](chapter2_pid_control.md) | 制御系設計の実務ポイント | PID制御、PWM、適応制御、現代制御理論の実践知識 |
| [第3章](chapter3_rtl_design.md) | RTL設計のAITL対応実務ポイント | RTL設計におけるAITL理論適用の実務ポイント |
| [第4章](chapter4_pdk_foundry.md) | PDKとファウンドリ選定（AITLと物理整合） | PDK選定とファウンドリ検討、AITL設計との整合性 |
| [第5章](chapter5_riscv_integration.md) | ソフト制御との連携設計（RISC-V上でのAITL連携） | RISC-Vを用いたソフト制御とAITL連携設計 |

---

### 【II】応用技術展開

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第6章](chapter6_sensor_if.md) | センサ混載技術とアナログIF設計（AITL構造反映） | センサ混載・アナログインターフェース設計 |
| [第7章](chapter7_dft.md) | DFT設計とテスト容易化（AITL評価指標含む） | DFT設計とAITL評価指標を踏まえたテスト容易化 |
| [第8章](chapter8_self_healing.md) | AI自己修復PoC設計手法（AITL理論適用） | AIを活用した自己修復設計手法 |
| [第9章](chapter9_soc_integration.md) | SoC統合と協調設計（ハード＋ソフト＋AITL連携） | ハード・ソフト統合設計とAITLによる協調設計 |
| [第10章](chapter10_poc_eval.md) | PoCプロジェクトの管理と評価（AITL評価体系） | プロジェクト管理とAITL評価体系、ドキュメント管理 |
| [第11章](chapter11_exit_plan.md) | 出口戦略とSystemDK移行設計 | PoCからSystemDKへの移行設計手法 |

---

### 【III】実装・検証

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第12章](chapter12_eval_metrics.md) | PoC評価の指標とプロジェクト管理（AITL観点） | PoC評価指標の詳細とプロジェクト管理 |

---

### 【IV】出口とSystemDK

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第13章](chapter13_physical_validation.md) | 製品化に向けた物理・実装検証 | SI/PI、熱、応力、EMI/EMCなど物理検証 |
| [第14章](chapter14_mixed_devices.md) | 外付け・混載デバイスとのインタフェース設計 | 外付け・混載デバイスのインターフェース設計 |
| [第15章](chapter15_ip_strategy.md) | SystemDK移行設計とIP再構成戦略（AITL設計資産化） | SystemDKへの設計資産化とIP再構成 |
| [第16章](chapter16_exit_strategy.md) | 出口戦略別SystemDK開発方針 | 出口戦略に応じたSystemDK開発の方針 |

---

### 【付録】

| 付録 | タイトル | 概要 |
|------|----------|------|
| [付録A](appendix_a_templates.md) | 設計テンプレート・PoC成果記録フォーマット | 設計テンプレートや成果記録のフォーマット |
| [付録B](appendix_b_exit_checklist.md) | 出口戦略別チェックリスト | 出口戦略ごとのチェックリスト |
| [付録C](appendix_c_conversion_cases.md) | PoCDK→SystemDK変換事例集 | PoCDKからSystemDKへ変換した事例集 |

---

## 📬 連絡先

技術監修・設計構成：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

## 📄 各章リンク一覧

- [第0章：PoC設計全体像・AITL対応マニュアル概要](./chapter00_intro.md)
- [第1章：PoC仕様策定と要件定義（AITL視点）](./chapter01_spec.md)
- [第2章：制御系設計の実務ポイント](./chapter02_control.md)
- [第3章：RTL設計のAITL対応実務ポイント](./chapter03_rtl.md)
- [第4章：PDKとファウンドリ選定（AITLと物理整合）](./chapter04_pdk.md)
- [第5章：ソフト制御との連携設計（RISC-V上でのAITL連携）](./chapter05_sw_control.md)
- [第6章：センサ混載技術とアナログIF設計（AITL構造反映）](./chapter06_sensor_if.md)
- [第7章：DFT設計とテスト容易化（AITL評価指標含む）](./chapter07_dft.md)
- [第8章：AI自己修復PoC設計手法（AITL理論適用）](./chapter08_self_repair.md)
- [第9章：SoC統合と協調設計（ハード＋ソフト＋AITL連携）](./chapter09_soc_integration.md)
- [第10章：PoCプロジェクトの管理と評価（AITL評価体系）](./chapter10_project_management.md)
- [第11章：出口戦略とSystemDK移行設計](./chapter11_exit_strategy.md)
- [第12章：PoC評価の指標とプロジェクト管理（AITL観点）](./chapter12_evaluation_management.md)
- [第13章：製品化に向けた物理・実装検証](./chapter13_physical_verification.md)
- [第14章：外付け・混載デバイスとのインタフェース設計](./chapter14_mixed_device_interface.md)
- [第15章：SystemDK移行設計とIP再構成戦略（AITL設計資産化）](./chapter15_systemdk_transition.md)
- [第16章：出口戦略別SystemDK開発方針](./chapter16_exit_policy.md)
- [付録A：設計テンプレート・PoC成果記録フォーマット](./appendix_a_templates.md)
- [付録B：出口戦略別チェックリスト](./appendix_b_exit_checklist.md)
- [付録C：PoCDK→SystemDK変換事例集](./appendix_c_conversion_cases.md)
