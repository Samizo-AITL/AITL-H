
# ChatGPTプロンプトテンプレート：FSM設計意図 → Cコード生成

## 🔧 指示内容（日本語）

以下のYAMLで記述された状態遷移仕様に基づいて、  
C言語でMoore型の状態機械コードを生成してください。

- 使用言語：C99準拠
- 状態は enum と switch-case で表現
- 出力は状態にのみ依存する（Moore型）
- クロック処理とリセット処理は main ループで模擬
- 入力信号は2bit整数で与えられるものとする

```yaml
（ここに fsm_template.yaml の内容を貼り付け）
```

## 💡 出力例（構成）

```c
typedef enum { IDLE, RUN, STOP } state_t;

state_t current_state = IDLE;

void fsm_step(uint8_t in_signal) {
    switch (current_state) {
        case IDLE:
            if (in_signal == 0x01) current_state = RUN;
            break;
        case RUN:
            if (in_signal == 0x02) current_state = STOP;
            break;
        case STOP:
            if (in_signal == 0x00) current_state = IDLE;
            break;
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
```

## 🧠 備考

- 状態遷移の仕様はChatGPTがパースする
- 生成後、main関数で動作ループ例を示すと実用的
