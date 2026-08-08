# Part III — Algorithm Analysis

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section introduces basic tools to evaluate algorithm efficiency. The focus is not on measuring wall-clock seconds on a specific machine, but on studying how resource usage grows as input size increases.

After this section, learners can:

- explain why algorithm analysis is necessary;
- identify appropriate input size;
- identify basic operation and count the number of executions;
- distinguish between time complexity and auxiliary space complexity;
- distinguish best, average, and worst cases;
- compare growth rates;
- explain asymptotic analysis;
- correctly use Big-O, Big-Omega, and Big-Theta;
- analyze code snippets containing loops, conditional branches, and basic structures.

---

## 2. Why Analyze Algorithms?

Actual execution time can be measured by running the program. However, results depend on:

- CPU;
- RAM;
- operating system;
- programming language;
- compiler or interpreter;
- libraries;
- implementation details;
- specific data;
- other processes currently running.

Therefore, statement:

```text
Algorithm A takes 0.2 seconds.
```

is not sufficient to conclude A is better than B in all cases.

Algorithm analysis focuses on the question:

> **When input size increases, according to what rule do the required time and memory increase?**

The main goal is to evaluate:

- efficiency;
- scalability;
- comparability between algorithms.

---

## 3. Input Size

Before analyzing complexity, it is necessary to clearly define input size.

The notation `n` has no fixed meaning for every problem.

| Problem | Commonly used input size |
|---|---|
| Array | number of elements `n` |
| String | length `n` |
| Matrix | number of rows `r`, number of columns `c` |
| Graph | number of vertices `V`, number of edges `E` |
| Big integer | number of bits or number of digits |
| Polynomial | number of coefficients or degree |
| TSP | number of cities |

Example with graph:

```text
T(V, E) = Θ(V + E)
```

is usually clearer than:

```text
T(n) = Θ(n)
```

Choosing the wrong input size may lead to misleading complexity conclusions.

---

## 4. Basic Operations and Operation Counting

A fundamental way to analyze algorithms:

1. identify the basic operation;
2. count the number of times the operation is executed;
3. express that count in terms of input size.

Example:

```python
for i in range(n):
    print(i)
```

If each `print(i)` execution is considered to have a constant cost, the loop body runs `n` times.

We can write:

```text
T(n) = c1 × n + c2
```

Therefore:

```text
T(n) = Θ(n)
```

The key point is that there is no need to count every machine-level instruction precisely. We are primarily concerned with growth rate.

---

## 5. Time Complexity

**Time complexity** describes how execution time grows as input size increases.

Example:

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

If:

```text
n = len(arr)
```

then the loop runs `n` times.

Therefore:

```text
T(n) = Θ(n)
```

Time complexity is not necessarily actual wall-clock seconds. It describes growth rate mathematically.

---

## 6. Space and Auxiliary Space Complexity

**Space complexity** describes the amount of memory needed.

It is necessary to distinguish:

- **Input space**: memory used to store the input.
- **Auxiliary space**: additional memory besides the input.

Example:

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

The algorithm uses only a fixed number of extra variables.

Therefore:

```text
Auxiliary space = Θ(1)
```

Conversely, if the algorithm creates a new list with `n` elements:

```python
def copy_array(arr):
    result = []

    for x in arr:
        result.append(x)

    return result
```

then auxiliary space is:

```text
Θ(n)
```

---

## 7. Best, Average, and Worst Cases

Execution time may vary across inputs of the same size.

Consider Linear Search:

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

### 7.1. Best Case

Best case is the class of inputs that minimizes the cost.

If target is at the first position:

```text
T_best(n) = Θ(1)
```

### 7.2. Worst Case

Worst case is the class of inputs that maximizes the cost.

If target:

- is at the last position;
- or does not exist;

then:

```text
T_worst(n) = Θ(n)
```

### 7.3. Average Case

Average-case analysis considers expected cost under a specified distribution.

Suppose target is guaranteed to exist and is equally likely at each position.

Average number of comparisons:

```text
(1 + 2 + ... + n) / n
= (n + 1) / 2
= Θ(n)
```

Average-case analysis cannot be precisely determined without specifying a probability model.

---

## 8. Growth Rates

Common growth rates:

| Complexity | Name | Example |
|---|---|---|
| `Θ(1)` | Constant | array indexing |
| `Θ(log n)` | Logarithmic | binary search |
| `Θ(n)` | Linear | linear scan |
| `Θ(n log n)` | Linearithmic | merge sort |
| `Θ(n²)` | Quadratic | considering all pairs |
| `Θ(n³)` | Cubic | three independent loops |
| `Θ(2^n)` | Exponential | iterating all subsets |
| `Θ(n!)` | Factorial | iterating all permutations |

Typical ordering:

```text
1 < log n < n < n log n < n² < n³ < 2^n < n!
```

The larger the growth rate, the harder it is for the algorithm to scale as input grows.

---

## 9. Why Growth Rate Matters

Suppose the same machine can perform about:

```text
100,000,000 operations per second
```

A `Θ(n)` algorithm can handle very large inputs.

A `Θ(n²)` algorithm quickly becomes slow.

A `Θ(2^n)` algorithm may become infeasible even when `n` is only a few dozen.

Therefore:

> **Complexity is a tool to evaluate scalability.**

---

## 10. Asymptotic Analysis

Asymptotic analysis studies the behavior of the cost function as input size becomes very large.

We usually:

- drop constant factors;
- drop lower-order terms;
- keep the dominant term.

Example:

```text
T(n) = 5n² + 100n + 200
```

When `n` is large, `n²` dominates.

Therefore:

```text
T(n) = Θ(n²)
```

Another example:

```text
T(n) = 100n log n + n
```

yields:

```text
T(n) = Θ(n log n)
```

---

## 11. Big-O Notation

Big-O describes an asymptotic upper bound.

We say:

```text
f(n) = O(g(n))
```

if there exist constants:

```text
c > 0
n0 > 0
```

such that for all `n ≥ n0`:

```text
0 ≤ f(n) ≤ c × g(n)
```

### Example

Consider:

```text
f(n) = 3n + 8
```

For `n ≥ 8`:

```text
3n + 8 ≤ 4n
```

Therefore:

```text
3n + 8 = O(n)
```

A function can have multiple upper bounds:

```text
3n + 8 = O(n)
3n + 8 = O(n²)
3n + 8 = O(n³)
```

But `O(n)` is a tighter bound.

---

## 12. Big-Omega Notation

Big-Omega describes an asymptotic lower bound.

We say:

```text
f(n) = Ω(g(n))
```

if there exist `c > 0`, `n0 > 0` such that:

```text
0 ≤ c × g(n) ≤ f(n)
```

for all `n ≥ n0`.

Example:

```text
5n² = Ω(n²)
```

because we can choose `c = 5`.

---

## 13. Big-Theta Notation

Big-Theta describes an asymptotically tight bound.

We say:

```text
f(n) = Θ(g(n))
```

if there exist `c1 > 0`, `c2 > 0`, `n0 > 0` such that:

```text
0 ≤ c1 × g(n) ≤ f(n) ≤ c2 × g(n)
```

for all `n ≥ n0`.

Equivalent to:

```text
f(n) = O(g(n))
```

and:

```text
f(n) = Ω(g(n))
```

Example:

```text
6n³ = Θ(n³)
```

---

## 14. Important Distinction: Cases vs Bounds

One should not equate:

```text
Big-O = Worst Case
Big-Omega = Best Case
```

Best, average, and worst cases speak about **types of input**.

`O`, `Ω`, `Θ` describe **bounds of a complexity function**.

Example:

```text
T_worst(n) = Θ(n)
```

then simultaneously:

```text
T_worst(n) = O(n)
```

and:

```text
T_worst(n) = Ω(n)
```

---

## 15. Rules for Analyzing Loops and Code Fragments

### 15.1. Constant Operations

```python
x = a + b
```

If addition is considered constant-time:

```text
Θ(1)
```

### 15.2. Single Loop

```python
for i in range(n):
    print(i)
```

The loop body runs `n` times:

```text
Θ(n)
```

### 15.3. Consecutive Loops

```python
for i in range(n):
    work_a()

for j in range(n):
    work_b()
```

Total:

```text
Θ(n) + Θ(n) = Θ(n)
```

Not `Θ(n²)`.

### 15.4. Nested Independent Loops

```python
for i in range(n):
    for j in range(n):
        work()
```

The inner body runs `n × n` times:

```text
Θ(n²)
```

### 15.5. Dependent Loops

```python
for i in range(n):
    for j in range(i):
        work()
```

Execution count:

```text
0 + 1 + 2 + ... + (n - 1)
```

Using the formula:

```text
0 + 1 + ... + (n - 1) = n(n - 1) / 2
```

Therefore:

```text
Θ(n²)
```

### 15.6. If-Else

```python
if n == 1:
    print("Wrong Value")
else:
    for i in range(n):
        print(i)
```

Worst-case time:

```text
Θ(n)
```

In general:

```text
cost(condition) + max(cost(if-branch), cost(else-branch))
```

### 15.7. Logarithmic Loop

```python
i = 1

while i < n:
    i *= 2
```

Values:

```text
1, 2, 4, 8, 16, ...
```

After `k` iterations:

```text
i = 2^k
```

Stops when:

```text
2^k ≥ n
```

Therefore:

```text
k = Θ(log n)
```

### 15.8. Halving Loop

```python
i = n

while i > 1:
    i //= 2
```

Sequence:

```text
n, n/2, n/4, n/8, ...
```

Iteration count:

```text
Θ(log n)
```

---

## 16. Useful Mathematical Sums

### 16.1. Arithmetic Sum

```text
1 + 2 + ... + n = n(n + 1) / 2 = Θ(n²)
```

### 16.2. Geometric Sum

For `x ≠ 1`:

```text
1 + x + x² + ... + x^n
= (x^(n + 1) - 1) / (x - 1)
```

Example:

```text
1 + 2 + 4 + ... + 2^k
= 2^(k + 1) - 1
= Θ(2^k)
```

### 16.3. Harmonic Sum

```text
1 + 1/2 + 1/3 + ... + 1/n = Θ(log n)
```

### 16.4. Logarithmic Sum

```text
Σ log k = log(n!) = Θ(n log n)
```

### 16.5. Power Sum

For `p > -1`:

```text
Σ k^p = Θ(n^(p + 1))
```

---

## 17. Common Mistakes

### Mistake 1: Two loops always mean `O(n²)`

False.

Two consecutive loops can be just `O(n)`.

### Mistake 2: One line means `O(1)`

False.

```python
result = sorted(arr)
```

is one line of code but not constant-time.

### Mistake 3: Ignore operation cost

```python
arr[:k]
```

takes time proportional to the number of copied elements.

### Mistake 4: Ignore input size definition

For graphs, `O(V + E)` is usually more accurate than `O(n)`.

### Mistake 5: Use only `O` when `Θ` is known

If:

```text
T(n) = 3n + 7
```

then one should write:

```text
T(n) = Θ(n)
```

---

## 18. Summary

- Algorithm analysis studies how resource usage increases with input size.
- Input size must be clearly specified.
- Basic operation counting is a fundamental tool.
- Time complexity and auxiliary space complexity are the two main metrics.
- Best, average, and worst cases are input categories.
- Growth rate determines scalability.
- Big-O is upper bound, Big-Omega is lower bound, Big-Theta is tight bound.
- Do not equate Big-O with worst case or Big-Omega with best case.
- You cannot merely count the number of loops; you must calculate the actual number of operations executed.
