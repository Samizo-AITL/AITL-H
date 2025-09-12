# AITL on Space — 状態空間モデル（PoC基準）
Version: v0.1 / Target: **8–20 次元 MIMO**

---

## 0. 設計方針
- **離散時間**モデル（制御周期 `Ts = 2 ms` 既定、可変）  
- **3サブプラント**を結合：姿勢（3軸）＋電源（2次元）＋サーマル（3ノード）  
- 拡張で：並進2–3自由度／バイアス推定を追加（最大 20 次元）

---

## 1. 姿勢（3軸）モデル（反応ホイール駆動）
状態変数 `x_a = [θ_x, θ_y, θ_z, ω_x, ω_y, ω_z]^T`  
入力 `u_a = [τ_x, τ_y, τ_z]^T`（ホイール合力トルク）  
出力 `y_a = [θ_x, θ_y, θ_z]^T`（またはスター/サン・ジャイロの擬似）

連続系：
\begin{align}
\dot{\theta} &= \omega \\
J\dot{\omega} &= -D\omega - K\theta + u_a + d_a
\end{align}

- 慣性行列 `J = diag(Jx, Jy, Jz)`  
- 粘性 `D = diag(d_x, d_y, d_z)`、ばね `K = diag(k_x, k_y, k_z)`（弱結合なら0近似）  
- 外乱 `d_a` は太陽輻射・重力勾配トルク等

離散化（ZOH, Ts）：`(A_a, B_a, C_a, D_a)` を数値生成（EduController側）。

---

## 2. 電源（EPS）2次元モデル
状態 `x_e = [v_bus, i_bat]^T`  
入力 `u_e = [i_pv, i_load]^T`  
出力 `y_e = [v_bus]^T`

連続近似：
\begin{align}
C_{bus}\dot{v}_{bus} &= i_{pv} - i_{load} - i_{bat} \\
L_{bat}\dot{i}_{bat} &= -R_{bat} i_{bat} + v_{bus} - E_{oc}(SOC)
\end{align}

- `E_oc(SOC)` は線形化点での勾配 `k_soc` を用いて近似  
- MPC/H∞用に線形化し、`(A_e, B_e, C_e, D_e)` を得る

---

## 3. サーマル（3ノード）モデル
状態 `x_t = [T_chip, T_pkg, T_rad]^T`  
入力 `u_t = [P_chip, Q_rad]^T`（消費電力・放熱制御）  
出力 `y_t = [T_chip, T_pkg]^T`

連続：
\begin{align}
C_c \dot{T}_c &= -\frac{T_c - T_p}{R_{cp}} + P_{chip} \\
C_p \dot{T}_p &= \frac{T_c - T_p}{R_{cp}} - \frac{T_p - T_r}{R_{pr}} \\
C_r \dot{T}_r &= \frac{T_p - T_r}{R_{pr}} - \frac{T_r - T_{space}}{R_{r\infty}} + Q_{rad}
\end{align}

- パラメタは SystemDK FEM から同定（`R_*`, `C_*`）

---

## 4. 結合モデル（PoC最小 11次元）
\begin{align}
x &= \begin{bmatrix} x_a \\ x_e \\ x_t \end{bmatrix},\quad
u = \begin{bmatrix} u_a \\ u_e \\ u_t \end{bmatrix}
\end{align}

ブロック対角を基本に、以下の弱結合を追加：  
- **熱→電源**：`v_bus` の ESR/温度係数 → 行列項 `A_{e\leftarrow t}`  
- **熱→姿勢**：ホイール摩擦 `d(T_chip)` → `A_{a\leftarrow t}`  
- **電源→姿勢**：供給電圧低下による最大トルク低下 → `B_{a\leftarrow e}`

最終離散モデル：
\begin{align}
x_{k+1} &= A x_k + B u_k + E w_k \\
y_k &= C x_k + D u_k + v_k
\end{align}

- 外乱 `w_k`：トルク、日照、負荷変動、放熱境界  
- 観測ノイズ `v_k`：IMU/スター/サン、電圧・温度センサ

---

## 5. 推定器（H∞ / EKF）
- **IMU (1 kHz)**＋**Sun/Star (5–20 Hz)** のマルチレート融合  
- H∞フィルタ：`γ` 最小化で最悪外乱に対する誤差上界を保証  
- EKF：非線形（姿勢クォータニオン）運用時に採用

---

## 6. JSON エクスポート仕様（EduController→AITL‑H）
```json
{
  "Ts": 0.002,
  "A": [[...]], "B": [[...]], "C": [[...]], "D": [[...]],
  "E": [[...]],
  "state_names": ["thx","thy","thz","wx","wy","wz","vbus","ibat","Tchip","Tpkg","Trad"],
  "input_names": ["tax","tay","taz","ipv","iload","Pchip","Qrad"],
  "output_names": ["thx","thy","thz","vbus","Tchip"],
  "notes": "PoC minimal 11D model with weak thermal/power couplings",
  "version": "1.0"
}
```

---

## 7. 目標制御性能（例）
- 姿勢ステップ整定 ≤ **5 s**（±0.2° 精度）  
- 電源バス電圧リップル ≤ **50 mVpp**（0.5–10 Hz）  
- T_chip ≤ **110 °C**（外乱 +P_chip=peak）

---

## 8. 拡張（20次元まで）
- 並進 2–3 自由度（太陽帆/スラスタ）  
- センサバイアス（gyrobias xyz, scale）→ 状態に追加  
- 熱ノード 5–7 に拡張（ラジエータ分割、電源/バッテリ）
