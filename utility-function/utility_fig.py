"""CRRA utility function U(c) = c^(1-eta) / (1-eta), with marginal utility at two consumption levels."""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

ETA = 1.5
C1, C2 = 0.1, 0.6  # consumption levels where marginal utility is illustrated

INK, MUTED, GRID = "#1f2937", "#6b7280", "#e5e7eb"
CURVE, ACCENT = "#1f5fa8", "#c2410c"


def U(c):
    return c ** (1 - ETA) / (1 - ETA)


def dU(c):
    return c ** (-ETA)


c = np.linspace(0.02, 1.0, 500)

fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
ax.plot(c, U(c), color=CURVE, lw=2.2, zorder=3)

# (consumption level, horizontal leg of slope triangle, label offset in points)
for i, (ci, run, offset) in enumerate(((C1, 0.1, (8, -4)), (C2, 0.25, (-60, -22))), start=1):
    ui, slope = U(ci), dU(ci)
    # tangent line
    t = np.array([ci - 0.08, ci + run + 0.08])
    ax.plot(t, ui + slope * (t - ci), color=ACCENT, lw=1.2, ls="--", zorder=2)
    # slope triangle: horizontal leg run, vertical leg slope*run
    ax.plot([ci, ci + run, ci + run], [ui, ui, ui + slope * run], color=ACCENT, lw=1.2, zorder=2)
    ax.plot(ci, ui, "o", ms=6, color=CURVE, mec="white", mew=1.5, zorder=4)
    ax.annotate(
        rf"$U'(c_{i}) = c_{i}^{{-\eta}} = {slope:.2f}$",
        xy=(ci + run, ui + slope * run / 2),
        xytext=offset, textcoords="offset points",
        color=INK, fontsize=10, va="center",
    )
    ax.annotate(rf"$c_{i}$", xy=(ci, ui), xytext=(-4, 10), textcoords="offset points",
                color=MUTED, fontsize=10, ha="right")

ax.set_title(r"Utility function  $U(c) = \dfrac{c^{\,1-\eta}}{1-\eta}$,  $\eta = 1.5$",
             color=INK, fontsize=13, pad=12)
ax.set_xlabel("Consumption, $c$", color=INK)
ax.set_ylabel("Utility, $U(c)$", color=INK)
ax.set_xlim(0, 1.02)
ax.set_ylim(U(0.02), U(1.0) + 1)

ax.text(0.97, 0.06,
        "Marginal utility $U'(c)$ is the slope of the curve.\n"
        "It is large at low consumption and small at high consumption.",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color=MUTED)

ax.grid(True, color=GRID, lw=0.8)
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(MUTED)
ax.tick_params(colors=MUTED)

fig.tight_layout()
out = Path(__file__).with_suffix("")
fig.savefig(out.with_suffix(".png"))
fig.savefig(out.with_suffix(".pdf"))
