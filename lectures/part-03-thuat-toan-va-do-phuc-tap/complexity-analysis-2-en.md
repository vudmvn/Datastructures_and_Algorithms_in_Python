# Lecture: Algorithm Complexity and Asymptotic Notation

**Last updated:** August 31, 2026

## 1. Learning Objectives

After completing this lesson, learners will be able to:

1. Define and explain the purpose of **asymptotic analysis**.
2. Differentiate between the three fundamental asymptotic notations: Big $O$ (Upper Bound), Big $\Omega$ (Lower Bound), and Big $\Theta$ (Tight Bound).
3. Apply mathematical rules (sum rule, product rule) to compute time complexity for single loops, nested loops, and sequential execution blocks.
4. Set up recurrence relations for recursive algorithms and solve them using recursion trees or the **Master Theorem**.
5. Distinguish clearly between **Space Complexity** and **Auxiliary Space**.

---

## 2. Why Do We Need Asymptotic Analysis?

In Lesson 1, we learned that the wall-clock execution time (in seconds) of a program depends heavily on hardware configurations, programming languages, and compilers. To evaluate algorithms objectively and independently of hardware or environment, we use **Asymptotic Analysis**.

> **Core Idea:** Asymptotic analysis focuses on how the running time (or memory consumption) of an algorithm grows as the input size ($n$) approaches infinity ($n \to \infty$).

When $n$ becomes very large, constant factors and lower-order terms become negligible. 

For example, if an algorithm executes $f(n) = 3n^2 + 5n + 100$ basic operations:
- When $n = 10$: $f(10) = 300 + 50 + 100 = 450$ (the constant term $100$ contributes significantly).
- When $n = 10,000$: $f(10,000) = 300,000,000 + 50,000 + 100 \approx 3 \times 10^8$ (the $5n + 100$ portion accounts for less than $0.02\%$ of total operations).

Therefore, we say the growth rate of this algorithm is proportional to $n^2$.

---

## 3. Three Fundamental Asymptotic Notations

To describe the mathematical relationship between input size and resource consumption, we use asymptotic notations: $O$, $\Omega$, and $\Theta$.

```text
  Resource (y)
      |         f(n) = O(g(n))  [Upper Bound - Worst Case]
      |         f(n) = Θ(g(n))  [Tight Bound - Average Case]
      |         f(n) = Ω(g(n))  [Lower Bound - Best Case]
      +------------------------------> Input Size n (x)
```

### 3.1. Big $O$ Notation (Upper Bound)

Big $O$ notation describes the worst-case scenario. It provides an upper bound on the growth rate of an algorithm: actual running time will never exceed this bound.

*   **Mathematical Definition:** $f(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that:
    $$0 \le f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0$$

*   **Meaning:** The algorithm runs at most as fast as $g(n)$ for sufficiently large inputs.
*   **Example:** Linear search has a worst-case time complexity of $O(n)$ (traversing the entire array).

### 3.2. Big $\Omega$ Notation (Lower Bound)

Big $\Omega$ notation describes the best-case scenario. It provides a lower bound: the algorithm requires at least this many steps to complete.

*   **Mathematical Definition:** $f(n) = \Omega(g(n))$ if there exist positive constants $c$ and $n_0$ such that:
    $$0 \le c \cdot g(n) \le f(n) \quad \text{for all } n \ge n_0$$

*   **Meaning:** The algorithm runs at least as slowly as $g(n)$ in all cases for sufficiently large inputs.
*   **Example:** Regardless of array arrangement, comparison-based sorting algorithms require at least $\Omega(n \log n)$ comparisons in the worst case.

### 3.3. Big $\Theta$ Notation (Tight Bound)

Big $\Theta$ notation describes the average case or exact growth rate of an algorithm when upper and lower bounds coincide.

*   **Mathematical Definition:** $f(n) = \Theta(g(n))$ if there exist positive constants $c_1, c_2$ and $n_0$ such that:
    $$0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \text{for all } n \ge n_0$$

*   **Meaning:** $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$.
*   **Example:** Traversing an entire array of size $n$ to print elements always takes exactly $\Theta(n)$ steps.

---

## 4. Rules for Calculating Time Complexity

When analyzing a program, simple rules help simplify Big $O$ expressions.

### 4.1. Sum Rule (Sequential Execution)
If a program consists of two sequential independent code blocks: Block 1 takes $O(f(n))$, Block 2 takes $O(g(n))$, total complexity is:
$$T(n) = O(f(n) + g(n)) = O(\max(f(n), g(n)))$$

**Example:**
```python
# Block 1: O(n)
for i in range(n):
    print(i)

# Block 2: O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)
```
Total running time is $O(n + n^2) = O(n^2)$.

### 4.2. Product Rule (Nested Loops)
If an outer loop runs $f(n)$ times and an inner loop runs $g(n)$ times for each outer iteration, total complexity is:
$$T(n) = O(f(n) \times g(n))$$

**Example:**
```python
# Outer loop runs n times, inner loop runs m times
for i in range(n):
    for j in range(m):
        # O(1) work
        sum += i * j
```
Time complexity is $O(n \times m)$. If $n = m$, time complexity is $O(n^2)$.

---

## 5. Analysis of Classic Loop Structures

### 5.1. Linear Increment / Decrement Loops: $O(n)$
```python
i = 0
while i < n:
    # O(1) work
    i += 2  # Or i += c for constant c
```
The loop performs approximately $n / 2$ steps. Omitting the constant factor $1/2$, complexity is $O(n)$.

### 5.2. Logarithmic Multiplication / Division Loops: $O(\log n)$
```python
i = 1
while i < n:
    # O(1) work
    i *= 2  # Or i *= c
```
Values of `i`: $1, 2, 4, 8, \dots, 2^k$. The loop terminates when $2^k \ge n \implies k \ge \log_2 n$. Steps scale with $\log n$.

```python
i = n
while i > 0:
    # O(1) work
    i //= 2
```
Similarly, `i` is halved continuously until reaching 0. Complexity is $O(\log n)$.

### 5.3. Triangular Nested Loops: $O(n^2)$
```python
for i in range(n):
    for j in range(i, n):
        # O(1) work
        print(i, j)
```
- When $i = 0$, inner loop runs $n$ times.
- When $i = 1$, inner loop runs $n-1$ times.
- ...
- When $i = n-1$, inner loop runs $1$ time.

Total iterations:
$$S = n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2} = \frac{1}{2}n^2 + \frac{1}{2}n$$
Ignoring constant factors and lower-order terms, time complexity is $O(n^2)$.

---

## 6. Recursive Analysis and the Master Theorem

When a function calls itself recursively, we set up a **recurrence relation**.

### 6.1. Recurrence Relation for Binary Search
For each recursive step, we halve the array size and perform constant work ($O(1)$) to compare the middle element:
$$T(n) = T\left(\frac{n}{2}\right) + c$$
Using recursion tree analysis, we obtain $O(\log n)$ time complexity.

### 6.2. Master Theorem
The Master Theorem provides a fast technique for solving divide-and-conquer recurrences:
$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$
Where:
*   $a \ge 1$ is the number of recursive subproblems.
*   $b > 1$ is the division factor for input size.
*   $f(n)$ is the cost of dividing the problem and combining results.

Compare $f(n)$ with $n^{\log_b a}$:

| Case | Condition | Complexity $T(n)$ | Example |
| :--- | :--- | :--- | :--- |
| **Case 1** | $f(n) < n^{\log_b a}$ (recursion dominates) | $T(n) = \Theta(n^{\log_b a})$ | $T(n) = 8T(n/2) + n^2 \implies \Theta(n^3)$ |
| **Case 2** | $f(n) = \Theta(n^{\log_b a})$ (balanced) | $T(n) = \Theta(n^{\log_b a} \log n)$ | $T(n) = 2T(n/2) + n \implies \Theta(n \log n)$ (Merge Sort) |
| **Case 3** | $f(n) > n^{\log_b a}$ (combine dominates)* | $T(n) = \Theta(f(n))$ | $T(n) = 2T(n/2) + n^2 \implies \Theta(n^2)$ |

*\*Note for Case 3: Regularity condition must hold: $a \cdot f(n/b) \le c \cdot f(n)$ for constant $c < 1$.*

---

## 7. Memory Complexity Analysis (Space Complexity)

Space complexity measures total memory required by an algorithm, including input data. In algorithm analysis, we pay close attention to **Auxiliary Space**.

*   **Auxiliary Space:** Extra or temporary memory allocated by the algorithm itself (auxiliary variables, dynamic arrays, call stack).
*   **Space Complexity:** Input Space + Auxiliary Space.

### 7.1. Auxiliary Space $O(1)$ Example
```python
def swap(a, b):
    temp = a  # 1 extra variable
    a = b
    b = temp
```
Memory usage remains constant regardless of input magnitude $\implies$ Auxiliary Space: $O(1)$.

### 7.2. Recursive Memory (Call Stack Frame)
When calling recursive functions, parameters and return addresses are pushed onto the **Call Stack**. Maximum recursion depth determines auxiliary space consumed.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
`factorial(n)` recurses $n$ times before reaching the base case, storing $n$ stack frames.
$$\implies \text{Auxiliary Space: } O(n)$$

---

## 8. Common Misconceptions

1.  **Confusing $O(1)$ with "No Loops":** Code with no loops calling library functions (e.g., `list.sort()` in Python) has complexity dependent on the library function ($O(n \log n)$).
2.  **Treating Constants as Variables:** A loop running $1,000,000$ fixed times has time complexity $O(1)$, not $O(n)$, because iteration count does not change with input size.
3.  **Ignoring Call Stack Space in Recursion:** Recursive factorial functions use $O(n)$ stack space even if no temporary arrays are declared.

---

## 9. Review Questions

1.  Define $O(g(n))$, $\Omega(g(n))$, and $\Theta(g(n))$. Why is Big $O$ used most frequently by software developers?
2.  An algorithm takes $100n^2$ steps while another takes $2^n$ steps. For what value of $n$ does the second algorithm become slower than the first?
3.  What algorithm does the following recurrence relation describe, and what is its complexity?
    $$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$
4.  What is the main distinction between Space Complexity and Auxiliary Space?

---

## 10. Practical Exercises

### Exercise 1 — Analyze the time complexity:
```python
def print_patterns(n):
    i = n
    while i > 0:
        for j in range(i):
            print(j)
        i = i // 2
```
*Solution:* 
- Outer loop halves `i`: $i = n, n/2, n/4, \dots$
- Inner loop runs `i` times.
- Total operations: $n + n/2 + n/4 + n/8 + \dots \le 2n$.
- Time complexity is $O(n)$, not $O(n \log n)$ or $O(n^2)$.

### Exercise 2 — Use Master Theorem:
Solve the recurrence relation:
$$T(n) = 4T\left(\frac{n}{2}\right) + n$$
*Solution:*
- Coefficients: $a = 4, b = 2, f(n) = n$.
- Compute $n^{\log_b a} = n^{\log_2 4} = n^2$.
- Since $f(n) = n < n^2$, this falls into **Case 1** of the Master Theorem.
- Conclusion: $T(n) = \Theta(n^2)$.

### Exercise 3 — Analyze space complexity:
```python
def prefix_sums(arr):
    n = len(arr)
    result = [0] * n
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        result[i] = current_sum
    return result
```
*Solution:*
- Input array size $n$.
- Result array `result` size $n$.
- Total Space Complexity: $O(n) + O(n) = O(n)$.
- Auxiliary Space: $O(n)$.


---

## 11. References

1.  *Introduction to Algorithms* (CLRS) - Chapter 3: Growth of Functions & Chapter 4: Divide-and-Conquer.
2.  GeeksforGeeks: *Analysis of Algorithms*.
