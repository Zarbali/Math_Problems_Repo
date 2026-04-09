# Task List 04 — Algebra of Events and Conditional Probability

> **Note:** This task list is still being developed. For now, please don’t work on it yet. :)

## Introduction

Probability theory does not only study numerical values of probabilities. It also studies the **structure of events** and the relations between them.

Before computing probabilities, one must understand:

* what an event is,
* how events can be combined,
* how to describe events using set operations,
* how probabilities behave under union, intersection, and complement,
* how additional information changes probability.

This task list develops two closely connected topics:

* **algebra of events**,
* **conditional probability**.

The main goal is to learn how to move fluently between:

* verbal descriptions of events,
* set-theoretic notation,
* probability formulas,
* and concrete probabilistic models.

# Theoretical Background

## Random Experiment, Sample Space, and Events

A **random experiment** is a process whose outcome cannot be predicted with certainty in advance.

The **sample space**, denoted by

$$
\Omega
$$

is the set of all possible elementary outcomes of the experiment.

An **elementary event** is a one-element subset of the sample space.

An **event** is any subset of the sample space.

Thus, if

$$
A \subseteq \Omega
$$

then $A$ is an event.

---

## Event as a Set

In probability theory, events are treated as sets. Therefore, operations on events are the same as operations on sets.

If $A$ and $B$ are events, then we can form:

* the union,
* the intersection,
* the complement,
* the difference.

This set-theoretic point of view is the foundation of the algebra of events.

---

## Union of Events

The union of two events $A$ and $B$ is the event that at least one of them occurs.

It is denoted by

$$
A \cup B
$$

and means:

* $A$ occurs,
* or $B$ occurs,
* or both occur.

---

## Intersection of Events

The intersection of two events $A$ and $B$ is the event that both occur.

It is denoted by

$$
A \cap B
$$

---

## Complement of an Event

The complement of an event $A$ is the event that $A$ does not occur.

It is denoted by

$$
A^c
$$

or sometimes by

$$
\Omega \setminus A
$$

depending on notation.

---

## Difference of Events

The difference

$$
A \setminus B
$$

is the event that $A$ occurs but $B$ does not.

---

## Mutually Exclusive Events

Two events $A$ and $B$ are **mutually exclusive** if they cannot occur together.

This means

$$
A \cap B = \varnothing
$$

Such events are also called **disjoint**.

---

## Certain Event and Impossible Event

The **certain event** is the whole sample space:

$$
\Omega
$$

The **impossible event** is the empty set:

$$
\varnothing
$$

Their probabilities satisfy

$$
P(\Omega)=1
$$

and

$$
P(\varnothing)=0
$$

---

## Basic Properties of Probability

A probability measure assigns to each event $A$ a number

$$
P(A)
$$

such that:

$$
0 \le P(A) \le 1
$$

$$
P(\Omega)=1
$$

and for mutually exclusive events,

$$
P(A \cup B)=P(A)+P(B)
$$

More generally, if $A_1,A_2,\dots,A_n$ are pairwise disjoint, then

$$
P(A_1 \cup A_2 \cup \dots \cup A_n)=P(A_1)+P(A_2)+\dots+P(A_n)
$$

---

## Complement Rule

For every event $A$,

$$
P(A^c)=1-P(A)
$$

This is one of the most frequently used identities in elementary probability.

---

## Inclusion–Exclusion Formula

For any two events $A$ and $B$,

$$
P(A \cup B)=P(A)+P(B)-P(A \cap B)
$$

This formula corrects for double counting.

---

## Conditional Probability

Often the probability of an event changes when we know that another event has already occurred.

The **conditional probability** of $A$ given $B$ is denoted by

$$
P(A \mid B)
$$

and is defined by

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

provided that

$$
P(B)>0
$$

---

## Multiplication Rule

From the definition of conditional probability, we obtain

$$
P(A \cap B)=P(B)P(A \mid B)
$$

and equivalently

$$
P(A \cap B)=P(A)P(B \mid A)
$$

This rule is fundamental in multi-stage random experiments.

---

## Independence of Events

Two events $A$ and $B$ are **independent** if the occurrence of one does not affect the probability of the other.

Mathematically, this means

$$
P(A \cap B)=P(A)P(B)
$$

If $P(B)>0$, then this is equivalent to

$$
P(A \mid B)=P(A)
$$

It is important to distinguish **independence** from **mutual exclusivity**:

* mutually exclusive events cannot occur together,
* independent events do not influence each other probabilistically.

---

## Law of Total Probability

Suppose that events

$$
B_1,B_2,\dots,B_n
$$

form a partition of the sample space, that is:

* they are pairwise disjoint,
* their union is the whole sample space.

Then for any event $A$,

$$
P(A)=\sum_{i=1}^{n} P(A \mid B_i)P(B_i)
$$

This formula is especially useful when a problem naturally splits into cases.

---

## Bayes’ Formula

If

$$
B_1,B_2,\dots,B_n
$$

form a partition of the sample space and $P(A)>0$, then

$$
P(B_k \mid A)=\frac{P(A \mid B_k)P(B_k)}{\sum_{i=1}^{n} P(A \mid B_i)P(B_i)}
$$

Bayes’ formula allows us to reverse conditional information.

---

## How to Read Event Statements Correctly

In many exercises, the main difficulty is not the computation itself, but translating words into event notation.

Examples:

* “at least one” often suggests a complement,
* “exactly one” requires separating cases,
* “both” means intersection,
* “at least one of” suggests union,
* “given that” signals conditional probability.

The ability to move between verbal and symbolic language is one of the core aims of this list.

# Task 01 – Basic Event Notation and Set Operations

For each random experiment below:

1. define the sample space,
2. define the events described in words,
3. write the corresponding unions, intersections, complements, and differences.

### Experiments

1. One toss of a coin.
2. One roll of a fair die.
3. Two tosses of a coin.
4. Drawing one card from a standard deck.

### Event descriptions

Use event notation for statements such as:

* the result is heads,
* the result is not tails,
* the die shows an even number,
* the die shows a number greater than 3,
* at least one head occurs in two tosses,
* both tosses give the same result,
* the drawn card is a heart,
* the drawn card is a face card.

---

# Task 02 – Algebra of Events in a Finite Sample Space

Consider the experiment of rolling a fair die once.

Let

$$
A = {2,4,6}
$$

be the event “the result is even”, and let

$$
B = {2,3,5}
$$

be the event “the result is prime”.

1. Compute:

   * $A \cup B$
   * $A \cap B$
   * $A^c$
   * $B^c$
   * $A \setminus B$
   * $B \setminus A$

2. Decide whether $A$ and $B$ are mutually exclusive.

3. Decide whether one of the events is a subset of the other.

4. Interpret each of the above events verbally.

---

# Task 03 – Event Algebra for Two Coin Tosses

Consider the experiment of tossing a fair coin twice.

Let

$$
A = \text{“at least one head occurs”}
$$

and

$$
B = \text{“both tosses give the same result”}
$$

1. Write the sample space explicitly.

2. Describe the events $A$ and $B$ as subsets of the sample space.

3. Determine:

   * $A \cup B$
   * $A \cap B$
   * $A^c$
   * $B^c$
   * $A \setminus B$
   * $B \setminus A$

4. Decide whether $A$ and $B$ are mutually exclusive.

5. Decide whether $A$ and $B$ are independent.

---

# Task 04 – Basic Probability Properties

Use only standard probability rules to solve the following.

1. If

$$
P(A)=0.35
$$

find

$$
P(A^c)
$$

2. If

$$
P(A)=0.4, \qquad P(B)=0.5, \qquad P(A \cap B)=0.2
$$

compute

$$
P(A \cup B)
$$

3. If $A$ and $B$ are mutually exclusive and

$$
P(A)=0.18, \qquad P(B)=0.27
$$

compute

$$
P(A \cup B)
$$

4. If

$$
P(A \cup B)=0.9, \qquad P(A)=0.6, \qquad P(B)=0.5
$$

compute

$$
P(A \cap B)
$$

5. Can two events satisfy simultaneously:

   * they are mutually exclusive,
   * they are independent,
   * both have positive probability?

Justify your answer.

---

# Task 05 – Event Algebra in Card and Urn Problems

Solve the following problems by first describing the relevant events using set notation.

1. One card is drawn from a standard deck.
   Define events:

   * $A$ — the card is a heart,
   * $B$ — the card is a king.

   Then describe:

   * $A \cup B$,
   * $A \cap B$,
   * $A^c$,
   * $B \setminus A$.

2. One ball is drawn from an urn containing:

   * 5 red balls,
   * 3 blue balls,
   * 2 green balls.

   Define events:

   * $A$ — the ball is red,
   * $B$ — the ball is not green.

   Then compute the probabilities of:

   * $A$,
   * $B$,
   * $A \cap B$,
   * $A \cup B$.

3. A class contains 12 girls and 15 boys. A 3-person delegation is selected uniformly at random.
   Define the event:

   * $A$ — at least one girl is selected.

   Express $A$ using a complement event and compute its probability.

---

# Task 06 – Conditional Probability: Definition and Direct Computation

For each problem:

1. define events $A$ and $B$,
2. compute $P(A)$, $P(B)$, and $P(A \cap B)$,
3. then compute

$$
P(A \mid B)
$$

1. From the numbers 1, 2, 3, 4, 5, two numbers are drawn successively without replacement. Let:

   * $A$ — the product of the drawn numbers is greater than 10,
   * $B$ — the first number drawn is odd.

2. One card is drawn from a standard deck. Let:

   * $A$ — the card is a face card,
   * $B$ — the card is a spade.

3. Two cards are drawn from a standard deck. Let:

   * $A$ — at least one card is greater than 9,
   * $B$ — neither card is a diamond.

---

# Task 07 – Conditional Probability in Dice, Cards, and Selection Problems

Solve the following problems.

1. Two fair dice are rolled. What is the probability that the sum is 6, given that at least one die shows a prime number?
2. From a group of 4 men and 3 women, 2 people are chosen at random. What is the probability that both chosen people are women?
3. A card is drawn from a standard deck. What is the probability that it is a face card, given that it is black?
4. Two cards are drawn without replacement. What is the probability that both are aces, given that at least one is an ace?

---

# Task 08 – Multiplication Rule and Multi-Stage Experiments

Use the multiplication rule

$$
P(A \cap B)=P(B)P(A \mid B)
$$

or its equivalent form to solve the following.

1. An urn contains 6 white and 4 black balls. Two balls are drawn without replacement. What is the probability that:

   * the first is white,
   * the second is black?

2. A box contains 5 defective and 15 non-defective components. Three components are drawn without replacement. What is the probability that exactly the first two are defective and the third is non-defective?

3. A family has two children. Assume that each child is equally likely to be a boy or a girl, independently of the other. What is the probability that both are girls, given that the older child is a girl?

4. A machine produces parts, each defective with probability 0.03, independently of others. What is the probability that among the next three parts:

   * the first two are good,
   * the third is defective?

---

# Task 09 – Independence of Events

For each pair of events below, decide whether they are independent.

1. One roll of a die:

   * $A$ — the result is even,
   * $B$ — the result is greater than 3.

2. Two tosses of a coin:

   * $A$ — the first toss is heads,
   * $B$ — exactly one head occurs.

3. One card drawn from a standard deck:

   * $A$ — the card is a heart,
   * $B$ — the card is a king.

4. Two cards drawn without replacement:

   * $A$ — the first card is an ace,
   * $B$ — the second card is an ace.

5. Can two nonempty mutually exclusive events be independent? Explain.

---

# Task 10 – Law of Total Probability

In each problem, split the sample space into natural cases and use the law of total probability.

1. A factory has two production lines.

   * Line I produces 60% of all parts and has defect probability 0.02.
   * Line II produces 40% of all parts and has defect probability 0.05.

   What is the probability that a randomly chosen part is defective?

2. A student answers a multiple-choice question.

   * With probability 0.7 the student knows the answer and chooses correctly.
   * Otherwise the student guesses among 4 options.

   What is the probability that the answer is correct?

3. An urn is chosen at random:

   * Urn A contains 3 red and 2 blue balls,
   * Urn B contains 1 red and 4 blue balls.

   One ball is then drawn from the chosen urn.
   What is the probability that the ball is red?

---

# Task 11 – Bayes’ Formula

Use Bayes’ formula to solve the following problems.

1. In the factory problem from Task 10, compute the probability that a defective part came from Line II.

2. In the student-answering problem from Task 10, compute the probability that the student actually knew the answer, given that the answer was correct.

3. In the urn problem from Task 10, compute the probability that Urn A was chosen, given that the drawn ball is red.

4. A medical test is used in a population where 2% of people have a disease.

   * The test is positive with probability 0.95 for a diseased person.
   * The test is positive with probability 0.04 for a healthy person.

   What is the probability that a person actually has the disease, given that the test result is positive?

---

# Task 12 – Interpreting Conditional Information

For each statement below:

1. rewrite it using event notation,
2. explain whether it refers to:

   * intersection,
   * union,
   * complement,
   * conditional probability,
   * or independence.

Statements:

1. At least one of the two events occurs.
2. Both events occur.
3. Event $A$ occurs but event $B$ does not.
4. Event $A$ occurs, given that event $B$ has occurred.
5. The occurrence of event $B$ does not change the probability of event $A$.
6. Neither $A$ nor $B$ occurs.
7. Exactly one of the two events occurs.

---

# Task 13 – Mixed Problems: Algebra of Events and Conditional Probability

Solve the following comprehensive problems.

1. A fair die is rolled twice.
   Let:

   * $A$ — the sum is greater than 8,
   * $B$ — at least one roll is even.

   Compute:

   * $P(A)$,
   * $P(B)$,
   * $P(A \cap B)$,
   * $P(A \cup B)$,
   * $P(A \mid B)$.

2. Three cards are drawn without replacement from a standard deck.
   Let:

   * $A$ — at least one card is a heart,
   * $B$ — exactly one card is a face card.

   Describe both events carefully and compute:

   * $P(A)$,
   * $P(B)$,
   * $P(A \cap B)$,
   * $P(A \mid B)$.

3. A box contains 5 red, 4 blue, and 3 green balls. Two balls are drawn without replacement.
   Let:

   * $A$ — the two balls have the same color,
   * $B$ — at least one ball is red.

   Compute:

   * $P(A)$,
   * $P(B)$,
   * $P(A \cap B)$,
   * $P(A \mid B)$.

---

# Task 14 – Optional Interactive Exploration

Design a minimal interactive HTML/JavaScript tool illustrating the ideas of this list.

The webpage should allow the user to choose a simple random experiment, for example:

* one die roll,
* two coin tosses,
* drawing one card,
* drawing two balls from an urn.

The program should then:

1. display the sample space,
2. allow the user to define events,
3. display unions, intersections, and complements visually,
4. compute probabilities of the chosen events,
5. allow the user to specify a conditioning event,
6. display the conditional sample space and the value of conditional probability.

The visual style should be minimal and focused on clarity.
