# 🔩 ハードウェア設計 / Hardware Design
*🔩 Hardware Design*

このディレクトリには、人型ロボットPoCにおける **ハードウェア設計ファイル** を格納します。  
*This directory contains the **hardware design files** for the humanoid robot PoC.*

## 🧩 対象ブロック / Target Blocks
- **22nm SoC**: FSM/LLM実装部, UART/SPI/I²C/CSI2 IF
- **0.18µm AMS**: センサHub, AFE, ADC
- **0.35µm LDMOS**: 駆動回路 (PWM/Hブリッジ, ゲートドライバ)
- **Energy Harvest**: 圧電, 薄膜PV, 回生ブレーキ + DC-DC制御

## 📂 内容 / Contents
- `soc/` : SoC RTL・IP設計 (SoC RTL and IP design)
- `ams/` : AMS回路設計 (AMS circuit design)
- `ldmos/` : LDMOSパワーデバイス設計 (LDMOS power device design)
- `harvest/` : エナジーハーベスト回路設計 (Energy harvesting circuit design)
