---
title: "Part III — Algorithm Analysis"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "2.1"
---

# Part III — Algorithm Analysis

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section introduces fundamental tools for evaluating algorithm efficiency independently of specific hardware or environments.

After completing this section, learners will be able to:

- Explain why algorithm analysis is necessary;
- Identify appropriate **input size** parameters;
- Identify **basic operations** and count operation frequencies;
- Differentiate between **time complexity** and **auxiliary space complexity**;
- Distinguish between **best, average, and worst cases**;
- Compare common **growth rates**;
- Apply asymptotic notations: **Big-O ($O$)**, **Big-Omega ($\Omega$)**, and **Big-Theta ($\Theta$)**.

---

## 2. Input Size and Basic Operations

| Problem | Input Size Parameter | Basic Operation |
|---|---|---|
| Array / List | Number of elements $n$ | Element comparison / assignment |
| Graph | Vertices $V$ and Edges $E$ | Edge traversal |
| Matrix | Rows $r$ and Columns $c$ | Multiplication / addition |

---

## 3. Best, Average, and Worst Cases

- **Worst Case:** Upper bound on running time over all inputs of size $n$.
- **Best Case:** Lower bound on running time over all inputs of size $n$.
- **Average Case:** Expected running time under a assumed probability distribution over inputs.

---

## 4. Growth Rates Comparison

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$
