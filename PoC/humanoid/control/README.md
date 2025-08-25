# 🎛️ 制御アーキテクチャ / Control Architecture
*🎛️ Control Architecture*

このディレクトリには、人型ロボットPoCの **制御アルゴリズム** を格納します。  
*This directory contains the **control algorithms** for the humanoid robot PoC.*

## ⚙️ 含まれる要素 / Included Components
- **FSM制御** (Finite State Machine control)
- **PID制御** (Proportional-Integral-Derivative control)
- **状態空間制御（LQR/LQG）** (State-space control: LQR/LQG)
- **LLM連携モジュール** (LLM interaction modules)

## 📂 内容 / Contents
- `fsm/` : FSMエンジン・状態定義 (FSM engine & state definitions)
- `pid/` : PIDコントローラ (PID controllers)
- `state_space/` : 状態空間制御 (State-space control modules)
- `llm_interface/` : LLM接続・ログ (LLM interface & logging)
