---
title: "Lecture: Algorithm Analysis — Problem Set and Solutions"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "1.2"
---

# Lecture: Algorithm Analysis — Problem Set and Solutions

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section focuses on practicing complexity analysis through common problem patterns: solving recurrence relations, analyzing non-linear loops, analyzing recursive functions, applying the Master Theorem, substitution method, recursion trees, and comparing growth rates of functions.

After completing this section, learners will be able to:

- Solve recurrences of the form $T(n) = aT(n-b) + f(n)$ using substitution or applicable theorems;
- Analyze loops whose control variables increase via cumulative sums, geometric progressions, or square roots;
- Formulate recurrences from recursive source code;
- Recognize when the Master Theorem applies and when variable substitution or recursion trees are required;
- Distinguish upper, lower, and tight bounds;
- Compare growth rates of polynomial, exponential, factorial, and logarithmic functions.

---

## 2. Subtract-and-Conquer Recurrences and Substitution Method

### Problem 1. Recurrence $T(n) = 3T(n-1)$

**Problem Statement.** Determine the time complexity of the following recurrence relation:

```text
T(n) = 3T(n - 1), if n > 0
T(0) = 1
```

<details>
<summary><strong>Show Solution</strong></summary>

Expanding step by step:
$$T(n) = 3T(n-1) = 3^2 T(n-2) = 3^3 T(n-3) = \dots = 3^n T(0) = 3^n$$

Therefore:
$$T(n) = \Theta(3^n)$$

</details>

### Problem 2. Recurrence with Cancellation

**Problem Statement.** Determine the time complexity of:

```text
T(n) = 2T(n - 1) - 1, if n > 0
T(0) = 1
```

<details>
<summary><strong>Show Solution</strong></summary>

Expanding step by step:
$$T(n) = 2T(n-1) - 1 = 2(2T(n-2) - 1) - 1 = 2^2 T(n-2) - 2 - 1$$
$$T(n) = 2^n T(0) - (2^{n-1} + 2^{n-2} + \dots + 2 + 1)$$
Since $T(0) = 1$ and $\sum_{i=0}^{n-1} 2^i = 2^n - 1$:
$$T(n) = 2^n - (2^n - 1) = 1$$

Therefore:
$$T(n) = \Theta(1)$$

</details>

---

## 3. Non-Linear Loop Analysis

### Problem 3. Cumulative Sum Loop Variable

**Problem Statement.** Analyze the time complexity:

```python
def function(n):
    i = 1
    s = 1
    while s < n:
        i = i + 1
        s = s + i
    print("*")
```

<details>
<summary><strong>Show Solution</strong></summary>

After $k$ iterations, $s = \sum_{j=1}^k j = \frac{k(k+1)}{2}$.
The loop terminates when $s \ge n \implies \frac{k^2}{2} \approx n \implies k = \Theta(\sqrt{n})$.

Therefore:
$$T(n) = \Theta(\sqrt{n})$$

</details>

---

## 4. Master Theorem Practice

### Problem 4. Master Theorem Case 1

**Problem Statement.** Solve $T(n) = 8T(n/2) + n^2$.

<details>
<summary><strong>Show Solution</strong></summary>

Coefficients: $a = 8, b = 2, f(n) = n^2$.
Compute $n^{\log_b a} = n^{\log_2 8} = n^3$.
Since $f(n) = n^2 < n^3$, recursion dominates (Case 1).

Therefore:
$$T(n) = \Theta(n^3)$$

</details>

---

## 5. Summary and Takeaways

- Always test base cases and check for algebraic cancellation before jumping to exponential conclusions.
- Non-linear loop variables (e.g., $s = s + i$, $i = i \times 2$, $i = i^2$) alter loop iteration counts significantly.
- Master Theorem provides quick answers when conditions are met, but substitution and recursion trees handle arbitrary recurrences.
