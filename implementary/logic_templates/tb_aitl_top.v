// tb_aitl_top.v
// aitl_top.v に対する統合テストベンチ（FSM + PID + LLMスタブ）

`timescale 1ns / 1ps

module tb_aitl_top;

    reg clk;
    reg reset;
    reg signed [15:0] feedback;
    wire signed [15:0] control_out;

    // DUT: aitl_top
    aitl_top uut (
        .clk(clk),
        .reset(reset),
        .feedback(feedback),
        .control_out(control_out)
    );

    // クロック生成（10ns周期）
    always #5 clk = ~clk;

    initial begin
        $display("Start AITL Top Test");
        clk = 0;
        reset = 1;
        feedback = 16'sd0;
        #10;

        reset = 0;
        #10;

        // 模擬応答：徐々に feedback を上げてみる
        repeat (5) begin
            feedback = feedback + 16'sd10;
            #20;
        end

        repeat (5) begin
            feedback = feedback - 16'sd5;
            #20;
        end

        $finish;
    end

endmodule
