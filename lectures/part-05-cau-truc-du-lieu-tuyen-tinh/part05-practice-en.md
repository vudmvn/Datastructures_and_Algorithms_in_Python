# 📝 Practice Problems, Conceptual Quizzes & Coding Exercises: Linked Lists

> **Course:** Data Structures and Algorithms in Python (DSAI1002)  
> **Topic:** Linear Data Structures – Linked Lists  
> **Reference:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Structure of this Document:**
> - **Part 1:** Conceptual Multiple-Choice Quizzes (12 in-depth questions with detailed explanations)
> - **Part 2:** Theoretical & Analytical Proof Problems (5 rigorous questions)
> - **Part 3:** Hands-on Coding Practice – Easy Level (8 curated LeetCode & GeeksforGeeks problems)
> - **Part 4:** Hands-on Coding Practice – Medium Level (8 curated LeetCode & GeeksforGeeks problems)

---

## 📌 Coding Problem Set Index (LeetCode & GeeksforGeeks)

| No. | Problem Name | Difficulty | Core Technique | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** | 🟢 Easy | 3 Pointers (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Middle of the Linked List** | 🟢 Easy | Fast & Slow Pointers | [#876](https://leetcode.com/problems/middle-of-the-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1) |
| 03 | **Linked List Cycle** | 🟢 Easy | Floyd's Tortoise and Hare | [#141](https://leetcode.com/problems/linked-list-cycle/) | [GfG Practice](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1) |
| 04 | **Merge Two Sorted Lists** | 🟢 Easy | Dummy Sentinel Node | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 05 | **Delete Node Without Head** | 🟢 Easy | Node Value Copying Trick | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 06 | **Remove Duplicates from Sorted List** | 🟢 Easy | Single Pointer Forward Scan | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 07 | **Palindrome Linked List** | 🟢 Easy | Slow/Fast + Reversal + Comparison | [#234](https://leetcode.com/problems/palindrome-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1) |
| 08 | **Intersection of Two Linked Lists** | 🟢 Easy | Two-Pointer Traversal Switch | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |
| 09 | **Remove Nth Node From End** | 🟡 Medium | Two Pointers with Fixed Gap ($N$) | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Linked List Cycle II** | 🟡 Medium | Floyd's Phase 2 Mathematical Reset | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | [GfG Practice](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1) |
| 11 | **Reorder List** | 🟡 Medium | Split + Reverse + Interleave | [#143](https://leetcode.com/problems/reorder-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reorder-list/1) |
| 12 | **Odd Even Linked List** | 🟡 Medium | Multi-pointer In-place Relinking | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** | 🟡 Medium | Elementary Math with Carry Simulation | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Practice](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** | 🟡 Medium | Dummy Node + Pointer Swap | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Practice](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Copy List with Random Pointer** | 🟡 Medium | Interweaving Nodes In-place | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |
| 16 | **Sort List** | 🟡 Medium | Merge Sort on Linked List ($O(n \log n)$) | [#148](https://leetcode.com/problems/sort-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1) |

---

# Part 1: Conceptual Multiple-Choice Quizzes

### Quiz 01. Memory Overhead: Array vs Singly Linked List
In a 64-bit operating system architecture, which statement is **most accurate** regarding the memory cost of storing $n$ integers?

- [ ] A. A singly linked list consumes less memory than an array because its size dynamically expands.
- [ ] B. A singly linked list requires significant additional memory per node for the `next` pointer (8 bytes), plus language-level object header overhead.
- [ ] C. A static array and a singly linked list incur exactly identical memory footprints.
- [ ] D. A singly linked list uses four times as much memory as a doubly linked list.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
- In an array (or C-style contiguous memory buffer), elements are packed side-by-side with zero per-element reference overhead.
- In a singly linked list, each element is wrapped inside an allocated `Node` instance. In 64-bit systems, each node carries at least one 8-byte pointer (`next`). In Python, every object additionally bears object header metadata (`PyObject_HEAD` $\ge 16$ bytes) and an internal dictionary pointer, resulting in significant memory overhead per item.

</details>

---

### Quiz 02. Random Access Complexity
Why does retrieving the $i$-th element (`A[i]`) take $O(1)$ in an array, but $O(n)$ in a singly linked list?

- [ ] A. CPUs do not support reading non-array memory structures.
- [ ] B. Arrays store elements in contiguous physical memory, permitting direct address arithmetic ($\text{Address}(i) = \text{Base} + i \times \text{Size}$), whereas linked list nodes are scattered across the heap and must be traversed sequentially from `head`.
- [ ] C. The linked list `head` pointer does not know the data types of its nodes.
- [ ] D. Python lists are compiled directly into assembly instructions.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
Contiguous memory allocation allows calculating the exact physical memory location in constant time using a single multiplication and addition. In contrast, in a linked list, node $i$ can only be reached by dereferencing node $i - 1$'s `next` pointer, requiring $i$ pointer transitions starting from `head`, which yields worst-case $O(n)$ time.

</details>

---

### Quiz 03. Constant-time Node Deletion
Given a singly linked list of $n$ nodes, in which of the following scenarios can node deletion be accomplished in strictly $O(1)$ time?

- [ ] A. Deleting the last node of the list when only `head` is provided.
- [ ] B. Deleting the node containing a specific target value `x`.
- [ ] C. Deleting the `head` node, or deleting the immediate successor of a known node reference `prev_node`.
- [ ] D. Deleting the $k$-th node from the beginning of the list.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
- Deleting `head`: `self.head = self.head.next` $\implies O(1)$.
- Deleting node right after `prev_node`: `prev_node.next = prev_node.next.next` $\implies O(1)$.
- All other scenarios necessitate sequential traversal from `head` to locate the target node's predecessor, incurring $O(n)$ runtime.

</details>

---

### Quiz 04. Key Advantage of Doubly Linked Lists
What is the primary operational advantage of a Doubly Linked List over a Singly Linked List?

- [ ] A. Lower memory utilization.
- [ ] B. Bidirectional traversal and the capability to delete a known node reference in $O(1)$ time without requiring access to its predecessor.
- [ ] C. Constant-time $O(1)$ random indexing.
- [ ] D. Automatic prevention of cyclical references.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
In a singly linked list, deleting a given node reference requires traversing from `head` to locate the predecessor. In a doubly linked list, the `prev` reference is embedded in the node itself, permitting instant pointer rewiring: `node.prev.next = node.next` and `node.next.prev = node.prev` in $O(1)$ time.

</details>

---

### Quiz 05. Circular Singly Linked List with a `tail` Pointer
If a Circular Singly Linked List maintains only a single reference pointer `tail`, which operations can be executed in $O(1)$ time?

- [ ] A. Only appending to the end (`insert_end`).
- [ ] B. Only prepending to the beginning (`insert_front`).
- [ ] C. Both prepending (`insert_front`) and appending (`insert_end`).
- [ ] D. Neither, because `head` is missing.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
By circular definition, `tail.next` always points directly to `head`.
- **Prepend:** Create `new_node`, set `new_node.next = tail.next`, then `tail.next = new_node`. Do not update `tail`. $\implies O(1)$.
- **Append:** Same as prepend, followed by updating `tail = new_node`. $\implies O(1)$.
Thus, maintaining only `tail` affords instantaneous $O(1)$ access to both ends of the list.

</details>

---

### Quiz 06. The Role of Dummy Sentinel Nodes
What is the primary motivation for introducing a **Dummy (Sentinel) Node** in linked list algorithms?

- [ ] A. Reducing overall runtime from $O(n)$ to $O(\log n)$.
- [ ] B. Eliminating edge-case handling (such as empty lists or updates to `head`), simplifying code logic.
- [ ] C. Minimizing auxiliary heap memory.
- [ ] D. Automatically converting a linear list into a circular structure.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
A dummy node (`dummy = ListNode(0, head)`) ensures that every active node in the list—including the first one—always has a predecessor. This avoids repetitive `if head is None` or `if curr == head` checks, preventing `NullPointer` / `AttributeError` bugs.

</details>

---

### Quiz 07. Floyd's Cycle Detection Mechanics
In Floyd's Tortoise and Hare algorithm, what guarantees that `fast` (moving 2 steps) will always intercept `slow` (moving 1 step) inside a loop?

- [ ] A. The `fast` pointer reverses direction when reaching the cycle boundary.
- [ ] B. At each iteration, the relative distance between `fast` and `slow` along the cycle direction decreases by exactly 1 ($2 - 1 = 1$). Since this distance is a finite integer, it strictly converges to 0 without skipping.
- [ ] C. The `slow` pointer halts and waits for `fast`.
- [ ] D. The Master Theorem governs the convergence rate.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
Once both pointers reside within a cycle of length $C$, let their separation distance along the traversal direction be $d$. In each step, `fast` gains 1 step on `slow`. The updated gap is $(d - 1) \pmod C$. Because the distance decrements by 1 step at every tick, it must eventually reach 0, meaning `fast` cannot skip over `slow`.

</details>

---

### Quiz 08. Feasibility of Binary Search on a Sorted Linked List
Why is Binary Search ineffective for achieving $O(\log n)$ lookup on a sorted Singly Linked List?

- [ ] A. Linked lists cannot maintain ordered values.
- [ ] B. Node comparisons take $O(n)$ time.
- [ ] C. Linked lists lack $O(1)$ random access to the midpoint; finding the middle node requires sequential traversal taking $O(k)$ time, keeping the overall runtime at $O(n)$.
- [ ] D. Binary search can achieve $O(\log n)$ if implemented with two pointers.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
The binary search recurrence on an array is $T(n) = T(n/2) + O(1) \implies O(\log n)$. On a linked list, locating the middle element of a sublist of length $k$ takes $O(k)$ steps. The recurrence becomes:
$$T(n) = T(n/2) + O(n) \implies T(n) = O(n)$$
Hence, Binary Search provides zero asymptotic improvement over linear search on standard linked lists. Efficient binary searching requires multi-level pointer skipping structures like **Skip Lists**.

</details>

---

### Quiz 09. Hardware Cache Locality & Performance
From the perspective of computer systems and CPU architecture, why is iterating through an array of $1,000,000$ integers typically 5 to 20 times faster than traversing a linked list of $1,000,000$ nodes, despite both having $O(n)$ theoretical complexity?

- [ ] A. Linked list traversals increase CPU clock frequencies.
- [ ] B. Arrays enjoy high **Spatial Locality**: loading one element preloads adjacent elements into CPU L1/L2 cache lines (64 bytes), whereas linked list nodes reside at fragmented heap addresses, triggering frequent, high-latency **Cache Misses**.
- [ ] C. Python only supports cache optimizations for built-in sequences.
- [ ] D. Node pointers saturate CPU registers.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
Modern CPUs rely heavily on multi-level caching. Contiguous array blocks ensure nearly 100% cache hit rates. In contrast, traversing a linked list (`curr = curr.next`) involves chasing memory pointers to unpredictable heap addresses, constantly causing cache misses that force CPU stalls while waiting for main RAM data transfers.

</details>

---

### Quiz 10. Two-Pointer Setup for $k$-th Node from End
To locate the $k$-th node from the end of a singly linked list in a **single pass**, how many initial steps must pointer `fast` advance ahead of pointer `slow`?

- [ ] A. $k - 1$ steps
- [ ] B. $k$ steps
- [ ] C. $k + 1$ steps
- [ ] D. $2k$ steps

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
By advancing `fast` by exactly $k$ steps ahead of `slow`, a fixed window of width $k$ is established. When `fast` eventually steps past the final node (`fast is None`), `slow` is positioned exactly $k$ nodes behind the termination point, identifying the $k$-th node from the end.

</details>

---

### Quiz 11. Minimum Pointers for In-place List Reversal
What is the minimum number of pointer variables required to reverse a singly linked list in-place without losing nodes?

- [ ] A. 1 pointer
- [ ] B. 2 pointers
- [ ] C. 3 pointers
- [ ] D. 4 pointers

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
Three pointers are essential:
1. `prev`: tracks the newly reversed head.
2. `curr`: the current node being redirected.
3. `next_node`: temporarily holds `curr.next` before the link is overwritten (`curr.next = prev`), preventing the loss of the remaining sublist.

</details>

---

### Quiz 12. Detecting Even vs Odd Length in a Single Pass
To determine whether a singly linked list has an even or odd total number of nodes in the fewest possible loop iterations, one should:

- [ ] A. Traverse and count all nodes, then evaluate `count % 2`.
- [ ] B. Step a pointer forward by 2 nodes per iteration (`current = current.next.next`). If it halts at `current is None`, length is even; if it halts at `current.next is None`, length is odd.
- [ ] C. Reverse the list and compare head and tail.
- [ ] D. Convert the list into a Python array first.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
Option B accomplishes the determination in $\lceil n/2 \rceil$ iterations:
- Loop: `while current is not None and current.next is not None: current = current.next.next`
- Termination:
  - If `current is None`: even number of nodes.
  - If `current.next is None`: odd number of nodes.

</details>

---

# Part 2: Theoretical & Analytical Problems

## Problem T1. Loop Invariant Analysis of In-Place List Reversal

### Prompt
Consider the standard iterative list reversal implementation:

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

1. Formulate the **Loop Invariant** for the `while` loop.
2. Prove algorithm correctness via **Initialization**, **Maintenance**, and **Termination**.

<details>
<summary><strong>Detailed Proof</strong></summary>

### 1. Loop Invariant Formulation
At the beginning of each iteration of the `while` loop:
- Pointer `prev` points to the head of a correctly reversed sublist consisting of all nodes originally at indices $0$ through $i - 1$.
- Pointer `curr` points to the head of the unreversed sublist consisting of all nodes originally at indices $i$ through $n - 1$.
- No node in the reversed sublist points to any node in the unreversed sublist.

### 2. Proof Steps
- **Initialization:** Prior to iteration 1, `prev = None` and `curr = head`. The reversed list is empty, and the unreversed list comprises all $n$ nodes. Invariant holds trivially.
- **Maintenance:** During the loop body:
  - Stash `next_node = curr.next`.
  - Redirect `curr.next = prev`, making `curr` the new head of the reversed prefix.
  - Advance `prev = curr` and `curr = next_node`.
  Now `prev` encompasses the first $i$ reversed nodes, and `curr` points to node $i + 1$. The invariant is maintained for the subsequent cycle.
- **Termination:** The loop terminates when `curr is None`. By the invariant, `prev` points to the head of the fully reversed list containing all $n$ nodes. Returning `prev` is provably correct. $\blacksquare$

</details>

---

## Problem T2. Mathematical Proof of Floyd's Cycle Detection Phase 2

### Prompt
In LeetCode #142, after `slow` and `fast` pointers collide within a cycle, setting `ptr1 = head` and `ptr2 = meeting_node` and moving both forward at 1 step per cycle guarantees they will collide precisely at the **cycle entrance**. Prove this mathematically.

<details>
<summary><strong>Detailed Proof</strong></summary>

### Mathematical Derivation
Define geometric distances:
- $L_1$: distance from `head` to the cycle entrance node.
- $L_2$: distance from the cycle entrance node to the collision point.
- $C$: total number of nodes in the cycle ($C \ge 1$).

```text
head ---------( L1 )---------> [Cycle Entry] ---------( L2 )---------> [Collision Point]
                                     ^                                          |
                                     |----------------( C - L2 )----------------+
```

1. **Distance Equations at First Collision:**
   - Distance traveled by `slow`: $d_{\text{slow}} = L_1 + L_2$
   - Distance traveled by `fast`: $d_{\text{fast}} = L_1 + L_2 + k \cdot C$ (for integer $k \ge 1$)

2. **Speed Relationship ($d_{\text{fast}} = 2 \cdot d_{\text{slow}}$):**
   $$L_1 + L_2 + k \cdot C = 2(L_1 + L_2)$$
   $$\implies k \cdot C = L_1 + L_2$$
   $$\implies L_1 = k \cdot C - L_2 = (k - 1) \cdot C + (C - L_2)$$

3. **Physical Interpretation:**
   - Left hand ($L_1$): distance from `head` to `Cycle Entry`.
   - Right hand ($(k - 1)C + (C - L_2)$): traveling $(k - 1)$ complete cycles plus the remaining $(C - L_2)$ steps from `Collision Point` to `Cycle Entry`.
   - Because both distances are identical, marching `ptr1` from `head` and `ptr2` from `Collision Point` at identical speeds will cause them to collide after exactly $L_1$ steps at the **cycle entry node**. $\blacksquare$

</details>

---

## Problem T3. Why Merge Sort Outperforms Quick Sort on Linked Lists

### Prompt
Explain why **Merge Sort** is universally preferred over **Quick Sort** for sorting linked lists across three criteria:
1. Auxiliary memory during merging/partitioning.
2. Partitioning mechanics and node access patterns.
3. Stability.

<details>
<summary><strong>Detailed Analysis</strong></summary>

| Criterion | Array | Linked List |
|---|---|---|
| **Auxiliary Merge Space** | Merging arrays requires $O(n)$ auxiliary buffer allocation. | Merging linked lists requires zero memory allocation; it merely splices existing pointer links in-place $\implies S(n) = O(1)$ iterative or $O(\log n)$ recursive stack. |
| **Partitioning Mechanics** | Quick Sort partitions arrays via bidirectional two-pointer scanning ($O(1)$ random indexing). | Singly linked lists cannot be scanned backwards. Selecting pivots and performing in-place partitioning is inefficient. |
| **Stability** | Array Merge Sort is stable; Quick Sort is unstable. | Linked List Merge Sort naturally preserves stable order for equal elements without additional overhead. |

**Conclusion:** With worst-case $O(n \log n)$ guarantee and in-place pointer merging, **Merge Sort** is the definitive sorting algorithm for linked structures.

</details>

---

## Problem T4. Stack & Queue Design via Linked List ADT

### Prompt
Specify design architectures implementing:
1. **Stack ADT** (`push`, `pop`, `peek`) in $O(1)$ worst-case time.
2. **Queue ADT** (`enqueue`, `dequeue`, `front`) in $O(1)$ worst-case time.

<details>
<summary><strong>Architectural Solution</strong></summary>

### 1. Stack Implementation (Stack Top at `head`)
- `push(x)`: Prepend to head (`new_node.next = self.head; self.head = new_node`) $\implies O(1)$.
- `pop()`: Remove head (`val = self.head.val; self.head = self.head.next; return val`) $\implies O(1)$.
- `peek()`: Inspect `self.head.val` $\implies O(1)$.

### 2. Queue Implementation (Head at `front`, Tail at `rear`)
- `enqueue(x)`: Append to tail (`self.tail.next = new_node; self.tail = new_node`) $\implies O(1)$.
- `dequeue()`: Pop from head (`val = self.head.val; self.head = self.head.next`) $\implies O(1)$.
- `front()`: Inspect `self.head.val` $\implies O(1)$.

</details>

---

## Problem T5. Real-world Memory Footprint of Python Nodes

### Prompt
In 64-bit CPython:
1. Calculate the memory consumption of a default `Node` instance:
   ```python
   class Node:
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
2. Contrast with an optimized `__slots__` implementation:
   ```python
   class OptimizedNode:
       __slots__ = ['val', 'next']
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
3. Discuss practical implications for large-scale graph/node systems.

<details>
<summary><strong>Memory Calculation & Discussion</strong></summary>

### 1. Standard Node Overhead
- Standard objects allocate an instance `__dict__` to permit arbitrary dynamic attributes.
- `PyObject_HEAD`: 16 bytes.
- Reference to `__dict__`: 8 bytes.
- Dedicated `__dict__` object: $\ge 104$ bytes.
$\implies$ Total memory per standard node is **150–160 bytes**.

### 2. `__slots__` Optimization
- Eliminates `__dict__` entirely, allocating attributes as a fixed-size C array of pointers:
- `PyObject_HEAD`: 16 bytes.
- `val` reference: 8 bytes.
- `next` reference: 8 bytes.
$\implies$ Total memory per optimized node is exactly **48 bytes** ($>70\%$ memory reduction).

### 3. Practical Impact
When processing $10,000,000$ nodes (e.g. graph or pipeline queues), standard nodes consume $\approx 1.5 \text{ GB}$ RAM purely for structural overhead, whereas `__slots__` reduces this to $\approx 480 \text{ MB}$.

</details>

---

# Part 3: Easy Level Coding Exercises

## Problem 01. Reverse Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 206 | GfG: Reverse a linked list
- **Online Judges:** [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1)

### Description
Given the `head` of a singly linked list, reverse the list in-place and return the reversed list's head.

```python
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 02. Middle of the Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 876 | GfG: Finding middle element in a linked list
- **Online Judges:** [LeetCode #876](https://leetcode.com/problems/middle-of-the-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1)

### Description
Given the `head` of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.

```python
def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 03. Linked List Cycle Detection

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 141 | GfG: Detect Loop in linked list
- **Online Judges:** [LeetCode #141](https://leetcode.com/problems/linked-list-cycle/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)

### Description
Given `head`, determine if the linked list has a cycle in it using $O(1)$ memory.

```python
def hasCycle(head: ListNode) -> bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 04. Merge Two Sorted Lists

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 21 | GfG: Merge two sorted linked lists
- **Online Judges:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

### Description
Merge two sorted linked lists into one sorted list by splicing together the existing nodes.

```python
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 is not None else list2
    return dummy.next
```

- **Time Complexity:** $T(m, n) = O(m + n)$.
- **Auxiliary Space:** $S(m, n) = O(1)$.

---

## Problem 05. Delete Node Without Head Pointer

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 237 | GfG: Delete without head pointer
- **Online Judges:** [LeetCode #237](https://leetcode.com/problems/delete-node-in-a-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1)

### Description
Delete a given non-tail node when no access to `head` is granted.

```python
def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
```

- **Time Complexity:** $T(n) = O(1)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 06. Remove Duplicates from Sorted List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 83 | GfG: Remove duplicate element from sorted Linked List
- **Online Judges:** [LeetCode #83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

### Description
Delete all duplicates from a sorted linked list so that each element appears only once.

```python
def deleteDuplicates(head: ListNode) -> ListNode:
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 07. Palindrome Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 234 | GfG: Check if Linked List is Palindrome
- **Online Judges:** [LeetCode #234](https://leetcode.com/problems/palindrome-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1)

### Description
Return `True` if a linked list is a palindrome in $O(n)$ time and $O(1)$ space.

```python
def isPalindrome(head: ListNode) -> bool:
    if head is None or head.next is None:
        return True

    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first_half = head
    second_half = prev
    while second_half is not None:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 08. Intersection of Two Linked Lists

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 160 | GfG: Intersection Point in Y Shaped Linked Lists
- **Online Judges:** [LeetCode #160](https://leetcode.com/problems/intersection-of-two-linked-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)

### Description
Find and return the node where two singly linked lists intersect, or `None` if they do not intersect.

```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None
    pA, pB = headA, headB
    while pA is not pB:
        pA = pA.next if pA is not None else headB
        pB = pB.next if pB is not None else headA
    return pA
```

- **Time Complexity:** $T(m, n) = O(m + n)$.
- **Auxiliary Space:** $S(m, n) = O(1)$.

---

# Part 4: Medium Level Coding Exercises

## Problem 09. Remove Nth Node From End of List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 19 | GfG: Nth node from end of linked list
- **Online Judges:** [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1)

### Description
Remove the $n$-th node from the end of the list and return its head in one single pass.

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

- **Time Complexity:** $T(L) = O(L)$.
- **Auxiliary Space:** $S(L) = O(1)$.

---

## Problem 10. Linked List Cycle II (Find Cycle Start)

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 142 | GfG: Find the first node of loop in linked list
- **Online Judges:** [LeetCode #142](https://leetcode.com/problems/linked-list-cycle-ii/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1)

### Description
Return the node where the cycle begins without modifying list structure.

```python
def detectCycle(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return None
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    ptr1 = head
    ptr2 = slow
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 11. Reorder List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 143 | GfG: Reorder List
- **Online Judges:** [LeetCode #143](https://leetcode.com/problems/reorder-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reorder-list/1)

### Description
Reorder $L_0 \to L_1 \dots \to L_n$ into $L_0 \to L_n \to L_1 \to L_{n-1} \dots$ in-place.

```python
def reorderList(head: ListNode) -> None:
    if head is None or head.next is None:
        return

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    curr = second
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    first = head
    while second is not None:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 12. Odd Even Linked List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 328 | GfG: Rearrange a linked list
- **Online Judges:** [LeetCode #328](https://leetcode.com/problems/odd-even-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1)

### Description
Group odd-indexed nodes followed by even-indexed nodes in-place.

```python
def oddEvenList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 13. Add Two Numbers

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 2 | GfG: Add two numbers represented by linked lists
- **Online Judges:** [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1)

### Description
Add two numbers represented by reversed linked lists and return the resulting sum.

```python
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry > 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    return dummy.next
```

- **Time Complexity:** $T(m, n) = O(\max(m, n))$.
- **Auxiliary Space:** $S(m, n) = O(\max(m, n))$.

---

## Problem 14. Swap Nodes in Pairs

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 24 | GfG: Pairwise swap elements of a linked list
- **Online Judges:** [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

### Description
Swap adjacent node pairs by manipulating node pointers.

```python
def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 15. Copy List with Random Pointer

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 138 | GfG: Clone a linked list with next and random pointer
- **Online Judges:** [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

### Description
Construct a Deep Copy of a list containing `random` pointers in $O(1)$ auxiliary space.

```python
def copyRandomList(head: 'NodeWithRandom') -> 'NodeWithRandom':
    if head is None:
        return None

    curr = head
    while curr is not None:
        copy_node = NodeWithRandom(curr.val, curr.next)
        curr.next = copy_node
        curr = copy_node.next

    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next

    dummy = NodeWithRandom(0)
    copy_tail = dummy
    curr = head
    while curr is not None:
        copy_node = curr.next
        curr.next = copy_node.next
        copy_tail.next = copy_node
        copy_tail = copy_node
        curr = curr.next

    return dummy.next
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

---

## Problem 16. Sort List (Merge Sort on Linked List)

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 148 | GfG: Sort a linked list
- **Online Judges:** [LeetCode #148](https://leetcode.com/problems/sort-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1)

### Description
Sort a linked list in $O(n \log n)$ time using recursive Merge Sort.

```python
def sortList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    prev = None
    slow = fast = head
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None

    left = sortList(head)
    right = sortList(slow)
    return merge(left, right)

def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return dummy.next
```

- **Time Complexity:** $T(n) = O(n \log n)$.
- **Auxiliary Space:** $S(n) = O(\log n)$.

---

> © 2026 Dr. Minh Duc Vu – Faculty of Data Science & Artificial Intelligence, National Economics University (NEU).
