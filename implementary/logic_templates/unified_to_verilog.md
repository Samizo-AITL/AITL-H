# ChatGPTプロンプトテンプレート：統合Cコード → Verilog変換

## 🎯 目的

以下に示す C 言語コード（FSMとPIDの統合ロジック）を元に、  
Verilog HDL で動作等価な設計を生成してください。

- モジュール分割：fsm_core / pid_controller / aitl_top
- 命名ルール：C側と一致させる
- 出力は1ファイルずつ明示（FSM、PID、Top）

---

## 💻 入力（例：統合Cコード）

```c
// 状態定義と遷移
typedef enum { IDLE, RUN, STOP } state_t;
state_t current_state = IDLE;

void fsm_step(uint8_t in_signal) {
    switch (current_state) {
        case IDLE: if (in_signal == 0x01) current_state = RUN; break;
        case RUN:  if (in_signal == 0x02) current_state = STOP; break;
        case STOP: if (in_signal == 0x00) current_state = IDLE; break;
    }
}

uint8_t get_output() {
    switch (current_state) {
        case IDLE: return 0x00;
        case RUN:  return 0x01;
        case STOP: return 0x02;
        default:   return 0x00;
    }
}

// PID 制御
int16_t kp = 1, ki = 1, kd = 1;
int16_t error, prev_error, integral, derivative;

int16_t pid_step(int16_t setpoint, int16_t feedback) {
    error = setpoint - feedback;
    integral += error;
    derivative = error - prev_error;
    prev_error = error;
    return (kp * error) + (ki * integral) + (kd * derivative);
}
```

---

## 🔧 指示内容（ChatGPT用）

- 上記の C コードを Verilog に翻訳してください
- `fsm_core.v`, `pid_controller.v`, `aitl_top.v` の3ファイルに分けて出力
- トップモジュールは fsm出力を元に setpoint を切り替え、pid_controller に接続
- クロック、リセット信号を含めた同期設計とする
