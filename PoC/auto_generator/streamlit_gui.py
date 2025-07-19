import streamlit as st
import yaml

st.set_page_config(page_title="AITL FSM/PID Auto Generator", layout="wide")
st.title("⚙️ AITL-H Auto Generator (YAML → Cコード)")

# YAMLアップロード
st.header("📄 YAMLファイルをアップロード")
uploaded_file = st.file_uploader("test_config.yaml を選択してください", type=["yaml", "yml"])

if uploaded_file:
    config = yaml.safe_load(uploaded_file)

    if 'fsm' in config and 'pid' in config:
        fsm = config['fsm']
        pid = config['pid']

        # FSM Cコード生成
        states = fsm.get("states", [])
        transitions = fsm.get("transitions", [])
        initial = fsm.get("initial_state", states[0] if states else "IDLE")

        fsm_code = "#include <stdio.h>\n#include <string.h>\n\n"
        fsm_code += "typedef enum {\n"
        fsm_code += ",\n".join([f"    STATE_{s.upper()}" for s in states])
        fsm_code += "\n} FSMState;\n\n"
        fsm_code += f"FSMState state = STATE_{initial.upper()};\n\n"
        fsm_code += "void fsm_step(const char* input) {\n    switch (state) {\n"
        for s in states:
            fsm_code += f"        case STATE_{s.upper()}:\n"
            for t in transitions:
                if t['from'] == s:
                    fsm_code += f"            if (strcmp(input, \"{t['condition']}\") == 0) state = STATE_{t['to'].upper()};\n"
            fsm_code += "            break;\n"
        fsm_code += "    }\n}\n"

        # PID Cコード生成
        kp, ki, kd = pid.get('kp', 1.0), pid.get('ki', 0.0), pid.get('kd', 0.0)
        setpoint = pid.get('setpoint', 0)
        out_min, out_max = pid.get('output_limits', [-100, 100])

        pid_code = "#include <stdio.h>\n\n"
        pid_code += f"double kp = {kp}, ki = {ki}, kd = {kd};\n"
        pid_code += f"double setpoint = {setpoint};\n"
        pid_code += f"double out_min = {out_min}, out_max = {out_max};\n"
        pid_code += "double integral = 0, prev_error = 0;\n\n"
        pid_code += "double pid_step(double input) {\n"
        pid_code += "    double error = setpoint - input;\n"
        pid_code += "    integral += error;\n"
        pid_code += "    double derivative = error - prev_error;\n"
        pid_code += "    double output = kp * error + ki * integral + kd * derivative;\n"
        pid_code += "    if (output > out_max) output = out_max;\n"
        pid_code += "    if (output < out_min) output = out_min;\n"
        pid_code += "    prev_error = error;\n"
        pid_code += "    return output;\n}\n"

        unified_code = f"// === FSM MODULE ===\n{fsm_code}\n\n// === PID MODULE ===\n{pid_code}"

        # 表示
        st.header("🧠 FSM Cコード")
        st.code(fsm_code, language='c')

        st.header("🎯 PID Cコード")
        st.code(pid_code, language='c')

        st.header("🔗 統合Cコード unified.c")
        st.code(unified_code, language='c')

    else:
        st.error("YAMLファイルに 'fsm' と 'pid' セクションが必要です。")
