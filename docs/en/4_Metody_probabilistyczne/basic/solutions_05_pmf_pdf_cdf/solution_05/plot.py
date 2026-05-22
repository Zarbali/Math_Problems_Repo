"""Generate PMF/CDF comparison plots for Solution 05 — Poisson."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

HERE = Path(__file__).resolve().parent

cases = [("λ=0.5", 0.5), ("λ=2", 2.0), ("λ=5", 5.0), ("λ=10", 10.0)]
k_max = 20

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, lam in cases:
    k = np.arange(0, k_max + 1)
    pmf = poisson.pmf(k, lam)
    ax.stem(k, pmf, linefmt="-", markerfmt="o", basefmt=" ", label=label)
ax.set_xlabel("k (number of events)")
ax.set_ylabel("P(X = k)")
ax.set_title("Poisson PMF — varying rate λ")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pmf_lambda_varied.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, lam in cases:
    k = np.arange(0, k_max + 1)
    cdf = poisson.cdf(k, lam)
    ax.step(k, cdf, where="post", linewidth=2, label=label, marker="o", markersize=4)
ax.set_xlabel("k")
ax.set_ylabel("F(k) = P(X ≤ k)")
ax.set_title("Poisson CDF — varying λ")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_lambda_varied.png", dpi=160)
plt.close(fig)
print("Saved Poisson plots to", HERE)
