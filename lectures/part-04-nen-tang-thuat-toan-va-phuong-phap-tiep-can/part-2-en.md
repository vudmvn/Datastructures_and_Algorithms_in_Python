# Part II — Algorithmic Approaches

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section introduces fundamental approaches to describe, design, and organize algorithm execution. The goal is not to view all algorithms as completely separated classes, but to understand that iteration, recursion, Divide and Conquer, sequential execution, and parallel execution belong to different perspectives.

After this section, learners will be able to:

- explain what an iterative algorithm is;
- explain what a recursive algorithm is;
- distinguish between base case and recursive case;
- compare iteration and recursion on the same problem;
- explain the Divide and Conquer paradigm;
- distinguish recursion from Divide and Conquer;
- understand the roles of sequential execution and parallel execution at an introductory level;
- recognize when a problem can be divided into independent subproblems.

---

## 2. Overview of Algorithmic Approaches

Commonly encountered terms such as:

- iterative;
- recursive;
- Divide and Conquer;
- sequential;
- parallel;

do not lie on the same classification criterion.

It can be broadly understood as follows:

| Concept | Essence |
|---|---|
| Iteration | Looping technique using loops |
| Recursion | Technique of solving a problem by calling itself |
| Divide and Conquer | Algorithm design paradigm |
| Sequential execution | Sequential execution model |
| Parallel execution | Concurrent execution model |

Therefore, an algorithm can be both recursive and Divide and Conquer, while being executed sequentially or in parallel depending on implementation.

---

## 3. Iterative Algorithms

An **iterative algorithm** uses loops to repeat a sequence of operations until a termination condition is reached.

Common loop structures include:

- `for`;
- `while`;
- nested loops.

Example of calculating factorial:

```python
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
```

Algorithmic idea:

1. initialize `result = 1`;
2. sequentially multiply by numbers from `1` to `n`;
3. return the result.

With input `n`, the loop runs `n` times.

Therefore:

```text
Time complexity: Θ(n)
Auxiliary space: Θ(1)
```

Iteration is usually suitable when:

- the processing can be described naturally by a loop;
- there is no need to divide the problem into subproblems;
- one wants to avoid call stack overhead;
- direct control over state across loop iterations is required.

---

## 4. Recursive Algorithms

A **recursive algorithm** solves a problem by calling itself on a smaller subproblem.

A recursive algorithm typically requires two components:

1. **Base case**: base condition, making no further recursive calls.
2. **Recursive case**: function call on a smaller input.

Example of calculating factorial:

```python
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)
```

Function call process with `n = 4`:

```text
factorial_recursive(4)
    ↓
4 × factorial_recursive(3)
    ↓
4 × 3 × factorial_recursive(2)
    ↓
4 × 3 × 2 × factorial_recursive(1)
    ↓
4 × 3 × 2 × 1
```

Recurrence:

```text
T(n) = T(n - 1) + Θ(1)
```

Therefore:

```text
Time complexity: Θ(n)
Auxiliary space: Θ(n)
```

Auxiliary space increases because the call stack stores the state of pending function calls.

---

## 5. Base Case and Recursive Case

### 5.1. Base Case

The base case is the termination condition of a recursive algorithm.

Example:

```python
if n <= 1:
    return 1
```

Without an appropriate base case, the algorithm may continue to call itself until causing stack overflow or recursion depth exceeded error.

### 5.2. Recursive Case

The recursive case is the step that transforms the current problem into a smaller subproblem.

Example:

```python
return n * factorial_recursive(n - 1)
```

The input decreases from `n` to `n - 1`.

A correct recursive algorithm must guarantee that after a finite number of steps, execution always progresses toward the base case.

---

## 6. Iteration and Recursion

Iteration and recursion can be used to solve the same problem.

### Example: Factorial

#### Iterative version

```python
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
```

#### Recursive version

```python
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)
```

Comparison:

| Criterion | Iterative | Recursive |
|---|---|---|
| Mechanism | Loop | Function calls |
| Termination condition | Loop condition | Base case |
| Call stack | Does not grow with `n` in this example | Grows with `n` |
| Time complexity | `Θ(n)` | `Θ(n)` |
| Auxiliary space | `Θ(1)` | `Θ(n)` |
| Tree/Decomposition expressiveness | Usually less intuitive | Usually more natural |

Key point:

> **Two algorithms may have the same time complexity but different space complexity.**

One should not assume that recursion is always better than iteration or vice versa. The choice depends on:

- problem structure;
- clarity of the solution;
- stack limits;
- function call overhead;
- language optimization capabilities.

---

## 7. Divide and Conquer

**Divide and Conquer** is an algorithmic paradigm in which a large problem is divided into smaller subproblems, the subproblems are solved, and then the results are combined to form the solution to the original problem.

Three basic steps:

1. **Divide**: divide the problem into subproblems.
2. **Conquer**: solve the subproblems.
3. **Combine**: combine the results.

Can be described as:

```text
Original problem
      ↓
Divide into smaller subproblems
      ↓
Solve subproblems
      ↓
Combine partial solutions
      ↓
Final solution
```

Typical examples:

- Binary Search;
- Merge Sort;
- Quick Sort;
- Karatsuba multiplication;
- Closest pair of points.

---

## 8. Recursion Is Not the Same as Divide and Conquer

Recursion and Divide and Conquer are related but not identical.

Factorial:

```text
factorial(n) = n × factorial(n - 1)
```

is recursive because the function calls itself.

However, it does not divide the problem into multiple independent subproblems.

In contrast, Merge Sort:

```text
Divide array into two halves
        ↓
Sort left half recursively
        ↓
Sort right half recursively
        ↓
Merge two sorted halves
```

Recurrence:

```text
T(n) = 2T(n / 2) + Θ(n)
```

This is a classic example of Divide and Conquer.

Key point to remember:

> **A Divide and Conquer algorithm often uses recursion, but a recursive algorithm is not necessarily Divide and Conquer.**

---

## 9. Example: Binary Search

Binary Search is applied on sorted data.

Each step:

1. select the middle element;
2. compare with target;
3. discard the half that cannot contain target;
4. continue on the remaining half.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Search space reduces according to the sequence:

```text
n → n/2 → n/4 → n/8 → ...
```

Therefore:

```text
Time complexity: Θ(log n)
```

Binary Search illustrates a form of Divide and Conquer in which only one subproblem is further processed after each step.

---

## 10. Example: Merge Sort

Merge Sort operates in three steps:

1. divide the array into two halves;
2. recursively sort each half;
3. merge the two sorted halves.

Structure:

```text
Array of size n
      ↓
Two arrays of size n/2
      ↓
Sort both recursively
      ↓
Merge in linear time
```

Recurrence:

```text
T(n) = 2T(n / 2) + Θ(n)
```

Result:

```text
T(n) = Θ(n log n)
```

Merge Sort is an important example because it directly connects:

- recursion;
- Divide and Conquer;
- recurrence relations;
- Master Theorem.

---

## 11. Sequential Execution Model

In **sequential execution**, steps are performed one after another in a specified order.

```text
Step 1 → Step 2 → Step 3 → Step 4
```

Example:

```python
def sequential_example(arr):
    total = sum(arr)
    maximum = max(arr)
    average = total / len(arr)

    return total, maximum, average
```

In this implementation:

1. compute sum;
2. find maximum;
3. compute average.

The steps are executed in order.

Sequential execution is the most common model in basic programs and is the foundation for introductory algorithm analysis.

---

## 12. Parallel Execution Model

In **parallel execution**, multiple tasks can be performed concurrently if they are independent or can be coordinated.

Visual example:

```text
           ┌── Task A ──┐
Input ─────┼── Task B ──┼────→ Combine
           └── Task C ──┘
```

Example of computing the sum of a large array:

1. divide the array into multiple blocks;
2. compute the sum of each block concurrently;
3. sum the local totals.

Common concepts:

- number of processors;
- work;
- span;
- synchronization;
- communication cost;
- speedup;
- scalability.

Parallel execution does not guarantee a faster program in all cases. It is necessary to consider:

- task division overhead;
- synchronization cost;
- data communication cost;
- degree of independence between tasks.

In an introductory DSA course, this section should only be viewed as an introduction for learners to understand that algorithm design and execution models are two distinct issues.

---

## 13. Sequential vs Parallel Execution

| Criterion | Sequential | Parallel |
|---|---|---|
| Number of tasks executed concurrently | One | Possibly multiple |
| Model simplicity | Yes | Usually more complex |
| Synchronization | Minimal | May be required |
| Communication overhead | Usually negligible | Can be significant |
| Speedup capability | Limited by a single execution thread | Can leverage multiple processors |

Not all problems parallelize well.

Some problems have strong dependencies between steps, so the degree of parallelism is limited.

---

## 14. Summary

- Iteration uses loops.
- Recursion uses self-calls.
- Recursive algorithm needs a base case and a recursive case.
- Iteration and recursion may have the same time complexity but different auxiliary space.
- Divide and Conquer consists of Divide, Conquer, and Combine.
- Recursion is not synonymous with Divide and Conquer.
- Binary Search and Merge Sort are two classic examples.
- Sequential and Parallel are execution models, not the same classification category as recursion or Divide and Conquer.
- Parallel execution can achieve speedup but comes with overhead and synchronization costs.
