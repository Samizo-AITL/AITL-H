---
layout: clean
# title: AITL-H/en/index.md  
---

---

# 🤖 **AITL-H: Hybrid Structural Control Framework**

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back_to-Samizo--AITL_Portal-brightgreen)](https://samizo-aitl.github.io/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-license)

> ⚠️ **Under Development**  
> This project is currently **in progress**, and its structure, specifications, and implementation details are subject to change.  
> Please check the latest repository content before using or referencing it.

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/en) |

---

**AITL-H (All-in-Theory Logic - Hybrid)** is a **hierarchical intelligent control architecture** designed for humanoid robots and adaptive systems.  
With its three-layer structure of **FSM (instinct) × PID (reason) × LLM (intelligence)**, it combines **instant responsiveness, stability, and flexibility**.

---

## 🧭 Overview

| Item | Details |
|------|---------|
| **Name** | **AITL-H (Hybrid)** |
| **Purpose** | **Establishing a humanoid robot control methodology using structured AI control** |
| **Core Principles** | - **FSM**: instinctive behavioral control through state transitions<br>- **PID**: continuous control of physical quantities (angle, velocity)<br>- **LLM**: intelligent decision-making, dialogue, and learning |

---

## 🧘 Three-Layer Architecture

| Layer | Function | Example Implementation |
|-------|----------|------------------------|
| **FSM Layer** | Logic control based on state transitions | `fsm_engine.py`, `fsm_state_def.yaml` |
| **PID Layer** | Physical control of joints and movement | `pid_controller.py`, `pid_module.py` |
| **LLM Layer** | Situation judgment, anomaly detection, language response | `llm_interface.py`, `llm_logger.py` |

> Each layer is designed to be **loosely coupled yet collaborative**, enabling **independent development and phased integration**.

### AITL-H: Hybrid Architecture

> 📌 This diagram is **displayed on GitHub**. On the site, use the button below to view the GitHub version.  
> [![View on GitHub](https://img.shields.io/badge/View_on-GitHub-black?logo=github)](https://github.com/Samizo-AITL/AITL-H/blob/main/README.md#aitl-h-hybrid-architecture)

```mermaid
flowchart TB
  subgraph LLM["LLM Layer"]
    L1[Decision-Making]
    L2[Anomaly Detection]
    L3[Language Response]
  end
  subgraph PID["PID Layer"]
    P1[Continuous Control]
    P2[Joint Angles / MIMO]
  end
  subgraph FSM["FSM Layer"]
    F1[Logic Control]
    F2[State Transitions]
  end

  LLM -->|Scenario / Commands| FSM
  FSM -->|Mode Control / Gain Select| PID
  PID -->|PWM / Control Signals| ACT["Actuators"]
  ACT -->|Motion Response| SEN["Sensors (IMU, etc.)"]
  SEN -->|Perception Feedback| LLM

  classDef box fill:#eaf5ff,stroke:#6ca7ff,stroke-width:1px,rx:6,ry:6;
  class LLM,PID,FSM,ACT,SEN box

  click F1 "https://github.com/Samizo-AITL/AITL-H/search?q=fsm_engine.py" "FSM Implementation"
  click P1 "https://github.com/Samizo-AITL/AITL-H/search?q=pid_controller.py" "PID Implementation"
  click L1 "https://github.com/Samizo-AITL/AITL-H/search?q=llm_interface.py" "LLM Interface"
```

---

## 🌏 Strategic Significance

AITL-H is not just a control architecture —  
it integrates **state feedback control** and **state transition control**, combined with **LLM (Large Language Models)** and **SystemDK**,  
to enable **real-time, physically-constrained optimal design**.

- **Industrial Impact**  
  - Major reduction in fault recovery time (PoC evaluation: 94% reduction)  
  - 8× faster production line reconfiguration  
  - 40% reduction in design change costs  
- **National Importance**  
  - Securing competitiveness in advanced-node semiconductors and industrial autonomous systems  
  - Leadership in international standardization  

> **This technology must be integrated now.**  
> SystemDK is not unique to AITL-H — it is **a core technology required for all advanced-node semiconductor design**.

---

## 🧪 PoC-Related

| Title | Summary | Path |
|-------|---------|------|
| 📘 **PoC Design Manual** | Humanoid robot PoC design manual based on FSM×PID×LLM integration (16 chapters) | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/docs/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/docs) |
| 🧭 **Gimbal Control (FSM + PID + LLM)** | Hybrid closed-loop control | [`PoC/gimbal_control`](../PoC/gimbal_control) |
| ⚙️ **Verilog Auto-Generation (FSM + PID)** | YAML → C → Verilog generation & verification | [`PoC/verilog_demo`](../PoC/verilog_demo) |

---

## 🧭 PoC Example: 3-Axis Gimbal Control with FSM × PID × LLM

> **Natural language command → State transition (FSM) → PID stabilization → Actuator** closed-loop configuration.  
> A basic implementation of the **AITL-HX architecture**, ideal for education and applied use.

📂 Directory: [**`PoC/gimbal_control/`**](../PoC/gimbal_control/)  
📘 Details: [**`README here`**](../PoC/gimbal_control/README.md)

<div align="center">
  <img src="../docs/images/figure9_1_gimbal_control_architecture.svg" alt="Gimbal Control Architecture" width="700">
</div>

---

## 🤖 ChatGPT Support Tools

Provided in `accelerated_design/`: **Design support tools using ChatGPT**

- State transition design support (prompt → FSM YAML automation)
- Test scenario / log visualization
- Automatic generation of design documents

> A **human-AI collaborative design framework**.

---

## 🎛️ Connection with EduController

**AITL-H** is **fully integrated** with **Chapter 9** (FSM × PID × LLM Hybrid Control) of the educational material **EduController**.

| Part | Content | Relation to AITL-H |
|------|---------|--------------------|
| **Part 01–05**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#制御理論系) | Classical to modern control theory (PID, state-space, etc.) | **Theoretical basis of PID layer** |
| **Part 06–08**<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController#ai制御系) | AI control (NN control, reinforcement learning, data-driven) | **Supplementary knowledge for AI application design** |
| **Part 09**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)&nbsp;[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | FSM × PID × LLM integrated control | **AITL-H architecture implemented as educational material** |

---

## 🎓 Integrated Design Deployment with Edusemi-v4x

To extend towards **SoC/RTL design**, see the “Special Edition” of **[Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x)**, which covers:

| Chapter | Content | Link |
|---------|---------|------|
| Chapter 3 | SoC design with FSM × PID × LLM integrated control | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |
| Chapter 4 | RTL → GDSII layout automation with OpenLane | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) |
| Chapter 5 | Physical verification and consistency check with DRC / LVS / DFM | [![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) |

### 📌 If you want to study physical constraints in more depth
Once you understand the flow from SoC design to physical verification, proceed to **Special Edition Chapter 2a: Handling Thermal, Stress, and Noise Constraints in SystemDK**.

[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)  
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk)

---

## 📚 Related Projects

| Project | Description | Link |
|---------|-------------|------|
| **Edusemi-v4x** | Semiconductor / SoC design educational material | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| **EduController** | Control theory × AI control educational material | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| **SamizoGPT** | Project Design Hub guide management | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT) |
| **AITL-Strategy-Proposal** | AITL strategic proposals and policy recommendations | [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-Strategy-Proposal/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-Strategy-Proposal) |

---

## 👤 Author

| 📌 Item | Details |
|---------|---------|
| **Name** | **Shinichi Samizo**<br>*Shinichi Samizo* |
| **Education** | **M.S. in Electrical and Electronic Engineering, Shinshu University** |
| **Career** | **Former Engineer at Seiko Epson Corporation (since 1997)** |
| **Expertise** | **Semiconductor devices** (logic, memory, high-voltage mixed integration)<br>**Inkjet thin-film piezo actuators**<br>**Productization of PrecisionCore printheads, BOM management, ISO training** |
| **Contact** | ✉️ [Email](mailto:shin3t72@gmail.com) / 🐦 [X](https://x.com/shin3t72) / 💻 [GitHub](https://samizo-aitl.github.io/) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-license)  

> **This project adopts a hybrid license**  
> Depending on the nature of the educational materials, code, and figures, the following licenses apply.

| 📌 Item | License | Description |
|---------|---------|-------------|
| **Code** | **[MIT License](https://opensource.org/licenses/MIT)** | Free to use, modify, redistribute |
| **Text materials** | **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** | Attribution required |
| **Figures & diagrams** | **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** | Non-commercial use only |
| **External references** | Follow original license | Clearly indicate source |

---

## 💬 Feedback

> Please submit improvement suggestions or start discussions via **GitHub Discussions**.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/AITL-H/discussions)
