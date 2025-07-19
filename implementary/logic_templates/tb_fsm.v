// tb_fsm.v
// fsm_core.v に対する簡易テストベンチ

`timescale 1ns / 1ps

module tb_fsm;

    reg clk;
    reg reset;
    reg [1:0] in_signal;
    wire [1:0] out_signal;

    // DUTインスタンス
    fsm_core uut (
        .clk(clk),
        .reset(reset),
        .in_signal(in_signal),
        .out_signal(out_signal)
    );

    // クロック生成
    always #5 clk = ~clk;

    initial begin
        $display("Start FSM Test");
        clk = 0;
        reset = 1;
        in_signal = 2'b00;
        #10;

        reset = 0;
        #10;

        // IDLE → RUN
        in_signal = 2'b01;
        #10;

        // RUN → STOP
        in_signal = 2'b10;
        #10;

        // STOP → IDLE
        in_signal = 2'b00;
        #10;

        $finish;
    end

endmodule
