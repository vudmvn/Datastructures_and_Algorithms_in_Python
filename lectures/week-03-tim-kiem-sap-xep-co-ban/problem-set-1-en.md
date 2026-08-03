---
title: "Lecture: Algorithm Analysis — Exercises and Solutions"
course: "Data Structures and Algorithmic Thinking with Python"
language: "en"
version: "1.2"
---

# Lecture: Algorithm Analysis — Exercises and Solutions

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section focuses on practicing complexity analysis through common problem types: solving recurrence relations, analyzing loops with non-linear increments, analyzing recursive functions, using the Master Theorem, substitution method, recursion tree, and comparing function growth rates.

After completing this section, learners can:

- solve recurrences of the form `T(n) = aT(n-b) + f(n)` using substitution or an appropriate theorem;
- analyze loops whose control variables increase by cumulative sums, geometric progressions, or square roots;
- set up recurrence relations from recursive source code;
- recognize when the Master Theorem is applicable and when variable substitution or a recursion tree is required;
- distinguish between upper bounds, lower bounds, and tight bounds;
- compare growth rates of polynomial, exponential, factorial, and logarithmic functions.

An important principle is to never infer complexity solely from the superficial appearance of code or recurrences. Two seemingly similar expressions can lead to completely different results due to cancellation, recursive structure, or the growth rule of control variables.

> **Usage:** Each problem is presented with a complete statement. The solution section is hidden by default and only displays when clicking the triangle next to **Show Solution**.

---

## 2. Subtract-and-Conquer Recurrences and Substitution

### Problem 1. Recurrence `T(n) = 3T(n-1)`

**Problem statement.** Determine the time complexity of the following recurrence:

```text
T(n) = 3T(n - 1), if n > 0
T(0) = 1
```

Solve the recurrence using substitution or direct expansion.

<details>
<summary><strong>Show Solution</strong></summary>

Consider:

```text
T(n) = 3T(n-1),  if n > 0
T(0) = 1
```

Expanding repeatedly:

```text
T(n) = 3T(n-1)
     = 3²T(n-2)
     = 3³T(n-3)
     = ...
     = 3ⁿT(0)
     = 3ⁿ
```

Therefore:

`T(n) = Θ(3ⁿ)`.

This problem can also be viewed as a subtract-and-conquer case with a branching factor greater than `1`.


</details>

### Problem 2. Recurrence with Cancellation

**Problem statement.** Determine the time complexity of the following recurrence:

```text
T(n) = 2T(n - 1) - 1, if n > 0
T(0) = 1
```

Solve the recurrence using substitution and note the potential occurrence of cancellation between terms.

<details>
<summary><strong>Show Solution</strong></summary>

Consider:

```text
T(n) = 2T(n-1) - 1,  if n > 0
T(0) = 1
```

Expanding:

```text
T(n) = 2T(n-1) - 1
     = 2(2T(n-2) - 1) - 1
     = 2²T(n-2) - 2 - 1
```

Continuing:

```text
T(n) = 2ⁿT(0) - (2ⁿ⁻¹ + 2ⁿ⁻² + ... + 2 + 1)
```

Since `T(0) = 1` and `2ⁿ⁻¹ + ... + 2 + 1 = 2ⁿ - 1`, it follows that:

```text
T(n) = 2ⁿ - (2ⁿ - 1) = 1
```

Therefore:

`T(n) = Θ(1)`.

This example shows that one cannot conclude a recurrence with a coefficient `2` before the recursive call necessarily has exponential complexity; the remaining part of the recurrence can create exact cancellation.


</details>

## 3. Loop Analysis with Non-Linear Increments

### Problem 3. Cumulative Variable Increasing as `1 + 2 + ... + k`

**Problem statement.** Determine the time complexity of the following function with respect to input size `n`:

```python
def function(n):
    i = 1
    s = 1

    while s < n:
        i = i + 1
        s = s + i

    print("*")

function(20)
```

Determine the number of times the `while` loop executes as the value of `s` increases according to the cumulative sum `1 + 2 + ... + k`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

After `k` loop iterations, the value of `s` has order:

```text
s = 1 + 2 + ... + k = k(k+1)/2
```

The loop stops when `s ≥ n`, that is:

`k(k+1)/2 ≥ n`.

Hence `k = Θ(√n)`, so:

`T(n) = Θ(√n)`.

The point to note is that the variable `s` does not increase by one unit each time; it increases according to the sum of consecutive integers.


</details>

### Problem 4. Increasing Step Size

**Problem statement.** Determine the time complexity of the following function:

```python
def function(n):
    i = 1
    count = 0

    while i < n:
        count = count + 1
        i = i + count
        print(count)

function(20)
```

Analyze the number of loop iterations based on the growth pattern of `i`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    i = 1
    count = 0

    while i < n:
        count = count + 1
        i = i + count
        print(count)
```

After `k` iterations:

```text
i ≈ 1 + 1 + 2 + ... + k
```

Therefore `i = Θ(k²)`. The loop stops when `i ≥ n`, so:

`k = Θ(√n)`.

Thus:

`T(n) = Θ(√n)`.


</details>

### Problem 5. Three Loops with One Logarithmic Loop

**Problem statement.** Determine the time complexity of the following program:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            k = 1

            while k <= n:
                count = count + 1
                k = k * 2

            j = j + 1

    print(count)

function(20)
```

Separately analyze the execution counts of the outer loop, middle loop, and inner loop.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                count = count + 1
                k = k * 2
            j = j + 1

    print(count)
```

The outer loop runs `Θ(n)` times. The middle loop runs `Θ(n)` times. The inner loop doubles `k`, so it runs `Θ(log n)` times.

Therefore:

`T(n) = Θ(n² log n)`.


</details>

### Problem 6. Two Logarithmic Loops Nested in a Linear Loop

**Problem statement.** Determine the time complexity of the following program:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            k = 1

            while k <= n:
                count = count + 1
                k = k * 2

            j = j * 2

    print(count)

function(20)
```

Note that both `j` and `k` increase exponentially.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                count = count + 1
                k = k * 2
            j = j * 2

    print(count)
```

The outer loop runs `Θ(n)` times. The variable `j` doubles so the middle loop runs `Θ(log n)` times. The inner loop also runs `Θ(log n)` times.

Thus:

`T(n) = Θ(n log² n)`.


</details>

### Problem 7. Effect of `break`

**Problem statement.** Determine the time complexity of the following program:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            break
            j = j * 2

        print(count)

function(20)
```

Explain the effect of the `break` statement on the number of executions of the `while` loop.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            break
            j = j * 2

        print(count)
```

Although the condition of the `while` loop may be true, the `break` statement causes the loop to terminate immediately in the first iteration. Therefore, each iteration of the `for` loop incurs only constant cost.

Since the outer loop runs `Θ(n)` times:

`T(n) = Θ(n)`.


</details>

## 4. Setting Up Recurrences from Recursive Functions

### Problem 8. Two Quadratic Loops and a Call to `n-3`

**Problem statement.** Consider the following recursive function:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            count = count + 1

    function(n - 3)
    print(count)

function(20)
```

Please:

1. set up the recurrence equation for the running time `T(n)`;
2. prove using expansion that `T(n) = Θ(n³)`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            count = count + 1

    function(n - 3)
    print(count)
```

Each call performs `Θ(n²)` work and calls itself with size `n-3`. Therefore:

`T(n) = T(n-3) + Θ(n²)`.

Expanding:

```text
T(n) = Θ(n² + (n-3)² + (n-6)² + ...)
```

There are `Θ(n)` recursion levels and the sum of squares has degree `Θ(n³)`. Thus:

`T(n) = Θ(n³)`.


</details>

### Problem 9. Recurrence with `n log n`

**Problem statement.** Determine the tight bound `Θ` for the recurrence:

`T(n) = 2T(n/2) + n log n`.

Master Theorem or an appropriate extended form can be used.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

`T(n) = 2T(n/2) + n log n`.

With `a = 2`, `b = 2`, we have `n^(log₂2) = n`. Since:

`f(n) = Θ(n log n)`,

Extended Master Theorem yields:

`T(n) = Θ(n log² n)`.


</details>

### Problem 10. Three Subproblems with Total Size Less Than `n`

**Problem statement.** Determine the `Θ` bound for the recurrence:

`T(n) = T(n/2) + T(n/4) + T(n/8) + n`.

Analyze the total size of subproblems or use a recursion tree.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

The sum of size ratios of subproblems is:

The total ratio of subproblem sizes is:

Therefore the total work at each level of the recursion tree decreases geometrically:

Therefore, the total work at each level of the recursion tree decreases geometrically:

```text
n + (7/8)n + (7/8)²n + ...
```

The sum of the series is `Θ(n)`, so:

`T(n) = Θ(n)`.


</details>

### Problem 11. Recurrence Halving Size with Constant Cost

**Problem statement.** Determine the `Θ` bound for the recurrence:

`T(n) = T(⌊n/2⌋) + 7`.

Explain the number of recursion levels before the problem size becomes constant.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

`T(n) = T(⌊n/2⌋) + 7`.

After `Θ(log n)` halvings, the size becomes constant. Each level has cost `Θ(1)`, therefore:

`T(n) = Θ(log n)`.


</details>

### Problem 12. Proving Lower Bound `Ω(log n)`

**Problem statement.** Prove that the running time of the following code snippet has lower bound `Ω(log n)`; also determine the tight bound if possible:

```python
def Read(n):
    k = 1

    while k < n:
        k = 3 * k
```

<summary><strong>Show Solution</strong></summary>
<summary><strong>Show Solution</strong></summary>
Consider:
Consider:

```python
def Read(n):
    k = 1
    while k < n:
        k = 3 * k
```

After `t` iterations:

`k = 3^t`.

The loop stops when `3^t ≥ n`, so:

`t ≥ log₃n`.

Thus:

`T(n) = Θ(log n)`,

and in particular:

`T(n) = Ω(log n)`.


</details>

### Problem 13. Recurrence with Cost `n(n-1)`

**Problem statement.** Solve the following recurrence using expansion:

```text
T(1) = 1
T(1) = 1
T(n) = T(n - 1) + n(n - 1), for n ≥ 2

Determine the tight bound `Θ` of `T(n)`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```text
T(1) = 1
T(n) = T(n-1) + n(n-1), for n ≥ 2
```

Expanding:

```text
T(n) = T(1) + Σ[i=2..n] i(i-1)
We have:

We have:

```text
Σ i(i-1) = Σ i² - Σ i = Θ(n³)
```

Therefore:

`T(n) = Θ(n³)`.


</details>

### Problem 14. Direct Recursive Fibonacci

**Problem statement.** Consider the program calculating Fibonacci numbers via direct recursion:

```python
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)

print(Fib(3))
```

Please:

1. set up the running time recurrence;
2. analyze the complexity of the program;
3. state a simple upper bound and, if possible, a tighter bound.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
```

Time recurrence:

`T(n) = T(n-1) + T(n-2) + Θ(1)`.

A simple upper bound is `O(2^n)`. A tighter analysis shows the call count increases according to Fibonacci numbers, so:

`T(n) = Θ(φ^n)`,

where `φ = (1 + √5)/2`.


</details>

## 5. Harmonic Sums, Logarithmic Sums, and Pitfalls

### Problem 15. Loop with Increment Step `i`

**Problem statement.** Determine the time complexity of the following program:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        j = 1

        while j <= n:
            j = j + i
            count = count + 1

    print(count)

function(20)
```

Before analyzing complexity, check if the program always terminates. If an error causing non-termination is found, point it out and analyze a reasonable fixed version.
<summary><strong>Show Solution</strong></summary>
<details>
If the outer loop is corrected to:

If the outer loop is corrected to:

```python
for i in range(1, n):
```

then for each `i`, the inner loop runs about `n/i` times. Total number of iterations is:

```text
n/1 + n/2 + ... + n/(n-1) = Θ(n log n)
```

Therefore, the corrected version has:

`T(n) = Θ(n log n)`.


</details>

### Problem 16. Sum `Σ log i`

**Problem statement.** Determine the complexity of the sum:

`Σ[i=1..n] log i`.

Simplify the sum using logarithm properties and determine the tight bound `Θ`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

Using logarithm properties:

Using logarithm properties:

```text
log 1 + log 2 + ... + log n
= log(1 × 2 × ... × n)
= log(n!)
By Stirling's approximation:

Theo Stirling:

`log(n!) = Θ(n log n)`.

Thus:

`Σ[i=1..n] log i = Θ(n log n)`.


</details>

## 6. Special Recursive Patterns

### Problem 17. Three Calls on Size `n/3`

**Problem statement.** Consider the following recursive function:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n / 3)

function(20)
```

Please:

1. set up the time recurrence equation;
2. determine the complexity using Master Theorem.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n / 3)
```

Recurrence:

`T(n) = 3T(n/3) + Θ(1)`.

By Master Theorem:

`T(n) = Θ(n)`.


</details>

### Problem 18. Three Calls on `n-1`

**Problem statement.** Consider the following recursive function:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n - 1)

function(20)
```

Please:

1. set up the recurrence equation;
2. solve the recurrence using expansion or subtract-and-conquer;
3. determine the tight bound `Θ`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n - 1)
```

Recurrence:

`T(n) = 3T(n-1) + Θ(1)`.

The number of calls grows exponentially:

`T(n) = Θ(3^n)`.


</details>

### Problem 19. Three Calls on `0.8n`

**Problem statement.** Consider the following recursive function:

```python
def function3(n):
    if n <= 0:
        return

    for i in range(3):
        function3(0.8 * n)

function3(20)
```
Correctly set up the recurrence equation and determine the time complexity in terms of `n`.
<summary><strong>Show Solution</strong></summary>

Consider:
<summary><strong>Show Solution</strong></summary>

Consider:

```python
def function3(n):
    if n <= 0:
        return

    for i in range(3):
        function3(0.8 * n)
```

The correct recurrence is:

Writing `0.8n = n/1.25`, we have `a = 3`, `b = 1.25`. By Master Theorem:

Writing `0.8n = n/1.25`, we have `a = 3`, `b = 1.25`. By Master Theorem:

`T(n) = Θ(n^(log_{1.25} 3))`.

Since `log_{1.25}3 ≈ 4.923`, we get:

`T(n) = Θ(n^4.923...)`.


</details>

### Problem 20. Recurrence `2T(√n) + log n`

**Problem statement.** Determine the complexity of the recurrence:

`T(n) = 2T(√n) + log n`.

Hint: use variable substitution `m = log n` to transform the recurrence into a form suitable for Master Theorem.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

`T(n) = 2T(√n) + log n`.

Set:

`m = log n`

and:

`S(m) = T(2^m)`.

Since `√n = 2^(m/2)`, it follows that:

`S(m) = 2S(m/2) + m`.

By Master Theorem:

`S(m) = Θ(m log m)`.

Substituting `m = log n`:

`T(n) = Θ(log n · log log n)`.


</details>

### Problem 21. Recurrence `T(√n) + 1`

**Problem statement.** Determine the complexity of the recurrence:

`T(n) = T(√n) + 1`.

Variable substitution `m = log n` can be used.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

`T(n) = T(√n) + 1`.

Setting `m = log n` and `S(m) = T(2^m)`, we get:

`S(m) = S(m/2) + 1`.

Therefore:

`S(m) = Θ(log m)`,

so:

`T(n) = Θ(log log n)`.


</details>

### Problem 22. Recurrence `2T(√n) + 1`

**Problem statement.** Determine the complexity of the recurrence:

`T(n) = 2T(√n) + 1`.

Variable substitution `m = log n` and Master Theorem on the new recurrence can be used.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

`T(n) = 2T(√n) + 1`.

With variable substitution `m = log n`:

`S(m) = 2S(m/2) + 1`.

By Master Theorem:

`S(m) = Θ(m)`.

Thus:

`T(n) = Θ(log n)`.


</details>

### Problem 23. Recursive Function on `√n`

**Problem statement.** Determine the time complexity of the following function:

```python
import math

count = 0

def function(n):
    global count

    if n <= 2:
        return 1
    else:
        function(round(math.sqrt(n)))
        count = count + 1
        return count

print(function(200))
```

Set up the time recurrence and determine how many consecutive square roots can be taken before the argument becomes constant.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
import math

count = 0

def function(n):
    global count

    if n <= 2:
        return 1
    else:
        function(round(math.sqrt(n)))
        count = count + 1
        return count
```

Each call creates only one new call of size approximately `√n`, so:

`T(n) = T(√n) + Θ(1)`.

Therefore:

`T(n) = Θ(log log n)`.


</details>

### Problem 24. Eight Calls to `n/2` and a Cubic Loop

**Problem statement.** Analyze the running time of the following recursive function with respect to `n`:

```python
def function(n):
    if n < 2:
        return

    counter = 0

    for i in range(8):
        function(n / 2)

    for i in range(n ** 3):
        counter = counter + 1
```

Set up the recurrence equation and solve using Master Theorem.
<summary><strong>Show Solution</strong></summary>
<details>
Recurrence:

Recurrence:

Since `n^(log₂8) = n³`, this is the balanced case:

Since `n^(log₂8) = n³`, this is the balanced case:

`T(n) = Θ(n³ log n)`.


</details>

## 7. Further Loop and Recurrence Problems

### Problem 25. Two Nested Linear Loops

**Problem statement.** Determine the time complexity of the following program:

```python
def function(n):
    for i in range(0, n // 3):
        j = 1

        while j <= n:
            j = j + 4
            print("*")

function(20)
```

Analyze the execution count of each loop.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def function(n):
    for i in range(0, n // 3):
        j = 1
        while j <= n:
            j = j + 4
            print("*")
```

The outer loop runs `Θ(n)` times. The inner loop increments `j` by `4` so it also runs `Θ(n)` times.

Therefore:

`T(n) = Θ(n²)`.


</details>

### Problem 26. Two Calls to `n/2`

**Problem statement.** Determine the time complexity of the following recursive function:

```python
def function(n):
    if n <= 0:
        return

    print("*")
    function(n / 2)
    function(n / 2)
    print("*")

function(20)
Set up the recurrence equation and solve using Master Theorem.
<summary><strong>Show Solution</strong></summary>
Set up the recurrence equation and solve using Master Theorem.
Consider:
<details>
<summary><strong>Show Solution</strong></summary>

Consider:

```python
def function(n):
    if n <= 0:
        return

    print("*")
    function(n / 2)
    function(n / 2)
    print("*")
```

Recurrence:
Recurrence:
`T(n) = 2T(n/2) + Θ(1)`.

Theo Master Theorem:
By Master Theorem:
`T(n) = Θ(n)`.


</details>

### Problem 27. Two Nested Logarithmic Loops

**Problem statement.** Determine the time complexity of the following program:

```python
count = 0

def logarithms(n):
    i = 1
    global count

    while i <= n:
        j = i

        while j > 0:
            j = j // 2
            count = count + 1

        i = i * 2

    return count

print(logarithms(10))
```

Calculate the total number of inner loop executions across all values of `i`.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
count = 0

def logarithms(n):
    i = 1
    global count

    while i <= n:
        j = i

        while j > 0:
            j = j // 2
            count = count + 1

        i = i * 2

    return count
```

Values of `i` are `1, 2, 4, ..., 2^k`, with `k = Θ(log n)`.

At level `i = 2^r`, the inner loop runs `Θ(r)` times. Total cost:

```text
1 + 2 + ... + Θ(log n) = Θ(log² n)
```

Therefore:

`T(n) = Θ(log² n)`.


</details>

## 8. Asymptotic Notation Questions

### Problem 28. Sum of `n` Terms of `O(n)`

**Problem statement.** Consider the expression:

`Σ[i=1..n] O(n)`,

where each term is a function of order `O(n)`. Choose a suitable upper bound for the entire sum:

A. `O(n)`  
B. `O(n²)`  
C. `O(n³)`  
D. `O(3n²)`  
E. `O(1.5n²)`

<summary><strong>Show Solution</strong></summary>
<summary><strong>Show Solution</strong></summary>
If:
If:

`Σ[i=1..n] O(n)`,
there are `n` terms, each having bound `O(n)`. Therefore:
there are `n` terms, each having bound `O(n)`. Therefore:

`Σ[i=1..n] O(n) = O(n²)`.

</details>

### Problem 29. True Statements About Big-O

**Problem statement.** Consider three statements, where `k` and `m` are constants:

I. `(n + k)^m = O(n^m)`  
II. `2^(n+1) = O(2^n)`  
III. `2^(2n+1) = O(2^n)`

Determine the correct group of statements:

A. I and II  
B. I and III  
C. II and III  
D. I, II, and III

<summary><strong>Show Solution</strong></summary>
<summary><strong>Show Solution</strong></summary>
Consider the three statements:
Consider three statements:
1. `(n+k)^m = O(n^m)`, with `k`, `m` constants;
2. `2^(n+1) = O(2^n)`;
3. `2^(2n+1) = O(2^n)`.
3. `2^(2n+1) = O(2^n)`.
Statement 1 is true because when `n` is large, `(n+k)^m` has the same order as `n^m`.
Statement 1 is true because when `n` is large, `(n+k)^m` has the same order as `n^m`.
Statement 2 is true because:
Statement 2 is true because:

`2^(n+1) = 2·2^n`.
Statement 3 is false because:
Statement 3 is false because:

`2^(2n+1) / 2^n = 2^(n+1) → ∞`.
Therefore, only statements **I and II** are true.
Therefore, only statements **I and II** are true.

</details>

### Problem 30. Comparing `2^n`, `n!`, and `n^(log n)`

**Problem statement.** Consider three functions:

```text
f(n) = 2^n
g(n) = n!
h(n) = n^(log n)
```

Which of the following statements correctly describes the asymptotic growth relation between the three functions?

A. `f(n) = O(g(n))` and `g(n) = O(h(n))`  
B. `f(n) = Ω(g(n))` and `g(n) = O(h(n))`  
C. `g(n) = O(f(n))` and `h(n) = O(f(n))`  
D. `h(n) = O(f(n))` and `g(n) = Ω(f(n))`

<summary><strong>Show Solution</strong></summary>
<summary><strong>Show Solution</strong></summary>
Consider:
Consider:

```text
f(n) = 2^n
g(n) = n!
h(n) = n^(log n)
```
When `n` is sufficiently large:
When `n` is sufficiently large:

`h(n) < f(n) < g(n)`.
Indeed:
Indeed:

```text
log h(n) = Θ((log n)²)
log f(n) = Θ(n)
log g(n) = Θ(n log n)
```
Therefore:
Therefore:

`h(n) = o(f(n))` and `f(n) = o(g(n))`.


</details>

### Problem 31. Number of Condition Checks in a Doubling Loop

**Problem statement.** Consider the following C code:

```c
j = 1;
while (j <= n) {
    j = j * 2;
}
```

For `n > 0`, determine:

1. the number of loop body executions;
2. the number of condition checks for `j <= n`.
Clearly distinguish these two quantities.
<summary><strong>Show Solution</strong></summary>

Consider:
<summary><strong>Show Solution</strong></summary>

Consider:

```c
j = 1;
while (j <= n) {
    j = j * 2;
}
```
The loop body executes `Θ(log n)` times.
The loop body executes `Θ(log n)` times.
If counting **the number of loop body executions**, the result is `⌊log₂n⌋ + 1` for `n ≥ 1`.
If counting **the number of loop body executions**, the result is `⌊log₂n⌋ + 1` for `n ≥ 1`.
If counting **the number of condition checks for `j <= n`**, add the final failing check.
If counting **the number of condition checks for `j <= n`**, add the final failing check.


</details>

### Problem 32. Prime Checking by Trial Division up to `√n`

**Problem statement.** Consider the prime checking function:

```python
import math

def IsPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
print("Not Prime")
            return 0

    return 1
```
Which of the following statements is true regarding time complexity?
Which of the following statements is true regarding time complexity?
A. `T(n) = O(√n)` and `T(n) = Ω(√n)`  
B. `T(n) = O(√n)` and `T(n) = Ω(1)`  
C. `T(n) = O(√n)` and `T(n) = Ω(n)`  
D. None of the above choices is correct
D. None of the above choices is correct
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
import math

def IsPrime(n):
    for i in range(2, math.sqrt(n)):
print("Not Prime")
            print("Not Prime")
            return 0

    return 1
```

In the worst case, the loop must check up to `Θ(√n)` values, so:

`T(n) = O(√n)`.

In the best case, a divisor can be found immediately:

`T(n) = Ω(1)`.


</details>

### Problem 33. Euclidean Algorithm

**Problem statement.** Consider the Euclidean algorithm for greatest common divisor:

```python
def gcd(m, n):
    if n % m == 0:
        return m

    m = n % m
    return gcd(m, n)
```

Determine the correct statement about the time complexity of the algorithm and explain why a logarithmic lower bound does not necessarily hold for all inputs.
<summary><strong>Show Solution</strong></summary>
<details>
Consider:

Consider:

```python
def gcd(m, n):
    if n % m == 0:
        return m
    m = n % m
    return gcd(m, n)
```
The worst-case complexity of the Euclidean algorithm is:
The worst-case complexity of the Euclidean algorithm is:

`O(log min(m,n))`.
However, one cannot claim a tight lower bound `Ω(log m)` for all inputs, because there are cases where the algorithm terminates after just one step. Therefore, when choices provide a mandatory logarithmic lower bound for all inputs, that choice is incorrect.
However, one cannot claim a tight lower bound `Ω(log m)` for all inputs, because there are cases where the algorithm terminates after just one step. Therefore, when choices provide a mandatory logarithmic lower bound for all inputs, that choice is incorrect.


</details>

### Problem 34. Identifying False Statement

**Problem statement.** Suppose recurrence:

`T(n) = 2T(n/2) + n`, with `T(0) = T(1) = 1`.

Which of the following statements is false?

A. `T(n) = O(n²)`  
B. `T(n) = Θ(n log n)`  
C. `T(n) = Ω(n²)`  
D. `T(n) = O(n log n)`

<summary><strong>Show Solution</strong></summary>
<summary><strong>Show Solution</strong></summary>
Consider:
Consider:

`T(n) = 2T(n/2) + n`.
By Master Theorem:
Theo Master Theorem:

`T(n) = Θ(n log n)`.
Therefore any statement claiming this recurrence has tight bound `Θ(n²)` is false.
Therefore any statement claiming this recurrence has tight bound `Θ(n²)` is false.


</details>

## 9. Multi-tier Loop Analysis and Exponentiation

### Problem 35. Loop with Divisibility Condition

**Problem statement.** Determine the tight time complexity of the following function:

```python
def function(n):
    for i in range(1, n):
        j = i

        while j < i * i:
            j = j + 1

            if j % i == 0:
                for k in range(0, j):
                    print("*")

function(10)
```
Do not merely provide a crude upper bound; analyze the total cost of the `for k` loop across values of `j` and `i`.
<summary><strong>Show Solution</strong></summary>

Consider:
<summary><strong>Show Solution</strong></summary>

Consider:

```python
def function(n):
    for i in range(1, n):
        j = i

        while j < i * i:
            j = j + 1

            if j % i == 0:
                for k in range(0, j):
                    print("*")
```
For each `i`, the `while` loop runs `Θ(i²)` times. However, the `for k` loop is executed only when `j` is a multiple of `i`. There are `Θ(i)` such values in the range from `i` to `i²`, and total cost of the `for k` loops is:
For each `i`, the `while` loop runs `Θ(i²)` times. However, the `for k` loop is executed only when `j` is a multiple of `i`. There are `Θ(i)` such values in the range from `i` to `i²`, and total cost of the `for k` loops is:

```text
i(2 + 3 + ... + i) = Θ(i³)
```
Hence cost for a single value `i` is `Θ(i³)`, and total:
Hence cost for a single value `i` is `Θ(i³)`, and total:

```text
Σ[i=1..n] Θ(i³) = Θ(n⁴)
```
Therefore, a tight analysis for the code snippet is:
Therefore, a tight analysis for the code snippet is:

`T(n) = Θ(n⁴)`.
A looser bound like `O(n⁵)` is still a valid upper bound but not tight.
A looser bound like `O(n⁵)` is still a valid upper bound but not tight.


</details>

### Problem 36. Computing `9^n` by Iterative Multiplication

**Problem statement.** Design a simple algorithm to compute `9^n` by iterative multiplication from `1` and analyze its time complexity.
<summary><strong>Show Solution</strong></summary>
<details>
<summary><strong>Show Solution</strong></summary>

using `n` multiplications, so:
uses `n` multiplications, so:

`T(n) = Θ(n)`.
This can be improved to `Θ(log n)` multiplications using **fast exponentiation / exponentiation by squaring**.
Can be improved to `Θ(log n)` multiplications using **fast exponentiation / exponentiation by squaring**.


</details>

### Problem 37. Improving Exponentiation Algorithm

**Problem statement.** For the problem of computing `9^n` in Problem 36, improve time complexity using *exponentiation by squaring*. State the main idea and complexity of the improved algorithm.
<summary><strong>Show Solution</strong></summary>
<details>
<summary><strong>Show Solution</strong></summary>

This method reduces the number of multiplications from `Θ(n)` down to:
This method reduces the number of multiplications from `Θ(n)` down to:

`Θ(log n)`.


</details>

### Problem 38. Worst-Case Analysis of Branching Loop

**Problem statement.** Consider the following function:

```python
def function(n):
    sum = 0

    for i in range(0, n - 1):
        if i > j:
            sum = sum + 1
        else:
            for k in range(0, j):
                sum = sum - 1

    print(sum)

function(10)
```
Analyze the complexity in the worst case. Also point out that the conclusion depends on the value or range of variable `j`, which is not specified in the code.
<summary><strong>Show Solution</strong></summary>

In the worst case, if the `else` branch is executed `Θ(n)` times and each time the inner loop runs `Θ(n)` times, then:
<summary><strong>Show Solution</strong></summary>

In the worst case, if the `else` branch is executed `Θ(n)` times and each time the inner loop runs `Θ(n)` times, then:

`T(n) = Θ(n²)`.
The conclusion depends on assumptions about `j`; therefore when this variable is not clearly defined, conditions must be stated when giving complexity.
The conclusion depends on assumptions about `j`; therefore when this variable is not clearly defined, conditions must be stated when giving complexity.


</details>

## 10. Recursion Trees and Multi-Branch Recurrences

### Problem 39. Recurrence `T(n) = T(n/2) + T(2n/3) + n²`

**Problem statement.** Solve the following recurrence using the recursion tree method:

`T(n) = T(n/2) + T(2n/3) + n²`.
Determine the work at each level and prove the `Θ` bound of total time.
<summary><strong>Show Solution</strong></summary>

Consider:
<summary><strong>Show Solution</strong></summary>

Consider:

At the first level, non-recursive cost is `n²`.

At the next level:

At the next level:

```text
(n/2)² + (2n/3)²
= (1/4 + 4/9)n²
= (25/36)n²
At level `k`, total work is bounded by:

At level `k`, total work is bounded by:

Since `25/36 < 1`, the sum across the entire tree is a convergent geometric series:

Since `25/36 < 1`, the sum across the entire tree is a convergent geometric series:

```text
T(n) ≤ n² Σ[k≥0] (25/36)^k = Θ(n²)
```
Therefore:
Therefore:

`T(n) = Θ(n²)`.


</details>

### Problem 40. Recurrence `T(n) = T(n/2) + T(n/4) + T(n/8) + n`

**Problem statement.** Determine the complexity of recurrence:

`T(n) = T(n/2) + T(n/4) + T(n/8) + n`.
Guess-and-prove method or recursion tree can be used. Explain why the sum of subproblem sizes is smaller than the parent problem size.
<summary><strong>Show Solution</strong></summary>

Total size of subproblems at each level is smaller than the parent size:
<summary><strong>Show Solution</strong></summary>

Total size of subproblems at each level is smaller than the parent problem size:
Therefore, total work across levels is bounded by:
`n/2 + n/4 + n/8 = 7n/8`.

Therefore, total work across levels is bounded by:

```text
n + (7/8)n + (7/8)²n + ...
```
Hence:
Suy ra:

`T(n) = Θ(n)`.


</details>

## 11. Ranking Growth Rates

### Problem 41. Sorting Functions in Decreasing Order

**Problem statement.** Sort the following functions in decreasing order of asymptotic growth rate:

```text
(n + 1)!
n!
4^n
n·3^n
3^n + n^3 + 20n
3^n
(3/2)^n
4n²
4^(log n)
n² + 200
20n + 500
2^(log n)
n^(2/3)
1
```
When necessary, assume `log` has base `2` and point out functions with the same growth order.
<summary><strong>Show Solution</strong></summary>

When `log` has base `2`:
<summary><strong>Show Solution</strong></summary>

When `log` has base `2`:

and:

and:

Therefore, in asymptotic notation, several functions in the list have the same order.

Therefore, in asymptotic notation, several functions in the list have the same order.


</details>

### Problem 42. Is `3^(n^5) = O(3^n)`?

**Problem statement.** Determine whether the following statement is true or false and prove it:

`3^(n^5) = O(3^n)`.
<summary><strong>Show Solution</strong></summary>
<details>
As `n → ∞`, this ratio approaches infinity. Therefore:

As `n → ∞`, this ratio approaches infinity. Therefore:

`3^(n^5) ∉ O(3^n)`.


</details>

### Problem 43. Is `3^n = O(2^n)`?

**Problem statement.** Determine whether the following statement is true or false and prove it:

`3^n = O(2^n)`.
<summary><strong>Show Solution</strong></summary>
<details>
<summary><strong>Show Solution</strong></summary>

Therefore:

`3^n ∉ O(2^n)`.


</details>

## 12. Summary of Core Techniques

Problem types in this section can be reduced to several core techniques.

**For loops**, accurately determine the change rule of the control variable. If the variable increases linearly, the iteration count is usually `Θ(n)`; if multiplied or divided by a constant, it is usually `Θ(log n)`; if accumulated as `1 + 2 + ... + k`, it can be `Θ(√n)`.

**For nested loops**, do not mechanically multiply loop counts. When the inner loop count depends on the outer variable, express as a summation and simplify.

**For recursion**, the first step is to correctly set up the recurrence relation. Then decide whether to use Master Theorem, substitution, change of variables, recursion tree, or another tool.

**For recurrences containing `√n`**, variable substitution `m = log n` usually transforms them into familiar recurrences in `m`.

**For Big-O, Big-Ω, and Theta questions**, distinguish valid bounds from tight bounds. An expression `O(n^5)` can be correct yet very loose if actual complexity is `Θ(n^4)`.

**For source code**, check termination before analyzing complexity. A loop with an unchanged control variable (e.g. increment step 0) may never terminate.

---

## 13. Self-Practice Exercises

1. Analyze `T(n) = 4T(n-1) - 3` with `T(0) = 1`.
2. Analyze a loop where `i` increases successively by `1, 2, 3, ...`.
3. Solve `T(n) = 3T(n/3) + n log²n`.
4. Solve `T(n) = T(√n) + log log n`.
5. Analyze `T(n) = 4T(√n) + log n` using variable substitution.
6. Use recursion tree to solve `T(n) = T(n/3) + T(2n/3) + n²`.
7. Prove `Σ[i=1..n] log i = Θ(n log n)`.
8. Tightly analyze a code snippet with outer loop `i = 1..n` and inner loop running `n/i` times.
9. Compare `n!`, `2^n`, `n^(log n)`, and `n^100`.
10. Explain the difference between a valid upper bound and a tight bound.
