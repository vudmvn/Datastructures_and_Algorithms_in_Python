# 📝 Practice Problems & Coding Exercises: Linked Lists

> **Course:** Data Structures and Algorithms in Python (DSAI1002)  
> **Topic:** Linear Data Structures – Linked Lists  
> **Reference:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Online Judge Platforms:** LeetCode & GeeksforGeeks.

---

## 📌 Problem Set Index

| No. | Problem Name | Difficulty | Core Technique | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** | 🟢 Easy | 3 Pointers (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Middle of the Linked List** | 🟢 Easy | Fast & Slow Pointers | [#876](https://leetcode.com/problems/middle-of-the-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1) |
| 03 | **Linked List Cycle** | 🟢 Easy | Floyd's Tortoise and Hare | [#141](https://leetcode.com/problems/linked-list-cycle/) | [GfG Link](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1) |
| 04 | **Merge Two Sorted Lists** | 🟢 Easy | Dummy Sentinel Node | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Link](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 05 | **Delete Node Without Head** | 🟢 Easy | Node Value Copying Trick | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 06 | **Remove Duplicates from Sorted List** | 🟢 Easy | Single Pointer Forward Scan | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 07 | **Palindrome Linked List** | 🟢 Easy | Slow/Fast + Reversal + Comparison | [#234](https://leetcode.com/problems/palindrome-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1) |
| 08 | **Intersection of Two Linked Lists** | 🟢 Easy | Two-Pointer Traversal Switch | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Link](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |
| 09 | **Remove Nth Node From End** | 🟡 Medium | Two Pointers with Gap ($N$) | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Linked List Cycle II** | 🟡 Medium | Floyd's Phase 2 Mathematical Reset | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | [GfG Link](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1) |
| 11 | **Reorder List** | 🟡 Medium | Split + Reverse + Interleave | [#143](https://leetcode.com/problems/reorder-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/reorder-list/1) |
| 12 | **Odd Even Linked List** | 🟡 Medium | Multi-pointer In-place Relinking | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** | 🟡 Medium | Elementary Math with Carry Simulation | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Link](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** | 🟡 Medium | Dummy Node + Pointer Swap | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Link](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Copy List with Random Pointer** | 🟡 Medium | Interweaving Nodes In-place | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Link](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |
| 16 | **Sort List** | 🟡 Medium | Merge Sort on Linked List | [#148](https://leetcode.com/problems/sort-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1) |

---

# Part 1: Easy Level Problems

## Problem 01. Reverse Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 206 | GfG: Reverse a linked list
- **Online Judges:** [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1)

### Description
Given the `head` of a singly linked list, reverse the list in-place and return the reversed list's head.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Use three pointers:
- `prev`: initially set to `None`.
- `curr`: pointer iterating through the list, initialized to `head`.
- `next_temp`: temporary reference storing `curr.next` before overwriting the link to avoid losing the remainder of the list.

At each iteration:
1. `next_temp = curr.next`
2. `curr.next = prev`
3. `prev = curr`
4. `curr = next_temp`

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

- **Time Complexity:** $T(n) = O(n)$, visiting each node exactly once.
- **Auxiliary Space:** $S(n) = O(1)$, modifying pointers in-place.

</details>

---

## Problem 02. Middle of the Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 876 | GfG: Finding middle element in a linked list
- **Online Judges:** [LeetCode #876](https://leetcode.com/problems/middle-of-the-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1)

### Description
Given the `head` of a singly linked list, return the middle node of the linked list. If there are two middle nodes (i.e. even number of elements), return the second middle node.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: Node 3

Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
Output: Node 4 (second middle node)
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Use the **Fast & Slow Pointers** technique:
- Initialize both `slow` and `fast` pointers at `head`.
- In each step, advance `slow` by 1 node and `fast` by 2 nodes.
- When `fast` reaches the end (`fast is None` or `fast.next is None`), `slow` will be stationed precisely at the middle node.

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

</details>

---

## Problem 03. Linked List Cycle Detection

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 141 | GfG: Detect Loop in linked list
- **Online Judges:** [LeetCode #141](https://leetcode.com/problems/linked-list-cycle/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)

### Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. A cycle occurs if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Example:**
```text
3 -> 2 -> 0 -> -4
     ^          |
     +----------+
Output: True (cycle loops from -4 back to 2)
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Apply **Floyd's Tortoise and Hare Algorithm**:
- If there is no cycle, `fast` will promptly reach `None`.
- If there is a cycle, both pointers will circulate within the cycle. Because `fast` gains 1 step on `slow` in every iteration, the relative distance between them decreases by 1 each round, guaranteeing that `fast` will catch up to `slow`.

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

</details>

---

## Problem 04. Merge Two Sorted Lists

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 21 | GfG: Merge two sorted linked lists
- **Online Judges:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

### Description
Merge two sorted linked lists `list1` and `list2` into one sorted list by splicing together the nodes of the original lists. Return the head of the merged linked list.

**Example:**
```text
list1: 1 -> 2 -> 4 -> None
list2: 1 -> 3 -> 4 -> None
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
- Use a **Dummy Sentinel Node** to eliminate special-case code for assigning the first node to the result head.
- Maintain a `tail` pointer. Compare values at the heads of `list1` and `list2`, appending the smaller node to `tail`.
- Once one list is exhausted, attach the remaining non-empty list directly to `tail.next`.

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

## Problem 05. Delete Node Without Head Pointer

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 237 | GfG: Delete without head pointer
- **Online Judges:** [LeetCode #237](https://leetcode.com/problems/delete-node-in-a-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1)

### Description
You are given the `node` to be deleted in a singly linked list. You are **not given access** to the `head` of the list. It is guaranteed that the node to be deleted is not the tail node.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Since we do not have access to the predecessor node, copy the value from `node.next` into the current node, then delete `node.next`:
1. `node.val = node.next.val`
2. `node.next = node.next.next`

```python
def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
```

- **Time Complexity:** $T(n) = O(1)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 06. Remove Duplicates from Sorted List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 83 | GfG: Remove duplicate element from sorted Linked List
- **Online Judges:** [LeetCode #83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

### Description
Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

**Example:**
```text
Input:  1 -> 1 -> 2 -> 3 -> 3 -> None
Output: 1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Because the input list is sorted, duplicate values are consecutive:
- Iterate with `curr = head`.
- If `curr.val == curr.next.val`, bypass the duplicate node via `curr.next = curr.next.next`.
- Otherwise, advance `curr = curr.next`.

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

## Problem 07. Palindrome Linked List

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 234 | GfG: Check if Linked List is Palindrome
- **Online Judges:** [LeetCode #234](https://leetcode.com/problems/palindrome-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1)

### Description
Given the `head` of a singly linked list, return `True` if it is a palindrome or `False` otherwise. Solve it in $O(n)$ time and $O(1)$ auxiliary space.

**Example:**
```text
Input: 1 -> 2 -> 2 -> 1 -> None  ==>  True
Input: 1 -> 2 -> 3 -> None        ==>  False
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
1. **Locate Middle:** Use `slow` and `fast` pointers to locate the start of the second half.
2. **Reverse Second Half:** Invert the second half in-place starting from `slow`.
3. **Compare Halves:** Traverse from the original `head` and the head of the reversed second half simultaneously.

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
    is_pal = True
    while second_half is not None:
        if first_half.val != second_half.val:
            is_pal = False
            break
        first_half = first_half.next
        second_half = second_half.next

    return is_pal
```

- **Time Complexity:** $T(n) = O(n)$.
- **Auxiliary Space:** $S(n) = O(1)$.

</details>

---

## Problem 08. Intersection of Two Linked Lists

- **Difficulty:** 🟢 Easy
- **Problem IDs:** LeetCode 160 | GfG: Intersection Point in Y Shaped Linked Lists
- **Online Judges:** [LeetCode #160](https://leetcode.com/problems/intersection-of-two-linked-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)

### Description
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `None`.

**Illustration:**
```text
A:          a1 -> a2 \
                       c1 -> c2 -> c3 -> None
B:    b1 -> b2 -> b3 /
Intersection node is c1.
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Let $a$ and $b$ be the individual prefix lengths of list A and B, and $c$ be the length of the common intersected segment:
- Pointer $p_A$ travels $a + c$, then switches to `headB` and travels $b$.
- Pointer $p_B$ travels $b + c$, then switches to `headA` and travels $a$.
- Since $a + c + b = b + c + a$, both pointers cover the exact same cumulative distance and will collide at node $c_1$ (or terminate at `None` if disjoint).

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

</details>

---

# Part 2: Medium Level Problems

## Problem 09. Remove Nth Node From End of List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 19 | GfG: Nth node from end of linked list
- **Online Judges:** [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1)

### Description
Given the `head` of a linked list, remove the $n$-th node from the end of the list and return its head in **one single pass**.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, n = 2
Output: 1 -> 2 -> 3 -> 5 -> None (node 4 removed)
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
- Use a `dummy` node before `head` to handle cases where the first node is deleted.
- Advance pointer `fast` by $n + 1$ steps from `dummy`.
- Move both `fast` and `slow` forward together one step at a time until `fast` becomes `None`.
- `slow` is now positioned immediately before the target node. Unlink it: `slow.next = slow.next.next`.

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

- **Time Complexity:** $T(L) = O(L)$ (one pass over list length $L$).
- **Auxiliary Space:** $S(L) = O(1)$.

</details>

---

## Problem 10. Linked List Cycle II (Find Start of Cycle)

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 142 | GfG: Find the first node of loop in linked list
- **Online Judges:** [LeetCode #142](https://leetcode.com/problems/linked-list-cycle-ii/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1)

### Description
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `None`. Do not modify the linked list.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Mathematical Proof (Floyd's Algorithm Phase 2)
Let:
- $L_1$: distance from `head` to cycle entry.
- $L_2$: distance from cycle entry to the meeting point.
- $C$: circumference (length) of the cycle.

At collision:
$$d_{\text{slow}} = L_1 + L_2$$
$$d_{\text{fast}} = L_1 + L_2 + k \cdot C$$
$$d_{\text{fast}} = 2 \cdot d_{\text{slow}} \implies L_1 = k \cdot C - L_2$$

Thus, moving one pointer to `head` while keeping the other at the collision spot, and marching both forward at identical speed, guarantees they will meet at the cycle entry node.

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

</details>

---

## Problem 11. Reorder List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 143 | GfG: Reorder List
- **Online Judges:** [LeetCode #143](https://leetcode.com/problems/reorder-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reorder-list/1)

### Description
You are given the head of a singly linked-list:
$$L_0 \to L_1 \to \dots \to L_{n-1} \to L_n$$

Reorder the list to be on the following form:
$$L_0 \to L_n \to L_1 \to L_{n-1} \to L_2 \to L_{n-2} \to \dots$$
Modify the list in-place without altering node values.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 1 -> 5 -> 2 -> 4 -> 3 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Combine three classic techniques:
1. Find the middle node via fast/slow pointers and bisect the list into two halves.
2. Reverse the second half.
3. Merge the two halves by alternating nodes.

```python
def reorderList(head: ListNode) -> None:
    if head is None or head.next is None:
        return

    # 1. Bisect list
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    # 2. Reverse second half
    prev = None
    curr = second
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    # 3. Interleave
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

</details>

---

## Problem 12. Odd Even Linked List

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 328 | GfG: Rearrange a linked list
- **Online Judges:** [LeetCode #328](https://leetcode.com/problems/odd-even-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1)

### Description
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list. Maintain the relative order of elements within both groups.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 1 -> 3 -> 5 -> 2 -> 4 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
- Initialize `odd = head`, `even = head.next`, and `even_head = even`.
- In each step:
  - Link `odd.next = even.next` and advance `odd = odd.next`.
  - Link `even.next = odd.next` and advance `even = even.next`.
- Conclude by connecting the tail of odd nodes to the head of even nodes: `odd.next = even_head`.

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
- **Problem IDs:** LeetCode 2 | GfG: Add two numbers represented by linked lists
- **Online Judges:** [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1)

### Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

**Example:**
```text
l1: 2 -> 4 -> 3 (represents 342)
l2: 5 -> 6 -> 4 (represents 465)
Sum: 342 + 465 = 807
Output: 7 -> 0 -> 8 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
Simulate column-wise addition with a `carry` flag:
- $\text{sum} = \text{val}_1 + \text{val}_2 + \text{carry}$
- $\text{digit} = \text{sum} \pmod{10}, \quad \text{carry} = \lfloor \text{sum} / 10 \rfloor$
- Append the new digit node to the result list via a `dummy` head.

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
- **Auxiliary Space:** $S(m, n) = O(\max(m, n))$ for the output list.

</details>

---

## Problem 14. Swap Nodes in Pairs

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 24 | GfG: Pairwise swap elements of a linked list
- **Online Judges:** [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

### Description
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.

**Example:**
```text
Input:  1 -> 2 -> 3 -> 4 -> None
Output: 2 -> 1 -> 4 -> 3 -> None
```

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
- Position `prev = dummy`. Let `first = prev.next` and `second = first.next`.
- Rewire pointers:
  1. `first.next = second.next`
  2. `second.next = first`
  3. `prev.next = second`
- Advance `prev = first`.

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

## Problem 15. Copy List with Random Pointer

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 138 | GfG: Clone a linked list with next and random pointer
- **Online Judges:** [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

### Description
Construct a **Deep Copy** of a linked list of length $n$ where each node contains an additional `random` pointer that could point to any node in the list, or `None`.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Optimal $O(1)$ Space Interweaving Strategy
1. **Interweave Nodes:** Create duplicate nodes and inject each copy immediately after its original:  
   `A -> A' -> B -> B' -> C -> C'`.
2. **Assign Random Pointers:** `curr.next.random = curr.random.next` (if `curr.random` exists).
3. **Disentangle Lists:** Separate the cloned list from the original list cleanly.

```python
class NodeWithRandom:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'NodeWithRandom') -> 'NodeWithRandom':
    if head is None:
        return None

    # Step 1: Duplicate nodes
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

    # Step 3: Separate cloned list from original
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
- **Auxiliary Space:** $S(n) = O(1)$ extra space.

</details>

---

## Problem 16. Sort List (Merge Sort on Linked List)

- **Difficulty:** 🟡 Medium
- **Problem IDs:** LeetCode 148 | GfG: Sort a linked list
- **Online Judges:** [LeetCode #148](https://leetcode.com/problems/sort-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1)

### Description
Given the `head` of a linked list, return the list after sorting it in ascending order in $O(n \log n)$ time complexity.

<details>
<summary><strong>Solution & Python Implementation</strong></summary>

### Approach
**Merge Sort** is the optimal algorithm for linked lists:
1. **Divide:** Bisect the list at the middle node using fast/slow pointers. Sever the link to obtain two independent sublists.
2. **Conquer:** Recursively sort both halves.
3. **Combine:** Merge the two sorted sublists.

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

- **Time Complexity:** $T(n) = O(n \log n)$ across worst, best, and average cases.
- **Auxiliary Space:** $S(n) = O(\log n)$ for recursive call stack.

</details>

---

> © 2026 Dr. Minh Duc Vu – Faculty of Data Science & Artificial Intelligence, National Economics University (NEU).
