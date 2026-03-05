# Problem 01 – Operations on Events

## Given

$\Omega = \{\omega_1, \omega_2, \omega_3, \omega_4, \omega_5\}$

This is the sample space of the experiment, so there are five possible elementary outcomes.

$A = \{\omega_1, \omega_3, \omega_5\}$

$B = \{\omega_2, \omega_3, \omega_4\}$

Need to find:

1. $A \cup B$  
2. $A \cap B$  
3. $B \setminus A$  
4. $A \setminus B$

## My approach

First I wrote $A$ and $B$ next to each other to see the overlap. $\omega_3$ is in both that's the intersection. I solve it first, then union, then the two differences. Venn diagram helps: two circles, $\omega_3$ in the middle.

Reminders:
- $\cup$ = **"or"** everything in $A$ or $B$
- $\cap$ = **"and"** only what's in both
- $B \setminus A$ = in $B$ but **not** in $A$ order matters I used to mix this up

## 1. $A \cap B$ 

Only elements in both sets. From $A$ and $B$, only $\omega_3$.

$$
A \cap B = \{\omega_3\}
$$

## 2. $A \cup B$

Take all from both sets, no duplicates

$A$: $\omega_1, \omega_3, \omega_5$  
$B$: $\omega_2, \omega_3, \omega_4$

$$
A \cup B = \{\omega_1, \omega_2, \omega_3, \omega_4, \omega_5\} = \Omega
$$

Whole sample space every outcome is in at least one event

## 3. $B \setminus A$

In $B$ but not in $A$. From $B = \{\omega_2, \omega_3, \omega_4\}$ remove $\omega_3$ (we already know it's in $A \cap B$).

$$
B \setminus A = \{\omega_2, \omega_4\}
$$

## 4. $A \setminus B$

In $A$ but not in $B$. From $A = \{\omega_1, \omega_3, \omega_5\}$ remove $\omega_3$.

$$
A \setminus B = \{\omega_1, \omega_5\}
$$

Note: $B \setminus A \neq A \setminus B$ different elements get removed

## Result (as in the task)

$$
A \cup B = \Omega, \quad A \cap B = \{\omega_3\}, \quad B \setminus A = \{\omega_2, \omega_4\}, \quad A \setminus B = \{\omega_1, \omega_5\}
$$

## Sanity check

All results are subsets of $\Omega$  no extra elements.

The three parts $(A \cap B)$, $(B \setminus A)$, $(A \setminus B)$ don't overlap and together give $A \cup B = \Omega$.