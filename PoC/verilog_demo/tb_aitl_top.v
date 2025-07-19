`timescale 1ns / 1ps

module tb_aitl_top;

  reg clk;
  reg reset;
  reg [1:0] input_signal;
  reg [7:0] sensor_input;
  wire [1:0] fsm_state;
  wire [7:0] pid_output;

  aitl_top uut (
    .clk(clk),
    .reset(reset),
    .input_signal(input_signal),
    .sensor_input(sensor_input),
    .fsm_state(fsm_state),
    .pid_output(pid_output)
  );

  always #5 clk = ~clk;

  initial begin
    $dumpfile("aitl_top.vcd");
    $dumpvars(0, tb_aitl_top);

    clk = 0;
    reset = 1;
    input_signal = 0;
    sensor_input = 80;
    #10 reset = 0;

    $display("=== AITL Unified Test Start ===");

    // IDLE → TRACK
    input_signal = 1; sensor_input = 85; #20;
    $display("FSM=%d, PID_OUT=%d", fsm_state, pid_output);

    // TRACK → RECOVERY
    input_signal = 2; sensor_input = 70; #20;
    $display("FSM=%d, PID_OUT=%d", fsm_state, pid_output);

    // RECOVERY → IDLE
    input_signal = 3; sensor_input = 90; #20;
    $display("FSM=%d, PID_OUT=%d", fsm_state, pid_output);

    $display("=== AITL Unified Test Done ===");
    $finish;
  end

endmodule
