// tb_pid.v
// pid_controller.v に対する簡易テストベンチ

`timescale 1ns / 1ps

module tb_pid;

    reg clk;
    reg reset;
    reg signed [15:0] setpoint;
    reg signed [15:0] feedback;
    wire signed [15:0] control_out;

    // DUTインスタンス
    pid_controller #(
        .WIDTH(16),
        .KP(1),
        .KI(1),
        .KD(1)
    ) uut (
        .clk(clk),
        .reset(reset),
        .setpoint(setpoint),
        .feedback(feedback),
        .control_out(control_out)
    );

    // クロック生成
    always #5 clk = ~clk;

    initial begin
        $display("Start PID Test");
        clk = 0;
        reset = 1;
        setpoint = 16'sd100;
        feedback = 16'sd0;
        #10;

        reset = 0;
        #10;

        repeat (10) begin
            feedback = feedback + 16'sd5;  // 模擬応答
            #10;
        end

        $finish;
    end

endmodule
