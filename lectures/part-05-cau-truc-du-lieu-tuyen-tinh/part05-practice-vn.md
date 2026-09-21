# 📝 Hệ thống Bài tập Thực hành: Danh sách Liên kết (Linked Lists Practice Set)

> **Học phần:** Cấu trúc Dữ liệu và Giải thuật với Python (DSAI1002)  
> **Chủ đề:** Cấu trúc Dữ liệu Tuyến tính – Danh sách Liên kết (Linear Data Structures – Linked Lists)  
> **Tài liệu tham khảo:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Cấu trúc bộ tài liệu:**
> - **Phần 1:** Câu hỏi Trắc nghiệm & Lý thuyết Cốt lõi (12 câu Quiz trắc nghiệm có giải thích chi tiết)
> - **Phần 2:** Bài tập Tự luận, Phân tích & Chứng minh Toán học (5 bài toán chuyên sâu)
> - **Phần 3:** Bài tập Lập trình Cơ bản – Easy Level (8 bài toán chuẩn LeetCode & GeeksforGeeks)
> - **Phần 4:** Bài tập Lập trình Trung bình – Medium Level (8 bài toán chuẩn LeetCode & GeeksforGeeks)

---

## 📌 Bảng Tổng hợp Bài tập Luyện Code (LeetCode & GeeksforGeeks)

| STT | Tên bài toán | Cấp độ | Kỹ thuật trọng tâm | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** (Đảo ngược DSLK) | 🟢 Easy | 3 con trỏ (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Middle of the Linked List** (Tìm node giữa) | 🟢 Easy | Fast & Slow Pointers | [#876](https://leetcode.com/problems/middle-of-the-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1) |
| 03 | **Linked List Cycle** (Phát hiện chu trình) | 🟢 Easy | Floyd's Tortoise and Hare | [#141](https://leetcode.com/problems/linked-list-cycle/) | [GfG Practice](https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1) |
| 04 | **Merge Two Sorted Lists** (Hợp nhất 2 DSLK đã sắp xếp) | 🟢 Easy | Dummy Sentinel Node | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 05 | **Delete Node Without Head** (Xóa node không cần head) | 🟢 Easy | Kỹ thuật sao chép giá trị node kế cận | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 06 | **Remove Duplicates from Sorted List** (Xóa trùng lặp) | 🟢 Easy | Quét và nhảy liên kết bỏ qua node trùng | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 07 | **Palindrome Linked List** (DSLK đối xứng) | 🟢 Easy | Slow/Fast + Reversal + Comparison | [#234](https://leetcode.com/problems/palindrome-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1) |
| 08 | **Intersection of Two Linked Lists** (Giao điểm 2 DSLK) | 🟢 Easy | Two-Pointer Traversal Switch | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |
| 09 | **Remove Nth Node From End** (Xóa node thứ N từ cuối) | 🟡 Medium | Two Pointers with Fixed Gap ($N$) | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Linked List Cycle II** (Tìm điểm bắt đầu chu trình) | 🟡 Medium | Floyd's Phase 2 Mathematical Reset | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | [GfG Practice](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1) |
| 11 | **Reorder List** (Đan xen danh sách) | 🟡 Medium | Split + Reverse + Interleave | [#143](https://leetcode.com/problems/reorder-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reorder-list/1) |
| 12 | **Odd Even Linked List** (Gom nhóm node vị trí chẵn/lẻ) | 🟡 Medium | Multi-pointer Relinking in-place | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** (Cộng 2 số dạng DSLK ngược) | 🟡 Medium | Elementary Math with Carry Simulation | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Practice](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** (Đổi chỗ từng cặp node liền kề) | 🟡 Medium | Dummy Node + Pointer Swap | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Practice](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Copy List with Random Pointer** (Clone DSLK ngẫu nhiên) | 🟡 Medium | Interweaving Nodes in-place / Hash Map | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |
| 16 | **Sort List** (Sắp xếp DSLK tối ưu) | 🟡 Medium | Merge Sort on Linked List ($O(n \log n)$) | [#148](https://leetcode.com/problems/sort-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/sort-a-linked-list/1) |

---

# Phần 1: Câu hỏi Trắc nghiệm & Lý thuyết (Conceptual Quizzes)

### Quiz 01. So sánh chi phí bộ nhớ giữa Mảng và Danh sách liên kết đơn
Trong kiến trúc máy tính 64-bit, nhận định nào sau đây là **chính xác nhất** về chi phí bộ nhớ khi lưu trữ $n$ phần tử số nguyên?

- [ ] A. Danh sách liên kết đơn luôn tốn ít bộ nhớ hơn mảng vì kích thước của nó co giãn linh hoạt.
- [ ] B. Danh sách liên kết đơn tiêu tốn thêm bộ nhớ cho con trỏ `next` (8 bytes) tại mỗi node, cộng thêm chi phí overhead của đối tượng node.
- [ ] C. Mảng tĩnh và danh sách liên kết đơn tiêu tốn lượng bộ nhớ hoàn toàn bằng nhau.
- [ ] D. Danh sách liên kết đơn tốn gấp 4 lần bộ nhớ so với danh sách liên kết đôi.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
- Trong mảng (hoặc `array` kiểu C thuần), các phần tử nằm liên tiếp nhau và chỉ tốn đúng kích thước của dữ liệu nguyên thủy (ví dụ $4$ hoặc $8$ bytes mỗi số).
- Trong singly linked list, mỗi phần tử được gói trong một `Node`. Trên hệ thống 64-bit, ngoài dữ liệu, mỗi node bắt buộc phải chứa ít nhất 1 con trỏ `next` (chiếm 8 bytes). Ngoài ra, trong Python, mỗi đối tượng `Node` là một PyObject có phần header (PyObject_HEAD) chiếm thêm 16 bytes. Do đó, danh sách liên kết luôn có **memory overhead** lớn hơn đáng kể so với mảng liền khối.

</details>

---

### Quiz 02. Khả năng truy cập ngẫu nhiên (Random Access)
Tại sao phép truy cập phần tử thứ $i$ (`A[i]`) trên mảng có độ phức tạp $O(1)$, trong khi trên danh sách liên kết đơn lại là $O(n)$?

- [ ] A. Vì CPU không hỗ trợ đọc bộ nhớ của danh sách liên kết.
- [ ] B. Vì mảng lưu trữ các phần tử tại các ô nhớ vật lý liên tiếp nhau, cho phép tính địa chỉ trực tiếp qua công thức `Address(i) = Base + i * Size`, còn linked list phân tán rải rác trong bộ nhớ và buộc phải duyệt tuần tự từ `head`.
- [ ] C. Vì con trỏ `head` của linked list không biết kích thước của các node.
- [ ] D. Vì Python list được biên dịch thành mã máy tối ưu hơn class tự tạo.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
- Mảng sử dụng mô hình bộ nhớ liên tục (*contiguous memory allocation*). Nhờ đó, địa chỉ của ô nhớ thứ $i$ được suy ra trực tiếp chỉ bằng một phép nhân và một phép cộng số học: $\text{Base} + i \times \text{SizeOfElement}$, đạt thời gian $O(1)$.
- Linked list lưu trữ các node ở các vị trí bất kỳ trên bộ nhớ Heap. Địa chỉ của node thứ $i$ chỉ được biết khi ta đã đọc được con trỏ `next` của node thứ $i - 1$. Do đó, để đến được node thứ $i$, bắt buộc phải duyệt tuần tự qua $i$ bước liên kết từ `head`, dẫn tới chi phí trường hợp xấu nhất là $O(n)$.

</details>

---

### Quiz 03. Độ phức tạp của thao tác xóa node
Cho một danh sách liên kết đơn có $n$ node. Thao tác xóa node có độ phức tạp thời gian là $O(1)$ trong trường hợp nào sau đây?

- [ ] A. Xóa node ở cuối danh sách khi chỉ biết con trỏ `head`.
- [ ] B. Xóa node có giá trị bằng `x` bất kỳ.
- [ ] C. Xóa node đầu danh sách (`head`), hoặc xóa node kế tiếp ngay sau một node `prev_node` đã có sẵn tham chiếu.
- [ ] D. Xóa node thứ $k$ bất kỳ tính từ đầu danh sách.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: C**

**Giải thích:**
- Xóa node đầu danh sách chỉ cần: `self.head = self.head.next` $\to O(1)$.
- Xóa node ngay sau `prev_node` chỉ cần: `prev_node.next = prev_node.next.next` $\to O(1)$.
- Các trường hợp còn lại (xóa cuối khi chỉ có `head`, xóa theo giá trị `x`, xóa vị trí thứ $k$) đều đòi hỏi phải duyệt từ `head` để tìm node trước node cần xóa, do đó mất $O(n)$ thời gian.

</details>

---

### Quiz 04. Ưu điểm nổi bật của Doubly Linked List so với Singly Linked List
Ưu điểm lớn nhất của Danh sách liên kết đôi (Doubly Linked List) so với Danh sách liên kết đơn là gì?

- [ ] A. Tiết kiệm bộ nhớ hơn vì không cần `None` ở cuối.
- [ ] B. Có thể duyệt theo cả hai chiều (tiến và lùi), đồng thời xóa một node đã biết trong $O(1)$ mà không cần duyệt tìm node đứng trước (*predecessor*).
- [ ] C. Cho phép truy cập phần tử thứ $i$ trong thời gian $O(1)$.
- [ ] D. Tự động phát hiện và ngăn ngừa chu trình lặp vô hạn.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Trong singly linked list, nếu ta có con trỏ trỏ trực tiếp đến `node` cần xóa, ta vẫn không thể xóa nó trong $O(1)$ theo cách thông thường vì không biết ai đang trỏ vào nó (node đứng trước). Trong doubly linked list, nhờ con trỏ `node.prev`, ta có thể nối trực tiếp `node.prev.next = node.next` và `node.next.prev = node.prev` ngay lập tức trong $O(1)$.

</details>

---

### Quiz 05. Cơ chế con trỏ trong Circular Singly Linked List có `tail`
Nếu một danh sách liên kết vòng đơn (*Circular Singly Linked List*) chỉ duy trì một con trỏ duy nhất là `tail`, ta có thể thực hiện thao tác nào với thời gian $O(1)$?

- [ ] A. Chỉ có chèn ở cuối danh sách.
- [ ] B. Chỉ có chèn ở đầu danh sách.
- [ ] C. Cả chèn ở đầu (`insert_front`) và chèn ở cuối (`insert_end`).
- [ ] D. Không thể làm được thao tác nào trong $O(1)$ nếu không có con trỏ `head`.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: C**

**Giải thích:**
Vì là danh sách liên kết vòng, node cuối cùng luôn trỏ về node đầu tiên: `tail.next` chính là `head`!
- **Chèn ở đầu:** Tạo `new_node`, gán `new_node.next = tail.next`, sau đó `tail.next = new_node`. Giữ nguyên `tail`. $\to O(1)$.
- **Chèn ở cuối:** Tương tự chèn ở đầu, nhưng sau đó cập nhật thêm `tail = new_node`. $\to O(1)$.
Như vậy, chỉ cần 1 con trỏ `tail`, ta vừa quản lý được node cuối, vừa truy cập được node đầu trong $O(1)$!

</details>

---

### Quiz 06. Kỹ thuật Dummy Sentinel Node
Mục đích chính của việc sử dụng **Dummy Node** (hoặc **Sentinel Node**) khi thao tác với danh sách liên kết là gì?

- [ ] A. Giúp thuật toán chạy nhanh hơn từ $O(n)$ xuống $O(\log n)$.
- [ ] B. Đơn giản hóa mã nguồn bằng cách loại bỏ các câu lệnh `if head is None` hoặc kiểm tra điều kiện biên khi thao tác tại node đầu tiên.
- [ ] C. Giảm thiểu bộ nhớ phụ của chương trình.
- [ ] D. Biến singly linked list thành circular linked list một cách tự động.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Dummy node là một node giả đứng trước `head` (`dummy = ListNode(0, head)`). Khi cần chèn hoặc xóa node ở đầu danh sách, thao tác này được đối xử giống hệt như chèn/xóa ở giữa danh sách (luôn có một node đứng trước là `dummy`), giúp loại bỏ hoàn toàn các trường hợp biên rắc rối và làm code ngắn gọn, không bị lỗi `NullPointerException` / `AttributeError: 'NoneType' object has no attribute 'next'`.

</details>

---

### Quiz 07. Thuật toán Floyd phát hiện chu trình
Trong thuật toán rùa và thỏ của Floyd, nếu một linked list có $n$ node và có chu trình, điều gì đảm bảo con trỏ `fast` (đi 2 bước) nhất định sẽ gặp con trỏ `slow` (đi 1 bước)?

- [ ] A. Vì `fast` sẽ quay đầu lại khi chạm điểm cuối.
- [ ] B. Vì trong mỗi bước, khoảng cách tương đối giữa `fast` và `slow` theo chiều chu trình giảm đi đúng 1 đơn vị ($2 - 1 = 1$). Do khoảng cách là số nguyên hữu hạn, nó chắc chắn sẽ giảm dần về 0.
- [ ] C. Vì `slow` sẽ đứng yên một chỗ chờ `fast` tới.
- [ ] D. Do định lý Master Theorem quy định.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Khi cả hai con trỏ đã cùng nằm trong chu trình có độ dài $C$: giả sử `fast` đang đứng sau `slow` một khoảng cách là $d$ bước ($1 \le d < C$). Sau mỗi nhịp lặp:
- `slow` tiến 1 bước.
- `fast` tiến 2 bước.
Khoảng cách mới giữa chúng theo chiều kim đồng hồ sẽ là: $(d + 2 - 1) \pmod C = (d + 1) \pmod C$, hay nói cách khác, khoảng cách mà `fast` đuổi theo `slow` giảm đi đúng 1 bước sau mỗi vòng. Vì khoảng cách giảm liên tục: $d, d-1, d-2, \dots, 0$, chắc chắn `fast` sẽ bắt kịp `slow` tại một node mà không thể "nhảy cóc" qua mặt `slow`.

</details>

---

### Quiz 08. Binary Search trên Danh sách liên kết đã sắp xếp
Tại sao ta **không thể** áp dụng hiệu quả thuật toán Tìm kiếm nhị phân (Binary Search) để đạt độ phức tạp $O(\log n)$ trên một Singly Linked List đã được sắp xếp tăng dần?

- [ ] A. Vì Linked List không thể lưu trữ các giá trị có thứ tự.
- [ ] B. Vì phép so sánh giữa các node trong Linked List tốn $O(n)$ thời gian.
- [ ] C. Vì Linked List không hỗ trợ truy cập phần tử trung vị (`mid`) trong $O(1)$; mỗi lần tìm node giữa phải duyệt tuần tự mất $O(k)$ thời gian, dẫn tới tổng thời gian vẫn là $O(n)$.
- [ ] D. Binary Search hoàn toàn chạy được $O(\log n)$ trên Linked List nếu dùng con trỏ kép.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: C**

**Giải thích:**
Hệ thức truy hồi của Binary Search trên mảng là: $T(n) = T(n/2) + O(1) \implies T(n) = O(\log n)$ (nhờ tìm phần tử ở giữa `mid = (low + high) // 2` trong $O(1)$).
Trên Linked list, để tìm phần tử giữa một khoảng có độ dài $k$, ta phải mất $O(k)$ bước duyệt. Khi đó:
$$T(n) = T(n/2) + O(n) \implies T(n) = O(n)$$
Do đó, Binary Search trên DSLK không đem lại bất kỳ cải thiện nào về bậc độ phức tạp so với Tìm kiếm tuyến tính ($O(n)$). Muốn tìm kiếm nhị phân hiệu quả trên cấu trúc liên kết, ta phải chuyển sang dùng **Skip List** hoặc **Cây tìm kiếm nhị phân (Binary Search Tree)**.

</details>

---

### Quiz 09. Cache Locality và Hiệu năng phần cứng
Xét về góc độ kiến trúc máy tính và bộ nhớ đệm (CPU Cache), tại sao việc duyệt qua một mảng $1.000.000$ số nguyên thường nhanh hơn rất nhiều (từ 5 đến 20 lần) so với duyệt qua một linked list có $1.000.000$ node, dù cả hai đều có độ phức tạp lý thuyết là $O(n)$?

- [ ] A. Vì linked list làm tăng nhiệt độ CPU.
- [ ] B. Vì mảng có tính định vị không gian tuyệt vời (**Spatial Locality**), khi truy cập một phần tử, cả đường truyền bộ nhớ đệm (Cache Line, thường 64 bytes) sẽ nạp sẵn các phần tử lân cận vào L1/L2 Cache; trong khi các node của linked list phân tán rải rác trên RAM, gây ra liên tiếp các lần trượt cache (**Cache Misses**).
- [ ] C. Vì ngôn ngữ lập trình Python chỉ hỗ trợ cache cho mảng.
- [ ] D. Do kích thước con trỏ `next` làm tràn thanh ghi của CPU.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Đây là bài học kinh điển về sự khác biệt giữa **Độ phức tạp lý thuyết** ($O(n)$) và **Hiệu năng thực tế trên phần cứng**:
- Mảng liên tục trong RAM: CPU nạp sẵn 1 khối 64 bytes (Cache line) chứa nhiều phần tử tiếp theo vào L1/L2 Cache cực nhanh $\to$ Hầu như luôn gặp **Cache Hit**.
- Linked List: mỗi lần `curr = curr.next`, CPU phải nhảy tới một địa chỉ ngẫu nhiên trên Heap. Dữ liệu không nằm trong Cache $\to$ **Cache Miss** $\to$ CPU phải tạm dừng chu kỳ lệnh chờ nạp dữ liệu từ thanh RAM chính với độ trễ lớn (hàng trăm chu kỳ CPU).

</details>

---

### Quiz 10. Tìm node thứ k từ cuối danh sách
Cho một singly linked list có độ dài $n$ ($n > k$). Nếu sử dụng kỹ thuật hai con trỏ `fast` và `slow` để tìm node thứ $k$ từ cuối chỉ trong **một lượt duyệt**, ban đầu con trỏ `fast` phải xuất phát trước con trỏ `slow` bao nhiêu bước?

- [ ] A. $k - 1$ bước
- [ ] B. $k$ bước
- [ ] C. $k + 1$ bước
- [ ] D. $2k$ bước

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Nếu cho `fast` đi trước `slow` đúng $k$ bước, khoảng cách giữa `fast` và `slow` sẽ luôn được giữ cố định là $k$ node.
Khi `fast` tiến đến vị trí sau node cuối cùng (`fast is None`), con trỏ `slow` sẽ dừng lại chính xác tại node cách phần kết thúc $k$ vị trí, tức là **node thứ $k$ từ cuối**.

</details>

---

### Quiz 11. Đảo ngược danh sách liên kết đơn in-place
Số lượng con trỏ tối thiểu cần thiết để đảo ngược một danh sách liên kết đơn ngay tại chỗ (*in-place*) mà không làm đứt đoạn hay thất lạc dữ liệu là bao nhiêu?

- [ ] A. 1 con trỏ
- [ ] B. 2 con trỏ
- [ ] C. 3 con trỏ
- [ ] D. 4 con trỏ

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: C**

**Giải thích:**
Bắt buộc cần 3 con trỏ:
1. `prev`: lưu node phía trước (đích đến mới của liên kết đảo ngược).
2. `curr`: node hiện tại đang xử lý.
3. `next_temp`: lưu node đứng sau `curr` trước khi thực hiện gán `curr.next = prev`. Nếu không có con trỏ thứ 3 này, ngay sau lệnh đổi hướng, ta sẽ mất hoàn toàn liên kết đến toàn bộ phần danh sách còn lại phía sau.

</details>

---

### Quiz 12. Phát hiện danh sách liên kết có độ dài Chẵn hay Lẻ
Cho con trỏ `head` của một singly linked list. Để kiểm tra danh sách có tổng số node là chẵn hay lẻ chỉ trong một lượt duyệt với số bước lặp ít nhất, ta nên:

- [ ] A. Duyệt đếm toàn bộ số node rồi lấy `count % 2`.
- [ ] B. Cho một con trỏ nhảy 2 bước mỗi lần (`current = current.next.next`). Nếu dừng lại ở `current is None` thì độ dài là chẵn; nếu dừng lại ở `current.next is None` thì độ dài là lẻ.
- [ ] C. Đảo ngược danh sách rồi so sánh node đầu và node cuối.
- [ ] D. Bắt buộc phải chuyển danh sách sang dạng mảng mới kiểm tra được.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Cách B giúp giải quyết bài toán chỉ với $\lceil n/2 \rceil$ bước lặp:
- Ban đầu `current = head`.
- Tại mỗi vòng lặp, kiểm tra `while current is not None and current.next is not None: current = current.next.next`.
- Khi vòng lặp kết thúc:
  - Nếu `current is None`: số node là **chẵn** (bước nhảy cuối cùng từ node $n-1$ ra ngoài phạm vi).
  - Nếu `current.next is None`: số node là **lẻ** (con trỏ dừng lại đúng tại node cuối cùng $n$).

</details>

---

# Phần 2: Bài tập Tự luận & Phân tích Thuật toán (Theoretical Problems)

## Bài T1. Phân tích Bất biến vòng lặp (Loop Invariant) của thuật toán Đảo ngược DSLK

### Đề bài
Cho đoạn mã Python kinh điển đảo ngược singly linked list:

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

1. Hãy phát biểu **Bất biến vòng lặp (Loop Invariant)** của vòng lặp `while`.
2. Chứng minh tính đúng đắn của thuật toán thông qua 3 bước: Khởi tạo (*Initialization*), Duy trì (*Maintenance*) và Kết thúc (*Termination*).

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

### 1. Phát biểu Bất biến vòng lặp
Tại thời điểm bắt đầu mỗi vòng lặp `while`:
- Con trỏ `prev` đang trỏ vào đầu của một danh sách liên kết đã được đảo ngược hoàn chỉnh chứa các phần tử từ vị trí ban đầu $0$ đến vị trí hiện tại $- 1$.
- Con trỏ `curr` đang trỏ vào đầu của phần danh sách còn lại (chưa bị đảo ngược), bắt đầu từ node ban đầu thứ $i$ đến node cuối cùng.
- Hai danh sách con này hoàn toàn tách rời nhau (không có liên kết chéo nào từ danh sách `prev` sang danh sách `curr`).

### 2. Chứng minh 3 bước
- **Khởi tạo (Initialization):**  
  Trước vòng lặp đầu tiên, `prev = None`, `curr = head`. Danh sách đã đảo ngược là rỗng (`None`), danh sách chưa đảo ngược là toàn bộ danh sách ban đầu. Bất biến hiển nhiên đúng.
- **Duy trì (Maintenance):**  
  Trong thân vòng lặp:
  - Lưu `next_node = curr.next`.
  - Nối `curr.next = prev`: node `curr` trở thành node đầu mới của danh sách đã đảo ngược.
  - Cập nhật `prev = curr`: danh sách đã đảo ngược nay bao gồm thêm node `curr`.
  - Cập nhật `curr = next_node`: danh sách chưa đảo ngược nay bắt đầu từ `next_node`.
  Sau các thao tác trên, `prev` chứa thêm 1 phần tử được đảo đúng thứ tự, và `curr` tiến thêm 1 bước. Bất biến được bảo toàn trước vòng lặp kế tiếp.
- **Kết thúc (Termination):**  
  Vòng lặp kết thúc khi `curr is None`, tức là không còn node nào trong danh sách chưa đảo ngược. Theo bất biến, `prev` lúc này chứa toàn bộ các node của danh sách ban đầu theo thứ tự đảo ngược hoàn chỉnh. Hàm trả về `prev` là hoàn toàn chính xác.

</details>

---

## Bài T2. Chứng minh Toán học Thuật toán Floyd giai đoạn 2 (Tìm điểm bắt đầu chu trình)

### Đề bài
Trong bài toán LeetCode #142, sau khi con trỏ `slow` và `fast` gặp nhau lần đầu tiên trong chu trình, thuật toán đặt một con trỏ `ptr1 = head` và giữ nguyên `ptr2 = slow` tại điểm gặp nhau, sau đó cho cả hai cùng tiến từng bước một ($1$ node/lượt). Điểm gặp nhau lần thứ hai chính là **node bắt đầu chu trình**.

Hãy thiết lập phương trình toán học chứng minh tính đúng đắn của khẳng định trên.

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

### Chứng minh toán học
Ký hiệu các tham số hình học của danh sách liên kết có chu trình như sau:
- $L_1$: khoảng cách (số bước đi) từ `head` đến node bắt đầu chu trình.
- $L_2$: khoảng cách từ node bắt đầu chu trình đến điểm gặp nhau đầu tiên của `slow` và `fast`.
- $C$: tổng số node (chu vi) của chu trình ($C \ge 1$).

```text
head ---------( L1 )---------> [Start of Cycle] ---------( L2 )---------> [Meeting Point]
                                     ^                                          |
                                     |----------------( C - L2 )----------------+
```

1. **Quãng đường di chuyển tại lần gặp đầu tiên:**
   - Con trỏ `slow` di chuyển quãng đường:
     $$d_{\text{slow}} = L_1 + L_2$$
   - Con trỏ `fast` di chuyển quãng đường bằng tổng quãng đường vào chu trình cộng thêm $k$ vòng quay trong chu trình ($k \ge 1$):
     $$d_{\text{fast}} = L_1 + L_2 + k \cdot C$$

2. **Mối quan hệ vận tốc:**
   Vì mỗi bước `fast` đi gấp đôi `slow`:
   $$d_{\text{fast}} = 2 \cdot d_{\text{slow}}$$
   $$\implies L_1 + L_2 + k \cdot C = 2(L_1 + L_2)$$
   $$\implies k \cdot C = L_1 + L_2$$
   $$\implies L_1 = k \cdot C - L_2 = (k - 1) \cdot C + (C - L_2)$$

3. **Ý nghĩa của đẳng thức:**
   - Vế trái ($L_1$): là quãng đường một con trỏ xuất phát từ `head` cần đi để chạm đến `Start of Cycle`.
   - Vế phải ($(k - 1)C + (C - L_2)$): là quãng đường một con trỏ xuất phát từ `Meeting Point` cần đi: nó sẽ quay $(k - 1)$ vòng chu trình đầy đủ, cộng thêm quãng đường $(C - L_2)$ để đi từ `Meeting Point` về lại `Start of Cycle`.
   - Vì hai quãng đường này **bằng nhau từng bước một**, nếu ta cho `ptr1` đi từ `head` và `ptr2` đi từ `Meeting Point` với cùng tốc độ 1 bước/nhịp, chúng chắc chắn sẽ chạm nhau lần đầu tiên ngay tại **node bắt đầu chu trình**! $\blacksquare$

</details>

---

## Bài T3. Vì sao Merge Sort là thuật toán sắp xếp tối ưu nhất cho Linked List?

### Đề bài
Khi sắp xếp dữ liệu trên **Mảng**, Quicksort thường được ưa chuộng hơn Merge Sort. Tuy nhiên, khi sắp xếp trên **Danh sách liên kết**, Merge Sort lại được coi là lựa chọn tiêu chuẩn và tối ưu vượt trội.

Hãy giải thích nguyên nhân dựa trên 3 tiêu chí:
1. Chi phí bộ nhớ phụ (Auxiliary Space).
2. Chi phí phân chia và truy cập phần tử (Partitioning & Access Cost).
3. Tính ổn định (Stability).

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

| Tiêu chí | Mảng (Array) | Danh sách liên kết (Linked List) |
|---|---|---|
| **Bộ nhớ phụ khi Merge** | Trên mảng, thao tác trộn đòi hỏi một mảng phụ kích thước $O(n)$ để sao chép dữ liệu. | Trên DSLK, thao tác trộn chỉ cần **đổi hướng các con trỏ liên kết** (`next`), hoàn toàn không cần cấp phát thêm bộ nhớ phụ $\implies S(n) = O(1)$ (nếu khử đệ quy hoặc $O(\log n)$ call stack). |
| **Thao tác Partition của Quicksort** | Trên mảng, Quicksort duyệt ngẫu nhiên từ hai đầu mảng vào giữa ($O(1)$ random access), swap cực nhanh. | Trên DSLK đơn, không thể duyệt lùi (`prev`), việc chọn pivot và phân hoạch Lomuto/Hoare rất kém hiệu quả và làm mất tính liên tục. |
| **Tính định vị bộ nhớ & Trộn** | Thao tác chia đôi mảng mất $O(1)$ qua chỉ số `mid = (low + high) // 2`. | Trên DSLK, tìm điểm giữa mất $O(n)$ bằng con trỏ rùa-thỏ, nhưng tổng thời gian chia đệ quy vẫn thỏa mãn $T(n) = 2T(n/2) + O(n) = O(n \log n)$. |
| **Tính ổn định (Stability)** | Merge Sort trên mảng giữ được tính ổn định. | Merge Sort trên DSLK bảo toàn tuyệt đối thứ tự tương đối ban đầu của các node có giá trị bằng nhau một cách tự nhiên. |

**Kết luận:** Nhờ khả năng hợp nhất hai danh sách đã sắp xếp trong $O(1)$ bộ nhớ phụ và đảm bảo thời gian chạy $O(n \log n)$ trong mọi trường hợp, **Merge Sort** chính là thuật toán sắp xếp tốt nhất cho cấu trúc danh sách liên kết.

</details>

---

## Bài T4. Thiết kế Stack và Queue bằng Danh sách liên kết

### Đề bài
Trình bày phương án thiết kế để cài đặt hai Kiểu dữ liệu trừu tượng (ADT) sau bằng Singly Linked List sao cho tất cả các thao tác chính đều đạt thời gian $O(1)$:
1. **Stack ADT:** `push(x)`, `pop()`, `peek()`.
2. **Queue ADT:** `enqueue(x)`, `dequeue()`, `front()`.

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

### 1. Cài đặt Stack bằng Singly Linked List (Đỉnh Stack ở `head`)
- **Nguyên lý:** Luôn chọn đỉnh Stack (`top`) trùng với node đầu tiên (`head`) của danh sách.
- `push(x)`: Chèn phần tử mới vào đầu danh sách (`insert_front`).  
  `new_node.next = self.head; self.head = new_node` $\implies O(1)$.
- `pop()`: Xóa phần tử ở đầu danh sách (`delete_front`).  
  `val = self.head.val; self.head = self.head.next; return val` $\implies O(1)$.
- `peek()`: Trả về giá trị của `self.head.val` $\implies O(1)$.
- *(Lưu ý: Không được chọn đỉnh Stack ở cuối danh sách, vì khi đó `pop()` sẽ mất $O(n)$ do phải tìm node đứng trước `tail`).*

### 2. Cài đặt Queue bằng Singly Linked List (Dùng 2 con trỏ `head` và `tail`)
- **Nguyên lý:** Đầu hàng đợi (`front`) đặt ở `head` (nơi lấy ra), cuối hàng đợi (`rear`) đặt ở `tail` (nơi thêm vào).
- `enqueue(x)`: Chèn vào cuối danh sách qua con trỏ `tail`.  
  `self.tail.next = new_node; self.tail = new_node` $\implies O(1)$.
- `dequeue()`: Xóa ở đầu danh sách qua con trỏ `head`.  
  `val = self.head.val; self.head = self.head.next` $\implies O(1)$.  
  *(Nếu sau khi xóa mà `self.head is None` thì cập nhật `self.tail = None`).*
- `front()`: Trả về `self.head.val` $\implies O(1)$.

</details>

---

## Bài T5. Tính toán chi phí bộ nhớ thực tế của Node trong Python

### Đề bài
Trong CPython 64-bit:
1. Hãy tính toán dung lượng bộ nhớ thực tế (tính bằng bytes) của một đối tượng `Node` được định nghĩa thông thường:
   ```python
   class Node:
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
2. So sánh với việc sử dụng `__slots__`:
   ```python
   class OptimizedNode:
       __slots__ = ['val', 'next']
       def __init__(self, val, next=None):
           self.val = val
           self.next = next
   ```
3. Ý nghĩa thực tiễn khi xây dựng các hệ thống xử lý dữ liệu lớn (Big Data / Graph) với hàng triệu node?

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

### 1. Phân tích chi tiết bộ nhớ của `Node` thông thường
Trong CPython (64-bit):
- Mỗi instance thông thường có một dictionary nội bộ `__dict__` để chứa các thuộc tính động.
- Header của đối tượng (`PyObject_HEAD`): 16 bytes.
- Con trỏ tham chiếu đến class (`ob_type`): nằm trong header.
- Con trỏ tham chiếu đến `__dict__`: 8 bytes.
- Bản thân `__dict__` (PyDictObject): tối thiểu khoảng 104 đến 144 bytes.
$\implies$ Tổng dung lượng của một `Node` rỗng thông thường dao động từ **150 đến 160 bytes**!

### 2. Tối ưu hóa bằng `__slots__`
Khi khai báo `__slots__ = ['val', 'next']`, Python sẽ không tạo `__dict__` và `__weakref__` cho mỗi instance, mà lưu các thuộc tính trực tiếp trong một mảng con trỏ có kích thước cố định:
- `PyObject_HEAD`: 16 bytes.
- Thuộc tính `val` (con trỏ tham chiếu đến đối tượng dữ liệu): 8 bytes.
- Thuộc tính `next` (con trỏ tham chiếu đến node kế tiếp): 8 bytes.
$\implies$ Tổng dung lượng của một `OptimizedNode` chỉ còn đúng **48 bytes**! *(Tiết kiệm hơn 70% bộ nhớ)*.

### 3. Ý nghĩa thực tiễn
Với một hệ thống xử lý $10.000.000$ nodes:
- Dùng `Node` thông thường: tiêu tốn $\approx 1.5 \text{ GB}$ RAM chỉ riêng cho cấu trúc node (chưa tính dữ liệu).
- Dùng `__slots__`: chỉ tiêu tốn $\approx 480 \text{ MB}$ RAM.
Đây là kỹ thuật bắt buộc phải nắm vững khi triển khai các cấu trúc dữ liệu đồ thị, danh sách liên kết hay cây phân cấp trong các ứng dụng Python thực tế đòi hỏi hiệu năng cao.

</details>

---

# Phần 3: Bài tập Lập trình Cơ bản (Easy Level)

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

# Phần 4: Bài tập Lập trình Trung bình (Medium Level)

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

### Thuật toán Floyd giai đoạn 2
Sau khi hai con trỏ gặp nhau tại lần 1:
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
        return None

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
- Trong vòng lặp:
  - `odd.next = even.next`; `odd = odd.next`
  - `even.next = odd.next`; `even = even.next`
- Khi kết thúc: `odd.next = even_head`.

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
- Sau khi duyệt hết, nếu `carry > 0` thì tạo thêm node cuối chứa `carry`.

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

        first.next = second.next
        second.next = first
        prev.next = second

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
