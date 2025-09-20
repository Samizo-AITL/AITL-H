# SkyEdge High-Altitude Drone Platform — Specification

## 1. 概要
**SkyEdge (High-Altitude Ver.)** は、**高度 10,000 m 対応**を目指した国産セキュアドローンです。  
AITL三層制御（H∞ + FSM + LLM）を中核に、国産デバイス（65nm FDSOI SoC、0.35µm LDMOS、CIS）、  
高高度対応外装（可変ピッチ・断熱・防氷）、冗長・セキュア設計を統合します。  

- 運用高度: 最大 10,000 m  
- 用途: 防災・災害対応、インフラ点検、警備・安全保障  
- 特徴: 「外乱に強い制御」＋「外装/電源設計」＋「国産セキュリティ」  

---

## 2. 制御システム

### 内側ループ: H∞制御
- 外乱（風速 20–30 m/s 突風、乱気流）に対して安定余裕を保証  
- 数学的に ‖Tzw‖∞ を最小化、PIDより強い安定性  

### 中間ループ: FSM
- モード管理（通常 / 高高度 / 緊急帰還 / 通信断）  
- 電源劣化・モータ故障 → 自動遷移  

### 外側ループ: LLM
- 未知の障害に対する制御則再設計  
- FSM遷移条件の最適化（例：抗力増大時の可変ピッチ切替）  

---

## 3. デバイス仕様

- **65nm FDSOI AMS SoC**  
  - IMU/GNSS/CIS集約、TinyML  
  - 電源管理（EH＋デュアルバッテリ）  
- **0.35µm LDMOSドライバ**  
  - 高耐圧 (30–60V)、高トルクモータ駆動  
- **CMOSイメージセンサ**  
  - 可視光＋近赤外、NDVI/監視対応  
- **エナジーハーベスト**  
  - PZT振動＋ソーラー → ブラックボックス電源用  

---

## 4. 外装仕様（高高度版）

- **プロペラ**: 14–20インチ可変ピッチ、低Re空力プロファイル  
- **モータ**: 320–500 kV トルク型、冗長6ローター  
- **フレーム**: CFRP＋発泡コア、半カウル整形で抗力低減  
- **バッテリ外装**: 断熱＋PTCヒータ、-50℃運用  
- **デアイシング**: 撥水・氷着防止コート  
- **気密設計**: 凝露対策に乾燥剤＋ベント  
- **アンテナ配置**: 衛星通信ラドーム（上面）＋GNSS/5G/LPWA分離  

---

## 5. 構成部品表 (BOM Tree)

```
SkyEdge High-Altitude Drone
├── Airframe
│   ├── Frame tubes — 8 / 8
│   ├── Center plate — 2 / 2
│   ├── Landing gear — 1 / 1
│   ├── Prop guards — 0 / 4
│   └── Radome (satellite/GNSS) — 1 / 1
│
├── Propulsion
│   ├── Propellers — 0 / 6 (14–20" variable pitch)
│   ├── Motors (BLDC) — 0 / 6 (320–500 kV)
│   ├── ESC — 0 / 6
│   └── Servo actuators (pitch) — 0 / 6
│
├── Power
│   ├── Main battery pack — 1 / 2
│   ├── Battery heater/insulation — 0 / 1
│   ├── Power distribution board — 1 / 1
│   └── Backup EH supply — 1 / 1
│
├── Control & Compute
│   ├── Main SoC board (65nm FDSOI) — 1 / 1
│   ├── Motor driver board (0.35µm LDMOS) — 1 / 1
│   └── RT SBC (optional vision) — 0 / 1
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
    ├── RTOS/Flight stack (H∞ kernel + FSM) — 1 / 1
    └── OTA/Bootloader (Secure boot, TPM bound) — 1 / 1
```

---

## 6. セキュリティ & 冗長性
- TPM, セキュアブート, PQC暗号  
- 6ローター冗長設計  
- デュアルバッテリ＋EH補機  
- IMU 2系統＋GNSS/SLAM冗長  

---

## 7. 政策・社会的意義
- **国産セキュアドローン**（高市発言「国産不足」に対応）  
- **GX**（高高度観測・災害モニタリング）  
- **安全保障**（通信断・妨害時でも継続飛行）  
- **教育資産**（制御理論＋デバイス＋実装を統合した教材化）  
