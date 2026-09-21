# 📝 Hệ thống Bài tập Thực hành: Danh sách Liên kết (Linked Lists Practice Set)

> **Học phần:** Cấu trúc Dữ liệu và Giải thuật với Python (DSAI1002)  
> **Chủ đề:** Cấu trúc Dữ liệu Tuyến tính – Danh sách Liên kết (Linear Data Structures – Linked Lists)  
> **Tài liệu tham khảo:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Nền tảng luyện code trực tuyến:** LeetCode & GeeksforGeeks.

---

## 📌 Bảng Tổng hợp Bài tập (Problem Set Index)

| STT | Tên bài toán | Cấp độ | Kỹ thuật cốt lõi | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** (Đảo ngược DSLK) | 🟢 Easy | 3 con trỏ (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Middle of the Linked List** (Tìm node giữa) | 🟢 Easy | Fast & Slow Pointers | [#876](https://leetcode.com/problems/middle-of-the-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1) |
| 03 | **Linked List Cycle** (Phát hiện chu trình) | 🟢 Easy | Floyd's Tortoise and Hare | [#141](https://leetcode.com/problems/linked-list-cycle/) | [GfG Link](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1) |
| 04 | **Merge Two Sorted Lists** (Hợp nhất 2 DSLK đã sắp xếp) | 🟢 Easy | Dummy Sentinel Node | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Link](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 05 | **Delete Node Without Head** (Xóa node không cần head) | 🟢 Easy | Node Value Copying Trick | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 06 | **Remove Duplicates from Sorted List** (Xóa trùng lặp) | 🟢 Easy | Single Pointer Scan | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 07 | **Palindrome Linked List** (DSLK đối xứng) | 🟢 Easy | Slow/Fast + Reversal + Comparison | [#234](https://leetcode.com/problems/palindrome-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1) |
| 08 | **Intersection of Two Linked Lists** (Giao điểm 2 DSLK) | 🟢 Easy | Two-Pointer Traversal Switch | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Link](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |
| 09 | **Remove Nth Node From End** (Xóa node thứ N từ cuối) | 🟡 Medium | Two Pointers with Fixed Gap ($N$) | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Linked List Cycle II** (Tìm điểm bắt đầu chu trình) | 🟡 Medium | Floyd's Phase 2 Mathematical Reset | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | [GfG Link](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1) |
| 11 | **Reorder List** (Đan xen danh sách) | 🟡 Medium | Split + Reverse + Interleave | [#143](https://leetcode.com/problems/reorder-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/reorder-list/1) |
| 12 | **Odd Even Linked List** (Gom nhóm node vị trí chẵn/lẻ) | 🟡 Medium | Multi-pointer Relinking | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** (Cộng 2 số dạng DSLK ngược) | 🟡 Medium | Elementary Math with Carry Simulation | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Link](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** (Đổi chỗ từng cặp node liền kề) | 🟡 Medium | Dummy Node + Pointer Swap | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Link](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Copy List with Random Pointer** (Clone DSLK ngẫu nhiên) | 🟡 Medium | Interweaving Nodes in-place / Hash Map | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Link](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |
| 16 | **Sort List** (Sắp xếp DSLK tối ưu) | 🟡 Medium | Merge Sort on Linked List | [#148](https://leetcode.com/problems/sort-list/) | [GfG Link](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1) |

---

# Phần 1: Cấp độ Cơ bản (Easy Level)

## Bài 01. Đảo ngược Danh sách Liên kết (Reverse Linked List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 206 | GfG: Reverse a linked list
- **Đường dẫn thực hành:** [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một singly linked list, hãy đảo ngược danh sách này ngay tại chỗ (*in-place*) và trả về con trỏ `head` mới của danh sách sau khi đảo.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None
Đầu ra:  5 -> 4 -> 3 -> 2 -> 1 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng 3 con trỏ:
- `prev`: ban đầu trỏ tới `None`.
- `curr`: con trỏ duyệt qua danh sách, bắt đầu từ `head`.
- `next_temp`: biến tạm lưu lại `curr.next` trước khi bẻ hướng liên kết, tránh làm mất phần danh sách phía sau.

Tại mỗi bước:
1. `next_temp = curr.next` (lưu node kế tiếp)
2. `curr.next = prev` (đổi hướng liên kết)
3. `prev = curr` (tiến `prev` lên node hiện tại)
4. `curr = next_temp` (tiến `curr` lên node tiếp theo)

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

- **Độ phức tạp thời gian:** $T(n) = O(n)$ do duyệt qua mỗi node đúng 1 lần.
- **Bộ nhớ phụ:** $S(n) = O(1)$ vì chỉ dùng một số con trỏ phụ.

</details>

---

## Bài 02. Tìm Node giữa Danh sách (Middle of the Linked List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 876 | GfG: Finding middle element in a linked list
- **Đường dẫn thực hành:** [LeetCode #876](https://leetcode.com/problems/middle-of-the-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một singly linked list, hãy tìm và trả về node nằm ở vị trí chính giữa danh sách. Nếu danh sách có số lượng node là chẵn (nghĩa là có 2 node ở giữa), hãy trả về node ở vị trí giữa thứ hai.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None
Đầu ra:  Node có giá trị 3

Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
Đầu ra:  Node có giá trị 4 (node giữa thứ hai)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng kỹ thuật **Fast & Slow Pointers**:
- Khởi tạo cả `slow` và `fast` đều trỏ vào `head`.
- Trong mỗi vòng lặp, `slow` tiến 1 bước (`slow = slow.next`), còn `fast` tiến 2 bước (`fast = fast.next.next`).
- Khi `fast` đi đến cuối danh sách (`fast is None` hoặc `fast.next is None`), `slow` sẽ đứng đúng vị trí giữa danh sách mà không cần phải đếm tổng số node trước.

```python
def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 03. Phát hiện Chu trình trong Danh sách (Linked List Cycle)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 141 | GfG: Detect Loop in linked list
- **Đường dẫn thực hành:** [LeetCode #141](https://leetcode.com/problems/linked-list-cycle/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)

### Mô tả bài toán
Cho `head` của một linked list, xác định xem danh sách này có chứa chu trình (vòng lặp vô tận) hay không. Chu trình xuất hiện khi có một node trong danh sách mà con trỏ `next` của nó trỏ ngược lại một node đã xuất hiện trước đó.

**Ví dụ:**
```text
3 -> 2 -> 0 -> -4
     ^          |
     +----------+
Đầu ra: True (tồn tại chu trình từ -4 về 2)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Áp dụng **Thuật toán rùa và thỏ của Floyd (Floyd's Cycle-Finding Algorithm)**:
- Nếu danh sách không có chu trình, con trỏ `fast` sẽ nhanh chóng chạm tới `None`.
- Nếu danh sách có chu trình, hai con trỏ sẽ lặp vô tận bên trong chu trình đó. Vì `fast` chạy nhanh hơn `slow` 1 node sau mỗi lượt, khoảng cách tương đối giữa chúng giảm đi 1 ở mỗi bước. Do đó, chắc chắn `fast` sẽ đuổi kịp `slow` (`slow is fast`).

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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$ (tối ưu hơn cách dùng `set` để lưu các node đã duyệt mất $O(n)$ bộ nhớ).

</details>

---

## Bài 04. Hợp nhất Hai Danh sách đã Sắp xếp (Merge Two Sorted Lists)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 21 | GfG: Merge two sorted linked lists
- **Đường dẫn thực hành:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

### Mô tả bài toán
Cho hai danh sách liên kết đơn đã được sắp xếp theo thứ tự tăng dần `list1` và `list2`. Hãy hợp nhất chúng thành một danh sách liên kết đơn duy nhất cũng được sắp xếp theo thứ tự tăng dần, bằng cách ghép nối trực tiếp các node của hai danh sách ban đầu.

**Ví dụ:**
```text
list1: 1 -> 2 -> 4 -> None
list2: 1 -> 3 -> 4 -> None
Đầu ra: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
- Sử dụng một node giả (**Dummy / Sentinel node**) để đơn giản hóa thao tác chèn node vào đầu danh sách, tránh phải viết riêng logic kiểm tra `head` rỗng.
- Dùng con trỏ `tail` trỏ vào node cuối cùng của danh sách kết quả. So sánh giá trị ở đầu hai danh sách, nối node nhỏ hơn vào `tail` rồi tịnh tiến con trỏ tương ứng.
- Khi một trong hai danh sách đã hết phần tử, chỉ cần nối phần còn lại của danh sách kia vào sau `tail`.

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

    # Nối phần còn lại (nếu có)
    tail.next = list1 if list1 is not None else list2

    return dummy.next
```

- **Độ phức tạp thời gian:** $T(m, n) = O(m + n)$ với $m, n$ là số node của `list1` và `list2`.
- **Bộ nhớ phụ:** $S(m, n) = O(1)$ vì tái sử dụng toàn bộ các node cũ.

</details>

---

## Bài 05. Xóa Node khi không có Con trỏ Head (Delete Node in a Linked List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 237 | GfG: Delete without head pointer
- **Đường dẫn thực hành:** [LeetCode #237](https://leetcode.com/problems/delete-node-in-a-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1)

### Mô tả bài toán
Cho tham chiếu đến một `node` cần xóa trong danh sách liên kết đơn. Bạn **không được cấp quyền truy cập** vào con trỏ `head` của danh sách. Đảm bảo rằng node cần xóa không phải là node cuối cùng (`tail`) của danh sách.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Thông thường, để xóa một node trong singly linked list, ta cần biết node đứng trước (*predecessor*) để gán `prev.next = node.next`. Tuy nhiên ở đây ta không có `head`, cũng không thể duyệt lùi vì là DSLK đơn.

**Ý tưởng thông minh:**
Thay vì thực sự xóa cấu trúc node hiện tại, ta sao chép dữ liệu từ `node.next` đè lên `node` hiện tại, rồi xóa `node.next`:
1. `node.val = node.next.val`
2. `node.next = node.next.next`

```python
def deleteNode(node: ListNode):
    """
    Xóa node được chỉ định mà không cần biết con trỏ head.
    """
    node.val = node.next.val
    node.next = node.next.next
```

- **Độ phức tạp thời gian:** $T(n) = O(1)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 06. Xóa Phần tử Trùng lặp trong Danh sách đã Sắp xếp (Remove Duplicates from Sorted List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 83 | GfG: Remove duplicate element from sorted Linked List
- **Đường dẫn thực hành:** [LeetCode #83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một danh sách liên kết đã được sắp xếp tăng dần. Hãy xóa tất cả các phần tử trùng lặp sao cho mỗi giá trị chỉ xuất hiện đúng một lần. Trả về danh sách sau khi lọc bỏ trùng lặp.

**Ví dụ:**
```text
Đầu vào: 1 -> 1 -> 2 -> 3 -> 3 -> None
Đầu ra:  1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Vì danh sách đã được sắp xếp, các phần tử có cùng giá trị chắc chắn nằm liền kề nhau:
- Dùng một con trỏ `curr = head`.
- So sánh `curr.val` với `curr.next.val`:
  - Nếu bằng nhau: bỏ qua node kế tiếp bằng cách trỏ `curr.next = curr.next.next`.
  - Nếu khác nhau: an tâm tiến con trỏ lên `curr = curr.next`.

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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 07. Kiểm tra Danh sách Liên kết Đối xứng (Palindrome Linked List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 234 | GfG: Check if Linked List is Palindrome
- **Đường dẫn thực hành:** [LeetCode #234](https://leetcode.com/problems/palindrome-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1)

### Mô tả bài toán
Cho `head` của một singly linked list, hãy kiểm tra xem chuỗi giá trị trong danh sách có phải là một đối xứng (palindrome) hay không. Yêu cầu đạt độ phức tạp $O(n)$ thời gian và $O(1)$ bộ nhớ phụ.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 2 -> 1 -> None  ==>  True
Đầu vào: 1 -> 2 -> 3 -> None        ==>  False
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Để đạt $O(1)$ bộ nhớ phụ mà không tạo mảng ngoài:
1. **Tìm điểm giữa:** Dùng `slow` và `fast` để xác định nửa sau của danh sách.
2. **Đảo ngược nửa sau:** Áp dụng thuật toán đảo ngược danh sách từ vị trí `slow`.
3. **So sánh hai nửa:** Dùng hai con trỏ xuất phát từ `head` và đầu danh sách nửa sau đã đảo ngược.
4. *(Tùy chọn)* Đảo ngược lại nửa sau để trả danh sách về nguyên trạng.

```python
def isPalindrome(head: ListNode) -> bool:
    if head is None or head.next is None:
        return True

    # 1. Tìm node giữa
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2. Đảo ngược nửa sau từ slow
    prev = None
    curr = slow
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 3. So sánh nửa đầu và nửa sau
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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 08. Giao điểm của Hai Danh sách Liên kết (Intersection of Two Linked Lists)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 160 | GfG: Intersection Point in Y Shaped Linked Lists
- **Đường dẫn thực hành:** [LeetCode #160](https://leetcode.com/problems/intersection-of-two-linked-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)

### Mô tả bài toán
Cho `headA` và `headB` của hai singly linked list, hãy tìm và trả về node mà tại đó hai danh sách bắt đầu giao nhau. Nếu hai danh sách hoàn toàn không giao nhau, trả về `None`.

**Ví dụ minh họa:**
```text
A:          a1 -> a2 \
                       c1 -> c2 -> c3 -> None
B:    b1 -> b2 -> b3 /
Giao điểm chính là node c1.
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Gọi độ dài phần riêng của A là $a$, phần riêng của B là $b$, và độ dài phần chung là $c$:
- Con trỏ $p_A$ duyệt qua A rồi nhảy sang đầu B sẽ đi quãng đường $a + c + b$.
- Con trỏ $p_B$ duyệt qua B rồi nhảy sang đầu A sẽ đi quãng đường $b + c + a$.
- Vì $a + c + b = b + c + a$, hai con trỏ sẽ đi cùng tổng số bước và chạm nhau chính xác tại giao điểm `c1` (hoặc cùng bằng `None` nếu không giao nhau).

```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    pA = headA
    pB = headB

    while pA is not pB:
        pA = pA.next if pA is not None else headB
        pB = pB.next if pB is not None else headA

    return pA
```

- **Độ phức tạp thời gian:** $T(m, n) = O(m + n)$.
- **Bộ nhớ phụ:** $S(m, n) = O(1)$.

</details>

---

# Phần 2: Cấp độ Trung bình (Medium Level)

## Bài 09. Xóa Node thứ N từ Cuối Danh sách (Remove Nth Node From End of List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 19 | GfG: Nth node from end of linked list
- **Đường dẫn thực hành:** [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một danh sách liên kết, hãy xóa node thứ $n$ tính từ cuối danh sách lên và trả về `head` của danh sách sau khi xóa trong **đúng một lượt duyệt**.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None, n = 2
Đầu ra:  1 -> 2 -> 3 -> 5 -> None (node 4 bị xóa)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
- Sử dụng `dummy` node trỏ tới `head` để xử lý mượt mà trường hợp xóa chính node đầu tiên.
- Khởi tạo hai con trỏ `fast` và `slow` bắt đầu tại `dummy`.
- Cho `fast` tiến về phía trước $n + 1$ bước để duy trì khoảng cách cố định giữa `fast` và `slow`.
- Sau đó, cho cả `fast` và `slow` cùng tịnh tiến 1 bước mỗi lần cho đến khi `fast` chạm `None`. Lúc này, `slow` sẽ đứng ngay trước node cần xóa.
- Thực hiện xóa: `slow.next = slow.next.next`.

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Cho fast đi trước n + 1 bước
    for _ in range(n + 1):
        fast = fast.next

    # Cùng tiến cho đến khi fast chạm None
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # Xóa node thứ n từ cuối
    slow.next = slow.next.next

    return dummy.next
```

- **Độ phức tạp thời gian:** $T(L) = O(L)$ với $L$ là tổng số node của danh sách (duyệt đúng 1 lần).
- **Bộ nhớ phụ:** $S(L) = O(1)$.

</details>

---

## Bài 10. Tìm Điểm Bắt đầu của Chu trình (Linked List Cycle II)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 142 | GfG: Find the first node of loop in linked list
- **Đường dẫn thực hành:** [LeetCode #142](https://leetcode.com/problems/linked-list-cycle-ii/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1)

### Mô tả bài toán
Cho một linked list, hãy tìm và trả về **node nơi chu trình bắt đầu**. Nếu danh sách không có chu trình, trả về `None`. Yêu cầu không được sửa đổi cấu trúc danh sách liên kết.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích toán học & Thuật toán Floyd giai đoạn 2
Gọi:
- $L_1$: khoảng cách từ `head` đến node bắt đầu chu trình.
- $L_2$: khoảng cách từ node bắt đầu chu trình đến điểm gặp nhau của `slow` và `fast`.
- $C$: chu vi của chu trình.

Tại điểm gặp nhau:
- Quãng đường `slow` đã đi: $d_{\text{slow}} = L_1 + L_2$
- Quãng đường `fast` đã đi: $d_{\text{fast}} = L_1 + L_2 + k \cdot C$ (với $k \ge 1$)
- Vì tốc độ của `fast` gấp đôi `slow`: $d_{\text{fast}} = 2 \cdot d_{\text{slow}}$
$$\implies L_1 + L_2 + k \cdot C = 2(L_1 + L_2) \implies L_1 = k \cdot C - L_2$$

**Ý nghĩa:** Khoảng cách từ `head` đến điểm bắt đầu chu trình ($L_1$) bằng đúng khoảng cách từ điểm gặp nhau đi tiếp theo chu trình để về lại điểm bắt đầu ($k \cdot C - L_2$).
**Chiến thuật:** Sau khi hai con trỏ gặp nhau:
1. Đưa một con trỏ về lại `head`, giữ con trỏ kia tại điểm gặp nhau.
2. Cho cả hai cùng tiến từng bước một. Điểm chúng gặp nhau lần thứ hai chính là **node bắt đầu chu trình**.

```python
def detectCycle(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    # Giai đoạn 1: Tìm điểm gặp nhau
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None  # Không có chu trình

    # Giai đoạn 2: Tìm điểm bắt đầu chu trình
    ptr1 = head
    ptr2 = slow
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 11. Đan xen Danh sách Liên kết (Reorder List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 143 | GfG: Reorder List
- **Đường dẫn thực hành:** [LeetCode #143](https://leetcode.com/problems/reorder-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/reorder-list/1)

### Mô tả bài toán
Cho một singly linked list có dạng:
$$L_0 \to L_1 \to \dots \to L_{n-1} \to L_n$$

Hãy sắp xếp lại danh sách theo thứ tự đan xen:
$$L_0 \to L_n \to L_1 \to L_{n-1} \to L_2 \to L_{n-2} \to \dots$$
Thao tác phải được thực hiện trực tiếp trên các liên kết (*in-place*), không được thay đổi giá trị node.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None
Đầu ra:  1 -> 5 -> 2 -> 4 -> 3 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Bài toán là sự kết hợp hoàn hảo của 3 kỹ thuật cơ bản:
1. **Tìm node giữa** danh sách bằng Fast & Slow pointers để tách danh sách thành hai nửa $L_{\text{first}}$ và $L_{\text{second}}$.
2. **Đảo ngược nửa sau** của danh sách ($L_{\text{second}}$).
3. **Trộn xen kẽ** (Interleave) từng cặp node của nửa đầu và nửa sau đã đảo.

```python
def reorderList(head: ListNode) -> None:
    if head is None or head.next is None:
        return

    # 1. Tìm node giữa
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Tách hai nửa
    second = slow.next
    slow.next = None

    # 2. Đảo ngược nửa sau
    prev = None
    curr = second
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    # 3. Trộn xen kẽ hai nửa
    first = head
    while second is not None:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 12. Gom nhóm Node theo Vị trí Chẵn - Lẻ (Odd Even Linked List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 328 | GfG: Rearrange a linked list
- **Đường dẫn thực hành:** [LeetCode #328](https://leetcode.com/problems/odd-even-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một singly linked list. Hãy nhóm tất cả các node ở **vị trí chỉ số lẻ** lại với nhau trước, theo sau là các node ở **vị trí chỉ số chẵn** (chỉ số tính từ 1: node 1, node 3, node 5... rồi đến node 2, node 4...). Thứ tự tương đối của các node trong từng nhóm phải được giữ nguyên.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None
Đầu ra:  1 -> 3 -> 5 -> 2 -> 4 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
- Dùng `odd` trỏ vào node 1, `even` trỏ vào node 2. Lưu lại `even_head = even` để sau này nối đuôi nhóm lẻ vào đầu nhóm chẵn.
- Trong vòng lặp, ta nối `odd.next = even.next`, sau đó tịnh tiến `odd`.
- Tiếp tục nối `even.next = odd.next`, sau đó tịnh tiến `even`.
- Khi kết thúc duyệt, nối đuôi của nhóm lẻ với đầu của nhóm chẵn: `odd.next = even_head`.

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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 13. Cộng Hai Số Dạng Danh Sách Liên Kết (Add Two Numbers)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 2 | GfG: Add two numbers represented by linked lists
- **Đường dẫn thực hành:** [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1)

### Mô tả bài toán
Cho hai danh sách liên kết khác rỗng đại diện cho hai số nguyên không âm. Các chữ số được lưu trữ theo **thứ tự đảo ngược** (chữ số hàng đơn vị nằm ở `head`). Hãy cộng hai số đó và trả về kết quả dưới dạng một danh sách liên kết tương tự.

**Ví dụ:**
```text
l1: 2 -> 4 -> 3 (đại diện cho số 342)
l2: 5 -> 6 -> 4 (đại diện cho số 465)
Tổng: 342 + 465 = 807
Đầu ra: 7 -> 0 -> 8 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
- Duyệt đồng thời cả hai danh sách và duy trì biến nhớ `carry`.
- Tại mỗi cột:
  $$\text{sum} = \text{val}_1 + \text{val}_2 + \text{carry}$$
  $$\text{chữ số mới} = \text{sum} \pmod{10}, \quad \text{carry mới} = \lfloor \text{sum} / 10 \rfloor$$
- Tạo node mới chứa chữ số này và gắn vào sau `tail`.
- Sau khi cả hai danh sách đều rỗng, nếu `carry > 0` thì phải tạo thêm một node cuối chứa `carry`.

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

- **Độ phức tạp thời gian:** $T(m, n) = O(\max(m, n))$.
- **Bộ nhớ phụ:** $S(m, n) = O(\max(m, n))$ cho danh sách kết quả trả về.

</details>

---

## Bài 14. Hoán đổi Từng Cặp Node Liền kề (Swap Nodes in Pairs)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 24 | GfG: Pairwise swap elements of a linked list
- **Đường dẫn thực hành:** [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

### Mô tả bài toán
Cho một singly linked list, hãy hoán đổi vị trí của từng cặp node liền kề nhau và trả về `head` mới. Bạn không được phép thay đổi giá trị bên trong node mà phải thay đổi chính các con trỏ liên kết.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> None
Đầu ra:  2 -> 1 -> 4 -> 3 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng `dummy` node đứng trước cặp cần đổi:
- Đặt `prev = dummy`, với cặp cần đổi là `first = prev.next` và `second = first.next`.
- Đổi liên kết:
  1. `first.next = second.next`
  2. `second.next = first`
  3. `prev.next = second`
- Nhảy `prev` lên `first` để chuẩn bị cho cặp tiếp theo.

```python
def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next

        # Thực hiện hoán đổi liên kết
        first.next = second.next
        second.next = first
        prev.next = second

        # Tiến con trỏ sang cặp kế tiếp
        prev = first

    return dummy.next
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 15. Sao chép Danh sách có Con trỏ Ngẫu nhiên (Copy List with Random Pointer)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 138 | GfG: Clone a linked list with next and random pointer
- **Đường dẫn thực hành:** [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

### Mô tả bài toán
Một danh sách liên kết có độ dài $n$ mà trong đó mỗi node ngoài con trỏ `next` còn chứa thêm con trỏ `random` có thể trỏ tới bất kỳ node nào trong danh sách hoặc `None`. Hãy tạo một bản sao sâu (**Deep Copy**) hoàn chỉnh của danh sách này.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán tối ưu $O(1)$ không gian phụ
Có hai cách tiếp cận:
- *Cách 1:* Dùng bảng băm `dict` lưu ánh xạ `{node_cũ: node_mới}`, độ phức tạp không gian $O(n)$.
- *Cách 2 (Tối ưu $O(1)$ bộ nhớ phụ):*
  1. **Nhân bản xen kẽ:** Tạo node copy và chèn ngay sau mỗi node gốc:  
     `A -> A' -> B -> B' -> C -> C'`.
  2. **Gán con trỏ random:**  
     `curr.next.random = curr.random.next` (nếu `curr.random` tồn tại).
  3. **Tách rời hai danh sách:** Khôi phục danh sách gốc và bóc tách danh sách clone hoàn chỉnh.

```python
class NodeWithRandom:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'NodeWithRandom') -> 'NodeWithRandom':
    if head is None:
        return None

    # Bước 1: Nhân bản node xen kẽ
    curr = head
    while curr is not None:
        copy_node = NodeWithRandom(curr.val, curr.next)
        curr.next = copy_node
        curr = copy_node.next

    # Bước 2: Thiết lập con trỏ random cho node copy
    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Bước 3: Tách danh sách copy ra khỏi danh sách gốc
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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$ (không dùng bảng băm phụ trợ).

</details>

---

## Bài 16. Sắp xếp Danh sách Liên kết (Sort List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 148 | GfG: Sort a linked list
- **Đường dẫn thực hành:** [LeetCode #148](https://leetcode.com/problems/sort-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1)

### Mô tả bài toán
Cho `head` của một danh sách liên kết, hãy sắp xếp danh sách theo thứ tự tăng dần với yêu cầu nghiêm ngặt: thời gian chạy $O(n \log n)$ và bộ nhớ phụ tối thiểu.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Thuật toán sắp xếp lý tưởng nhất trên danh sách liên kết là **Merge Sort**:
1. **Chia:** Tìm node giữa bằng kỹ thuật Fast & Slow pointer, ngắt liên kết đôi để tách thành hai nửa độc lập.
2. **Trị:** Đệ quy gọi sắp xếp cho nửa trái và nửa phải.
3. **Kết hợp:** Trộn hai danh sách con đã sắp xếp bằng thuật toán đã làm ở Bài 04.

```python
def sortList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    # 1. Tìm node giữa và tách đôi
    prev = None
    slow = fast = head
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Ngắt liên kết để tạo hai nửa độc lập
    prev.next = None

    # 2. Đệ quy sắp xếp từng nửa
    left = sortList(head)
    right = sortList(slow)

    # 3. Hợp nhất hai nửa đã sắp xếp
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

- **Độ phức tạp thời gian:** $T(n) = O(n \log n)$ trong mọi trường hợp (tốt nhất, trung bình, xấu nhất).
- **Bộ nhớ phụ:** $S(n) = O(\log n)$ do stack đệ quy.

</details>

---

> © 2026 TS. Vũ Đức Minh – Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo, Trường Đại học Kinh tế Quốc dân (NEU).
