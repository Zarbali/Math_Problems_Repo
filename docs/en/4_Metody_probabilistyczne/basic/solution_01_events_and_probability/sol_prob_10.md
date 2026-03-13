# Task 10 — Events and Probabilities in Buffon's Needle Experiment

This task continues from **Task 5**, where the sample space for the Buffon's needle experiment was defined.

---

## Setup and probability formula

In Task 5 we showed that each throw of the needle is completely described by two parameters:

- $x \in [0, d/2]$ — distance from the center of the needle to the nearest line
- $\theta \in [0, \pi/2]$ — angle between the needle and the parallel lines

Both variables are **independent** and **uniformly distributed**.

The sample space is therefore the rectangle:

$$\Omega = [0, d/2] \times [0, \pi/2]$$

Its area equals:

$$\mathrm{Area}(\Omega) = \frac{d}{2} \cdot \frac{\pi}{2} = \frac{d\pi}{4}$$

Because the variables are uniformly distributed and independent, every point
in the rectangle is equally likely per unit area. The probability of any
region $R \subseteq \Omega$ is therefore:

$$P(R) = \frac{\mathrm{Area}(R)}{\mathrm{Area}(\Omega)} = \frac{4}{d\pi} \cdot \mathrm{Area}(R)$$

This is called **geometric probability** — it is the continuous analogue of
the classical formula from earlier tasks. Instead of counting discrete
outcomes, we measure area. The reason we can do this is precisely because
$x$ and $\theta$ are uniformly distributed — if they had any other
distribution, this formula would not apply.

---

## The intersection condition

Before looking at any event, I need to establish when the needle actually
crosses a line — because this condition appears in several events below.

The needle has length $L$. Its center sits at distance $x$ from the nearest
line, and the needle makes angle $\theta$ with the direction of the lines.

The perpendicular reach of half the needle — that is, how far the needle
extends in the direction toward the line — is $\frac{L}{2}\sin\theta$.

The needle reaches the line when this perpendicular reach is at least $x$:

$$x \leq \frac{L}{2}\sin\theta$$

We also assume $L \leq d$, which guarantees that the needle is short enough
to cross **at most one line** per throw. Without this assumption the problem
would be more complicated.

---

## Event A — needle intersects a line

$$A = \{(x,\theta) : 0 \leq x \leq \frac{L}{2}\sin\theta,\; 0 \leq \theta \leq \frac{\pi}{2}\}$$

The boundary of this region is the curve $x = \frac{L}{2}\sin\theta$,
which is not a straight line — so $A$ is not a rectangle. I cannot just
multiply width by height. Instead I have to integrate.

For each fixed $\theta$, the values of $x$ that fall inside $A$ run from
$0$ to $\frac{L}{2}\sin\theta$. So I integrate that length over all
possible angles:

$$\mathrm{Area}(A) = \int_0^{\pi/2} \frac{L}{2}\sin\theta\, d\theta$$

Computing the integral using the antiderivative of $\sin\theta$, which is $-\cos\theta$:

$$= \frac{L}{2}\bigl[-\cos\theta\bigr]_0^{\pi/2} = \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos 0\right) = \frac{L}{2}(0 + 1) = \frac{L}{2}$$

Therefore:

$$P(A) = \frac{\mathrm{Area}(A)}{\mathrm{Area}(\Omega)} = \frac{L/2}{d\pi/4} = \frac{2L}{\pi d}$$

This is the **classical Buffon's needle formula**. What makes it remarkable
is that $\pi$ appears from a purely geometric argument — no circle is
directly involved, yet $\pi$ emerges from the integral. This is exactly
what the Monte Carlo simulation in Task 5 exploits: by throwing the needle
many times and counting crossings, we can rearrange the formula to estimate
$\pi \approx \frac{2L}{d \cdot P(A)}$.

---

## Event B — needle does not intersect a line

$B$ is the complement of $A$:

$$B = \Omega \setminus A$$

I use the complement rule here because $A$ and $B$ are mutually exclusive
and together cover all of $\Omega$ — every throw either crosses a line or
it does not. So:

$$P(B) = 1 - P(A) = 1 - \frac{2L}{\pi d}$$

No new integration needed — the complement rule gives the answer directly.

---

## Event C — angle less than $\frac{\pi}{6}$

$$C = \{(x,\theta) : 0 \leq x \leq \frac{d}{2},\; 0 \leq \theta < \frac{\pi}{6}\}$$

There is no constraint on $x$ here — it runs freely over its full range.
Only the angle is restricted. This means the region is a rectangle, so I
can find its area by simple multiplication:

$$\mathrm{Area}(C) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(C) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

This result makes sense without any calculation: $\theta$ is uniformly
distributed over $[0, \pi/2]$, and the interval $[0, \pi/6]$ covers
exactly one third of that range. Equal-length intervals of a uniform
distribution always have equal probability.

---

## Event D — center within $\frac{d}{4}$ of the nearest line

$$D = \{(x,\theta) : 0 \leq x < \frac{d}{4},\; 0 \leq \theta \leq \frac{\pi}{2}\}$$

Here only $x$ is constrained — $\theta$ runs freely. Again a rectangle:

$$\mathrm{Area}(D) = \frac{d}{4} \cdot \frac{\pi}{2} = \frac{d\pi}{8}$$

$$P(D) = \frac{d\pi/8}{d\pi/4} = \frac{1}{2}$$

Same reasoning as Event C but applied to $x$: the variable $x$ is
uniformly distributed over $[0, d/2]$, and the interval $[0, d/4]$
covers exactly half of that range. So the probability is one half
regardless of the value of $\pi$ or $d$.

---

## Event E — needle crosses a line and angle greater than $\frac{\pi}{4}$

$$E = \{(x,\theta) : 0 \leq x \leq \frac{L}{2}\sin\theta,\; \frac{\pi}{4} < \theta \leq \frac{\pi}{2}\}$$

This event is the intersection of two conditions: the crossing condition
from Event A, and the additional requirement that $\theta > \pi/4$.
Geometrically, this is the same curved region as in Event A, but only
over the upper part of the angle range.

The area is computed by the same integral as in Event A, but with the
lower limit changed from $0$ to $\pi/4$:

$$\mathrm{Area}(E) = \int_{\pi/4}^{\pi/2} \frac{L}{2}\sin\theta\, d\theta = \frac{L}{2}\bigl[-\cos\theta\bigr]_{\pi/4}^{\pi/2}$$

Evaluating at the bounds:

$$= \frac{L}{2}\left(-\cos\frac{\pi}{2} + \cos\frac{\pi}{4}\right) = \frac{L}{2}\left(0 + \frac{\sqrt{2}}{2}\right) = \frac{L\sqrt{2}}{4}$$

Here I used $\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$, which follows from
the fact that at 45 degrees the adjacent and opposite sides of a right
triangle are equal, giving both sine and cosine the value $\frac{\sqrt{2}}{2}$.

$$P(E) = \frac{L\sqrt{2}/4}{d\pi/4} = \frac{L\sqrt{2}}{d\pi}$$

As a sanity check: $P(E) < P(A)$ since we are restricting to a smaller
angle range. Indeed $\frac{L\sqrt{2}}{d\pi} < \frac{2L}{\pi d}$ because
$\sqrt{2} < 2$. Confirmed.

---

## Additional event F — angle at least $\frac{\pi}{3}$

Let $F$ be the event that the needle makes an angle of at least
**60 degrees** with the parallel lines.

$$F = \{(x,\theta) : 0 \leq x \leq \frac{d}{2},\; \frac{\pi}{3} \leq \theta \leq \frac{\pi}{2}\}$$

No constraint on $x$, so this is a rectangle. The height of the angle
interval is:

$$\frac{\pi}{2} - \frac{\pi}{3} = \frac{3\pi}{6} - \frac{2\pi}{6} = \frac{\pi}{6}$$

$$\mathrm{Area}(F) = \frac{d}{2} \cdot \frac{\pi}{6} = \frac{d\pi}{12}$$

$$P(F) = \frac{d\pi/12}{d\pi/4} = \frac{1}{3}$$

It is worth comparing Events C and F. Both give probability $\frac{1}{3}$,
even though they describe different angle ranges — C covers the lower
third $[0, \pi/6]$ and F covers the upper third $[\pi/3, \pi/2]$.
Both intervals have the same length $\frac{\pi}{6}$, and since $\theta$
is uniformly distributed, equal-length intervals always carry equal
probability. The position of the interval within $[0, \pi/2]$ does
not matter.