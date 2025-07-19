// pid_controller.v
// 離散時間型 PID コントローラ（Verilogテンプレート）
// 固定小数点（または整数）ベースで簡易に実装

module pid_controller #(
    parameter WIDTH = 16,           // ビット幅（例：16ビット）
    parameter KP = 1,               // 比例ゲイン
    parameter KI = 1,               // 積分ゲイン
    parameter KD = 1                // 微分ゲイン
)(
    input  wire clk,
    input  wire reset,
    input  wire signed [WIDTH-1:0] setpoint,   // 目標値
    input  wire signed [WIDTH-1:0] feedback,   // フィードバック値
    output reg  signed [WIDTH-1:0] control_out // 出力信号
);

    reg signed [WIDTH-1:0] error;
    reg signed [WIDTH-1:0] prev_error;
    reg signed [WIDTH-1:0] integral;
    reg signed [WIDTH-1:0] derivative;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            error       <= 0;
            prev_error  <= 0;
            integral    <= 0;
            derivative  <= 0;
            control_out <= 0;
        end else begin
            error      <= setpoint - feedback;
            integral   <= integral + error;
            derivative <= error - prev_error;
            control_out <= (KP * error) + (KI * integral) + (KD * derivative);
            prev_error <= error;
        end
    end

endmodule
