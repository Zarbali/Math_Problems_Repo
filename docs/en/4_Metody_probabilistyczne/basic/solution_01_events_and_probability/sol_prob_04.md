## Task 4 — Weekly Weather Observation

Experiment: observing the weather once per day for seven consecutive days.

Each day the weather can be classified into exactly one of three states:

- S — Sunny
- C — Cloudy
- R — Rainy

Note: I first noticed that each day has exactly three possible outcomes.  
This means the experiment is similar to previous tasks where we counted outcomes step by step.


## 1. Sample space Ω₁ (one day)

For one day the weather can only be in one of the three states.

| Outcome | Meaning |
|-------|-------|
| S | Sunny |
| C | Cloudy |
| R | Rainy |

So the sample space is

Ω₁ = {S, C, R}

Number of elementary outcomes:

|Ω₁| = 3

Note: at this point I just listed the possible states of weather for a single day.

Each outcome represents the weather observed on that day.

## 2. Sample space Ω₂ (two consecutive days)

Now we observe the weather for two days.

An outcome must describe the weather on both days, so we use ordered pairs.

Note: order matters because the first day and the second day are different days.

Examples:

| Day 1 | Day 2 | Outcome |
|------|------|------|
| S | S | SS |
| S | C | SC |
| S | R | SR |
| C | S | CS |
| C | C | CC |
| C | R | CR |
| R | S | RS |
| R | C | RC |
| R | R | RR |

So the sample space is

Ω₂ = {SS, SC, SR, CS, CC, CR, RS, RC, RR}

Number of outcomes:

|Ω₂| = 3 × 3 = 9

Note: I used the multiplication rule here —  
3 possible states on day 1 and 3 possible states on day 2.

## 3. Sample space Ω₇ (seven consecutive days)

Now we observe the weather during a whole week.

Each day still has 3 possible states.

So an outcome must describe the weather for all seven days.

That means each outcome is an ordered sequence of length 7.

Example outcome:

(S, C, R, R, S, C, S)

Meaning:
- Day 1: Sunny
- Day 2: Cloudy
- Day 3: Rainy
- Day 4: Rainy
- Day 5: Sunny
- Day 6: Cloudy
- Day 7: Sunny

Mathematically we can write

Ω₇ = {(w₁, w₂, … , w₇) : wᵢ ∈ {S, C, R}}

Note: each position corresponds to one day.

## 4. Number of elementary outcomes

Now we count the number of possible sequences.

Each day has 3 possible weather states.

So we multiply 3 by itself for each day.

| Sample space | Days observed | Outcomes |
|--------------|--------------|---------|
| Ω₁ | 1 | 3 |
| Ω₂ | 2 | 9 |
| Ω₇ | 7 | 2187 |

General rule:

|Ωₙ| = 3ⁿ

For seven days:

|Ω₇| = 3⁷ = 2187

Note: I used the multiplication rule again because each day adds another choice.


## 5. Meaning of an elementary outcome

An elementary outcome represents one complete weather sequence for the week.

Example:

(S, C, R, R, S, C, S)

This means:

Day 1 — Sunny  
Day 2 — Cloudy  
Day 3 — Rainy  
Day 4 — Rainy  
Day 5 — Sunny  
Day 6 — Cloudy  
Day 7 — Sunny  

Note: each elementary outcome describes exactly one possible weekly weather pattern.