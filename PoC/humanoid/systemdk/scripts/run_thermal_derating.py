#!/usr/bin/env python3
"""
run_thermal_derating.py
- 駆動LDMOSの発熱を簡易モデルで計算し、温度推移とデレート発生を評価
- 入力: benches/thermal_derating/bench.yml, models/ldm_035_drive_thermal.yaml
- 出力: reports/thermal_derating/ にCSVとグラフを保存
"""

from pathlib import Path
import yaml, pandas as pd, matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[2]
MODELS = BASE / "models"
BENCH = BASE / "benches" / "thermal_derating" / "bench.yml"
OUT = BASE / "reports" / "thermal_derating"

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    ldm = yaml.safe_load((MODELS / "ldm_035_drive_thermal.yaml").read_text())
    bench = yaml.safe_load(BENCH.read_text())

    rtheta = ldm["thermal"]["rtheta_ja_c_per_w"]
    shutdown = bench["control"]["shutdown_c"]
    derate_start = bench["control"]["derate_start_c"]

    rows = []
    for amb in bench["ambient_c"]:
        t_j = amb
        derate_events = 0
        for phase in bench["mission_profile"]["phases"]:
            power_w = phase["torque_pct"] * 10  # 仮の換算 (10W max)
            delta_t = power_w * rtheta
            t_j = amb + delta_t
            derated = t_j > derate_start
            shut = t_j > shutdown
            rows.append({
                "ambient_c": amb,
                "phase": phase["name"],
                "power_w": round(power_w, 2),
                "junction_temp_c": round(t_j, 1),
                "derated": derated,
                "shutdown": shut
            })
            if derated: derate_events += 1

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "thermal_derating_report.csv", index=False)
    (OUT / "thermal_derating_report.md").write_text(df.to_markdown(index=False))

    # グラフ
    for amb in df["ambient_c"].unique():
        sub = df[df["ambient_c"]==amb]
        plt.figure()
        plt.plot(sub["phase"], sub["junction_temp_c"], marker="o")
        plt.axhline(derate_start, color="orange", linestyle="--", label="Derate start")
        plt.axhline(shutdown, color="red", linestyle="--", label="Shutdown")
        plt.title(f"Junction Temp vs Phase (Ambient={amb}C)")
        plt.ylabel("Temp (°C)")
        plt.legend()
        plt.savefig(OUT / f"thermal_vs_phase_{amb}C.png")
        plt.close()

    print(f"Done. Reports saved to {OUT}")

if __name__ == "__main__":
    main()
