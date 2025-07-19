// llm_interface_stub.v
// LLM（知性層）による外部命令入力のスタブモジュール

module llm_interface_stub (
    input  wire clk,
    input  wire reset,
    output reg  [1:0] llm_command     // 外部からFSMへの命令信号
);

    reg [31:0] counter;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            counter     <= 0;
            llm_command <= 2'b00;
        end else begin
            counter <= counter + 1;

            // 模擬命令の生成（周期的に切り替える）
            case (counter[5:4])
                2'b00: llm_command <= 2'b01; // RUN命令
                2'b01: llm_command <= 2'b10; // STOP命令
                2'b10: llm_command <= 2'b00; // IDLE命令
                default: llm_command <= 2'b00;
            endcase
        end
    end

endmodule
