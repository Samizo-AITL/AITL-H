fsm_core u_fsm (
    .clk(clk),
    .reset(reset),
    .in_signal(llm_command),
    .out_signal(fsm_state_out)
);

assign setpoint = (fsm_state_out == 2'b01) ? 16'sd100 :
                  (fsm_state_out == 2'b10) ? 16'sd0   :
                                            16'sd50;

pid_controller u_pid (
    .clk(clk),
    .reset(reset),
    .setpoint(setpoint),
    .feedback(feedback),
    .control_out(control_out)
);
