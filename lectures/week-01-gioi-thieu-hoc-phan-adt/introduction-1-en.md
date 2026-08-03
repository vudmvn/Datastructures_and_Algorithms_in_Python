---
title: "Lecture: Introduction to Algorithms and Complexity Analysis"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "1.3"
---

# Lecture: Introduction to Algorithms and Complexity Analysis

**Last updated:** August 03, 2026

## 1. Objectives and Prerequisites

This lesson introduces foundational concepts before diving into data structures and algorithms. The goal is not only to understand how an algorithm works, but also how to **compare algorithms** and determine which is better suited as input size grows.

After this lesson, learners will be able to:

- Explain the relationship between **variables, data types, data structures, and abstract data types (ADTs)**.
- State the definition and core characteristics of an algorithm.
- Explain why algorithm analysis is necessary.
- Identify appropriate input sizes for different problems.
- Compare growth rates of common functions.
- Distinguish between **best case, average case, and worst case**.
- Correctly use asymptotic notations `O`, `Ω`, and `Θ`.
- Analyze simple code blocks containing loops, nested loops, sequential statements, conditions, and logarithmic loops.
- Apply basic logarithmic and summation formulas in complexity analysis.

Prerequisites:
- Variables, assignment, and expressions.
- Control flow: `if`, `for`, `while`.
- Functions and function calls.
- Basic arrays / lists.
- Introductory powers and logarithms.

---

## 2. From Variables and Data Types to Data Structures and ADTs

In mathematics, we write equations such as $x^2 + 2y - 2 = 1$. Here, $x$ and $y$ represent values. In programming, variables serve a similar purpose as placeholders for data.

```python
x = 10
y = 25
total = x + y
```

A variable name is not the data itself, but a mechanism to access and manipulate data. A variable's **data type** determines:
- The domain of representable values;
- Memory allocated;
- Valid operations.

```python
age = 20        # int
price = 19.95   # float
name = "Minh"   # str
is_valid = True # bool
```

### Abstract Data Types (ADTs) vs. Data Structures

An **Abstract Data Type (ADT)** is a mathematical model describing:
1. The collection of data objects managed;
2. The set of valid operations allowed on those objects;
3. Expected behavior of each operation.

An ADT specifies **what can be done**, not **how it is implemented**.

A **concrete data structure** defines how data is actually stored in memory and how operations are implemented.

> **ADT describes interface and behavior; data structure describes memory organization and implementation.**

Common ADTs and data structures:
- Array / Dynamic Array
- Linked List (Singly, Doubly, Circular)
- Stack, Queue, Deque
- Priority Queue / Heap
- Binary Tree / Binary Search Tree (BST)
- Hash Table / Map, Set
- Graph, Disjoint Set / Union-Find

<p align="center">
  <img src="images/image-5.png" alt="Data Structures Overview" width="800" />
</p>

---

## 3. What is an Algorithm?

An **algorithm** is a finite sequence of well-defined instructions designed to solve a specific problem or perform a computation.

```text
Input
  ↓
Algorithm Processing Steps
  ↓
Output
```

<p align="center">
  <img src="images/image-1.png" alt="Algorithm Processing Flow" width="800" />
</p>

### Algorithm vs. Program

| Aspect | Algorithm | Program |
|---|---|---|
| Nature | Abstract idea / problem-solving procedure | Concrete implementation of an algorithm |
| Language | Language independent | Written in Python, C++, Java, etc. |
| Detail Level | Focuses on logical steps | Includes syntax, data types, libraries, error handling |
| Goal | Describes solution | Executable by a computer |

---

## 4. Characteristics of a Good Algorithm

1. **Definiteness:** Each step must be clear and unambiguous.
2. **Input:** Zero or more well-defined inputs.
3. **Output:** At least one well-defined output.
4. **Finiteness:** Must terminate after a finite number of steps for any valid input.
5. **Effectiveness:** Every operation must be basic and feasible.
6. **Correctness:** Must produce correct results for all valid inputs.

---

## 5. Asymptotic Analysis and Growth Rates

Asymptotic analysis evaluates algorithm performance as input size $n \to \infty$.

### Common Growth Rates (from slowest to fastest):

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

<p align="center">
  <img src="images/image-4.png" alt="Growth Rates Comparison" width="800" />
</p>

### Asymptotic Notations:

- **Big-O ($O$):** Asymptotic Upper Bound ($f(n) \le c \cdot g(n)$).
- **Big-Omega ($\Omega$):** Asymptotic Lower Bound ($f(n) \ge c \cdot g(n)$).
- **Big-Theta ($\Theta$):** Asymptotic Tight Bound ($c_1 g(n) \le f(n) \le c_2 g(n)$).

<p align="center">
  <img src="images/image-1.png" alt="Big-O Upper Bound" width="800" />
</p>

<p align="center">
  <img src="images/image-2.png" alt="Big-Omega Lower Bound" width="800" />
</p>

<p align="center">
  <img src="images/image-3.png" alt="Big-Theta Tight Bound" width="800" />
</p>

---

## 6. Code Analysis Examples

### Single Loop: $O(n)$
```python
for i in range(n):
    print(i)
```

### Nested Loops: $O(n^2)$
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

### Logarithmic Loop: $O(\log n)$
```python
i = 1
while i < n:
    i *= 2
```

---

## 7. Quiz Questions

1. Which statement best describes an ADT?
   - **Answer: B. A model describing data and operations independent of implementation.**

2. For $T(n) = 5n^2 + 2n + 100$, the growth rate is:
   - **Answer: C. $\Theta(n^2)$**

3. A logarithmic loop `while i < n: i *= 2` has complexity:
   - **Answer: B. $\Theta(\log n)$**

---

## 8. Summary

- Variables store data; data types define values and valid operations.
- ADTs specify abstract operations; data structures define concrete memory layouts.
- Asymptotic analysis focuses on growth rates as input size $n \to \infty$.
- $O$ is upper bound, $\Omega$ is lower bound, $\Theta$ is tight bound.
