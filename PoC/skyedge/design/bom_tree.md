# SkyEdge Drone Platform — BOM Tree

部品構成を階層ツリーで示す。  
各ノードには **数量 (Std / High-Alt)** を付記。

---

## 📂 構成ツリー

```
SkyEdge Drone Platform
├── Airframe
│   ├── Frame tubes — 8 / 8
│   ├── Center plate — 2 / 2
│   ├── Landing gear — 1 / 1
│   ├── Prop guards — 0 / 4
│   └── Radome (top) — 1 / 1
│
├── Propulsion
│   ├── Propellers — 4 / 6
│   ├── Motors (BLDC) — 4 / 6
│   ├── ESC — 4 / 6
│   └── Servo actuators for pitch — 0 / 6
│
├── Power
│   ├── Main battery pack — 1 / 2
│   ├── Battery heater/insulation — 0 / 1
│   ├── Power distribution board — 1 / 1
│   └── Backup supply (EH) — 1 / 1
│
├── Control & Compute
│   ├── Main SoC board — 1 / 1
│   ├── Motor driver board — 1 / 1
│   └── RT SBC (optional) — 0 / 1
│
├── Sensors
│   ├── IMU — 2 / 2
│   ├── Magnetometer — 1 / 1
│   ├── Barometer — 1 / 1
│   └── GNSS/RTK — 1 / 1
│
├── Imaging
│   ├── CIS camera — 1 / 1
│   ├── Lens module — 1 / 1
│   └── Gimbal — 1 / 1
│
├── Communications
│   ├── LPWA radio — 1 / 1
│   ├── Wi-Fi/5G modem — 1 / 1
│   └── Satellite modem — 0 / 1
│
├── Security
│   ├── TPM/SE — 1 / 1
│   └── Crypto accelerator — 1 / 1
│
├── Environmental/Protection
│   ├── Enclosure seals — 1 / 1
│   ├── Conformal coating — 1 / 1
│   ├── Anti-icing coating — 0 / 1
│   └── Lens heater/anti-fog — 0 / 1
│
├── RF & Harness
│   ├── GNSS antenna — 1 / 1
│   ├── Wi-Fi/5G antennas — 2 / 2
│   ├── LPWA antenna — 1 / 1
│   ├── Power harness — 1 / 1
│   └── Data harness — 1 / 1
│
└── Software
    ├── RTOS/Flight stack — 1 / 1
    └── OTA/Bootloader — 1 / 1
```
