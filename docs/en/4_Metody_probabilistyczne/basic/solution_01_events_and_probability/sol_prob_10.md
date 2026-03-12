# Task 10 — Events and Probabilities in Buffon's Needle Experiment

This task continues from **Task 5**, where the sample space for the Buffon's needle experiment was defined.

---

## Setup and probability formula

In Task 5 we showed that each throw of the needle is completely described by two parameters:

- $x \in [0, d/2]$ — distance from the center of the needle to the nearest line
- $\theta \in [0, \pi/2]$ — angle between the needle and the parallel lines

Both variables are **independent** and **uniformly distributed**.

The sample space is therefore

$$\Omega = [0, d/2] \times [0, \pi/2]$$

This is a rectangle. Its area equals

$$\mathrm{Area}(\Omega) = \frac{d}{2} \cdot \frac{\pi}{2} = \frac{d\pi}{4}$$

Because the variables are uniformly distributed, the probability of a region $R \subseteq \Omega$ is

$$P(R) = \frac{\mathrm{Area}(R)}{\mathrm{Area}(\Omega)} = \frac{4}{d\pi} \cdot \mathrm{Area}(R)$$

This is called **geometric probability**.

---

## The intersection condition

The needle has length $L$. Its center is at distance $x$ from the nearest line and the needle forms angle $\theta$ with the lines.

The vertical reach of half the needle is $\frac{L}{2}\sin\theta$.

The needle crosses a line if $x \leq \frac{L}{2}\sin\theta$.

We assume $L \le d$ so the needle can intersect **at most one line**.

---

## Event A — needle intersects a line

$$A = \{(x,\theta) : 0 \le x \le \frac{L}{2}\sin\theta,\; 0 \le \theta \le \frac{\pi}{2} \}$$

For each fixed $\theta$, the possible values of $x$ range from $0$ to $\frac{L}{2}\sin\theta$. So the area of region $A$ is

$$\mathrm{Area}(A) = \int_0^{\pi/2} \frac{L}{2}\sin\theta\, d\theta$$

Compute the integral:

$$\mathrm{Area}(A) = \frac{L}{2}\bigl[-\cos\theta\bigr]_0^{\pi/2} = \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos 0\right) = \frac{L}{2}(0 + 1) = \frac{L}{2}$$

Therefore

$$P(A) = \frac{\mathrm{Area}(A)}{\mathrm{Area}(\Omega)} = \frac{L/2}{d\pi/4} = \frac{2L}{\pi d}$$

This is the **classical Buffon's needle formula**.

---

## Event B — needle does not intersect a line

Event $B$ is the complement of $A$: $B = \Omega \setminus A$.

$$P(B) = 1 - P(A) = 1 - \frac{2L}{\pi d}$$

---

## Event C — angle less than $\frac{\pi}{6}$

$$C = \{(x,\theta) : 0 \le x \le \frac{d}{2},\; 0 \le \theta < \frac{\pi}{6} \}$$

This region is a rectangle.

$$\mathrm{Area}(C) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(C) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

The angle interval $[0,\pi/6]$ is exactly one third of $[0,\pi/2]$.

---

## Event D — center within $\frac{d}{4}$ of the nearest line

$$D = \{(x,\theta) : 0 \le x < \frac{d}{4},\; 0 \le \theta \le \frac{\pi}{2} \}$$

$$\mathrm{Area}(D) = \frac{d}{4} \cdot \frac{\pi}{2} = \frac{d\pi}{8}$$

$$P(D) = \frac{d\pi/8}{d\pi/4} = \frac{1}{2}$$

---

## Event E — needle crosses a line and angle greater than $\frac{\pi}{4}$

$$E = \{(x,\theta) : 0 \le x \le \frac{L}{2}\sin\theta,\; \frac{\pi}{4} < \theta \le \frac{\pi}{2} \}$$

$$\mathrm{Area}(E) = \int_{\pi/4}^{\pi/2} \frac{L}{2}\sin\theta\, d\theta = \frac{L}{2}\bigl[-\cos\theta\bigr]_{\pi/4}^{\pi/2} = \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos\frac{\pi}{4}\right) = \frac{L}{2}\left(0 + \frac{\sqrt{2}}{2}\right) = \frac{L\sqrt{2}}{4}$$

$$P(E) = \frac{L\sqrt{2}/4}{d\pi/4} = \frac{L\sqrt{2}}{d\pi}$$

---

## Additional event F — angle at least $\frac{\pi}{3}$

Let $F$ be the event that the needle makes an angle of at least **60 degrees** with the parallel lines.

$$F = \{(x,\theta) : 0 \le x \le \frac{d}{2},\; \frac{\pi}{3} \le \theta \le \frac{\pi}{2} \}$$

Height of the interval: $\frac{\pi}{2} - \frac{\pi}{3} = \frac{\pi}{6}$.

$$\mathrm{Area}(F) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(F) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

Events $C$ and $F$ have the same probability because $\theta$ is uniformly distributed.
