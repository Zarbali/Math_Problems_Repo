# Task 10 — Events and Probabilities in Buffon's Needle Experiment

This task continues from **Task 5**, where we defined the sample space
for the Buffon's needle experiment.

---

## Setup and probability formula

As established in Task 5, each throw of the needle is completely
described by two parameters:

- $x \in [0,\, d/2]$ — distance from the center of the needle to the nearest line
- $\theta \in [0,\, \pi/2]$ — angle between the needle and the parallel lines

Both $x$ and $\theta$ are **independent** and **uniformly distributed**
over their respective ranges.

The sample space is the rectangle:

$$\Omega = \left[0,\, \frac{d}{2}\right] \times \left[0,\, \frac{\pi}{2}\right]$$

Its area is:

$$\text{Area}(\Omega) = \frac{d}{2} \cdot \frac{\pi}{2} = \frac{d\pi}{4}$$

Because $x$ and $\theta$ are uniformly distributed and independent,
every region of $\Omega$ is equally likely per unit area.
This means I can calculate the probability of any event $R \subseteq \Omega$
using the **geometric probability formula**:

$$P(R) = \frac{\text{Area}(R)}{\text{Area}(\Omega)} = \frac{4}{d\pi} \cdot \text{Area}(R)$$

This is the continuous analogue of the classical formula from the
previous tasks. Instead of counting outcomes I measure area,
because the sample space is continuous.

---

## The intersection condition

Before computing any probabilities, I need to know exactly when
the needle crosses a line.

The needle has length $L$. Its center is at distance $x$ from the
nearest line, and it makes angle $\theta$ with the lines.

The vertical reach of the needle — the component perpendicular to
the lines — is $\frac{L}{2}\sin\theta$ on each side of the center.

The needle crosses the nearest line when its vertical reach is at
least $x$, meaning:

$$x \leq \frac{L}{2}\sin\theta$$

This condition is the key to the whole task. Every crossing event
below is based on this inequality.

We assume $L \leq d$, which means the needle is short enough that
it can cross at most one line at a time.

---

## Event A — needle intersects a line

$$A = \left\{(x,\theta) : 0 \leq x \leq \frac{L}{2}\sin\theta,\; 0 \leq \theta \leq \frac{\pi}{2}\right\}$$

For each fixed angle $\theta$, the values of $x$ that cause a crossing
run from $0$ to $\frac{L}{2}\sin\theta$. So the area of $A$ is found
by integrating over all angles:

$$\text{Area}(A) = \int_0^{\pi/2} \frac{L}{2}\sin\theta\; d\theta$$

Computing the integral:

$$= \frac{L}{2}\left[-\cos\theta\right]_0^{\pi/2}
= \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos 0\right)
= \frac{L}{2}(0 + 1) = \frac{L}{2}$$

Therefore:

$$P(A) = \frac{L/2}{d\pi/4} = \frac{2L}{\pi d}$$

This is the **classical Buffon's needle formula**. It is remarkable
because $\pi$ appears naturally from the geometry of the problem —
and this is exactly what the Monte Carlo simulation from Task 5
exploits to estimate $\pi$.

---

## Event B — needle does not intersect any line

$B$ is simply the complement of $A$:

$$B = \Omega \setminus A$$

I use the complement rule because $A$ and $B$ together cover all
possible outcomes and cannot both occur at the same time:

$$P(B) = 1 - P(A) = 1 - \frac{2L}{\pi d}$$

---

## Event C — angle is less than $\frac{\pi}{6}$

$$C = \left\{(x,\theta) : 0 \leq x \leq \frac{d}{2},\; 0 \leq \theta < \frac{\pi}{6}\right\}$$

There is no constraint on $x$ here — only the angle is restricted.
So $C$ is a rectangle with width $\frac{d}{2}$ and height $\frac{\pi}{6}$:

$$\text{Area}(C) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(C) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

This makes sense: the angle $\theta$ is uniformly distributed over
$[0, \pi/2]$, and the interval $[0, \pi/6]$ covers exactly one third
of that range. So the probability is one third regardless of $d$.

---

## Event D — center is within $\frac{d}{4}$ of the nearest line

$$D = \left\{(x,\theta) : 0 \leq x < \frac{d}{4},\; 0 \leq \theta \leq \frac{\pi}{2}\right\}$$

There is no constraint on $\theta$ here — only the position is restricted.
So $D$ is a rectangle with width $\frac{d}{4}$ and height $\frac{\pi}{2}$:

$$\text{Area}(D) = \frac{d}{4} \cdot \frac{\pi}{2} = \frac{d\pi}{8}$$

$$P(D) = \frac{d\pi/8}{d\pi/4} = \frac{1}{2}$$

Again this makes sense: $x$ is uniformly distributed over $[0, d/2]$,
and the interval $[0, d/4]$ covers exactly half of that range.

---

## Event E — needle crosses a line and angle is greater than $\frac{\pi}{4}$

This event combines the crossing condition from Event A with an
additional constraint on the angle:

$$E = \left\{(x,\theta) : 0 \leq x \leq \frac{L}{2}\sin\theta,\;
\frac{\pi}{4} < \theta \leq \frac{\pi}{2}\right\}$$

The region is the same shape as in Event A, but the integral now
starts at $\frac{\pi}{4}$ instead of $0$:

$$\text{Area}(E) = \int_{\pi/4}^{\pi/2} \frac{L}{2}\sin\theta\; d\theta
= \frac{L}{2}\left[-\cos\theta\right]_{\pi/4}^{\pi/2}$$

$$= \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos\frac{\pi}{4}\right)
= \frac{L}{2}\left(0 + \frac{\sqrt{2}}{2}\right) = \frac{L\sqrt{2}}{4}$$

$$P(E) = \frac{L\sqrt{2}/4}{d\pi/4} = \frac{L\sqrt{2}}{d\pi}$$

Note: $\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ because $\frac{\pi}{4}$
is 45 degrees, and at 45 degrees both sine and cosine equal
$\frac{\sqrt{2}}{2}$.

---

## Additional event F — angle is at least $\frac{\pi}{3}$

Let $F$ be the event that the needle makes an angle of at least
60 degrees with the parallel lines.

$$F = \left\{(x,\theta) : 0 \leq x \leq \frac{d}{2},\;
\frac{\pi}{3} \leq \theta \leq \frac{\pi}{2}\right\}$$

No constraint on $x$, so this is again a rectangle.
The height of the angle range is:

$$\frac{\pi}{2} - \frac{\pi}{3} = \frac{3\pi}{6} - \frac{2\pi}{6} = \frac{\pi}{6}$$

$$\text{Area}(F) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(F) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

Interesting to compare with Event C: both C and F give probability
one third. Event C restricts the angle to the lower third of the
range $[0, \pi/2]$, and Event F restricts it to the upper third.
The probabilities are equal because $\theta$ is uniformly distributed —
equal-length intervals always give equal probabilities.