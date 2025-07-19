#!/bin/bash

# Verilogファイルのコンパイル
iverilog -o aitl_test \
    tb_aitl_top.v \
    aitl_top.v \
    fsm_core.v \
    pid_controller.v \
    llm_interface_stub.v

# 実行
vvp aitl_test

# 波形があれば開く
if [ -f waveform.vcd ]; then
    gtkwave waveform.vcd
fi
