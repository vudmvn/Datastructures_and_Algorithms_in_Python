---
title: "Part IV — Analysis of Recursive Algorithms"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "2.1"
---

# Part IV — Analysis of Recursive Algorithms

**Last updated:** August 03, 2026

## 1. Learning Objectives

Many recursive algorithms cannot be directly analyzed by counting loops. Instead, the running time is often described by a recurrence relation.

After this section, learners should be able to:

- establish a recurrence relation from the structure of a recursive algorithm;
- solve recurrences using expansion/iteration;
- use recursion trees to observe costs at each level;
- use the substitution method to prove bounds;
- apply the Master Theorem to standard recurrences;
- recognize cases where the Master Theorem cannot be directly applied.

---

## 2. Recurrence Relations

A **recurrence relation** describes the cost of a problem of size `n` in terms of the cost of one or more smaller subproblems.

Examples:

### Factorial

```text
T(n) = T(n - 1) + Θ(1)
```

### Binary Search

```text
T(n) = T(n / 2) + Θ(1)
```

### Merge Sort

```text
T(n) = 2T(n / 2) + Θ(n)
```

A recurrence consists of two components:

1. the cost of the recursive calls;
2. the cost outside the recursion.

The goal is to determine the growth rate of `T(n)`.

---

## 3. From Recursive Algorithm to Recurrence

Example: Recursive Binary Search

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search_recursive(
            arr,
            target,
            mid + 1,
            right
        )

    return binary_search_recursive(
        arr,
        target,
        left,
        mid - 1
    )
```

At each step:

- we continue on only one half;
- we perform a constant amount of work outside the recursion.

Thus:

```text
T(n) = T(n / 2) + Θ(1)
```

---

## 4. Expansion / Iteration Method

The expansion method repeatedly substitutes the recurrence into itself to discover a pattern.

Consider:

```text
T(n) = 2T(n / 2) + n
```

Expand once:

```text
T(n)
= 2[2T(n / 4) + n / 2] + n
= 4T(n / 4) + 2n
```

Expand again:

```text
T(n)
= 8T(n / 8) + 3n
```

After `k` steps:

```text
T(n)
= 2^k T(n / 2^k) + kn
```

Stop when:

```text
n / 2^k = 1
```

Which implies:

```text
k = log2(n)
```

Therefore:

```text
T(n)
= nT(1) + n log2(n)
= Θ(n log n)
```

The expansion method is suitable when the recurrence has a structure that is easy to expand and a clear pattern emerges.

---

## 5. Recursion Tree

A recursion tree represents each recursive call as a node in a tree.

Consider:

```text
T(n) = 2T(n / 2) + n
```

Cost per level:

```text
Level 0: n
Level 1: n/2 + n/2 = n
Level 2: 4 × n/4 = n
...
```

Number of levels:

```text
log2(n)
```

Each level has a total cost of `n`.

Therefore:

```text
T(n) = Θ(n log n)
```

Recursion trees are useful to:

- observe the number of subproblems;
- see the size of subproblems at each level;
- compute the total cost per level;
- guess a solution before proving it.

---

## 6. Substitution Method

The substitution method generally involves four steps:

1. guess a bound;
2. assume the bound holds for subproblems;
3. substitute the hypothesis into the recurrence;
4. prove it by mathematical induction.

Consider:

```text
T(n) = 2T(n / 2) + n
```

Guess:

```text
T(n) = O(n log n)
```

Assume:

```text
T(n / 2) ≤ c × (n / 2) × log(n / 2)
```

Then:

```text
T(n)
≤ 2 × c × (n / 2) × log(n / 2) + n
```

Which gives:

```text
T(n)
≤ cn(log n - 1) + n
```

Or:

```text
T(n)
≤ cn log n - (c - 1)n
```

If `c ≥ 1`:

```text
T(n) ≤ cn log n
```

Therefore:

```text
T(n) = O(n log n)
```

To conclude `Θ(n log n)`, a lower bound is also needed.

---

## 7. Master Theorem

The Master Theorem applies to recurrences of the form:

```text
T(n) = aT(n / b) + f(n)
```

Where:

- `a`: number of subproblems;
- `n / b`: size of each subproblem;
- `f(n)`: cost outside the recursion.

The quantity to compare with is:

```text
n^(log_b a)
```

The idea is to determine which component dominates the total cost:

- recursive work;
- non-recursive work;
- or the two components are balanced.

---

## 8. Master Theorem — Case 1

If there exists `ε > 0` such that:

```text
f(n) = O(n^(log_b a - ε))
```

then:

```text
T(n) = Θ(n^(log_b a))
```

The recursive work dominates.

### Example

```text
T(n) = 8T(n / 2) + n²
```

We have:

```text
n^(log_2 8) = n³
```

Since `n²` is polynomially smaller than `n³`:

```text
T(n) = Θ(n³)
```

---

## 9. Master Theorem — Case 2

If:

```text
f(n) = Θ(n^(log_b a) × log^k n)
```

for `k ≥ 0`, then:

```text
T(n)
= Θ(n^(log_b a) × log^(k + 1) n)
```

### Example: Merge Sort

```text
T(n) = 2T(n / 2) + n
```

We have:

```text
n^(log_2 2) = n
```

The two components are balanced.

Therefore:

```text
T(n) = Θ(n log n)
```

---

## 10. Master Theorem — Case 3

If there exists `ε > 0` such that:

```text
f(n) = Ω(n^(log_b a + ε))
```

and it satisfies the regularity condition:

```text
a × f(n / b) ≤ c × f(n)
```

for some constant `c < 1`, then:

```text
T(n) = Θ(f(n))
```

### Example

```text
T(n) = 2T(n / 2) + n²
```

We have:

```text
n^(log_2 2) = n
```

While:

```text
f(n) = n²
```

Therefore:

```text
T(n) = Θ(n²)
```

---

## 11. Extended Form for `n^k log^p n`

Consider:

```text
T(n)
= aT(n / b)
+ Θ(n^k × log^p n)
```

Compare `a` with `b^k`.

### If `a > b^k`

```text
T(n) = Θ(n^(log_b a))
```

### If `a = b^k` and `p > -1`

```text
T(n) = Θ(n^k × log^(p + 1) n)
```

### If `a = b^k` and `p = -1`

```text
T(n) = Θ(n^k × log log n)
```

### If `a = b^k` and `p < -1`

```text
T(n) = Θ(n^k)
```

### If `a < b^k`

In common cases, the non-recursive work dominates; you need to check the applicability condition to conclude a tight bound.

---

## 12. Workflow for Applying Master Theorem

When encountering:

```text
T(n) = aT(n / b) + f(n)
```

you can follow these four steps.

### Step 1. Identify Parameters

Identify:

```text
a, b, f(n)
```

### Step 2. Compute Critical Function

Compute:

```text
n^(log_b a)
```

### Step 3. Compare

Compare `f(n)` with `n^(log_b a)`.

### Step 4. Conclude

Choose the appropriate case and write the conclusion.

---

## 13. Representative Examples

| Recurrence | Result |
|---|---|
| `T(n) = 2T(n/2) + n` | `Θ(n log n)` |
| `T(n) = 4T(n/2) + n²` | `Θ(n² log n)` |
| `T(n) = 8T(n/2) + n²` | `Θ(n³)` |
| `T(n) = 2T(n/2) + n²` | `Θ(n²)` |
| `T(n) = 2T(n/2) + n log n` | `Θ(n log² n)` |
| `T(n) = 2T(n/2) + n/log n` | `Θ(n log log n)` |

---

## 14. When Master Theorem Does Not Apply Directly

The Master Theorem does not directly apply to all recurrences.

Common cases:

- the number of subproblems depends on `n`;
- subproblems have unequal sizes;
- the size is not of the form `n / b`;
- the recurrence is of the subtract-and-conquer form;
- `f(n)` does not satisfy the necessary conditions.

Examples:

```text
T(n) = T(n - 1) + n
```

```text
T(n) = T(n / 3) + T(2n / 3) + n
```

```text
T(n) = sqrt(n) × T(sqrt(n)) + n
```

In these cases, you can use:

- expansion;
- recursion tree;
- substitution;
- direct summation;
- change of variables;
- Akra–Bazzi theorem.

---

## 15. Example Outside Standard Master Theorem

Consider:

```text
T(n) = T(n - 1) + n
```

Expand:

```text
T(n)
= n + T(n - 1)
= n + (n - 1) + T(n - 2)
= ...
```

This yields:

```text
T(n)
= 1 + 2 + ... + n
= Θ(n²)
```

This example shows that a recurrence without the Master Theorem can still be solved using expansion.

---

## 16. Summary

- Recursive algorithms often lead to recurrence relations.
- The expansion method repeatedly expands the recurrence to find a pattern.
- A recursion tree helps to observe the cost by level.
- The substitution method is used to guess and prove bounds.
- The Master Theorem applies to the form `T(n) = aT(n/b) + f(n)`.
- The three cases of the Master Theorem depend on comparing `f(n)` with `n^(log_b a)`.
- Not all recurrences are suitable for the Master Theorem.
