# 🧭 SystemDK モデル / SystemDK Models
*🧭 SystemDK Models*

このディレクトリには、SystemDKを用いた **マルチフィジックスモデルとシミュレーション** を格納します。  
*This directory contains **multi-physics models and simulations** using SystemDK.*

## 🔬 モデル化対象 / Modeling Targets
- SoC (22nm, FSM・LLM実行部)
- AMS回路 (0.18µm, センサAFE/ADC)
- LDMOS駆動回路 (0.35µm, PWM/Hブリッジ)
- 自己発電ブロック (圧電・PV・回生)

## 📂 内容 / Contents
- `bench/` : システム検証用ベンチモデル (Verification benches)
- `thermal/` : 熱解析モデル (Thermal models)
- `stress/` : 応力解析モデル (Stress models)
- `noise/` : ノイズ解析モデル (Noise coupling models)
