import yaml

def load_fsm_yaml(filename):
    with open(filename, 'r') as f:
        return yaml.safe_load(f)

def generate_c_fsm_code(fsm_def):
    states = fsm_def['states']
    transitions = fsm_def['transitions']
    initial = fsm_def['initial_state']

    code = "#include <stdio.h>\n\n"
    code += "typedef enum {\n"
    for state in states:
        code += f"    STATE_{state.upper()},\n"
    code = code.rstrip(",\n") + "\n} FSMState;\n\n"
    code += f"FSMState state = STATE_{initial.upper()};\n\n"

    code += "void fsm_step(const char* input) {\n"
    code += "    switch (state) {\n"
    for state in states:
        code += f"        case STATE_{state.upper()}:\n"
        for t in transitions:
            if t['from'] == state:
                cond = t['condition']
                next_state = t['to']
                code += f"            if (strcmp(input, \"{cond}\") == 0) state = STATE_{next_state.upper()};\n"
        code += "            break;\n"
    code += "    }\n}\n"

    return code

if __name__ == "__main__":
    fsm = load_fsm_yaml("test_config.yaml")['fsm']
    c_code = generate_c_fsm_code(fsm)
    with open("fsm_generated.c", "w") as f:
        f.write(c_code)
    print("â FSM C code generated â fsm_generated.c")
