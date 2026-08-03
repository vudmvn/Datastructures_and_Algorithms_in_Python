---
title: "Part II — Algorithmic Approaches"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "2.1"
---

# Part II — Algorithmic Approaches

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section introduces fundamental approaches for describing, designing, and organizing algorithm execution.

After completing this section, learners will be able to:

- Explain what an **iterative algorithm** is;
- Explain what a **recursive algorithm** is;
- Distinguish between **base case** and **recursive case**;
- Compare iteration and recursion on the same problem;
- Explain the **Divide and Conquer** paradigm;
- Distinguish recursion from Divide and Conquer;
- Understand the roles of **sequential execution** and **parallel execution** at an introductory level.

---

## 2. Overview of Algorithmic Approaches

| Term | Essential Nature |
|---|---|
| Iteration | Loop-based execution technique (`for`, `while`) |
| Recursion | Self-referential problem solving technique |
| Divide and Conquer | High-level algorithm design paradigm |
| Sequential Execution | Step-by-step execution model |
| Parallel Execution | Simultaneous multi-core execution model |

---

## 3. Iterative Algorithms

An **iterative algorithm** uses loops to repeat a set of operations until a termination condition is met.

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
- **Time Complexity:** $\Theta(n)$
- **Auxiliary Space:** $\Theta(1)$

---

## 4. Recursive Algorithms

A **recursive algorithm** solves a problem by calling itself on smaller instances of the same problem.

```python
def factorial_recursive(n):
    if n <= 1: # Base case
        return 1
    return n * factorial_recursive(n - 1) # Recursive case
```
- **Time Complexity:** $\Theta(n)$
- **Auxiliary Space:** $\Theta(n)$ (due to call stack frames)

---

## 5. Divide and Conquer Paradigm

Divide and Conquer breaks down a problem into independent subproblems:

1. **Divide:** Split the problem into smaller subproblems.
2. **Conquer:** Solve subproblems recursively.
3. **Combine:** Merge subproblem solutions.

Example: **Merge Sort** ($T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$).

---

## 6. Sequential vs. Parallel Execution

- **Sequential:** Operations execute sequentially on a single thread.
- **Parallel:** Independent subproblems execute simultaneously on multiple processor cores.
