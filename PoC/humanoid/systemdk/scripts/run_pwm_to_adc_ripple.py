#!/usr/bin/env python3
"""
run_pwm_to_adc_ripple.py
- PWM駆動のリップルがADC精度(ENOB)に与える影響を推定
- 入力: benches/pwm_to_adc_ripple/bench.yml, models/ams_018_afe_noise.yaml
- 出力: reports/pwm_to_adc_ripple/ にCSV, Markdown, グラフを保存
"""

from pathlib import Path
import yaml, math, pandas as pd, matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[2]
MODELS = BASE / "models"
BENCH = BASE / "benches" / "pwm_to_adc_ripple" / "bench.yml"
OUT = BASE / "reports" / "pwm_to_adc_ripple"

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    ams = yaml.safe_load((MODELS / "ams_018_afe_noise.yaml").read_text())
    bench = yaml.safe_load(BENCH.read_text())

    freqs = bench["supply"]["pwm"]["freq_khz"]
    duties = bench["supply"]["pwm"]["duty"]
    edge_ns = bench["supply"]["pwm"]["edge_ns"]

    enob_nom = ams["adc"]["enob_bits_nominal"]
    sens = ams["supply_sensitivity"]["ripple_to_enob_loss_bits_per_mVrms"]

    rows = []
    for f in freqs:
        for d in duties:
            # 簡易リップルモデル
            duty_factor = d * (1 - d) / 0.25
            edge_factor = 30.0 / max(edge_ns, 1.0)
            ripple_mVrms = 10.0 * duty_factor * edge_factor * (40.0 / f)

            enob_drop = sens * ripple_mVrms
            enob_eff = max(0.0, enob_nom - enob_drop)

            rows.append({
                "freq_khz": f,
                "duty": d,
                "ripple_mVrms": round(ripple_mVrms, 3),
                "enob_drop_bits": round(enob_drop, 3),
                "enob_effective_bits": round(enob_eff, 3),
            })

    df = pd.DataFrame(rows)
    (OUT / "pwm_to_adc_ripple_report.csv").write_text(df.to_csv(index=False))
    (OUT / "pwm_to_adc_ripple_report.md").write_text(df.to_markdown(index=False))

    # プロット
    for d in duties:
        sub = df[df["duty"] == d].sort_values("freq_khz")
        plt.figure()
        plt.plot(sub["freq_khz"], sub["enob_effective_bits"], marker="o")
        plt.title(f"ENOB vs PWM freq (duty={d})")
        plt.xlabel("PWM Frequency (kHz)")
        plt.ylabel("Effective ENOB (bits)")
        plt.grid(True, linestyle="--")
        plt.savefig(OUT / f"enob_vs_freq_duty_{str(d).replace('.','_')}.png")
        plt.close()

    print(f"Done. Reports saved to {OUT}")

if __name__ == "__main__":
    main()
