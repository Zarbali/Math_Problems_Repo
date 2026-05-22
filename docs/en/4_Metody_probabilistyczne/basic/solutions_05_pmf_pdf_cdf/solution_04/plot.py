"""Generate PMF/CDF comparison plots for Solution 04 — Geometric."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom

HERE = Path(__file__).resolve().parent

cases = [("p=0.15", 0.15), ("p=0.35", 0.35), ("p=0.60", 0.60)]
k_max = 25

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, p in cases:
    k = np.arange(1, k_max + 1)
    pmf = geom.pmf(k, p)
    ax.stem(k, pmf, linefmt="-", markerfmt="o", basefmt=" ", label=label)
ax.set_xlabel("k (trial of first success)")
ax.set_ylabel("P(X = k)")
ax.set_title("Geometric PMF — varying success probability p")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pmf_p_varied.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, p in cases:
    k = np.arange(1, k_max + 1)
    cdf = geom.cdf(k, p)
    ax.step(k, cdf, where="post", linewidth=2, label=label, marker="o", markersize=4)
ax.set_xlabel("k")
ax.set_ylabel("F(k) = P(X ≤ k)")
ax.set_title("Geometric CDF — varying p")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_p_varied.png", dpi=160)
plt.close(fig)
print("Saved geometric plots to", HERE)
