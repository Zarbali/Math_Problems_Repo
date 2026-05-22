"""Generate PMF/CDF comparison plots for Solution 03 — Binomial."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

HERE = Path(__file__).resolve().parent


def plot_pmf_compare(cases, title, filename, xlabel="k"):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for label, n, p in cases:
        k = np.arange(0, n + 1)
        pmf = binom.pmf(k, n, p)
        ax.stem(k, pmf, linefmt="-", markerfmt="o", basefmt=" ", label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("P(X = k)")
    ax.set_title(title)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(HERE / filename, dpi=160)
    plt.close(fig)


def plot_cdf_compare(cases, title, filename, xlabel="k"):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for label, n, p in cases:
        k = np.arange(0, n + 1)
        cdf = binom.cdf(k, n, p)
        ax.step(k, cdf, where="post", linewidth=2, label=label, marker="o", markersize=4)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("F(k) = P(X ≤ k)")
    ax.set_title(title)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(HERE / filename, dpi=160)
    plt.close(fig)


fixed_n = [("n=10, p=0.2", 10, 0.2), ("n=10, p=0.5", 10, 0.5), ("n=10, p=0.8", 10, 0.8)]
fixed_p = [("n=5, p=0.5", 5, 0.5), ("n=10, p=0.5", 10, 0.5), ("n=20, p=0.5", 20, 0.5)]

plot_pmf_compare(fixed_n, "Binomial PMF — fixed n=10, varying p", "pmf_fixed_n.png")
plot_pmf_compare(fixed_p, "Binomial PMF — fixed p=0.5, varying n", "pmf_fixed_p.png")
plot_cdf_compare(fixed_n, "Binomial CDF — fixed n=10, varying p", "cdf_fixed_n.png")
plot_cdf_compare(fixed_p, "Binomial CDF — fixed p=0.5, varying n", "cdf_fixed_p.png")
print("Saved binomial plots to", HERE)
