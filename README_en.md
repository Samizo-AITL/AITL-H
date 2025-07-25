# 🤖 AITL-H: Hybrid Intelligent Control Architecture

**AITL-H (All-in-Theory Logic - Hybrid)** is a **three-layered intelligent control framework** designed for humanoid robots and adaptive systems.  
By integrating **FSM (Instinct) × PID (Reason) × LLM (Intelligence)**, AITL-H realizes real-time, stable, and flexible control systems.

---

🇯🇵 [日本語READMEはこちら](./README.md)  
　→ AITL-H：人型制御向けハイブリッド型知能制御アーキテクチャ（FSM × PID × LLM）

---

## 🧭 Overview

| Item        | Description |
|-------------|-------------|
| **Name**    | AITL-H (Hybrid) |
| **Purpose** | Establishment of structured intelligent control methods for humanoid robotics |
| **Core Layers** | - **FSM**: Behavioral logic via state transitions<br>- **PID**: Continuous control of physical quantities (e.g., angle, velocity)<br>- **LLM**: Intelligent decision-making, dialogue, and learning |

---

## 🧘 Three-Layer Architecture

| Layer | Function                   | Implementation Examples              |
|-------|----------------------------|--------------------------------------|
| FSM   | Logic control based on states | `fsm_engine.py`, `fsm_state_def.yaml` |
| PID   | Physical control of joints/motion | `pid_controller.py`, `pid_module.py` |
| LLM   | Decision-making, anomaly detection, dialogue | `llm_interface.py`, `llm_logger.py` |

> Each layer is **loosely coupled but cooperatively integrated**, allowing independent development and step-by-step integration.

<div align="center"><img src="theory/aitl_h_architecture.png" alt="AITL-H Architecture" width="400"></div>

---

## 📘 PoC Design Manual (16 Chapters)

A full **PoC design manual for humanoid control systems using FSM×PID×LLM** is available.  
▶︎ [📖 Read the Manual](docs/README.md)

---

## 🧪 Proof-of-Concept (PoC) List

| Title | Description | Path |
|-------|-------------|------|
| 🧭 Gimbal Control (FSM + PID + LLM) | Hybrid closed-loop control | [`PoC/gimbal_control`](./PoC/gimbal_control) |
| ⚙️ Verilog Auto-Generation (FSM + PID) | YAML → C → Verilog conversion & validation | [`PoC/verilog_demo`](./PoC/verilog_demo) |
| 🔍 Others | Coming soon | - |

---

## 🧪 Gimbal Control PoC (AITL-HX)

> **AITL-HX Architecture** implements a 3-axis gimbal control demo.  
> Natural Language → FSM → PID → Actuator forms a closed intelligent loop.

📂 Directory: [`PoC/gimbal_control/`](./PoC/gimbal_control/)  
📘 Details: [`See README`](./PoC/gimbal_control/README.md)

![gimbal_architecture](./docs/images/figure9_1_gimbal_control_architecture.svg)

| Component | Description |
|-----------|-------------|
| LLM Layer | Converts natural language into goals and intentions |
| FSM Layer | Manages states: Idle / Track / Recover |
| PID Layer | Controls Roll, Pitch, and Yaw axes |
| Sensor Layer | Simulated 3-axis IMU sensor (pose estimation) |
| Actuator Layer | Simulated PWM-based motor control |

🧠 Key Learning Points:
- End-to-end hybrid control system with FSM + PID + LLM
- Natural language → adaptive goal generation
- MIMO control integrated with logical state switching

---

### 🧪 Verilog Auto-Generation PoC (FSM × PID)

> Using ChatGPT, define FSM and PID behavior via YAML and generate:  
> **C Code → Unified C → Verilog** with validation.

📂 Directory: [`PoC/verilog_demo/`](./PoC/verilog_demo/)  
📘 Details: [`See README`](./PoC/verilog_demo/README.md)

| Component | Description |
|----------|-------------|
| Input | `test_config.yaml` (FSM transitions + PID parameters) |
| Auto Gen | `fsm_auto_gen.py`, `pid_auto_gen.py` generate C code |
| Integration | `unified.c` → transformed into Verilog via GPT prompt |
| Verification | `tb_aitl_top.v` tested with iverilog |

🛠 Tools and Support Modules:
- ChatGPT for YAML → C → Verilog transformation
- [`auto_generator/`](./PoC/auto_generator/)
- [`logic_templates/`](./implementary/logic_templates/)

---

## 🤖 ChatGPT-Based Design Tools

Under `accelerated_design/`, a suite of GPT-assisted tools is provided:

- Prompt-based FSM generation (YAML output)
- Test scenario generation and log visualization
- Auto documentation and design review support

> 🧠 Goal: Build a **cooperative human-AI design environment**.

---

## 📂 Directory Structure

```
AITL-H/
├── theory/                # Design theory & architectural insights
├── PoC/                   # Proof-of-concept implementations
├── implementary/          # Python modules for FSM, PID, LLM
└── accelerated_design/    # ChatGPT-supported design tools
```

| Folder | Description |
|--------|-------------|
| [`theory/`](theory/) | Design principles and layered architecture |
| [`PoC/`](PoC/) | Demo codes and evaluation logs |
| [`implementary/`](implementary/) | Core implementation modules |
| [`accelerated_design/`](accelerated_design/) | AI-aided design tools & log processors |

---

## 🚀 Application Areas

- 🧓 **Elderly Care Robots**: Emotion-aware + physical assistance
- 🛠 **Self-evolving Controllers**: LLM-based feedback adaptation
- 🌏 **Disaster Response Robotics**: Rule-based + reasoned actions
- 🎓 **Education & Research**: Ideal platform for AI × control learning

---

## 🎓 Educational Linkage: EduController

AITL-H is fully integrated with **EduController**, an open educational framework on control theory and AI control.

| Part | Topics | AITL-H Relation |
|------|--------|-----------------|
| [Part 1–5](https://github.com/Samizo-AITL/EduController#制御理論系) | Classical & Modern Control | Theoretical foundation for PID layer |
| [Part 6–8](https://github.com/Samizo-AITL/EduController#ai制御系) | Neural & Reinforcement Control | AI control pathway |
| **[Part 9](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid)** | FSM × PID × LLM Integration | Direct implementation of AITL-H |

Also available:

🔹 **[matlab_tools](https://github.com/Samizo-AITL/EduController/tree/main/matlab_tools)**
- Visualize PID / state-space via Simulink
- Generate C code with Simulink Coder
- Extend to HDL via `c_to_hdl/`

🔹 **[SoC_DesignKit_by_ChatGPT](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT)**
- Templates for FSM, PID, LLM integration
- Verilog generation supported by GPT
- Testbenches included

> 🧠 Unified framework for **Education × Implementation × AI Design**

🔗 [View EduController](https://github.com/Samizo-AITL/EduController)

---

## 🧩 SoC Integration: Linked with Edusemi

To extend to **SoC / RTL / Physical Design**, check the related project: **[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)** – Special Edition.

| Chapter | Topic |
|---------|-------|
| [Chapter 3](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | SoC design with FSM×PID×LLM integration |
| [Chapter 4](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | OpenLane flow from RTL to GDSII |
| [Chapter 5](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | DRC/LVS/DFM for manufacturability |

---

## 📚 Related Projects

- [Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x): SoC/semiconductor design curriculum
- [EduController](https://github.com/Samizo-AITL/EduController): Classical + AI control learning materials

---

## 👤 Author

**Shinichi Samizo**  
- M.Eng. in Electrical & Electronic Engineering, Shinshu University  
- Former engineer at Seiko Epson Corporation (since 1997)  

📌 **Expertise**:
- Semiconductor (Logic, Memory, High-voltage mixed-signal)
- Thin-film piezo actuators
- PrecisionCore printhead development

📬 **Contact**
- ✉️ Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 Twitter: [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 GitHub: [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

© 2025 Shinichi Samizo — MIT License  
All materials, source code, and diagrams are freely available under the MIT License.

---

💬 Feedback or discussions → [Open Discussion](https://github.com/Samizo-AITL/AITL-H/discussions)

---
