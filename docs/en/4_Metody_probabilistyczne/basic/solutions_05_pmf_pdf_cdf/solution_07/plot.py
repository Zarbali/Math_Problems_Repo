"""Generate PMF/CDF plots for Solution 07 — Negative Binomial."""
from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent


def nb_pmf(k: int, r: int, p: float) -> float:
    """PMF for trial index of r-th success: k = r, r+1, ..."""
    if k < r:
        return 0.0
    return comb(k - 1, r - 1) * (p**r) * ((1 - p) ** (k - r))


def nb_cdf(k: int, r: int, p: float) -> float:
    return sum(nb_pmf(j, r, p) for j in range(r, k + 1))


cases = [
    ("r=1, p=0.25 (geometric)", 1, 0.25),
    ("r=3, p=0.40", 3, 0.40),
    ("r=5, p=0.30", 5, 0.30),
]
k_max = 30

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, r, p in cases:
    ks = np.arange(r, k_max + 1)
    pmf = [nb_pmf(int(k), r, p) for k in ks]
    ax.stem(ks, pmf, linefmt="-", markerfmt="o", basefmt=" ", label=label)
ax.set_xlabel("k (trial of r-th success)")
ax.set_ylabel("P(X = k)")
ax.set_title("Negative binomial PMF — varying r and p")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pmf_r_p_varied.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, r, p in cases:
    ks = np.arange(r, k_max + 1)
    cdf = [nb_cdf(int(k), r, p) for k in ks]
    ax.step(ks, cdf, where="post", linewidth=2, label=label, marker="o", markersize=4)
ax.set_xlabel("k")
ax.set_ylabel("F(k) = P(X ≤ k)")
ax.set_title("Negative binomial CDF — varying r and p")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_r_p_varied.png", dpi=160)
plt.close(fig)

# Compare r=1 vs r=3 at same p
p = 0.35
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for r, ax in zip([1, 3], axes):
    ks = np.arange(r, 25)
    pmf = [nb_pmf(int(k), r, p) for k in ks]
    ax.stem(ks, pmf, linefmt="-", markerfmt="o", basefmt=" ")
    ax.set_title(f"r={r}, p={p}")
    ax.set_xlabel("k")
    ax.set_ylabel("P(X = k)")
    ax.grid(True, alpha=0.3)
fig.suptitle("Negative binomial vs geometric (r=1) at p=0.35", fontsize=11)
fig.tight_layout()
fig.savefig(HERE / "nb_vs_geometric.png", dpi=160)
plt.close(fig)

print("Saved negative binomial plots to", HERE)
