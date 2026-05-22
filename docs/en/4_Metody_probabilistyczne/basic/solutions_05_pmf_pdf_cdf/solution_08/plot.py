"""Generate PDF/CDF plots for Solution 08 — Beta."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

HERE = Path(__file__).resolve().parent

x = np.linspace(0, 1, 400)
cases = [
    ("α=2, β=2 (symmetric)", 2, 2),
    ("α=2, β=5 (left skew)", 2, 5),
    ("α=5, β=2 (right skew)", 5, 2),
    ("α=0.5, β=0.5 (U-shaped)", 0.5, 0.5),
]

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, a, b in cases:
    ax.plot(x, beta.pdf(x, a, b), linewidth=2, label=label)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Beta PDF — shape families on [0, 1]")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pdf_shapes.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, a, b in cases:
    ax.plot(x, beta.cdf(x, a, b), linewidth=2, label=label)
ax.set_xlabel("x")
ax.set_ylabel("F(x) = P(X ≤ x)")
ax.set_title("Beta CDF — corresponding parameter choices")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "cdf_shapes.png", dpi=160)
plt.close(fig)

# Interval shading example: Beta(2,5), P(0.1 ≤ X ≤ 0.4)
a, b = 2, 5
lo, hi = 0.1, 0.4
fig, ax = plt.subplots(figsize=(7, 4))
pdf = beta.pdf(x, a, b)
ax.plot(x, pdf, "b-", linewidth=2, label=f"Beta({a},{b})")
mask = (x >= lo) & (x <= hi)
ax.fill_between(x, pdf, where=mask, alpha=0.35, color="#2563eb",
                label=f"P({lo} ≤ X ≤ {hi}) = {beta.cdf(hi,a,b)-beta.cdf(lo,a,b):.4f}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Area under PDF = interval probability")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pdf_interval_shaded.png", dpi=160)
plt.close(fig)

print("Saved beta plots to", HERE)
