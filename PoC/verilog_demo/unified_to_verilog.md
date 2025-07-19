
# 💬 Prompt Template: Convert Unified C Code to Verilog (AITL-H Structure)

This C code includes both a finite state machine (FSM) and a PID controller.  
Please convert it into Verilog modules according to the AITL-H architecture, separating logic as follows:

---

## 🧱 Required Verilog Modules

1. `fsm_core.v`: Moore-type FSM based on state transitions
2. `pid_controller.v`: Discrete-time PID controller
3. `aitl_top.v`: Top-level module to integrate FSM and PID (include I/O for LLM interface if needed)

---

## 📌 Requirements

- Use clear signal names (`clk`, `reset`, `input_signal`, `pid_output`, etc.)
- Assume synchronous logic with clock and reset
- Structure should enable testbench evaluation
- Add meaningful comments for clarity
- Maintain functional consistency with original C code logic

---

## 🔽 Target C Code

(Insert `unified.c` content here)
