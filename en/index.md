---
layout: clean
permalink: /en/
title: "AITL-H (Hybrid Structural Control Framework)"
show_title: true
---

---

# 🤖 **AITL-H: Hybrid Structural Control Framework**

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back_to-Samizo--AITL_Portal-brightgreen)](https://samizo-aitl.github.io/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-license)

> ⚠️ **Under Development / Testing**  
> This project is still **in progress**, and its structure, specifications, and implementation are subject to change.  
> Please always check the latest repository contents when using or referencing it.

---

## 🆕 Update Log

| Date | Update | Reference |
|------|--------|-----------|
| 2025-08-25 | 🚩 Added **Humanoid Robot PoC (Flagship)** to top | [PoC Page](../PoC/humanoid/) |
| 2025-08-25 | 📑 Published 3 PoC reports (PWM Ripple / Thermal / Mission Energy) | [Docs Index](../PoC/humanoid/docs/) |
| 2025-08-25 | 🎤 Added template for presentation slides | [Slides](../PoC/humanoid/docs/flagship_poc_slides.md) |

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-Japanese-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-Japanese-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/en) |

---

## 🧭 Overview

| Item | Details |
|------|---------|
| **Name** | **AITL-H (Hybrid)** |
| **Objective** | Establishing humanoid robot control methods using **structural AI control** |
| **Core Principles** | - **FSM**: instinctive behavior control via state transitions<br>- **PID**: continuous control of physical quantities (angle, velocity)<br>- **LLM**: intelligence through advanced decision-making, dialogue, and learning |

---

## 🧘 Three-Layer Architecture

| Layer | Function | Implementation |
|-------|----------|----------------|
| **FSM Layer** | Logic control based on state transitions | `fsm_engine.py`, `fsm_state_def.yaml` |
| **PID Layer** | Physical control of joints and motion quantities | `pid_controller.py`, `pid_module.py` |
| **LLM Layer** | Situation assessment, anomaly detection, language response | `llm_interface.py`, `llm_logger.py` |

> Each layer is **loosely coupled yet cooperative**, allowing **independent development and step-by-step integration**.

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
```

---

## 🌏 Strategic Significance

AITL-H is not just a control architecture.  
By integrating **state feedback control** and **state transition control**, and combining with **LLMs** and **SystemDK**, it achieves **real-time optimal design under physical constraints**.

- **Industrial impact**  
  - 94% reduction in fault response time (PoC evaluation)  
  - 8× faster reconfiguration of production lines  
  - 40% reduction in design change costs  

- **National significance**  
  - Securing competitiveness in advanced-node semiconductors and industrial autonomous systems  
  - Gaining leadership in international standardization  

> **This technology must be integrated now.**  
> SystemDK is not unique to AITL-H but is an **essential foundational technology for all advanced-node semiconductor designs**.

---

## 🧪 PoC Related

| Title | Description | Path |
|-------|-------------|------|
| 🚩 **Humanoid Robot PoC (Flagship)** | Integrated flagship with FSM × PID × LLM × State-Space × Energy Harvesting | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](../PoC/humanoid/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/humanoid) |
| 🧭 **Gimbal Control (FSM + PID + LLM)** | Educational PoC for hybrid closed-loop control | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](../PoC/gimbal_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/gimbal_control) |
| ⚙️ **Verilog Auto-Generation (FSM + PID)** | YAML → C → Verilog conversion & verification | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](../PoC/verilog_demo/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/verilog_demo) |
| 🛠 **Auto Generator** | Tools for YAML → C → Verilog conversion of FSM/PID configs | [![View Manual](https://img.shields.io/badge/View-Manual-brightgreen?logo=github)](../PoC/auto_generator/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H/tree/main/PoC/auto_generator) |

---

## 🗺️ Project Relationship Map

```mermaid
flowchart TB
  EC["EduController
(Control Theory → AI Control)"]
  AITLH["AITL-H
Hybrid Control & SystemDK"]
  ESV["Edusemi-v4x
(SoC/RTL/Layout)"]

  EC -- Teaching Feed --> AITLH
  AITLH -- Methods & PoC Results --> ESV
  EC -- Cross Reference --> ESV
```
*A simple diagram showing the cross-reference among EduController ⇔ AITL-H ⇔ Edusemi-v4x.*

---

## 👤 Author

| Item | Details |
|------|---------|
| **Name** | **Shinichi Samizo** |
| **Education** | M.S. in Electrical and Electronic Engineering, Shinshu University |
| **Career** | Former Engineer at Seiko Epson Corporation (since 1997) |
| **Expertise** | Semiconductor devices (logic, memory, HV mixed-signal)<br>Inkjet thin-film piezo actuators<br>PrecisionCore printhead productization, BOM management, ISO training |
| **Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **X** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-license)

This project adopts a **Hybrid License**. Different licenses apply depending on whether the content is code, text, or figures.

| Item | License | Description |
|------|---------|-------------|
| **Code** | [MIT License](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text materials** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Attribution required |
| **Figures & diagrams** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External references** | Follow the original license | Cite the source |

---

## 💬 Feedback

> Please propose improvements or start discussions via **GitHub Discussions**.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/AITL-H/discussions)
