"""Generate PMF/CDF comparison plots for Solution 06 — Hypergeometric."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom

HERE = Path(__file__).resolve().parent

# (label, N, K, n)  — population, successes in pop, sample size
cases = [
    ("N=30, K=10, n=5", 30, 10, 5),
    ("N=30, K=15, n=5", 30, 15, 5),
    ("N=30, K=10, n=10", 30, 10, 10),
]

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, N, K, n in cases:
    lo = max(0, n - (N - K))
    hi = min(n, K)
    k = np.arange(lo, hi + 1)
    pmf = hypergeom.pmf(k, N, K, n)
    ax.stem(k, pmf, linefmt="-", markerfmt="o", basefmt=" ", label=label)
ax.set_xlabel("k (distinguished objects in sample)")
ax.set_ylabel("P(X = k)")
ax.set_title("Hypergeometric PMF — parameter comparisons")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pmf_compare.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, N, K, n in cases:
    lo = max(0, n - (N - K))
    hi = min(n, K)
    k = np.arange(lo, hi + 1)
    cdf = hypergeom.cdf(k, N, K, n)
    ax.step(k, cdf, where="post", linewidth=2, label=label, marker="o", markersize=4)
ax.set_xlabel("k")
ax.set_ylabel("F(k) = P(X ≤ k)")
ax.set_title("Hypergeometric CDF — parameter comparisons")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_compare.png", dpi=160)
plt.close(fig)

# Binomial approximation overlay for N=30, K=10, n=5 vs Bin(5, 1/3)
from scipy.stats import binom

N, K, n = 30, 10, 5
p = K / N
lo, hi = max(0, n - (N - K)), min(n, K)
k = np.arange(lo, hi + 1)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.stem(k, hypergeom.pmf(k, N, K, n), linefmt="C0-", markerfmt="C0o", basefmt=" ", label="Hypergeom")
ax.stem(k + 0.15, binom.pmf(k, n, p), linefmt="C1-", markerfmt="C1o", basefmt=" ", label=f"Bin({n}, {p:.3f}) approx")
ax.set_xlabel("k")
ax.set_ylabel("P(X = k)")
ax.set_title("Hypergeometric vs Binomial approximation (N=30, K=10, n=5)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "hypergeom_vs_binomial.png", dpi=160)
plt.close(fig)
print("Saved hypergeometric plots to", HERE)
