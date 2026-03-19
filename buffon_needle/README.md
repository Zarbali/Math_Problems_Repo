# Buffon's Needle — Monte Carlo Simulation

## 1. What it is

Interactive simulation of the classical Buffon's needle experiment: a needle of length $L$ is thrown randomly onto a plane with parallel lines spaced $d$ apart.

## 2. The experiment

- **Parameters:** $L$ — needle length, $d$ — distance between lines (adjustable via sliders).
- **Condition:** $L \le d$ — the needle crosses at most one line.
- **Outcome:** the needle either crosses a line or it does not.

## 3. Probability of intersection

With uniform distribution of center and angle:

$$P(\text{intersection}) = \frac{2L}{\pi d}$$

## 4. Estimating $\pi$

From the formula:

$$\pi \approx \frac{2L}{d \cdot P}$$

where $P = \frac{\text{number of intersections}}{\text{number of throws}}$.

## 5. How to use

1. Open `index.html` in a browser.
2. **Throw Needle** — one throw.
3. **× 1000** — 1000 throws.
4. **Reset** — reset.
5. Sliders — adjust $L$ and $d$.

## 6. Result

- **Est. Probability P** — estimated probability of intersection.
- **Estimated π** — estimated $\pi$ from the formula above.
- **error** — relative error of the $\pi$ estimate.

More throws give a more accurate estimate of $\pi$.

---

# Oral explanation (~5 min)

## 1. What we do

We consider Buffon's experiment: a needle of length $L$ is thrown randomly onto a plane with parallel lines spaced $d$ apart. We count how many times the needle crosses a line.

## 2. What happens

The needle center is uniformly distributed over the plane; the angle is uniformly distributed from 0 to $\pi$. The needle crosses a line when the distance from its center to the nearest line is at most $(L/2)\sin\theta$.

## 3. Outcomes

Two outcomes: intersection or none. With $L \le d$, the needle crosses at most one line.

## 4. What we compute

Probability of intersection: $P = 2L/(\pi d)$. Hence $\pi \approx 2L/(d \cdot P)$. In the simulation, $P$ is estimated as the fraction of intersections among all throws.

## 5. What the result means

The estimate of $\pi$ converges to the true value as the number of throws increases. This is an example of geometric probability and the Monte Carlo method.
