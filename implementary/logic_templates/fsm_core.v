// fsm_core.v
// Moore型 状態遷移制御テンプレート（同期式）
// 状態変数・入力・出力はパラメータで再利用可能に設計

module fsm_core (
    input  wire clk,
    input  wire reset,
    input  wire [1:0] in_signal,   // 入力信号
    output reg  [1:0] out_signal   // 出力信号
);

    // 状態定義（例：IDLE, RUN, STOP）
    typedef enum logic [1:0] {
        IDLE = 2'b00,
        RUN  = 2'b01,
        STOP = 2'b10
    } state_t;

    state_t current_state, next_state;

    // 状態遷移
    always_ff @(posedge clk or posedge reset) begin
        if (reset)
            current_state <= IDLE;
        else
            current_state <= next_state;
    end

    // 次状態論理
    always_comb begin
        case (current_state)
            IDLE:  next_state = (in_signal == 2'b01) ? RUN : IDLE;
            RUN:   next_state = (in_signal == 2'b10) ? STOP : RUN;
            STOP:  next_state = (in_signal == 2'b00) ? IDLE : STOP;
            default: next_state = IDLE;
        endcase
    end

    // 出力論理（Moore型：状態のみで決まる）
    always_comb begin
        case (current_state)
            IDLE:  out_signal = 2'b00;
            RUN:   out_signal = 2'b01;
            STOP:  out_signal = 2'b10;
            default: out_signal = 2'b00;
        endcase
    end

endmodule
