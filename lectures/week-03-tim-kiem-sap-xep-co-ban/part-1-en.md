---
title: "Part I — Foundations of Algorithms and Data Structures"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "2.1"
---

# Part I — Foundations of Algorithms and Data Structures

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section provides foundational concepts before diving into specific data structures and algorithmic analysis techniques. The goal is not merely to memorize definitions, but to understand the relationship between problems, data, algorithms, programs, and data structures.

After this section, learners will be able to:

- Distinguish between **problem**, **input**, **output**, **algorithm**, and **program**;
- Explain what an algorithm is and state the core properties of a well-defined algorithm;
- Distinguish between **data type**, **data structure**, and **Abstract Data Type (ADT)**;
- Identify fundamental data structures and describe their typical use cases;
- Explain common operations on data structures such as access, search, insert, delete, update, and traverse;
- Explain the relationship between algorithms and data structures;
- Evaluate solutions based on three fundamental criteria: **correctness**, **efficiency**, and **scalability**.

---

## 2. Problems, Inputs, Outputs, Algorithms, and Programs

When solving a problem using a computer, we typically follow a sequence of logical steps:

```text
Problem
    ↓
Input and Output Specification
    ↓
Algorithm
    ↓
Data Structures
    ↓
Program
```

### 2.1. Problem
A **problem** is a task or question to be solved. For example:
> Given a list of integers and a `target` value, find the first index of `target` in the list. If `target` is not found, return `-1`.

### 2.2. Input
**Input** is the data supplied to the algorithm before processing begins.
```text
Input:
- n: positive integer (array length)
- A: array of n integers
- target: integer value to search for
```

### 2.3. Output
**Output** is the result produced after executing the algorithm.
```text
Output:
- first index i where A[i] == target; return -1 if target is absent.
```

### 2.4. Algorithm
An **algorithm** is a finite sequence of clear instructions to transform input into output.
```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
```

---

## 3. Data Types, Data Structures, and Abstract Data Types (ADTs)

- **Data Type:** Domain of values, memory representation, and allowed operations (e.g., `int`, `float`, `str`).
- **Abstract Data Type (ADT):** Logical specification of data organization and allowed operations (e.g., Stack ADT: `push`, `pop`, `peek`).
- **Data Structure:** Concrete physical implementation of an ADT in memory (e.g., Array-based Stack vs. Linked List-based Stack).

---

## 4. Fundamental Operations on Data Structures

1. **Access:** Retrieving an element at a given index or position.
2. **Search:** Finding the location of a target value.
3. **Insert:** Adding a new element.
4. **Delete:** Removing an existing element.
5. **Update:** Modifying an existing value.
6. **Traverse:** Visiting each element sequentially.

---

## 5. Evaluation Criteria for Solutions

1. **Correctness:** Does it produce valid output for all valid inputs?
2. **Efficiency:** How much time and memory does it consume?
3. **Scalability:** How well does it handle large-scale data ($n \to \infty$)?
