# PoC: AITLジンバル制御デモ

本ディレクトリは、FSM（本能）+ PID（理性）+ LLM（知性）に基づくAITL制御構成を、  
2軸ジンバルシステムに適用した評価用PoC構成です。

- FSM → センサ状態によるモード制御（例：IDLE→TRK→RECOVERY）
- PID → 角度誤差に基づくサーボ制御
- LLM → 目標方位 or コマンド発行（手動スタブ可）

## 使用ファイル
- `aitl_top.v`（logic_templatesより）
- `sensor_model.v`（PoC専用）
- `tb_gimbal.v`（統合ベンチ）
