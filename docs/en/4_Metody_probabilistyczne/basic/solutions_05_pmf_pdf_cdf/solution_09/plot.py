"""Generate PDF/CDF plots for Solution 09 — Gamma and chi-square."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, gamma

HERE = Path(__file__).resolve().parent

x = np.linspace(0, 20, 500)
cases = [
    ("shape=1, scale=2 (Exp)", 1, 2),
    ("shape=2, scale=2", 2, 2),
    ("shape=5, scale=1", 5, 1),
]

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, k, scale in cases:
    ax.plot(x, gamma.pdf(x, a=k, scale=scale), linewidth=2, label=label)
ax.set_xlabel("x (waiting time)")
ax.set_ylabel("f(x)")
ax.set_title("Gamma PDF — varying shape and scale")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pdf_gamma_varied.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, k, scale in cases:
    ax.plot(x, gamma.cdf(x, a=k, scale=scale), linewidth=2, label=label)
ax.set_xlabel("x")
ax.set_ylabel("F(x)")
ax.set_title("Gamma CDF — corresponding choices")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_gamma_varied.png", dpi=160)
plt.close(fig)

# Chi-square as Gamma(k/2, scale=2): χ²_4 = Gamma(2, scale=2)
df = 4
x2 = np.linspace(0, 15, 400)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x2, chi2.pdf(x2, df), "b-", linewidth=2, label=f"χ²({df})")
ax.plot(x2, gamma.pdf(x2, a=df / 2, scale=2), "r--", linewidth=2,
        label=f"Gamma({df/2}, scale=2)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Chi-square as a special case of Gamma")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "gamma_vs_chi2.png", dpi=160)
plt.close(fig)

print("Saved gamma plots to", HERE)
