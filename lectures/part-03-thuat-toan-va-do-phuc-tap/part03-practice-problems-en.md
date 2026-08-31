# Practice Exercises — Algorithm Complexity Analysis

**Last updated:** August 31, 2026

> **Objectives:** Practice determining input size, counting basic operations, analyzing loops, identifying growth rates, utilizing asymptotic notations ($O$, $\Omega$, $\Theta$), formulating and solving recurrence relations, and introducing amortized analysis.
>
> The exercises are designed following the topics in **Chapter 1 — Introduction** of *Data Structures and Algorithmic Thinking with Python*, specifically covering running-time analysis, rate of growth, asymptotic notation, guidelines for asymptotic analysis, logarithms/summations, recurrence relations, and amortized analysis.

---

## Operation Counting Conventions

Unless stated otherwise:

- Each **assignment**, **comparison**, and **arithmetic operation** ($+$, $-$, $\times$, $/$) is treated as one basic operation.
- When asked for the **number of times a statement is executed**, count only the designated statement.
- When asked for **asymptotic complexity**, disregard constant factors and lower-order terms.
- Assume $n$ is a positive integer.
- For problems involving division by 2, assume $n$ is a power of 2 if it simplifies the calculations.

---

## Part A. Counting Basic Operations

### Exercise 1. A Single Linear Loop

Consider the code snippet:

```python
count = 0
for i in range(n):
    count = count + 1
```

1. How many times is the statement `count = count + 1` executed?
2. If addition and assignment are treated as two distinct operations, how many operations are executed in the loop body?
3. What is the time complexity in terms of $\Theta$?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

1. The statement is executed exactly $n$ times.
2. Each iteration performs 1 addition and 1 assignment, resulting in $2n$ operations in the loop body.
3. Ignoring constant factors:

$$T(n) = \Theta(n)$$

</details>

---

### Exercise 2. Two Consecutive Loops

```python
count = 0

for i in range(n):
    count += 1

for i in range(n):
    for j in range(n):
        count += 1
```

1. How many total times is `count += 1` executed?
2. Express $T(n)$ as a polynomial.
3. Determine $\Theta(T(n))$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The first loop executes $n$ times.

The nested loop executes:

$$n \cdot n = n^2$$

times.

Therefore:

$$T(n) = n + n^2$$

The highest-order term is $n^2$, hence:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 3. Triangular Loop

```python
count = 0

for i in range(n):
    for j in range(i + 1):
        count += 1
```

1. For a fixed value of $i$, how many times does `count += 1` run?
2. Calculate the exact total number of executions of this statement.
3. Deduce the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

For $i = 0, 1, \dots, n-1$, the inner loop executes:

$$1, 2, 3, \dots, n$$

times respectively.

Therefore:

$$T(n) = 1 + 2 + \dots + n = \frac{n(n+1)}{2}$$

Thus:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 4. Reverse Triangular Loop

```python
count = 0

for i in range(n):
    for j in range(i, n):
        count += 1
```

Calculate the exact number of times `count += 1` is executed and determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The number of executions of the inner loop is:

$$n, (n-1), (n-2), \dots, 1$$

Therefore:

$$T(n) = n + (n-1) + \dots + 1 = \frac{n(n+1)}{2}$$

Hence:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 5. Step Size of 2

```python
count = 0

for i in range(n):
    for j in range(0, n, 2):
        count += 1
```

1. How many times does the inner loop execute?
2. What is the total number of increments to `count`?
3. What is the time complexity?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The inner loop iterates over values:

$$0, 2, 4, \dots$$

that are strictly less than $n$, which is roughly $n/2$ times, precisely:

$$\lceil n/2 \rceil$$

Total number of increments to `count`:

$$n \lceil n/2 \rceil$$

Therefore:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 6. Sum of Squares

```python
count = 0

for i in range(1, n + 1):
    for j in range(i * i):
        count += 1
```

1. Write the summation representing the number of executions of `count += 1`.
2. Evaluate it using the sum-of-squares formula.
3. Determine $\Theta$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

We have:

$$T(n) = \sum_{i=1}^n i^2$$

Using the formula:

$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$

The highest-order term is $\frac{1}{3}n^3$, hence:

$$T(n) = \Theta(n^3)$$

</details>

---

## Part B. Logarithmic Loop Analysis

### Exercise 7. Doubling the Control Variable

```python
i = 1
while i < n:
    i = i * 2
```

1. After $k$ iterations, what is the value of `i`?
2. When does the loop terminate?
3. Deduce the number of iterations and the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

After $k$ iterations:

$$i = 2^k$$

The loop stops as soon as $i \ge n$, so we seek the smallest integer $k$ such that:

$$2^k \ge n$$

Therefore:

$$k = \lceil \log_2 n \rceil$$

Hence:

$$T(n) = \Theta(\log n)$$

The base of the logarithm does not affect the asymptotic complexity class.

</details>

---

### Exercise 8. Halving the Control Variable

```python
i = n
while i > 1:
    i = i // 2
```

Determine the number of iterations in terms of $n$ and the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

After $k$ iterations:

$$i \approx \frac{n}{2^k}$$

The loop terminates when:

$$\frac{n}{2^k} \le 1 \implies 2^k \ge n$$

Thus, the number of iterations is approximately:

$$\log_2 n$$

and:

$$T(n) = \Theta(\log n)$$

</details>

---

### Exercise 9. Two Nested Logarithmic Loops

```python
count = 0
i = 1

while i <= n:
    j = n
    while j > 0:
        count += 1
        j = j // 2
    i = i * 2
```

Determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The outer loop executes:

$$\Theta(\log n)$$

times.

In each iteration of the outer loop, the inner loop also executes:

$$\Theta(\log n)$$

times.

Therefore:

$$T(n) = \Theta(\log n \cdot \log n) = \Theta(\log^2 n)$$

</details>

---

### Exercise 10. Linear Times Logarithmic

```python
count = 0

for i in range(n):
    j = 1
    while j <= n:
        count += 1
        j = j * 2
```

1. How many times does the `while` loop run for each $i$?
2. What is the total time complexity?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The `while` loop generates the sequence of values:

$$1, 2, 4, 8, \dots, 2^k \le n$$

The number of iterations is:

$$\lfloor \log_2 n \rfloor + 1$$

The outer loop executes $n$ times, so:

$$T(n) = n \cdot (\lfloor \log_2 n \rfloor + 1) = \Theta(n \log n)$$

</details>

---

### Exercise 11. Geometric Series in a Loop

```python
count = 0
i = n

while i >= 1:
    for j in range(i):
        count += 1
    i = i // 2
```

Do not simply multiply "number of outer iterations × cost of the first iteration". Write the summation of costs across all levels and determine the complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The cost across successive levels is approximately:

$$n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \dots$$

This is a geometric series whose infinite sum is bounded by:

$$2n$$

Therefore:

$$T(n) = \Theta(n)$$

This is an important example demonstrating that an outer logarithmic loop does **not necessarily** lead to $O(n \log n)$.

</details>

---

## Part C. Index-Dependent Loops

### Exercise 12. Harmonic Sum

```python
count = 0

for i in range(1, n + 1):
    j = i
    while j <= n:
        count += 1
        j += i
```

1. For each $i$, approximately how many times does the `while` loop run?
2. Write the summation for the total number of operations.
3. Deduce the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

For a fixed $i$, `j` assumes the values:

$$i, 2i, 3i, \dots$$

up to $n$. Thus, the inner loop executes approximately:

$$\lfloor n/i \rfloor$$

times.

Total cost:

$$T(n) = \sum_{i=1}^n \lfloor n/i \rfloor$$

Approximating by removing the floor function:

$$T(n) \approx n \cdot \sum_{i=1}^n \frac{1}{i}$$

Since:

$$\sum_{i=1}^n \frac{1}{i} = \Theta(\log n),$$

we have:

$$T(n) = \Theta(n \log n)$$

</details>

---

### Exercise 13. Variable with Accelerating Increment

```python
i = 1
s = 1

while s < n:
    i = i + 1
    s = s + i
```

Determine the time complexity of the loop.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

After $k$ iterations, $s$ is equal to the sum of the first $k$ integers:

$$s = \Theta(k^2)$$

The loop terminates when:

$$k^2 \approx n$$

Therefore:

$$k = \Theta(\sqrt{n})$$

Hence:

$$T(n) = \Theta(\sqrt{n})$$

</details>

---

### Exercise 14. Quadratic Condition

```python
i = 1
count = 0

while i * i < n:
    count += 1
    i += 1
```

Determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The loop terminates when:

$$i^2 \ge n$$

Thus:

$$i \approx \sqrt{n}$$

Therefore:

$$T(n) = \Theta(\sqrt{n})$$

</details>

---

## Part D. Best Case, Worst Case, and Conditional Branches

### Exercise 15. Linear Search

```python
def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1
```

Assume `len(A) = n`.

1. When does the best case occur? What is its complexity?
2. When does the worst case occur? What is its complexity?
3. If the probability of $x$ being at each position is uniformly distributed, what is the expected number of comparisons?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

1. Best case: $x$ is found at index `A[0]`.

$$T_{\text{best}}(n) = \Theta(1)$$

2. Worst case: $x$ is not in the array or is located at the very last index.

$$T_{\text{worst}}(n) = \Theta(n)$$

3. If $x$ is guaranteed to be present and equally likely at any position:

$$\frac{1 + 2 + \dots + n}{n} = \frac{n+1}{2}$$

Hence, the average case remains:

$$\Theta(n)$$

</details>

---

### Exercise 16. Branches with Asymmetric Costs

```python
count = 0

for i in range(n):
    if A[i] == 0:
        count += 1
    else:
        for j in range(n):
            count += 1
```

Determine:

1. Best-case complexity.
2. Worst-case complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

### Best Case

If `A[i] == 0` for all $i$, each outer iteration performs only constant work.

$$T_{\text{best}}(n) = \Theta(n)$$

### Worst Case

If `A[i] != 0` for all $i$, each iteration runs an inner loop of $n$ steps.

$$T_{\text{worst}}(n) = n \cdot n = \Theta(n^2)$$

</details>

---

### Exercise 17. `break` Statement Altering Complexity

```python
for i in range(n):
    j = 0
    while j < n:
        break
        j += 1
```

What is the time complexity of this code? Explain why it is not $O(n^2)$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

In every outer iteration, the `while` loop executes exactly once because the `break` statement terminates it immediately.

Therefore:

$$T(n) = n \cdot O(1) = \Theta(n)$$

One cannot determine complexity solely from the loop condition `j < n`; one must examine the **actual control flow**.

</details>

---

## Part E. Rate of Growth and Asymptotic Notations

### Exercise 18. Dropping Lower-Order Terms

Determine the $\Theta$ class for each of the following functions:

1. $5n + 100$
2. $3n^2 + 20n + 7$
3. $n^4 + 100n^2 + 500$
4. $9$
5. $n \log n + 20n$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

1. $\Theta(n)$
2. $\Theta(n^2)$
3. $\Theta(n^4)$
4. $\Theta(1)$
5. $\Theta(n \log n)$

Principle: For sufficiently large $n$, retain the term with the highest growth rate and drop leading constant coefficients.

</details>

---

### Exercise 19. Proof Using Big-O Definition

Prove:

$$5n + 12 = O(n)$$

Provide a valid pair of positive constants $c > 0$ and $n_0 > 0$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

By definition, we need:

$$5n + 12 \le c \cdot n$$

for all $n \ge n_0$.

For example, when $n \ge 12$:

$$12 \le n$$

Therefore:

$$5n + 12 \le 5n + n = 6n$$

We can choose:

$$c = 6, \quad n_0 = 12$$

Hence:

$$5n + 12 = O(n)$$

Note: The choice of $c$ and $n_0$ is **not unique**.

</details>

---

### Exercise 20. Proving a Tight Bound

Prove:

$$4n^2 + 3n + 2 = \Theta(n^2)$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

We need to find positive constants $c_1, c_2, n_0 > 0$ such that:

$$c_1 n^2 \le 4n^2 + 3n + 2 \le c_2 n^2 \quad \text{for all } n \ge n_0$$

For $n \ge 1$:

$$4n^2 \le 4n^2 + 3n + 2$$

Furthermore:

$$3n \le 3n^2, \quad 2 \le 2n^2$$

Thus:

$$4n^2 + 3n + 2 \le 4n^2 + 3n^2 + 2n^2 = 9n^2$$

We can choose:

$$c_1 = 4, \quad c_2 = 9, \quad n_0 = 1$$

Consequently:

$$4n^2 + 3n + 2 = \Theta(n^2)$$

</details>

---

### Exercise 21. True or False?

Determine whether each of the following statements is True or False.

1. $2^{n+1} = O(2^n)$
2. $2^{2n} = O(2^n)$
3. $n \log n = O(n^2)$
4. $n^2 = \Omega(n \log n)$
5. $100n + 1 = \Theta(n)$
6. $n = \Theta(n^2)$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

1. **True**, because $2^{n+1} = 2 \cdot 2^n$.
2. **False**, because $2^{2n} = 4^n$ grows strictly faster than $2^n$.
3. **True**.
4. **True**.
5. **True**.
6. **False**.

</details>

---

### Exercise 22. Ranking Growth Rates

Sort the following functions from slowest-growing to fastest-growing:

$$1, \quad \log n, \quad \sqrt{n}, \quad n, \quad n \log n, \quad 4^{\log_2 n}, \quad n^3, \quad 2^n, \quad n!$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Notice that:

$$4^{\log_2 n} = (2^2)^{\log_2 n} = (2^{\log_2 n})^2 = n^2$$

The correct ordering is:

$$1 < \log n < \sqrt{n} < n < n \log n < n^2 < n^3 < 2^n < n!$$

</details>

---

## Part F. Formulating Recurrences from Recursive Code

### Exercise 23. Single Recursive Call with Decrement of 1

```python
def f(n):
    if n <= 0:
        return
    do_constant_work()
    f(n - 1)
```

1. Write the recurrence relation for the running time.
2. Solve the recurrence.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Recurrence:

$$T(n) = T(n-1) + \Theta(1)$$

Unrolling (telescoping):

$$T(n) = T(n-2) + 2\Theta(1) = \dots = T(0) + n\Theta(1)$$

Therefore:

$$T(n) = \Theta(n)$$

</details>

---

### Exercise 24. Single Recursive Call with Linear Work

```python
def f(n):
    if n <= 0:
        return

    for i in range(n):
        do_constant_work()

    f(n - 1)
```

Formulate the recurrence relation and determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Each call performs $\Theta(n)$ work before calling `f(n-1)`:

$$T(n) = T(n-1) + \Theta(n)$$

Unrolling:

$$T(n) = n + (n-1) + \dots + 1$$

Therefore:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 25. Decrementing Size by 3

```python
def f(n):
    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            do_constant_work()

    f(n - 3)
```

1. Write the recurrence relation.
2. Determine the number of recursion levels.
3. Deduce the overall time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Each call performs work of order:

$$\Theta(n^2)$$

Recurrence relation:

$$T(n) = T(n-3) + \Theta(n^2)$$

The recursion depth is approximately $n/3 = \Theta(n)$.

Total work:

$$n^2 + (n-3)^2 + (n-6)^2 + \dots$$

This is a summation of $\Theta(n)$ decreasing quadratic terms, which is asymptotically equivalent to the sum of squares.

Therefore:

$$T(n) = \Theta(n^3)$$

</details>

---

### Exercise 26. Three Recursive Calls on Same Subproblem

```python
def f(n):
    if n <= 0:
        return

    f(n - 1)
    f(n - 1)
    f(n - 1)
```

Formulate the recurrence relation and determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Recurrence relation:

$$T(n) = 3T(n-1) + \Theta(1)$$

The recursion tree has a branching factor of 3 and a depth of approximately $n$.

The number of nodes across levels is:

$$1 + 3 + 3^2 + \dots + 3^n$$

Therefore:

$$T(n) = \Theta(3^n)$$

</details>

---

### Exercise 27. Two Subproblems of Half Size

```python
def f(n):
    if n <= 1:
        return

    f(n // 2)
    f(n // 2)
    do_constant_work()
```

Formulate the recurrence relation and determine the time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Recurrence relation:

$$T(n) = 2T(n/2) + \Theta(1)$$

By the Master Theorem:

$$a = 2, \quad b = 2, \quad n^{\log_b a} = n^{\log_2 2} = n$$

The work done outside recursion is $\Theta(1)$, which is polynomially smaller than $n$ (Case 1: subproblems dominate).

Therefore:

$$T(n) = \Theta(n)$$

</details>

---

## Part G. Master Theorem

### Exercise 28.

Solve the recurrence relation:

$$T(n) = 2T(n/2) + n$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Here:

$$a = 2, \quad b = 2$$

Hence:

$$n^{\log_b a} = n^{\log_2 2} = n$$

The non-recursive cost is:

$$f(n) = n$$

Since $f(n) = \Theta(n^{\log_b a})$, this corresponds to Master Theorem Case 2:

$$T(n) = \Theta(n \log n)$$

</details>

---

### Exercise 29.

Solve:

$$T(n) = 4T(n/2) + n$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

$$a = 4, \quad b = 2,$$

so:

$$n^{\log_b a} = n^{\log_2 4} = n^2$$

Since:

$$f(n) = n = O(n^{2 - \epsilon}) \quad (\text{with } \epsilon = 1),$$

the subproblems dominate (Master Theorem Case 1).

Therefore:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 30.

Solve:

$$T(n) = 2T(n/4) + n$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

$$a = 2, \quad b = 4$$

We have:

$$n^{\log_b a} = n^{\log_4 2} = n^{1/2} = \sqrt{n}$$

Meanwhile:

$$f(n) = n = \Omega(n^{1/2 + \epsilon}) \quad (\text{with } \epsilon = 0.5)$$

Since $n$ grows strictly faster than $\sqrt{n}$ and satisfies the regularity condition $2(n/4) \le c n$ for $c = 1/2 < 1$, the root work dominates (Master Theorem Case 3).

Therefore:

$$T(n) = \Theta(n)$$

</details>

---

### Exercise 31.

Solve:

$$T(n) = 3T(n/2) + n^2$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

$$a = 3, \quad b = 2,$$

so:

$$n^{\log_2 3} \approx n^{1.585}$$

Meanwhile:

$$f(n) = n^2$$

Since $n^2 = \Omega(n^{1.585 + \epsilon})$ and the regularity condition holds ($3(n/2)^2 = \frac{3}{4}n^2 \le c n^2$ with $c = 3/4 < 1$), the root work dominates (Master Theorem Case 3).

Therefore:

$$T(n) = \Theta(n^2)$$

</details>

---

### Exercise 32.

Solve:

$$T(n) = 8T(n/2) + n^3$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

$$a = 8, \quad b = 2,$$

so:

$$n^{\log_b a} = n^{\log_2 8} = n^3$$

The non-recursive cost is also:

$$f(n) = n^3$$

Since both terms have identical growth rates ($f(n) = \Theta(n^{\log_b a})$), an extra logarithmic factor is introduced (Master Theorem Case 2):

$$T(n) = \Theta(n^3 \log n)$$

</details>

---

## Part H. Non-Standard Recurrences (Beyond Standard Master Theorem)

### Exercise 33. Size Reduction from $n$ to $\sqrt{n}$

Solve the recurrence relation:

$$T(n) = T(\sqrt{n}) + 1$$

Hint: substitute $n = 2^m$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Let:

$$n = 2^m \implies m = \log_2 n$$

Define:

$$S(m) = T(2^m)$$

Then:

$$\sqrt{n} = \sqrt{2^m} = 2^{m/2}$$

Substituting gives:

$$S(m) = S(m/2) + 1$$

This standard recurrence yields:

$$S(m) = \Theta(\log m)$$

Substituting back $m = \log_2 n$:

$$T(n) = \Theta(\log \log n)$$

</details>

---

### Exercise 34. Two Recursive Calls on $\sqrt{n}$

Solve:

$$T(n) = 2T(\sqrt{n}) + 1$$

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Again substitute:

$$n = 2^m, \quad S(m) = T(2^m)$$

We obtain:

$$S(m) = 2S(m/2) + 1$$

By the Master Theorem:

$$S(m) = \Theta(m)$$

Substituting back $m = \log_2 n$:

$$T(n) = \Theta(\log n)$$

</details>

---

## Part I. Analysis of Composite Code Snippets

### Exercise 35.

```python
count = 0

for i in range(n // 2, n):
    j = 1
    while j <= n // 2:
        k = 1
        while k <= n:
            count += 1
            k *= 2
        j += 1
```

Assume $n$ is even. Determine the overall time complexity.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

- Outer loop: $n/2 = \Theta(n)$ iterations.
- Middle loop: $n/2 = \Theta(n)$ iterations.
- Inner loop: $\Theta(\log n)$ iterations (variable $k$ doubles each time until reaching $n$).

Multiplying the costs of the independent loops:

$$T(n) = \Theta(n) \cdot \Theta(n) \cdot \Theta(\log n) = \Theta(n^2 \log n)$$

</details>

---

### Exercise 36.

```python
count = 0

for i in range(n):
    j = 1
    while j <= n:
        k = j
        while k > 0:
            count += 1
            k //= 2
        j *= 2
```

Carefully analyze the total cost of the inner loop $k$ instead of merely multiplying three loop bounds together.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

For:

$$j = 1, 2, 4, \dots, 2^r \le n,$$

the $k$-loop executes approximately:

$$\log_2 j + 1$$

times.

Setting $j = 2^r$, the cost as $r$ ranges from $0$ to $\lfloor \log_2 n  \rfloor$ is:

$$1 + 2 + \dots + (\lfloor \log_2 n \rfloor + 1) = \Theta((\log n)^2)$$

Therefore, for each iteration of $i$, the nested loops take $\Theta(\log^2 n)$ steps.

Since the outer loop executes $n$ times:

$$T(n) = \Theta(n \log^2 n)$$

</details>

---

## Part J. Amortized Analysis

### Exercise 37. Dynamic Array with Doubling Strategy

A dynamic array initially has capacity 1. Whenever it becomes full, a new array with double the capacity is allocated, and all existing elements are copied into the new array.

Suppose we perform $n$ consecutive `append` operations.

1. What is the worst-case time complexity of a single `append` operation?
2. What is the asymptotic bound on the total number of element copies across all resizes during $n$ appends?
3. What is the amortized complexity of a single `append` operation?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

A single `append` that triggers a resize must copy all existing elements, requiring $\Theta(n)$ steps. Hence, the worst case of a **single operation** is:

$$O(n)$$

However, resizes only occur at array capacities:

$$1, 2, 4, 8, \dots$$

The total number of element copies across all $n$ appends is:

$$1 + 2 + 4 + \dots < 2n$$

Therefore, the total cost for $n$ operations is:

$$\Theta(n)$$

The amortized cost per `append` operation is:

$$\frac{\Theta(n)}{n} = \Theta(1)$$

</details>

---

## Part K. Advanced Self-Study Exercises

### Exercise 38.

Determine the time complexity:

```python
count = 0

for i in range(1, n + 1):
    j = 1
    while j <= i:
        count += 1
        j *= 2
```

<details>
<summary><strong>Click to show hints / solution</strong></summary>

For each $i$, the inner loop executes:

$$\Theta(\log i)$$

times.

Therefore:

$$T(n) = \sum_{i=1}^n \Theta(\log i)$$

Note that:

$$\sum_{i=1}^n \log i = \log(n!)$$

By Stirling's approximation:

$$\log(n!) = \Theta(n \log n)$$

Hence:

$$T(n) = \Theta(n \log n)$$

</details>

---

### Exercise 39.

Determine the time complexity:

```python
count = 0
i = 1

while i <= n:
    for j in range(i):
        count += 1
    i *= 2
```

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The costs for each outer iteration are:

$$1 + 2 + 4 + 8 + \dots + 2^k \quad (\text{where } 2^k \le n)$$

This is a geometric series:

$$T(n) < 2n$$

Therefore:

$$T(n) = \Theta(n)$$

</details>

---

### Exercise 40.

Given:

$$T(n) = T(n/2) + T(n/4) + T(n/8) + n$$

Without finding exact constants, predict and explain the asymptotic growth rate of $T(n)$.

<details>
<summary><strong>Click to show hints / solution</strong></summary>

The combined size of all subproblems at the first recursive level is:

$$\frac{n}{2} + \frac{n}{4} + \frac{n}{8} = \frac{7}{8}n < n$$

The non-recursive work at the root is $\Theta(n)$, and the total work at each subsequent depth decreases geometrically by a factor of $\frac{7}{8} < 1$.

We obtain a decaying geometric series:

$$n + \frac{7}{8}n + \left(\frac{7}{8}\right)^2 n + \dots$$

Sum of the geometric series:

$$\sum_{k=0}^{\infty} \left(\frac{7}{8}\right)^k n = \frac{1}{1 - 7/8} n = 8n = \Theta(n)$$

Therefore:

$$T(n) = \Theta(n)$$

</details>

---

## Part L. Conceptual Check Questions

### Exercise 41.

Suppose algorithm A has running time:

$$T_A(n) = 1000n$$

and algorithm B has running time:

$$T_B(n) = n^2$$

1. Which algorithm has a better asymptotic growth rate?
2. Does algorithm A necessarily run faster than B for all values of $n$?
3. Why is asymptotic analysis still useful despite constant factors?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

1. Algorithm A has a strictly superior growth rate because:

$$1000n = \Theta(n)$$

whereas:

$$n^2 = \Theta(n^2)$$

2. No. For small inputs ($n < 1000$), the constant factor $1000$ causes algorithm A to require more operations than B ($T_A(10) = 10000 > T_B(10) = 100$).
3. Asymptotic analysis focuses on the behavior of algorithms as $n \to \infty$. It allows comparing the fundamental scalability of algorithms independently of hardware platforms, execution environments, and compiler optimizations.

</details>

---

### Exercise 42.

Why should wall-clock running time (measured in seconds) on a single machine not be used alone to conclude which algorithm is superior in terms of complexity?

<details>
<summary><strong>Click to show hints / solution</strong></summary>

Actual wall-clock execution time depends on many confounding factors:

- CPU architecture, clock speed, cache hierarchy, and memory bandwidth;
- Compiler / interpreter optimizations;
- Choice of programming language and runtime environment;
- Specific implementation details and memory locality;
- Particular input instances and distributions;
- System background load and multitasking at execution time.

Complexity analysis expresses running time as a function of **input size $n$** and focuses on the rate of growth, making it a reliable, hardware-independent framework for understanding the algorithmic foundation.

</details>

---

# Guidelines for Using This Exercise Set

The exercises can be grouped into three levels:

- **Basic:** Exercises 1–17
- **Intermediate:** Exercises 18–32
- **Advanced:** Exercises 33–42

Recommended classroom teaching workflow:

1. Have students **count the exact number of operations** before applying Big-O.
2. Simplify exact summations to tight $\Theta$ bounds.
3. For `while` loops, prompt students to write out the explicit sequence of values of the control variable.
4. For recursive algorithms, follow a systematic sequence:
   - Identify the number of recursive calls;
   - Determine the size of each subproblem;
   - Calculate the extra non-recursive work;
   - Formulate the recurrence relation;
   - Finally, solve the recurrence using recursion trees or the Master Theorem.
5. Only apply the Master Theorem when the recurrence strictly matches its standard form and conditions.
