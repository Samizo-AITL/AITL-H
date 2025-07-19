import yaml

def load_pid_yaml(filename):
    with open(filename, 'r') as f:
        return yaml.safe_load(f)

def generate_c_pid_code(pid_def):
    kp = pid_def.get('kp', 1.0)
    ki = pid_def.get('ki', 0.0)
    kd = pid_def.get('kd', 0.0)
    setpoint = pid_def.get('setpoint', 0)
    out_min, out_max = pid_def.get('output_limits', [-100, 100])

    code = "#include <stdio.h>\n\n"
    code += f"double kp = {kp}, ki = {ki}, kd = {kd};\n"
    code += f"double setpoint = {setpoint};\n"
    code += f"double out_min = {out_min}, out_max = {out_max};\n"
    code += "double integral = 0, prev_error = 0;\n\n"
    code += "double pid_step(double input) {\n"
    code += "    double error = setpoint - input;\n"
    code += "    integral += error;\n"
    code += "    double derivative = error - prev_error;\n"
    code += "    double output = kp * error + ki * integral + kd * derivative;\n"
    code += "    if (output > out_max) output = out_max;\n"
    code += "    if (output < out_min) output = out_min;\n"
    code += "    prev_error = error;\n"
    code += "    return output;\n"
    code += "}\n"

    return code

if __name__ == "__main__":
    pid = load_pid_yaml("test_config.yaml")['pid']
    c_code = generate_c_pid_code(pid)
    with open("pid_generated.c", "w") as f:
        f.write(c_code)
    print("â PID C code generated â pid_generated.c")
