# Task 5 — Buffon's Needle Experiment

Experiment: a needle of length L is thrown randomly onto a floor with equally spaced parallel lines. The distance between neighboring lines is d.

Right away I noticed that this problem feels different from the previous ones. In earlier tasks we always had discrete outcomes — like flipping a coin, rolling a die, drawing cards, or observing weather states. In those cases we could list all outcomes.

Here the needle can land in many different positions and at many different angles, so we cannot list all outcomes anymore. That means the sample space will be continuous.

---

## 1. Sample Space Ω

The sample space Ω contains all possible outcomes of a single throw of the needle.

An outcome should describe exactly how the needle lands on the floor.

At first I asked myself what information is actually needed to describe the position of the needle completely. After thinking about it, I realized that two quantities are enough.

---

## 2. The Two Parameters

Two parameters fully determine the result of a throw:

| Parameter | Meaning |
|-----------|---------|
| x | Distance from the needle's center to the nearest parallel line |
| θ | Angle between the needle and the parallel lines |

Once we know where the center of the needle landed and how the needle is oriented, the entire configuration is determined.

---

## 3. What Each Parameter Means

### (a) Position — x

The variable x represents the distance from the center of the needle to the nearest parallel line.

Because the lines repeat every distance d, we only need to know the position within one strip between two neighboring lines.

By symmetry we can restrict the position to half of that strip:

x ∈ [0, d/2]

If x = 0, the center lies exactly on a line.

If x = d/2, the center lies exactly halfway between two lines.

---

### (b) Orientation — θ

The variable θ represents the angle between the needle and the direction of the parallel lines.

Because rotating the needle by 180 degrees produces the same physical configuration, we do not need to consider the full angle range.

Using symmetry we can restrict the angle to

θ ∈ [0, π/2]

If θ = 0, the needle is parallel to the lines.

If θ = π/2, the needle is perpendicular to the lines.

---

## 4. The Sample Space as a Set

Each elementary outcome can now be represented by a pair (x, θ).

So the sample space can be written as

Ω = { (x, θ) : x ∈ [0, d/2], θ ∈ [0, π/2] }

or equivalently

Ω = [0, d/2] × [0, π/2]

If we think about it geometrically, this sample space is simply a rectangle. Each point inside the rectangle corresponds to one possible position and orientation of the needle.

---

## 5. Why the Sample Space is Continuous

In the previous tasks the sample spaces were discrete.

Examples:

Coin toss → a small finite number of outcomes  
Die → a finite number of outcomes  
Cards → a finite number of outcomes  
Weather states → a finite number of outcomes

In this experiment the parameters x and θ can take infinitely many values.

For example x could be

0.1  
0.101  
0.10123  
0.10123456  
and so on.

The same is true for θ.

So the outcomes cannot be listed individually. Instead the sample space contains infinitely many possible values, which means it is continuous.

This also means that a single exact outcome like (x, θ) has probability zero. Instead probabilities are calculated for regions of the sample space rather than individual points.