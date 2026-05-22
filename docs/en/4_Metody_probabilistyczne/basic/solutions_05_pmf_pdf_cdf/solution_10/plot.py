"""Generate PDF/CDF plots for Solution 10 — Normal."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

HERE = Path(__file__).resolve().parent

x = np.linspace(-8, 12, 600)

# Fixed sigma, varying mu
fig, ax = plt.subplots(figsize=(8, 4.5))
sigma = 1.0
for mu in [-2, 0, 2]:
    ax.plot(x, norm.pdf(x, mu, sigma), linewidth=2, label=f"μ={mu}, σ={sigma}")
ax.set_xlabel("x")
ax.set_ylabel("φ(x)")
ax.set_title("Normal PDF — fixed σ, varying μ")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pdf_fixed_sigma.png", dpi=160)
plt.close(fig)

# Fixed mu, varying sigma
fig, ax = plt.subplots(figsize=(8, 4.5))
mu = 0
for sigma in [0.5, 1.0, 2.0]:
    ax.plot(x, norm.pdf(x, mu, sigma), linewidth=2, label=f"μ={mu}, σ={sigma}")
ax.set_xlabel("x")
ax.set_ylabel("φ(x)")
ax.set_title("Normal PDF — fixed μ, varying σ")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pdf_fixed_mu.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for mu in [-2, 0, 2]:
    ax.plot(x, norm.cdf(x, mu, sigma), linewidth=2, label=f"μ={mu}, σ={sigma}")
ax.set_xlabel("x")
ax.set_ylabel("Φ(x)")
ax.set_title("Normal CDF — fixed σ, varying μ")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_fixed_sigma.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
mu = 0
for sigma in [0.5, 1.0, 2.0]:
    ax.plot(x, norm.cdf(x, mu, sigma), linewidth=2, label=f"μ={mu}, σ={sigma}")
ax.set_xlabel("x")
ax.set_ylabel("Φ(x)")
ax.set_title("Normal CDF — fixed μ, varying σ")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_fixed_mu.png", dpi=160)
plt.close(fig)

print("Saved normal plots to", HERE)
