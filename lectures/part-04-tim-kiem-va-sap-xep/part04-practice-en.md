# Exercises and Solutions — Sorting, Selection, and Searching

> **Scope:** This file includes only exercises from **Chapter 10 (Sorting)** and **Chapter 11 (Searching)** of *Data Structures and Algorithmic Thinking with Python* that are directly related to the two provided Lecture 4 slide files.
>
> Topics outside the scope of those two lecture parts — such as searching in rotated sorted arrays, bitonic search, pair-sum with two pointers, specialized in-place marking techniques, and similar topics — are intentionally excluded.
>
> All **Solutions / Hints** are hidden using `<details>` blocks.

---

# Part A. Sorting

## Exercise 1. Stability of sorting algorithms
*Adapted from Chapter 10, Problem 12; restricted to algorithms covered in the lecture.*

Consider the following four algorithms:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Suppose two records $R$ and $S$ have the same key, and $R$ appears before $S$ in the input.

1. When is a sorting algorithm called **stable**?
2. Which of the four algorithms above are stable in their standard implementations?
3. Why can Quick Sort change the relative order of two records with the same key?

<details>
<summary><strong>Solution / Hint</strong></summary>

A sorting algorithm is **stable** if records with equal keys preserve their relative order after sorting.

| Algorithm | Stable? |
|---|---|
| Bubble Sort | Yes |
| Insertion Sort | Yes |
| Merge Sort | Yes, if equal keys are taken from the left half first |
| Quick Sort | Usually no |

Quick Sort performs swaps during partitioning. Two records with equal keys may be moved across one another, so the standard implementation is not stable.

</details>

---

## Exercise 2. Which algorithms are in-place?
*Adapted from Chapter 10, Problem 13; restricted to algorithms covered in the lecture.*

Consider:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Answer the following:

1. Which algorithms require only a small amount of auxiliary memory?
2. Which algorithm requires an auxiliary array whose size is proportional to $n$?
3. Compare the auxiliary-space requirements of all four algorithms.

<details>
<summary><strong>Solution / Hint</strong></summary>

For standard array-based implementations:

| Algorithm | Auxiliary space |
|---|---:|
| Bubble Sort | $\Theta(1)$ |
| Insertion Sort | $\Theta(1)$ |
| Merge Sort | $\Theta(n)$ |
| Quick Sort | About $\Theta(\log n)$ expected for the recursion stack; up to $\Theta(n)$ in the worst case |

Bubble Sort and Insertion Sort are clearly in-place.

Merge Sort on arrays needs temporary storage during merging, so the standard implementation is not in-place.

Quick Sort partitions directly inside the array, but still uses recursion-stack memory.

</details>

---

## Exercise 3. Compare worst-case complexity
*Adapted from Chapter 10, Problem 49.*

Among the following algorithms:

- Merge Sort
- Bubble Sort
- Quick Sort

which one has the **lowest worst-case time complexity**?

Explain your answer using the complexity results studied in class.

<details>
<summary><strong>Solution / Hint</strong></summary>

Merge Sort has:

$$
T_{\text{Merge}}(n)=\Theta(n\log n)
$$

in the best, average, and worst cases.

Bubble Sort has:

$$
T_{\text{Bubble}}(n)=\Theta(n^2)
$$

in the worst case, while Quick Sort has:

$$
T_{\text{Quick}}(n)=\Theta(n^2)
$$

in the worst case.

Therefore, **Merge Sort** has the best worst-case complexity among the three.

</details>

---

## Exercise 4. Effect of pivot choice in Quick Sort
*Adapted from Chapter 10, Problem 52.*

A Quick Sort implementation sorts in ascending order and always chooses the **first element** as the pivot.

Consider the two inputs:

```text
A = [1, 2, 3, 4, 5]
B = [4, 1, 5, 3, 2]
```

Let $t_1$ and $t_2$ be the number of comparisons made by Quick Sort on $A$ and $B$.

Determine the relationship between $t_1$ and $t_2$, and explain why.

<details>
<summary><strong>Solution / Hint</strong></summary>

For $A$, every pivot is the smallest element in the current subarray.

The partitions therefore have sizes:

$$
0 \quad \text{and} \quad n-1.
$$

Then:

$$
0 \quad \text{and} \quad n-2,
$$

and so on.

This is the most unbalanced possible partitioning pattern and leads to the worst case.

Input $B$ creates more balanced partitions.

Therefore:

$$
\boxed{t_1>t_2}.
$$

</details>

---

## Exercise 5. Recurrence for worst-case Quick Sort
*Adapted from Chapter 10, Problem 56.*

Suppose the pivot is always the smallest or largest value in the active subarray. After partitioning, we obtain:

- one empty subarray;
- the pivot in its final position;
- one subarray containing $n-1$ elements.

1. Write the recurrence for the running time.
2. Solve the recurrence asymptotically.

<details>
<summary><strong>Solution / Hint</strong></summary>

The partition step scans the current subarray, so it costs:

$$
\Theta(n).
$$

The recurrence is:

$$
T(n)=T(n-1)+T(0)+cn.
$$

Ignoring constants:

$$
T(n)=T(n-1)+\Theta(n).
$$

Expanding:

$$
T(n)
=
\Theta(n+(n-1)+(n-2)+\cdots+1)
=
\Theta(n^2).
$$

Therefore, the worst-case running time of Quick Sort is:

$$
\boxed{\Theta(n^2)}.
$$

</details>

---

## Exercise 6. Elements immediately after the median
*Adapted from Chapter 10, Problem 11; directly connected to the Selection section of Lecture 4.*

Given an array $A$ of $n$ elements and an integer $K<n/2$:

Design an approach that outputs, in increasing order, the **$K$ elements immediately after the median** in sorted order without fully sorting the entire array.

Target running time:

$$
O(n+K\log K).
$$

<details>
<summary><strong>Solution / Hint</strong></summary>

There is no need to completely sort all $n$ values.

One possible approach:

1. Find the median using a selection algorithm.
2. Partition the array around the median.
3. Consider only the side containing values larger than the median.
4. Use selection again to isolate the smallest $K$ values in that part.
5. Sort only those $K$ values.

The selection and partition steps take linear time in $n$, while sorting the final $K$ values costs:

$$
O(K\log K).
$$

Thus the total is:

$$
\boxed{O(n+K\log K)}.
$$

The main idea matches the lecture principle:

> Do not sort more than the output actually requires.

</details>

---

## Exercise 7. Find minimum and maximum together
*Adapted from Chapter 10, Problem 53; directly related to the extreme-value section of Lecture 4.*

Given $n$ distinct numbers:

1. If minimum and maximum are found using two independent scans, how many comparisons are required?
2. Design a pairwise method that reduces the number of comparisons.
3. For $n=100$, how many comparisons does the pairwise method require?

<details>
<summary><strong>Solution / Hint</strong></summary>

If we search separately:

- minimum requires $n-1$ comparisons;
- maximum requires $n-1$ comparisons.

Total:

$$
2n-2.
$$

### Pairwise method

For each pair $(a,b)$:

1. Compare $a$ and $b$.
2. Compare the smaller one with `min`.
3. Compare the larger one with `max`.

Using the first two elements to initialize `min` and `max`, for even $n$:

$$
1+3\frac{n-2}{2}
=
\frac{3n}{2}-2.
$$

For $n=100$:

$$
\frac{3(100)}{2}-2=148.
$$

Therefore:

$$
\boxed{148}
$$

comparisons are required.

> **Source note:** the provided book version reports 147 using $\frac{3n}{2}-3$. Under the standard comparison model and initialization using the first two elements, the count for $n=100$ is 148.

</details>

---

# Part B. Searching

## Exercise 8. Detect duplicates using brute force
*Chapter 11, Problem 1.*

Given:

```text
A = [3, 2, 1, 2, 5, 3]
```

Design the simplest algorithm to determine whether the array contains duplicates by comparing pairs of elements.

Analyze the time complexity and auxiliary space.

<details>
<summary><strong>Solution / Hint</strong></summary>

Pseudocode:

```text
FOR i = 0 TO n - 2
    FOR j = i + 1 TO n - 1
        IF A[i] == A[j]
            RETURN TRUE

RETURN FALSE
```

In the worst case, the algorithm checks:

$$
\frac{n(n-1)}{2}
$$

pairs.

Therefore:

$$
T(n)=\Theta(n^2),
\qquad
S(n)=\Theta(1).
$$

</details>

---

## Exercise 9. Detect duplicates using sorting
*Chapter 11, Problem 2.*

Improve Exercise 8 by using sorting.

Describe the algorithm and analyze its complexity.

<details>
<summary><strong>Solution / Hint</strong></summary>

After sorting:

```text
SORT(A)
```

equal values appear next to each other.

Then perform one scan:

```text
FOR i = 0 TO n - 2
    IF A[i] == A[i + 1]
        RETURN TRUE

RETURN FALSE
```

If sorting takes:

$$
O(n\log n),
$$

then the total running time is:

$$
O(n\log n)+O(n)
=
\boxed{O(n\log n)}.
$$

This directly illustrates the Lecture 4 idea:

> Sorting is often not the final goal; it creates structure that makes the next operation easier.

</details>

---

## Exercise 10. Detect duplicates using a hash set
*Chapter 11, Problem 3.*

Solve the duplicate-detection problem again using a `set` or hash table.

Compare this solution with Exercises 8 and 9.

<details>
<summary><strong>Solution / Hint</strong></summary>

Example in Python:

```python
def has_duplicate(A):
    seen = set()

    for x in A:
        if x in seen:
            return True
        seen.add(x)

    return False
```

With hashing:

- expected lookup:
  $$
  O(1);
  $$
- expected insertion:
  $$
  O(1).
  $$

For $n$ values:

$$
T(n)=O(n)
$$

expected, but it requires:

$$
S(n)=O(n).
$$

Comparison:

| Method | Time | Extra space |
|---|---:|---:|
| Brute force | $O(n^2)$ | $O(1)$ |
| Sort + scan | $O(n\log n)$ | depends on sorting method |
| Hash set | expected $O(n)$ | $O(n)$ |

This is a trade-off between time, memory, and data organization.

</details>

---

## Exercise 11. First occurrence using Binary Search
*Chapter 11, Problem 46.*

Given a sorted array containing duplicates:

```text
A = [2, 4, 4, 4, 4, 7, 9, 11]
```

Find the **first index** of `4` in:

$$
O(\log n)
$$

time.

<details>
<summary><strong>Solution / Hint</strong></summary>

When `target` is found, do not stop immediately. Save the position and continue searching to the left.

```text
FUNCTION FIRST_OCCURRENCE(A, target)
    low = 0
    high = LENGTH(A) - 1
    answer = NONE

    WHILE low <= high
        mid = low + (high - low) DIV 2

        IF A[mid] >= target
            IF A[mid] == target
                answer = mid
            high = mid - 1
        ELSE
            low = mid + 1

    RETURN answer
```

Each iteration discards about half of the current search interval:

$$
T(n)=\boxed{O(\log n)}.
$$

For the example, the answer is index `1` using zero-based indexing.

</details>

---

## Exercise 12. Last occurrence using Binary Search
*Chapter 11, Problem 47.*

Using the same array:

```text
A = [2, 4, 4, 4, 4, 7, 9, 11]
```

find the **last index** of `4` in:

$$
O(\log n).
$$

<details>
<summary><strong>Solution / Hint</strong></summary>

When `target` is found, save the position but continue searching to the right.

```text
FUNCTION LAST_OCCURRENCE(A, target)
    low = 0
    high = LENGTH(A) - 1
    answer = NONE

    WHILE low <= high
        mid = low + (high - low) DIV 2

        IF A[mid] == target
            answer = mid
            low = mid + 1
        ELSE IF A[mid] < target
            low = mid + 1
        ELSE
            high = mid - 1

    RETURN answer
```

The running time is:

$$
\boxed{O(\log n)}.
$$

For the example, the answer is index `4`.

</details>

---

## Exercise 13. Count occurrences using two Binary Searches
*Adapted from Chapter 11, Problems 48--50.*

Given the sorted array:

```text
A = [1, 2, 2, 2, 2, 5, 8]
```

Count how many times `target = 2` occurs in:

$$
O(\log n)
$$

time.

<details>
<summary><strong>Solution / Hint</strong></summary>

Find:

- `first` = first occurrence;
- `last` = last occurrence.

If the target does not occur:

```text
count = 0
```

Otherwise:

$$
\text{count}
=
\text{last}-\text{first}+1.
$$

For the example:

```text
first = 1
last  = 4
```

so:

$$
\text{count}=4-1+1=4.
$$

Two Binary Searches still cost only:

$$
O(\log n)+O(\log n)
=
\boxed{O(\log n)}.
$$

</details>

---

## Exercise 14. Linear Search or Binary Search?
*Adapted from Chapter 11, Problem 81.*

Compare:

- Linear Search on 1000 elements using a 5 GHz machine;
- Binary Search on 1,000,000 elements using a 1 GHz machine.

Assume, for simplicity, that each comparison takes approximately one CPU cycle.

1. How many comparisons does Linear Search require in the worst case?
2. About how many comparisons does Binary Search require in the worst case?
3. After accounting for the CPU-speed difference, which approach is still faster?

<details>
<summary><strong>Solution / Hint</strong></summary>

### Linear Search

Worst case:

$$
1000
$$

comparisons.

On a 5 GHz machine:

$$
t_L
\approx
\frac{1000}{5\times10^9}
=
2\times10^{-7}\text{ s}.
$$

### Binary Search

The number of steps is approximately:

$$
\lceil\log_2(1\,000\,000)\rceil
\approx 20.
$$

On a 1 GHz machine:

$$
t_B
\approx
\frac{20}{10^9}
=
2\times10^{-8}\text{ s}.
$$

Therefore, under this simplified model:

$$
\frac{t_L}{t_B}
\approx 10.
$$

Binary Search on **one million elements** is still about 10 times faster in worst-case comparison count, even though it runs on a slower CPU.

This illustrates the growth-rate difference:

$$
\Theta(n)
\quad \text{versus} \quad
\Theta(\log n).
$$

</details>

---

# Part C. Integrated exercise within the scope of the two lectures

## Exercise 15. Choose a method based on data organization

For each situation, choose the most appropriate method from:

- Linear Search
- Binary Search
- Sorting + scan
- Hash set
- Quickselect
- Merge Sort
- Quick Sort

### Situations

1. You need to find one target in an unsorted list and only one query will be made.
2. You have a sorted array and need to search for targets many times.
3. You need to detect duplicates and may use an additional $O(n)$ memory.
4. You need to find the median once and do not need the full sorted output.
5. You need stable sorting with a worst-case guarantee of $\Theta(n\log n)$.
6. You want an in-place sorting method and can accept a worst case of $\Theta(n^2)$.

<details>
<summary><strong>Solution / Hint</strong></summary>

One reasonable choice is:

| Situation | Method |
|---|---|
| 1 | Linear Search |
| 2 | Binary Search |
| 3 | Hash set |
| 4 | Quickselect |
| 5 | Merge Sort |
| 6 | Quick Sort |

Always consider:

- whether the input is already ordered;
- whether stability is required;
- whether the complete sorted order is needed or only one rank;
- memory limits;
- number of queries;
- worst-case guarantees.

</details>

---
