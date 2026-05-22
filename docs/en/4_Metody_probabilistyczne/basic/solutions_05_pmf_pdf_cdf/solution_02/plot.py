"""Generate PMF and CDF plots for Solution 02 (Discrete CDF given as a table)."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent

# Given CDF at support points; PMF recovered by jump rule
xs = np.array([-1, 0, 2, 4, 6], dtype=float)
cdf_vals = np.array([0.15, 0.35, 0.60, 0.85, 1.00], dtype=float)
cdf_prev = np.concatenate(([0.0], cdf_vals[:-1]))
ps = cdf_vals - cdf_prev
assert np.isclose(ps.sum(), 1.0), "PMF must sum to 1"

# ---------- PMF (stem / lollipop) ----------
fig, ax = plt.subplots(figsize=(7.5, 4.5))
markerline, stemlines, baseline = ax.stem(
    xs, ps, linefmt="C0-", markerfmt="C0o", basefmt=" "
)
plt.setp(markerline, markersize=8)
plt.setp(stemlines, linewidth=2)

for x, p in zip(xs, ps):
    ax.annotate(
        f"{p:.2f}",
        xy=(x, p),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        color="C0",
    )

ax.set_xlabel("x")
ax.set_ylabel("P(X = x)")
ax.set_title("PMF of X (reconstructed from CDF jumps)")
ax.set_xticks(xs)
ax.set_ylim(0, max(ps) * 1.25)
ax.set_xlim(xs.min() - 1, xs.max() + 1)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "pmf.png", dpi=160)
plt.close(fig)

# ---------- CDF (right-continuous step) ----------
fig, ax = plt.subplots(figsize=(7.5, 4.5))

x_left = xs.min() - 1.5
x_right = xs.max() + 1.5

ax.hlines(0.0, x_left, xs[0], colors="C3", linewidth=2)
for i, x in enumerate(xs):
    x_next = xs[i + 1] if i + 1 < len(xs) else x_right
    ax.hlines(cdf_vals[i], x, x_next, colors="C3", linewidth=2)

ax.plot(xs, cdf_vals, "o", color="C3", markersize=7, label="value at jump (closed)")
ax.plot(xs, cdf_prev, "o", mfc="white", mec="C3", markersize=7, label="open from below")

for x, y in zip(xs, cdf_vals):
    ax.annotate(
        f"F({int(x)}) = {y:.2f}",
        xy=(x, y),
        xytext=(8, -14),
        textcoords="offset points",
        fontsize=9,
        color="C3",
    )

ax.axhline(0.0, color="gray", linewidth=0.7)
ax.axhline(1.0, color="gray", linewidth=0.7, linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("F(x) = P(X ≤ x)")
ax.set_title("CDF of X (right-continuous step function)")
ax.set_xticks(xs)
ax.set_ylim(-0.05, 1.1)
ax.set_xlim(x_left, x_right)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
fig.savefig(HERE / "cdf.png", dpi=160)
plt.close(fig)

print("Saved:", HERE / "pmf.png")
print("Saved:", HERE / "cdf.png")
