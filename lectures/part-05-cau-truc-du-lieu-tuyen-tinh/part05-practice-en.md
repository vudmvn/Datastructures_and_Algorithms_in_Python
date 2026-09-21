# 📝 Practice Problems, Conceptual Quizzes & Coding Exercises: Linked Lists

> **Course:** Data Structures and Algorithms with Python (DSAI1002)  
> **Topic:** Linear Data Structures – Linked Lists  
> **Reference:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Structure of this Document:**
> - **Part 1:** Conceptual Multiple-Choice Quizzes (12 questions with detailed answers and explanations)
> - **Part 2:** Theoretical & Analytical Problems (5 in-depth architectural and complexity problems)
> - **Part 3:** Core ADT Implementation & Operations – Singly, Doubly & Circular Linked Lists (3 comprehensive problems covering Insert, Delete, Traversal)
> - **Part 4:** Coding Practice – Easy Level (8 curated LeetCode & GeeksforGeeks problems with complete Python solutions)
> - **Part 5:** Coding Practice – Medium Level (8 curated LeetCode & GeeksforGeeks problems with complete Python solutions)

---

## 📌 Coding Problem Set Index (LeetCode & GeeksforGeeks)

### Group I: Core Data Structures & Operations (Insert / Delete / Traversal)

| No. | Problem Name | Structure | Core Operations | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| C01 | **Design Singly Linked List** | Singly LL | `traverse`, `addAtHead`, `addAtTail`, `addAtIndex`, `deleteAtIndex` | [#707](https://leetcode.com/problems/design-linked-list/) | [GfG Insertion](https://www.geeksforgeeks.org/problems/linked-list-insertion/1) \| [GfG Deletion](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1) \| [GfG Search](https://www.geeksforgeeks.org/problems/search-in-linked-list/1) |
| C02 | **Doubly Linked List Operations** | Doubly LL | Insert after node `p`, delete at position `pos`, bidirectional traversal | — | [GfG Insert DLL](https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1) \| [GfG Delete DLL](https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1) \| [GfG Display DLL](https://www.geeksforgeeks.org/problems/display-doubly-linked-list/1) |
| C03 | **Circular Linked List Operations** | Circular LL | Circular traversal (`curr != head`), insert at head/tail with `tail`, delete node | — | [GfG Traversal](https://www.geeksforgeeks.org/problems/circular-linked-list-traversal/1) \| [GfG Insertion](https://www.geeksforgeeks.org/problems/insert-in-sorted-circular-linked-list/1) \| [GfG Deletion](https://www.geeksforgeeks.org/problems/deletion-in-circular-linked-list/1) |

### Group II: Hands-on Coding Practice – Easy Level

| No. | Problem Name | Difficulty | Core Technique | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** | 🟢 Easy | 3 Pointers (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Remove Linked List Elements** | 🟢 Easy | Dummy Sentinel Node | [#203](https://leetcode.com/problems/remove-linked-list-elements/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1) |
| 03 | **Merge Two Sorted Lists** | 🟢 Easy | Dummy Sentinel + 2-Pointer Comparison | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 04 | **Delete Node Without Head** | 🟢 Easy | Adjacent Node Value Copy Trick | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 05 | **Remove Duplicates from Sorted List** | 🟢 Easy | Sequential Traversal & Duplicate Skip | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 06 | **Binary to Integer in Linked List** | 🟢 Easy | Bit Shift / Horner's Method ($2 	imes 	ext{ans} + 	ext{val}$) | [#1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/decimal-equivalent-of-binary-linked-list/1) |
| 07 | **Reverse a Doubly Linked List** | 🟢 Easy | Pointer Swap (`prev` $\leftrightarrow$ `next`) | — | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1) |
| 08 | **Intersection of Two Linked Lists** | 🟢 Easy | Length Difference Offset $\|L_A - L_B\|$ | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |

### Group III: Hands-on Coding Practice – Medium Level

| No. | Problem Name | Difficulty | Core Technique | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 09 | **Remove Nth Node From End** | 🟡 Medium | Two-Pass Length Counting ($L - n$) + Dummy | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Rotate List** | 🟡 Medium | Temporary Ring Connection + Split at $(L - k)$ | [#61](https://leetcode.com/problems/rotate-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1) |
| 11 | **Partition List** | 🟡 Medium | Dual Dummy Pointers (`less` and `greater`) | [#86](https://leetcode.com/problems/partition-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/partition-a-linked-list/1) |
| 12 | **Odd Even Linked List** | 🟡 Medium | Multi-pointer In-place Relinking | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** | 🟡 Medium | Elementary Addition with Carry Simulation | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Practice](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** | 🟡 Medium | Dummy Node + 3-Pointer Relinking | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Practice](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Remove Duplicates II** | 🟡 Medium | Sentinel Node + Sublist Skipping | [#82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-all-occurences-of-duplicates-in-a-linked-list/1) |
| 16 | **Copy List with Random Pointer** | 🟡 Medium | Interweaving Nodes In-place ($O(1)$ Space) | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |
---

# Part 1: Conceptual Multiple-Choice Quizzes

### Quiz 01. Memory Overhead: Array vs. Singly Linked List
In a 64-bit operating system architecture, which of the following statements is **most accurate** regarding the memory cost of storing $n$ integers?

- [ ] A. A singly linked list always consumes less memory than an array because its size dynamically adjusts.
- [ ] B. A singly linked list consumes additional memory for the `next` pointer (8 bytes) at each node, along with the object header overhead of each node.
- [ ] C. A static array and a singly linked list incur exactly identical memory footprints.
- [ ] D. A singly linked list uses four times as much memory as a doubly linked list.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
- In an array (or C-style contiguous memory buffer), elements are packed side-by-side with zero per-element reference overhead (e.g., 4 or 8 bytes per number).
- In a singly linked list, each element is wrapped inside an allocated `Node` instance. In 64-bit systems, each node carries at least one 8-byte pointer (`next`). In Python, every object additionally bears object header metadata (`PyObject_HEAD` $\ge 16$ bytes) and dictionary pointer overhead. Thus, linked lists incur significantly higher **memory overhead** than contiguous arrays.

</details>

---

### Quiz 02. Random Access Complexity
Why does accessing the $i$-th element (`A[i]`) take $O(1)$ time in an array, but $O(n)$ time in a singly linked list?

- [ ] A. CPUs do not support reading memory from linked list nodes.
- [ ] B. Arrays allocate elements in contiguous physical memory, enabling direct memory address calculation via $\text{Address}(i) = \text{Base} + i \times \text{Size}$, whereas linked list nodes are scattered across the heap and must be sequentially traversed from `head`.
- [ ] C. The linked list `head` pointer does not know the data types stored in its nodes.
- [ ] D. Python lists are compiled directly into native assembly instructions.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
Contiguous memory allocation allows calculating the exact physical memory location in constant time using a single multiplication and addition: $\text{Base} + i \times \text{SizeOfElement}$, achieving $O(1)$ access.
In a linked list, nodes reside at arbitrary addresses on the heap. Node $i$ can only be located by dereferencing the `next` pointer of node $i - 1$. Reaching node $i$ strictly requires $i$ pointer dereferences starting from `head`, yielding worst-case $O(n)$ runtime.

</details>

---

### Quiz 03. Pointer Assignment Order when Inserting After a Given Node
Given a singly linked list and a known node pointer `p`, we want to insert a new node `new_node` immediately after `p`. Which sequence of pointer assignments is **correct** to avoid losing the remainder of the list?

- [ ] A. `p.next = new_node; new_node.next = p.next`
- [ ] B. `new_node.next = p.next; p.next = new_node`
- [ ] C. `p = new_node; new_node.next = p`
- [ ] D. `new_node.next = p; p.next = new_node.next`

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
- Step 1: `new_node.next = p.next` (links the new node to the existing successor of `p`).
- Step 2: `p.next = new_node` (redirects `p`'s forward pointer to `new_node`).
- If option A were executed (`p.next = new_node` first), the original reference to the rest of the list would be overwritten and permanently lost (resulting in a memory leak / lost sublist).

</details>

---

### Quiz 04. Key Advantage of Doubly Linked List over Singly Linked List
What is the primary operational advantage of a Doubly Linked List over a Singly Linked List?

- [ ] A. It uses less memory because it does not require a `None` pointer at the end.
- [ ] B. It supports bidirectional traversal (forward and backward) and allows deleting a known node in $O(1)$ time without traversing from `head` to find its predecessor.
- [ ] C. It allows accessing the $i$-th element in $O(1)$ time.
- [ ] D. It automatically keeps elements sorted in ascending order.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
In a singly linked list, even if we hold a direct pointer to the `node` to be deleted, we cannot remove it in standard $O(1)$ time because we do not know its predecessor. In a doubly linked list, thanks to `node.prev`, we can directly bypass it:
`node.prev.next = node.next` and `node.next.prev = node.prev` in $O(1)$ time without any predecessor search.

</details>

---

### Quiz 05. Pointer Mechanics in Circular Singly Linked List with `tail`
If a Circular Singly Linked List maintains only a single reference pointer `tail`, which operations can be executed in $O(1)$ time?

- [ ] A. Insertion at the end only.
- [ ] B. Insertion at the beginning only.
- [ ] C. Both insertion at the beginning (`insert_front`) and insertion at the end (`insert_end`).
- [ ] D. No operation can achieve $O(1)$ without an explicit `head` pointer.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
Because the list is circular, the last node always points back to the first node: `tail.next` is effectively `head`!
- **Insert front:** Create `new_node`, set `new_node.next = tail.next`, then `tail.next = new_node`. Keep `tail` unchanged. $\to O(1)$.
- **Insert end:** Same as insert front, but also update `tail = new_node`. $\to O(1)$.
Thus, with a single `tail` pointer, we can access both the last node and the first node in $O(1)$ time!

</details>

---

### Quiz 06. Dummy Sentinel Node Pattern
What is the primary motivation for using a **Dummy Node** (or **Sentinel Node**) when manipulating linked lists?

- [ ] A. It accelerates algorithms from $O(n)$ down to $O(\log n)$.
- [ ] B. It simplifies source code by eliminating `if head is None` checks and special edge cases when inserting or deleting at the list head.
- [ ] C. It minimizes the auxiliary memory footprint of the program.
- [ ] D. It automatically transforms a singly linked list into a circular linked list.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
A dummy node is a sentinel node placed immediately before `head` (`dummy = ListNode(0, head)`). When inserting or deleting at the front, the operation becomes indistinguishable from inserting or deleting in the middle (the predecessor is always `dummy`). This completely removes boundary checks, prevents `AttributeError: 'NoneType' object has no attribute 'next'`, and keeps the code concise and clean.

</details>

---

### Quiz 07. Deleting the Last Node in a Singly Linked List with a `tail` Pointer
Given a Singly Linked List maintaining both `head` and `tail` pointers. What is the time complexity of deleting the last node (`delete_end`)?

- [ ] A. $O(1)$ because we already maintain a `tail` pointer.
- [ ] B. $O(n)$ because although we have `tail`, we must still traverse from `head` to the second-to-last node ($n - 1$) to update its `next` pointer to `None`.
- [ ] C. $O(\log n)$.
- [ ] D. $O(1)$ amortized.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
This is a classic algorithmic pitfall:
- In a singly linked list, pointers are strictly unidirectional. To delete `tail`, we must update the `next` pointer of its predecessor node to `None` and move `tail` backwards.
- However, `tail` cannot step backward! We must traverse $n - 1$ steps from `head` to locate the $(n - 1)$-th node. Therefore, deleting the tail remains $O(n)$. (In a Doubly Linked List, this operation becomes $O(1)$ via `tail.prev`).

</details>

---

### Quiz 08. Binary Search on a Sorted Linked List
Why can we **not** effectively apply Binary Search to achieve $O(\log n)$ runtime on a sorted Singly Linked List?

- [ ] A. Linked lists cannot store elements in sorted order.
- [ ] B. Node comparisons in a linked list require $O(n)$ time.
- [ ] C. Linked lists do not support $O(1)$ random access to the median element (`mid`); locating the middle node in a sublist of size $k$ takes $O(k)$ steps, causing the total recurrence to resolve to $O(n)$.
- [ ] D. Binary Search achieves $O(\log n)$ on linked lists if double pointers are used.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
The recurrence relation for Binary Search on an array is:
$$T(n) = T(n/2) + O(1) \implies T(n) = O(\log n)$$
(because `mid = (low + high) // 2` is computed in $O(1)$).
On a linked list, locating the middle node of a segment of length $k$ requires $O(k)$ sequential steps:
$$T(n) = T(n/2) + O(n) \implies T(n) = O(n)$$
Thus, Binary Search on a linked list provides zero asymptotic improvement over standard Linear Search ($O(n)$).

</details>

---

### Quiz 09. Cache Locality and Hardware Performance
From the perspective of computer architecture and CPU caches, why is iterating over an array of $1,000,000$ integers typically 5 to 20 times faster than iterating over a linked list of $1,000,000$ nodes, despite both having a theoretical complexity of $O(n)$?

- [ ] A. Linked lists cause CPU temperature spikes.
- [ ] B. Arrays exhibit superior **Spatial Locality**; when one element is accessed, the CPU hardware prefetcher loads an entire Cache Line (typically 64 bytes) of adjacent elements into L1/L2 Cache. In contrast, linked list nodes are scattered across RAM, triggering frequent **Cache Misses**.
- [ ] C. Python only supports CPU caching for array buffers.
- [ ] D. The size of the `next` pointer overflows CPU registers.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: B**

**Explanation:**
This illustrates the fundamental difference between **Theoretical Complexity** ($O(n)$) and **Hardware-level Performance**:
- Contiguous Array in RAM: The CPU preloads a 64-byte Cache Line into L1/L2 cache $\to$ Nearly every subsequent element access is a near-instantaneous **Cache Hit** (sub-nanosecond latency).
- Linked List: Each `curr = curr.next` jumps to an arbitrary heap memory address. The data is rarely in cache $\to$ **Cache Miss** $\to$ The CPU pipeline stalls waiting for data retrieval from main RAM (tens to hundreds of nanoseconds).

</details>

---

### Quiz 10. Finding the $k$-th Node from End via Two-Pass Algorithm
Given a singly linked list of $n$ nodes ($n \ge k$). If a first pass counts the total number of nodes as $n$, how many pointer steps from `head` must be taken in the second pass to land exactly on the $k$-th node from the end?

- [ ] A. $n - k$ steps
- [ ] B. $n - k + 1$ steps
- [ ] C. $k$ steps
- [ ] D. $k - 1$ steps

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: A**

**Explanation:**
- The first node (`head`) is at index $0$ (requiring $0$ steps).
- The $k$-th node from the end is located at 0-based index $n - k$.
- Therefore, starting from `head`, advancing forward exactly $n - k$ times via `.next` leads directly to the $k$-th node from the end.

</details>

---

### Quiz 11. In-place Singly Linked List Reversal
What is the minimum number of pointers required to reverse a singly linked list in-place without breaking link chains or losing nodes?

- [ ] A. 1 pointer
- [ ] B. 2 pointers
- [ ] C. 3 pointers
- [ ] D. 4 pointers

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
Strictly 3 pointer references are required:
1. `prev`: tracks the preceding node (the new destination for the reversed link).
2. `curr`: the current node undergoing reversal.
3. `next_temp`: temporarily stores `curr.next` before overwriting it with `curr.next = prev`. Without this third reference, the entire remainder of the list would be unreachable and lost immediately after relinking.

</details>

---

### Quiz 12. Prepend vs. Append in Singly Linked List
Given a Singly Linked List maintaining only a `head` reference, which of the following statements is **correct**?

- [ ] A. Prepend takes $O(1)$, Append takes $O(1)$.
- [ ] B. Prepend takes $O(n)$, Append takes $O(1)$.
- [ ] C. Prepend takes $O(1)$, Append takes $O(n)$ due to having to traverse from `head` to the last node.
- [ ] D. Both Prepend and Append take $O(n)$.

<details>
<summary><strong>Answer & Detailed Explanation</strong></summary>

**Correct Answer: C**

**Explanation:**
- Prepending only requires `new_node.next = self.head` and `self.head = new_node` $\to O(1)$, independent of $n$.
- Appending with only a `head` pointer requires running a traversal loop `while current.next is not None` across all $n$ nodes to find the tail $\to O(n)$.

</details>

---

---

# Part 2: Theoretical & Analytical Problems

## Problem T1. Loop Invariant Analysis for In-Place Linked List Reversal

### Problem Statement
Consider the canonical iterative Python implementation for reversing a singly linked list:

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

1. State the **Loop Invariant** for the `while` loop.
2. Formally prove the algorithm's correctness using the three standard steps: **Initialization**, **Maintenance**, and **Termination**.

<details>
<summary><strong>Detailed Solution</strong></summary>

### 1. Loop Invariant Formulation
At the start of each iteration of the `while` loop:
- Pointer `prev` points to the head of a correctly and fully reversed linked list containing nodes originally spanning index $0$ to index $i - 1$.
- Pointer `curr` points to the head of the unreversed remainder of the original linked list, spanning index $i$ to index $n - 1$.
- The two sublists are completely disjoint (no cross-links exist from the `prev` sublist to the `curr` sublist).

### 2. Correctness Proof
- **Initialization:**  
  Prior to the first iteration, `prev = None` and `curr = head`. The reversed list is empty (`None`), and the unreversed sublist is the entire original list starting at index $0$. The invariant holds vacuously.
- **Maintenance:**  
  During the loop body:
  - `next_node = curr.next` saves the unreversed successor.
  - `curr.next = prev` links the current node to the reversed prefix.
  - `prev = curr` expands the reversed prefix to include `curr`.
  - `curr = next_node` advances to the next unreversed node.  
  The reversed sublist now correctly contains nodes from $0$ to $i$, and `curr` points to node $i + 1$. The invariant is strictly preserved for the subsequent iteration.
- **Termination:**  
  The loop terminates when `curr is None`, meaning no nodes remain in the unreversed sublist ($i = n$). By the invariant, `prev` references the head of the completely reversed list spanning all nodes $0$ to $n - 1$. Returning `prev` yields the correct reversed list.

</details>

---

## Problem T2. Pointer Mechanics of Insertion and Deletion in Doubly Linked Lists

### Problem Statement
Given a Doubly Linked List where each node has attributes `data`, `prev`, and `next`:
1. Provide the exact 4 pointer assignments required to insert `new_node` immediately after a given node `p` (assuming `p` is not the tail).
2. Provide the exact 2 pointer assignments required to delete a node `curr` located in the interior of the list (both `curr.prev` and `curr.next` are non-null).
3. Draw an ASCII structural link diagram illustrating the pointers before and after the deletion.

<details>
<summary><strong>Detailed Solution</strong></summary>

### 1. Insertion After Node `p`
```python
new_node.next = p.next
new_node.prev = p
p.next.prev = new_node
p.next = new_node
```
*(This ordering ensures `p`'s successor recognizes `new_node` as its new predecessor before `p.next` is modified).*

### 2. Deletion of Interior Node `curr`
```python
curr.prev.next = curr.next
curr.next.prev = curr.prev
```

### 3. Structural Link Diagram
```text
Before Deletion:
    [prev_node] <===> [curr] <===> [next_node]

After Re-linking:
    [prev_node] --------------------> [next_node]
    [prev_node] <-------------------- [next_node]
```
Node `curr` is completely detached from the chain and will be reclaimed by Python's automatic garbage collector.

</details>

---

## Problem T3. Why Merge Sort Outperforms Quicksort on Linked Lists

### Problem Statement
When sorting data in **Arrays**, Quicksort is frequently preferred over Merge Sort. However, when sorting **Linked Lists**, Merge Sort is universally considered the gold standard.

Explain why based on three concrete criteria:
1. Auxiliary Space Complexity.
2. Partitioning and Element Access Cost.
3. Algorithm Stability.

<details>
<summary><strong>Detailed Solution</strong></summary>

| Criterion | Array | Linked List |
|---|---|---|
| **Auxiliary Space during Merge** | On arrays, merging requires an auxiliary array of size $O(n)$ to stage elements. | On linked lists, merging is achieved purely by **relinking existing pointers** (`next`), requiring $O(1)$ auxiliary memory (excluding recursive call stack). |
| **Quicksort Partitioning** | Arrays allow bidirectional two-pointer scanning and $O(1)$ random access swaps. | Singly linked lists cannot scan backward (`prev`), making Lomuto/Hoare partition schemes clumsy, cache-inefficient, and unstable. |
| **Stability** | Standard Quicksort on arrays is inherently unstable. | Merge Sort on linked lists naturally preserves the relative ordering of equal elements without additional overhead. |

**Conclusion:** Because linked lists allow merging two sorted lists in $O(1)$ auxiliary space and guarantee worst-case $O(n \log n)$ time, **Merge Sort** is asymptotically and practically optimal for linked list structures.

</details>

---

## Problem T4. Designing Stack and Queue using Singly Linked Lists in $O(1)$

### Problem Statement
Specify the design to implement the following two Abstract Data Types (ADTs) using a Singly Linked List such that all primary operations achieve strictly $O(1)$ time complexity:
1. **Stack ADT:** `push(x)`, `pop()`, `peek()`.
2. **Queue ADT:** `enqueue(x)`, `dequeue()`, `front()`.

<details>
<summary><strong>Detailed Solution</strong></summary>

### 1. Stack Implementation (Top at `head`)
- **Principle:** Align the Stack top (`top`) with the list `head`.
- `push(x)`: Insert at the front (`insert_front`).  
  `new_node.next = self.head; self.head = new_node` $\implies O(1)$.
- `pop()`: Delete from the front (`delete_front`).  
  `val = self.head.val; self.head = self.head.next; return val` $\implies O(1)$.
- `peek()`: Inspect `self.head.val` $\implies O(1)$.
- *(Note: Never place the top at the tail, because `pop()` would require $O(n)$ time to locate the node preceding `tail`).*

### 2. Queue Implementation (Two Pointers: `head` and `tail`)
- **Principle:** Queue front is at `head` (removal point); Queue rear is at `tail` (insertion point).
- `enqueue(x)`: Append at `tail`.  
  `self.tail.next = new_node; self.tail = new_node` $\implies O(1)$.
- `dequeue()`: Remove from `head`.  
  `val = self.head.val; self.head = self.head.next` $\implies O(1)$.  
  *(If `self.head` becomes `None`, set `self.tail = None`).*
- `front()`: Inspect `self.head.val` $\implies O(1)$.

</details>

---

## Problem T5. Real-World Memory Footprint of Python Nodes

### Problem Statement
In 64-bit CPython:
1. Compute the exact memory footprint (in bytes) of a standard `Node` instance:
   ```python
   class Node:
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
2. Compare this against an optimized node using `__slots__`:
   ```python
   class OptimizedNode:
       __slots__ = ['val', 'next']
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
3. What is the practical implication when designing big-data graphs or large linked lists holding 10 million nodes?

<details>
<summary><strong>Detailed Solution</strong></summary>

### 1. Memory Analysis of Standard `Node`
In 64-bit CPython:
- Every standard class instance contains an internal dictionary `__dict__` to hold dynamic attributes.
- Base object header (`PyObject_HEAD`): 16 bytes.
- Pointer referencing instance `__dict__`: 8 bytes.
- Underlying `PyDictObject` structure: $\approx 104$ to $144$ bytes.
$\implies$ A single standard `Node` object consumes between **150 and 160 bytes**!

### 2. Memory Optimization via `__slots__`
Declaring `__slots__ = ['val', 'next']` suppresses `__dict__` allocation, storing attributes directly in a fixed-size internal C pointer array:
- `PyObject_HEAD`: 16 bytes.
- Attribute reference pointer `val`: 8 bytes.
- Attribute reference pointer `next`: 8 bytes.
$\implies$ The total footprint of `OptimizedNode` drops to exactly **48 bytes** ($\approx 70\%$ memory reduction).

### 3. Practical Big-Data Implication
For a graph or linked list containing $10,000,000$ nodes:
- Standard `Node`: Consumes $\approx 1.5 \text{ GB}$ of RAM solely for node container overhead.
- `OptimizedNode` with `__slots__`: Consumes $\approx 480 \text{ MB}$ of RAM.  
This makes `__slots__` a mandatory design pattern for high-performance data engineering pipelines in Python.

</details>

---

---

# Part 3: Core Data Structures & Operations (Fundamental Operations)

This section focuses on the quintessential foundational skill: **implementing linked list variants from scratch**, covering the full spectrum of operations: **Traversal**, **Insertion**, and **Deletion** across three canonical variants: **Singly Linked List**, **Doubly Linked List**, and **Circular Linked List**.

---

## Problem C01. Design Singly Linked List: Traversal, Insertion & Deletion

- **Difficulty:** 🟢 Easy / 🟡 Medium (Comprehensive)
- **Problem ID:** LeetCode 707 | GfG: Linked List Insertion & Delete a Node in Single Linked List
- **Practice Links:**
  - [LeetCode #707 – Design Linked List](https://leetcode.com/problems/design-linked-list/)
  - [GeeksforGeeks – Linked List Insertion](https://www.geeksforgeeks.org/problems/linked-list-insertion/1)
  - [GeeksforGeeks – Delete a Node in Single Linked List](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1)
  - [GeeksforGeeks – Search in Linked List](https://www.geeksforgeeks.org/problems/search-in-linked-list/1)

### Problem Description
Design your implementation of the linked list class `MyLinkedList`. Support the following core operations:
1. `get(index)`: Get the value of the `index`-th node in the linked list (0-indexed). If invalid, return `-1`.
2. `addAtHead(val)`: Insert a node of value `val` before the first element of the linked list ($O(1)$).
3. `addAtTail(val)`: Append a node of value `val` as the last element of the linked list.
4. `addAtIndex(index, val)`: Add a node of value `val` before the `index`-th node in the linked list. If `index == size`, append to the end. If `index > size`, do not insert.
5. `deleteAtIndex(index)`: Delete the `index`-th node in the linked list if valid.
6. `traverse()`: Sequentially traverse all nodes and return a Python list of values.

<details>
<summary><strong>Solution & Python Implementation (Sentinel Dummy Node)</strong></summary>

### Design Analysis
- Using a **Sentinel Dummy Node** (`dummy`) before the actual head unifies head operations with interior operations, avoiding special cases for `index == 0`.
- Maintaining a `size` attribute enables $O(1)$ bounds verification.
- Traversing to `index` takes $O(	ext{index})$ steps, at most $O(n)$.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        # Sentinel dummy node preceding the first real node
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        # Locate predecessor at index - 1
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # Insert new node after prev
        new_node = ListNode(val, prev.next)
        prev.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Locate predecessor of the target node
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # Relink to bypass target node
        prev.next = prev.next.next
        self.size -= 1

    def traverse(self) -> list:
        """Traverse sequentially and export values as a Python list."""
        result = []
        curr = self.dummy.next
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result
```

- **Time Complexity:**
  - `addAtHead`: $O(1)$.
  - `get`, `addAtTail`, `addAtIndex`, `deleteAtIndex`, `traverse`: $O(n)$ worst-case.
- **Auxiliary Space:** $O(1)$ per operation.

</details>

---

## Problem C02. Doubly Linked List Operations: Insertion, Deletion & Bidirectional Traversal

- **Difficulty:** 🟢 Easy
- **Platform:** GeeksforGeeks
- **Practice Links:**
  - [GeeksforGeeks – Insert a node in Doubly Linked List](https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1)
  - [GeeksforGeeks – Delete node in Doubly Linked List](https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1)
  - [GeeksforGeeks – Display Doubly Linked List](https://www.geeksforgeeks.org/problems/display-doubly-linked-list/1)

### Problem Description
Given a Doubly Linked List where each node contains `val`, `prev`, and `next`, implement the following fundamental routines:
1. `insertAfter(head, p, x)`: Insert a new node with value `x` immediately after the `p`-th node (0-indexed).
2. `deleteNodeDLL(head, pos)`: Delete the node at position `pos` (1-indexed) in the doubly linked list and return the updated `head`.
3. `traverseForward(head)` & `traverseBackward(head)`: Sequentially traverse from `head` to tail, and from tail backward to `head`, verifying bidirectional pointer integrity.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Technical Mechanics
- **Insertion after node `p`:** Requires strictly 4 pointer updates:
  1. `new_node.next = curr.next`
  2. `new_node.prev = curr`
  3. `if curr.next is not None: curr.next.prev = new_node`
  4. `curr.next = new_node`
- **Deletion at position `pos`:**
  - If deleting `head` (`pos == 1`): `head = head.next`; if `head is not None: head.prev = None`.
  - If deleting an interior/tail node: `curr.prev.next = curr.next`, and if `curr.next is not None: curr.next.prev = curr.prev`.

```python
class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def insertAfter(head: DoublyNode, p: int, x: int) -> DoublyNode:
    """Insert value x after the p-th node (0-indexed)."""
    curr = head
    for _ in range(p):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    new_node = DoublyNode(x)
    new_node.next = curr.next
    new_node.prev = curr

    if curr.next is not None:
        curr.next.prev = new_node
    curr.next = new_node

    return head

def deleteNodeDLL(head: DoublyNode, pos: int) -> DoublyNode:
    """Delete node at position pos (1-indexed)."""
    if head is None:
        return None

    if pos == 1:
        new_head = head.next
        if new_head is not None:
            new_head.prev = None
        return new_head

    curr = head
    for _ in range(pos - 1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    # Update links bypassing curr
    if curr.prev is not None:
        curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev

    return head

def traverseForward(head: DoublyNode) -> list:
    """Forward traversal from head to tail."""
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result

def traverseBackward(head: DoublyNode) -> list:
    """Find tail, then backward traversal to head."""
    if head is None:
        return []
    curr = head
    while curr.next is not None:
        curr = curr.next
    result = []
    while curr is not None:
        result.append(curr.val)
        curr = curr.prev
    return result
```

- **Time Complexity:**
  - Insertion after a known node: $O(1)$; locating node $p$: $O(p) \le O(n)$.
  - Deletion at position: $O(	ext{pos}) \le O(n)$.
  - Traversal: $O(n)$.
- **Auxiliary Space:** $O(1)$.

</details>

---

## Problem C03. Circular Linked List Operations: Insertion, Deletion & Circular Traversal

- **Difficulty:** 🟢 Easy / 🟡 Medium
- **Platform:** GeeksforGeeks
- **Practice Links:**
  - [GeeksforGeeks – Circular Linked List Traversal](https://www.geeksforgeeks.org/problems/circular-linked-list-traversal/1)
  - [GeeksforGeeks – Insert in Sorted Circular Linked List](https://www.geeksforgeeks.org/problems/insert-in-sorted-circular-linked-list/1)
  - [GeeksforGeeks – Deletion in Circular Linked List](https://www.geeksforgeeks.org/problems/deletion-in-circular-linked-list/1)

### Problem Description
In a Circular Singly Linked List, the tail node points back to the head (`tail.next = head`). Implement the following core operations:
1. `traverseCircular(head)`: Traverse every node in the circular list exactly once and return the list of values.
2. `insertBegin(tail, val)` & `insertEnd(tail, val)`: Insert a node at the beginning or end of the circular list maintaining a single `tail` pointer in strictly $O(1)$ time.
3. `deleteNodeCircular(head, key)`: Delete the first node matching `key` in the circular list and return the updated `head`.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Technical Mechanics
- **Circular Traversal:** Begin at `curr = head`. Loop body visits `curr`, advances `curr = curr.next`, and terminates when `curr == head`.
- **`tail` Pointer Efficiency:**
  - Head is accessible in $O(1)$ as `tail.next`.
  - `insertBegin`: `new_node.next = tail.next; tail.next = new_node; return tail`.
  - `insertEnd`: `new_node.next = tail.next; tail.next = new_node; return new_node` (new tail is `new_node`).
- **Circular Deletion:**
  - Single-node list: If `head.val == key`, return `None`.
  - Deleting head: Traverse to locate `tail`, relink `tail.next = head.next`, and set `head = head.next`.
  - Deleting interior/tail: Advance `prev` and `curr` until `curr.val == key`, then `prev.next = curr.next`.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverseCircular(head: Node) -> list:
    """Traverse circular list from head for exactly one full cycle."""
    if head is None:
        return []
    result = []
    curr = head
    while True:
        result.append(curr.val)
        curr = curr.next
        if curr == head:
            break
    return result

def insertBegin(tail: Node, val: int) -> Node:
    """Insert at the beginning of a circular list with tail in O(1)."""
    new_node = Node(val)
    if tail is None:
        new_node.next = new_node
        return new_node

    new_node.next = tail.next
    tail.next = new_node
    return tail

def insertEnd(tail: Node, val: int) -> Node:
    """Insert at the end of a circular list with tail in O(1)."""
    new_node = Node(val)
    if tail is None:
        new_node.next = new_node
        return new_node

    new_node.next = tail.next
    tail.next = new_node
    return new_node  # new tail

def deleteNodeCircular(head: Node, key: int) -> Node:
    """Delete the first node with value matching key in circular list."""
    if head is None:
        return None

    # Single-node list edge case
    if head.next == head:
        return None if head.val == key else head

    curr = head
    prev = None

    # Deleting head node
    if head.val == key:
        tail = head
        while tail.next != head:
            tail = tail.next
        tail.next = head.next
        head = head.next
        return head

    # Deleting interior or tail node
    prev = head
    curr = head.next
    while curr != head:
        if curr.val == key:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next

    return head
```

- **Time Complexity:**
  - `insertBegin`, `insertEnd` (with `tail` pointer): $O(1)$.
  - `traverseCircular`: $O(n)$.
  - `deleteNodeCircular`: $O(n)$ to locate target node and locate `tail` if deleting head.
- **Auxiliary Space:** $O(1)$.

</details>

---

# Part 4: Coding Practice – Easy Level

## Problem 01. Reverse Linked List

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 206 | GfG: Reverse a linked list
- **Practice Links:** [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1)

### Problem Description
Given the `head` of a singly linked list, reverse the list in-place and return the new `head` pointer.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Maintain 3 pointers:
- `prev`: initialized to `None`.
- `curr`: list traversal pointer, starting at `head`.
- `next_temp`: temporarily stores `curr.next` before reversing the link direction.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

- **Time Complexity:** $T(n) = O(n)$ (single linear pass).
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 02. Remove Linked List Elements

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 203 | GfG: Delete a Node in Single Linked List
- **Practice Links:** [LeetCode #203](https://leetcode.com/problems/remove-linked-list-elements/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1)

### Problem Description
Given the `head` of a singly linked list and an integer `val`, remove all nodes having `node.val == val` and return the new `head`.

**Example:**
```text
Input:  head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None, val = 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Prepend a **Dummy Sentinel Node** before `head`. This unifies deletion at the head with deletion in the interior:
- Traverse with `curr = dummy`.
- If `curr.next.val == val`: skip the node via `curr.next = curr.next.next`.
- Otherwise: advance `curr = curr.next`.

```python
def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next is not None:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 03. Merge Two Sorted Lists

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 21 | GfG: Merge two sorted linked lists
- **Practice Links:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

### Problem Description
Merge two sorted linked lists `list1` and `list2` into a single sorted list by splicing together the existing nodes.

**Example:**
```text
list1:  1 -> 2 -> 4 -> None
list2:  1 -> 3 -> 4 -> None
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

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

</details>

---

## Problem 04. Delete Node in a Linked List Without Head

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 237 | GfG: Delete without head pointer
- **Practice Links:** [LeetCode #237](https://leetcode.com/problems/delete-node-in-a-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1)

### Problem Description
Delete a given non-tail `node` from a singly linked list without having access to `head`.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Copy the value from the next node into the current node, then bypass the next node:

```python
def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
```

- **Time Complexity:** $T(n) = O(1)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 05. Remove Duplicates from Sorted List

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 83 | GfG: Remove duplicate element from sorted Linked List
- **Practice Links:** [LeetCode #83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

### Problem Description
Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once.

**Example:**
```text
Input:  1 -> 1 -> 2 -> 3 -> 3 -> None
Output: 1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

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

</details>

---

## Problem 06. Convert Binary Number in a Linked List to Integer

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 1290 | GfG: Decimal Equivalent of Binary Linked List
- **Practice Links:** [LeetCode #1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/decimal-equivalent-of-binary-linked-list/1)

### Problem Description
Given `head` which is a reference node to a singly-linked list with each node containing `0` or `1`, return the decimal value of the binary number represented.

**Example:**
```text
Input:  1 -> 0 -> 1 -> None
Output: 5  (1*2^2 + 0*2^1 + 1*2^0 = 5)
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Traverse sequentially using Horner's rule or bitwise left shift:
$$\text{ans} = (\text{ans} \ll 1) \mid \text{curr.val} = 2 \times \text{ans} + \text{curr.val}$$

```python
def getDecimalValue(head: ListNode) -> int:
    ans = 0
    curr = head
    while curr is not None:
        ans = (ans << 1) | curr.val
        curr = curr.next
    return ans
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 07. Reverse a Doubly Linked List

- **Difficulty:** 🟢 Easy
- **Platform:** GeeksforGeeks: Reverse a Doubly Linked List
- **Practice Links:** [GeeksforGeeks Practice](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1)

### Problem Description
Given the `head` of a Doubly Linked List, reverse the list in-place and return the new `head`.

**Example:**
```text
Input:  None <- 1 <==> 2 <==> 3 <==> 4 -> None
Output: None <- 4 <==> 3 <==> 2 <==> 1 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
For every node in the doubly linked list, swap its `prev` and `next` pointers:
```python
temp = curr.prev
curr.prev = curr.next
curr.next = temp
```
Then advance to the original forward node (which is now stored in `curr.prev`).

```python
class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def reverseDLL(head: DoublyNode) -> DoublyNode:
    if head is None or head.next is None:
        return head

    curr = head
    temp = None

    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev

    if temp is not None:
        head = temp.prev

    return head
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 08. Intersection of Two Linked Lists

- **Difficulty:** 🟢 Easy
- **Problem ID:** LeetCode 160 | GfG: Intersection Point in Y Shaped Linked Lists
- **Practice Links:** [LeetCode #160](https://leetcode.com/problems/intersection-of-two-linked-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)

### Problem Description
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If they do not intersect, return `None`.

<details>
<summary><strong>Solution & Python Implementation (Length Difference Method)</strong></summary>

### Algorithm Analysis (Length Difference Offset Method)
1. Count lengths $L_A$ and $L_B$ of both lists.
2. Compute the difference: $d = |L_A - L_B|$.
3. Advance the pointer of the longer list forward by $d$ steps to equalize remaining lengths.
4. Advance both pointers synchronously. The node where `currA is currB` is the exact intersection point.

```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    # Step 1: Compute lengths
    lenA = 0
    currA = headA
    while currA is not None:
        lenA += 1
        currA = currA.next

    lenB = 0
    currB = headB
    while currB is not None:
        lenB += 1
        currB = currB.next

    # Step 2: Offset the longer list
    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next

    # Step 3: Traverse in lockstep
    while currA is not None and currB is not None:
        if currA is currB:
            return currA
        currA = currA.next
        currB = currB.next

    return None
```

- **Time Complexity:** $T(m, n) = O(m + n)$.
- **Auxiliary Space:** $S(m, n) = O(1)$.

</details>

---

---

# Part 5: Coding Practice – Medium Level

## Problem 09. Remove Nth Node From End of List

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 19 | GfG: Nth node from end of linked list
- **Practice Links:** [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1)

### Problem Description
Given the `head` of a linked list, remove the $n$-th node from the end of the list and return its `head`.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, n = 2
Output: 1 -> 2 -> 3 -> 5 -> None  (node 4 is removed)
```

<details>
<summary><strong>Solution & Python Implementation (Two-Pass Method)</strong></summary>

### Algorithm Analysis
- **Pass 1:** Traverse the list to compute total length $L$.
- The node to remove is at 0-based index $L - n$. Its predecessor is at index $L - n - 1$.
- **Pass 2:** Starting from `dummy = ListNode(0, head)`, advance $L - n$ steps to reach the predecessor, then perform `curr.next = curr.next.next`.

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Pass 1: Count total nodes
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next

    # Pass 2: Locate predecessor and delete
    dummy = ListNode(0, head)
    curr = dummy
    for _ in range(length - n):
        curr = curr.next

    curr.next = curr.next.next
    return dummy.next
```

- **Time Complexity:** $T(L) = O(L)$ (two linear passes).
- **Auxiliary Space:** $S(L) = O(1)$.

</details>

---

## Problem 10. Rotate List

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 61 | GfG: Rotate a Linked List
- **Practice Links:** [LeetCode #61](https://leetcode.com/problems/rotate-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1)

### Problem Description
Given the `head` of a linked list, rotate the list to the right by $k$ places.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, k = 2
Output: 4 -> 5 -> 1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
1. Traverse to the tail to determine length $L$ and record `tail`.
2. Normalize $k$: $k = k \pmod L$. If $k == 0$, return `head`.
3. Connect `tail.next = head` to form a temporary circular ring.
4. Advance $L - k - 1$ steps from `head` to find the new tail. Set `new_head = new_tail.next` and break the ring via `new_tail.next = None`.

```python
def rotateRight(head: ListNode, k: int) -> ListNode:
    if head is None or head.next is None or k == 0:
        return head

    # Step 1: Find length and tail node
    length = 1
    tail = head
    while tail.next is not None:
        length += 1
        tail = tail.next

    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head

    # Step 3: Connect into circular ring
    tail.next = head

    # Step 4: Find new break point at (length - k)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 11. Partition List

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 86 | GfG: Partition a Linked List
- **Practice Links:** [LeetCode #86](https://leetcode.com/problems/partition-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/partition-a-linked-list/1)

### Problem Description
Given the `head` of a linked list and a value $x$, partition it such that all nodes less than $x$ come before nodes greater than or equal to $x$, preserving relative initial order.

**Example:**
```text
Input:  head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Maintain two independent sublists using dummy sentinels:
- `less_dummy`: nodes with `val < x`.
- `greater_dummy`: nodes with `val >= x`.
Concatenate `less` tail to `greater_dummy.next`, and set `greater.next = None`.

```python
def partition(head: ListNode, x: int) -> ListNode:
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less = less_dummy
    greater = greater_dummy

    curr = head
    while curr is not None:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next

    # Break greater tail to avoid cycle
    greater.next = None
    # Concatenate two sublists
    less.next = greater_dummy.next

    return less_dummy.next
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 12. Odd Even Linked List

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 328 | GfG: Rearrange a linked list
- **Practice Links:** [LeetCode #328](https://leetcode.com/problems/odd-even-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1)

### Problem Description
Given the `head` of a singly linked list, group all odd-indexed nodes together followed by even-indexed nodes in-place.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Maintain two pointer streams `odd` and `even`:
- `odd` links odd-indexed nodes, `even` links even-indexed nodes.
- After processing the list, link `odd.next = even_head`.

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

</details>

---

## Problem 13. Add Two Numbers

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 2 | GfG: Add two numbers represented by linked lists
- **Practice Links:** [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1)

### Problem Description
Given two non-empty linked lists representing two non-negative integers stored in reverse order, add the two numbers and return the sum as a linked list.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Simulate elementary school addition digit-by-digit:
- Traverse both lists concurrently while maintaining a `carry`.
- At each node: $\text{total} = \text{val1} + \text{val2} + \text{carry}$, digit is $\text{total} \pmod{10}$, and $\text{carry} = \lfloor \text{total} / 10 \rfloor$.

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

</details>

---

## Problem 14. Swap Nodes in Pairs

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 24 | GfG: Pairwise swap elements of a linked list
- **Practice Links:** [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

### Problem Description
Given a linked list, swap every two adjacent nodes in-place by adjusting node pointers.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Use a sentinel dummy node and perform 3 pointer assignments per pair:
- `first = prev.next`, `second = prev.next.next`
- `first.next = second.next`, `second.next = first`, `prev.next = second`
- `prev = first`

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

</details>

---

## Problem 15. Remove Duplicates from Sorted List II

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 82 | GfG: Remove all occurrences of duplicates
- **Practice Links:** [LeetCode #82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-all-occurences-of-duplicates-in-a-linked-list/1)

### Problem Description
Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> None
Output: 1 -> 2 -> 5 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
Use a sentinel dummy node before head and check ahead for identical values:
- While `head.next` exists and `head.val == head.next.val`, skip through all duplicate nodes.
- Relink `prev.next = head.next` to eliminate the entire run.

```python
def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while head is not None:
        if head.next is not None and head.val == head.next.val:
            while head.next is not None and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next

    return dummy.next
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 16. Copy List with Random Pointer

- **Difficulty:** 🟡 Medium
- **Problem ID:** LeetCode 138 | GfG: Clone a linked list with next and random pointer
- **Practice Links:** [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

### Problem Description
Construct a deep copy of a linked list where each node contains an additional `random` pointer that could point to any node in the list or `None`. Achieve this in strictly $O(1)$ auxiliary space.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Algorithm Analysis
1. Interweave copied nodes directly: $A \to A' \to B \to B'$.
2. Assign random pointers: `curr.next.random = curr.random.next` (if `curr.random` is not `None`).
3. Disentangle the copied list from the original list.

```python
class NodeWithRandom:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'NodeWithRandom') -> 'NodeWithRandom':
    if head is None:
        return None

    # Step 1: Interweave cloned nodes A -> A' -> B -> B'
    curr = head
    while curr is not None:
        copy_node = NodeWithRandom(curr.val, curr.next)
        curr.next = copy_node
        curr = copy_node.next

    # Step 2: Assign random pointers
    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate original and cloned lists
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

</details>

---

> © 2026 Dr. Minh D. Vu – Faculty of Data Science and AI, National Economics University (NEU).
