---
title: "Lecture: Master Theorem, Recurrence Relations and Amortized Analysis"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "1.0"
---

# Lecture: Master Theorem, Recurrence Relations and Amortized Analysis

**Last updated:** August 03, 2026

## 1. Learning Objectives and Prerequisites

Many recursive algorithms cannot be analyzed simply by counting loop iterations. Their running time is often expressed by a **recurrence relation**, where the cost of a problem of size `n` is expressed in terms of the cost of one or more smaller subproblems.

After this lesson, learners will be able to:

- Formulate recurrence relations for recursive and divide-and-conquer algorithms;
- Apply the Master Theorem for recurrences of the form `T(n) = aT(n/b) + f(n)`;
- Use the extended form when `f(n) = Θ(n^k log^p n)`;
- Identify cases where the Master Theorem does not apply;
- Analyze subtract-and-conquer recurrences;
- Use the substitution method (guess and prove by mathematical induction);
- Distinguish amortized analysis from worst-case and average-case analysis.

Prerequisites include recursion, logarithms, asymptotic notation `O`, `Ω`, `Θ`, geometric series, recursion trees, and mathematical induction.

---

## 2. From Divide-and-Conquer Algorithms to Recurrence Relations

A divide-and-conquer algorithm typically consists of three steps:

1. **Divide:** Partition the original problem into smaller subproblems;
2. **Conquer:** Solve the subproblems recursively;
3. **Combine:** Merge the subproblem solutions to solve the original problem.

If a problem of size `n` is divided into `a` subproblems, each of size approximately `n/b`, and non-recursive work takes `f(n)`, the running time follows `T(n) = aT(n/b) + f(n)`.

Here, `a` is the number of subproblems, `n/b` is the size of each subproblem, and `f(n)` is the work done in dividing the problem and combining results.

### Example: Merge Sort

Merge Sort divides an array of size `n` into two halves, recursively sorts each half, and merges the sorted halves in linear time: `T(n) = 2T(n/2) + Θ(n)`, yielding `T(n) = Θ(n log n)`.

### Example: Binary Search

Binary Search proceeds on only one half of the array with constant work per step: `T(n) = T(n/2) + Θ(1)`, yielding `T(n) = Θ(log n)`.

---

## 3. Master Theorem for Divide-and-Conquer Recurrences

For recurrences `T(n) = aT(n/b) + f(n)` with `a ≥ 1`, `b > 1`, and non-negative `f(n)`:

Compare `f(n)` against `n^(log_b a)` (the work created by recursive branching).

### Case 1: Recursion Dominates

If there exists `ε > 0` such that `f(n) = O(n^(log_b a - ε))`, then `T(n) = Θ(n^(log_b a))`.

**Example:** For `T(n) = 8T(n/2) + n²`, we have `n^(log₂8) = n³`. Since `n²` is polynomially smaller than `n³`, `T(n) = Θ(n³)`.

### Case 2: Balanced Work

If `f(n) = Θ(n^(log_b a) log^k n)` for `k ≥ 0`, then `T(n) = Θ(n^(log_b a) log^(k+1) n)`.

**Example:** For `T(n) = 2T(n/2) + n`, `n^(log₂2) = n`. The components are balanced, so `T(n) = Θ(n log n)`.

### Case 3: Non-Recursive Work Dominates

If there exists `ε > 0` such that `f(n) = Ω(n^(log_b a + ε))` and the regularity condition `a f(n/b) ≤ c f(n)` holds for constant `c < 1`, then `T(n) = Θ(f(n))`.

**Example:** For `T(n) = 2T(n/2) + n²`, `n^(log₂2) = n`, while `f(n) = n²`. Regularity holds since `2(n/2)² = n²/2`. Thus `T(n) = Θ(n²)`.

---

## 4. Extended Master Theorem for `f(n) = Θ(n^k log^p n)`

For `T(n) = aT(n/b) + Θ(n^k log^p n)` with `a > 1`, `b > 1`, `k ≥ 0`, and real `p`:

Compare `a` with `b^k`:

### When `a > b^k`
Recursion dominates: `T(n) = Θ(n^(log_b a))`.

### When `a = b^k`
Balanced case, depending on `p`:
- If `p > -1`, `T(n) = Θ(n^k log^(p+1) n)`.
- If `p = -1`, `T(n) = Θ(n^k log log n)`.
- If `p < -1`, `T(n) = Θ(n^k)`.

### When `a < b^k`
If `p ≥ 0`, non-recursive work dominates: `T(n) = Θ(n^k log^p n)`.

| Condition | Result |
|---|---|
| `a > b^k` | `Θ(n^(log_b a))` |
| `a = b^k`, `p > -1` | `Θ(n^k log^(p+1) n)` |
| `a = b^k`, `p = -1` | `Θ(n^k log log n)` |
| `a = b^k`, `p < -1` | `Θ(n^k)` |
| `a < b^k`, `p ≥ 0` | `Θ(n^k log^p n)` |

---

## 5. Master Theorem Recurrence Examples

| No. | Recurrence | Result | Note |
|---|---|---|---|
| 1 | `T(n) = 3T(n/2) + n²` | `Θ(n²)` | Non-recursive work dominates |
| 2 | `T(n) = 4T(n/2) + n²` | `Θ(n² log n)` | Balanced case |
| 3 | `T(n) = T(n/2) + n²` | `Θ(n²)` | Non-recursive work dominates |
| 4 | `T(n) = 16T(n/4) + n` | `Θ(n²)` | Recursion dominates |
| 5 | `T(n) = 2T(n/2) + n log n` | `Θ(n log² n)` | Balanced with `p = 1` |
| 6 | `T(n) = 2T(n/2) + n/log n` | `Θ(n log log n)` | Boundary case `p = -1` |
| 7 | `T(n) = 3T(n/2) + n` | `Θ(n^(log₂3))` | Recursion dominates |

---

## 6. Subtract-and-Conquer Recurrences

For `T(n) = aT(n-b) + f(n)` with `a > 0`, `b > 0`, and `f(n) = O(n^k)`:

| Condition | Upper Bound |
|---|---|
| `a < 1` | `O(n^k)` |
| `a = 1` | `O(n^(k+1))` |
| `a > 1` | `O(n^k a^(n/b))` |

- `T(n) = T(n-1) + 1 \implies Θ(n)`
- `T(n) = T(n-1) + n \implies Θ(n²)`
- `T(n) = 2T(n-1) + 1 \implies Θ(2^n)`

---

## 7. Amortized Analysis

Amortized analysis computes the **average cost per operation over a sequence of operations** in the worst case, without assuming any probability distribution over inputs.

### Dynamic Array Example
For a dynamic array that doubles capacity when full:
- Most `append` operations cost `O(1)`.
- When full, copying elements costs `O(n)`.
- Total cost for `n` appends is `1 + 2 + 4 + ... < 2n = O(n)`.
- Amortized cost per operation is **$O(1)$**.

---

## 8. Quiz Questions & Answers

1. For `T(n) = 4T(n/2) + n²`, the result is:
   - **Answer: B. $\Theta(n^2 \log n)$**

2. For `T(n) = 2T(n/2) + n/log n`, the result is:
   - **Answer: C. $\Theta(n \log \log n)$**

3. Amortized analysis:
   - **Answer: B. Evaluates average cost over a sequence of operations in the worst case.**
