"""Build an exploratory perceived-gender chart from the public CV scores."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cv_scores.csv"
OUT = ROOT / "charts" / "10_gender_proxy.png"
GROUPS = {
    "Aisha Patel": "Female",
    "Alice Brown": "Female",
    "Fatima Okafor": "Female",
    "Mei Chen": "Female",
    "James Brown": "Male",
    "Mohammed Ali": "Male",
    "Olufemi Adebayo": "Male",
    "Alex Morgan": "Ambiguous",
    "Jamie Taylor": "Ambiguous",
    "Wei Chen": "Ambiguous",
}
ORDER = ["Female", "Male", "Ambiguous"]
COLORS = {"Female": "#2f6f9f", "Male": "#1d4e89", "Ambiguous": "#9aa4aa"}
INK = "#25313b"
MUTED = "#66727c"
GRID = "#e4e6e3"
ACCENT = "#c8553d"
RNG = np.random.default_rng(20261021)


def main() -> None:
    scores = pd.read_csv(DATA)
    scores["gender_proxy"] = scores["name"].map(GROUPS)
    data = [scores.loc[scores["gender_proxy"] == group, "score"].to_numpy() for group in ORDER]
    rows = []
    for group, values in zip(ORDER, data):
        rows.append((group, len(values), float(values.mean()), float(values.std(ddof=1))))
    table = pd.DataFrame(rows, columns=["group", "n", "mean", "sd"])
    overall = float(scores["score"].mean())

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 10,
            "axes.edgecolor": "#b9bfc2",
            "axes.linewidth": 0.8,
            "figure.facecolor": "#fcfcf9",
            "axes.facecolor": "#ffffff",
            "savefig.facecolor": "#fcfcf9",
        }
    )
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    positions = np.arange(len(table))
    box = ax.boxplot(
        data,
        positions=positions,
        orientation="horizontal",
        widths=0.56,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "white", "linewidth": 2},
        whiskerprops={"color": "#6a737a"},
        capprops={"color": "#6a737a"},
    )
    for patch, group in zip(box["boxes"], table["group"]):
        patch.set_facecolor(COLORS[group])
        patch.set_edgecolor(COLORS[group])
        patch.set_alpha(0.88)
    for position, values in zip(positions, data):
        jitter = RNG.normal(0, 0.065, len(values))
        ax.scatter(values, np.full(len(values), position) + jitter, s=9, color=INK, alpha=0.22, linewidths=0)
        ax.scatter(values.mean(), position, marker="D", s=34, color=ACCENT, zorder=5, edgecolor="white", linewidth=0.7)
    ax.axvline(overall, color=ACCENT, linewidth=1.2, linestyle="--")
    ax.set_yticks(positions, [f"{row.group} ({row.n}, {row.mean:.1f})" for row in table.itertuples()])
    ax.set_xlim(0, 65)
    ax.set_xlabel("CV-level mean score across two calls")
    ax.set_title("Perceived gender from name shows no detectable difference", loc="left", pad=34)
    ax.text(
        0,
        1.012,
        "Each point is one CV; boxes show median and quartiles; diamonds mark group means. Ambiguous names are not forced into a binary.",
        transform=ax.transAxes,
        va="bottom",
        color=MUTED,
        fontsize=9,
    )
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#b9bfc2")
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.grid(axis="y", visible=False)
    ax.set_axisbelow(True)
    fig.savefig(OUT, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(table.round(2).to_string(index=False))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
