#!/usr/bin/env python3
"""
run_mission_energy.py
- ミッション中の負荷電力とハーベスト発電を積算し、バッテリSOC変動と寄与率を計算
- 入力: benches/mission_energy/bench.yml, models/harvest_sources.yaml
- 出力: reports/mission_energy/ にCSVとグラフを保存
"""

from pathlib import Path
import yaml, pandas as pd, matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[2]
MODELS = BASE / "models"
BENCH = BASE / "benches" / "mission_energy" / "bench.yml"
OUT = BASE / "reports" / "mission_energy"

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    harvest = yaml.safe_load((MODELS / "harvest_sources.yaml").read_text())
    bench = yaml.safe_load(BENCH.read_text())

    batt_cap_wh = harvest["battery"]["capacity_wh"]
    soc_init = harvest["battery"]["soc_init"]

    soc = soc_init * 100
    total_load_wh = 0
    total_harvest_wh = 0

    rows = []
    for phase in bench["mission_profile"]:
        dur_h = phase["duration_s"] / 3600.0
        load_wh = phase["power_load_w"] * dur_h
        total_load_wh += load_wh

        regen = harvest["sources"]["regenerative"]["avg_power_mw_walk"]/1000 * dur_h
        piezo = harvest["sources"]["piezo_array"]["avg_power_mw_walk"]/1000 * dur_h
        pv = harvest["sources"]["thinfilm_pv"]["avg_power_mw_outdoor"]/1000 * dur_h
        harvest_wh = regen + piezo + pv
        total_harvest_wh += harvest_wh

        soc = soc - (load_wh - harvest_wh)/batt_cap_wh*100

        rows.append({
            "phase": phase["name"],
            "duration_s": phase["duration_s"],
            "load_wh": round(load_wh, 3),
            "harvest_wh": round(harvest_wh, 3),
            "soc_pct": round(soc, 2)
        })

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "mission_energy_report.csv", index=False)
    (OUT / "mission_energy_report.md").write_text(df.to_markdown(index=False))

    plt.figure()
    plt.plot(df["phase"], df["soc_pct"], marker="o")
    plt.title("Battery SOC over Mission")
    plt.ylabel("SOC (%)")
    plt.grid(True, linestyle="--")
    plt.savefig(OUT / "soc_vs_phase.png")
    plt.close()

    # Summary
    contrib_pct = total_harvest_wh/total_load_wh*100
    print(f"Total load {total_load_wh:.2f} Wh, harvest {total_harvest_wh:.2f} Wh, contribution {contrib_pct:.1f}%")
    print(f"Reports saved to {OUT}")

if __name__ == "__main__":
    main()
