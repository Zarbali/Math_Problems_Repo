## Task 1 — Coin Tossing

Experiment: tossing a fair coin.

Important assumption: the order of outcomes matters.  
For example, HT and TH represent different results.


### Sample space Ω₁ (one toss)

For one coin toss there are two possible outcomes:

H — heads  
T — tails

$$
\Omega_1 = \{H, T\}
$$

Number of elementary outcomes:

$$
|\Omega_1| = 2
$$

Note: an elementary outcome represents the result of one single toss.


### Sample space Ω₂ (two tosses)

For two tosses we must consider ordered sequences of results.

Possible outcomes:

HH  
HT  
TH  
TT

$$
\Omega_2 = \{HH, HT, TH, TT\}
$$

Number of elementary outcomes:

$$
|\Omega_2| = 4
$$

Note: HT means heads on the first toss and tails on the second toss.


### Sample space Ω₃ (three tosses)

For three tosses we extend the same idea.

Each sequence from Ω₂ can be followed by H or T.

Possible sequences:

HHH  
HHT  
HTH  
HTT  
THH  
THT  
TTH  
TTT

$$
\Omega_3 =
\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

Number of elementary outcomes:

$$
|\Omega_3| = 8
$$

Observation: each additional coin toss doubles the number of possible outcomes.


### General rule

For n coin tosses the number of outcomes is

$$
|\Omega_n| = 2^n
$$

because each toss has two possible results.


### Meaning of an elementary outcome

An elementary outcome represents one complete possible result of the experiment.

For example:

HTH means  
first toss = heads  
second toss = tails  
third toss = heads