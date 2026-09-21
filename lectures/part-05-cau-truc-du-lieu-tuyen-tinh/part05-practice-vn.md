# 📝 Hệ thống Bài tập Thực hành: Danh sách Liên kết (Linked Lists Practice Set)

> **Học phần:** Cấu trúc Dữ liệu và Giải thuật với Python (DSAI1002)  
> **Chủ đề:** Cấu trúc Dữ liệu Tuyến tính – Danh sách Liên kết (Linear Data Structures – Linked Lists)  
> **Tài liệu tham khảo:** Narasimha Karumanchi (2020), *Data Structures and Algorithmic Thinking with Python*, Chapter 3.  
> **Cấu trúc bộ tài liệu:**
> - **Phần 1:** Câu hỏi Trắc nghiệm & Lý thuyết Cốt lõi (12 câu Quiz trắc nghiệm có đáp án và giải thích chi tiết)
> - **Phần 2:** Bài tập Tự luận, Phân tích Kiến trúc & Bộ nhớ (5 bài toán chuyên sâu)
> - **Phần 3:** Bài tập Lập trình Cơ bản – Easy Level (8 bài toán chuẩn LeetCode & GeeksforGeeks)
> - **Phần 4:** Bài tập Lập trình Trung bình – Medium Level (8 bài toán chuẩn LeetCode & GeeksforGeeks)

---

## 📌 Bảng Tổng hợp Bài tập Luyện Code (LeetCode & GeeksforGeeks)

| STT | Tên bài toán | Cấp độ | Kỹ thuật trọng tâm | LeetCode | GeeksforGeeks |
|:---:|:---|:---:|:---|:---:|:---:|
| 01 | **Reverse Linked List** (Đảo ngược DSLK) | 🟢 Easy | 3 con trỏ (`prev`, `curr`, `next`) | [#206](https://leetcode.com/problems/reverse-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1) |
| 02 | **Remove Linked List Elements** (Xóa node theo giá trị) | 🟢 Easy | Dummy Sentinel Node | [#203](https://leetcode.com/problems/remove-linked-list-elements/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1) |
| 03 | **Merge Two Sorted Lists** (Hợp nhất 2 DSLK đã sắp xếp) | 🟢 Easy | Dummy Sentinel + So sánh 2 con trỏ | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1) |
| 04 | **Delete Node Without Head** (Xóa node không cần head) | 🟢 Easy | Sao chép giá trị node kế cận | [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1) |
| 05 | **Remove Duplicates from Sorted List** (Xóa trùng lặp) | 🟢 Easy | Quét và nhảy liên kết bỏ qua node trùng | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1) |
| 06 | **Binary to Integer in Linked List** (Chuyển nhị phân sang số) | 🟢 Easy | Duyệt tuần tự và dịch bit ($2 \times \text{ans} + \text{val}$) | [#1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/decimal-equivalent-of-binary-linked-list/1) |
| 07 | **Reverse a Doubly Linked List** (Đảo ngược DSLK đôi) | 🟢 Easy | Hoán đổi cặp con trỏ `prev` và `next` | — | [GfG Practice](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1) |
| 08 | **Intersection of Two Linked Lists** (Giao điểm 2 DSLK) | 🟢 Easy | Cân bằng hiệu độ dài $\|L_A - L_B\|$ | [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [GfG Practice](https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1) |
| 09 | **Remove Nth Node From End** (Xóa node thứ N từ cuối) | 🟡 Medium | Two-Pass đếm độ dài ($L - n$) + Dummy | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) |
| 10 | **Rotate List** (Xoay danh sách k vị trí) | 🟡 Medium | Nối vòng tròn tạm thời + Cắt tại $(L - k)$ | [#61](https://leetcode.com/problems/rotate-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1) |
| 11 | **Partition List** (Phân hoạch DSLK quanh giá trị x) | 🟡 Medium | 2 con trỏ Dummy (`less` và `greater`) | [#86](https://leetcode.com/problems/partition-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/partition-a-linked-list/1) |
| 12 | **Odd Even Linked List** (Gom nhóm node vị trí chẵn/lẻ) | 🟡 Medium | Tách 2 luồng liên kết in-place | [#328](https://leetcode.com/problems/odd-even-linked-list/) | [GfG Practice](https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1) |
| 13 | **Add Two Numbers** (Cộng 2 số dạng DSLK ngược) | 🟡 Medium | Mô phỏng phép cộng số học có nhớ | [#2](https://leetcode.com/problems/add-two-numbers/) | [GfG Practice](https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1) |
| 14 | **Swap Nodes in Pairs** (Đổi chỗ từng cặp node liền kề) | 🟡 Medium | Dummy Node + Hoán đổi 3 liên kết | [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [GfG Practice](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1) |
| 15 | **Remove Duplicates II** (Xóa sạch các node bị trùng) | 🟡 Medium | Sentinel Node + Bỏ qua toàn bộ cụm trùng | [#82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | [GfG Practice](https://www.geeksforgeeks.org/problems/remove-all-occurences-of-duplicates-in-a-linked-list/1) |
| 16 | **Copy List with Random Pointer** (Clone DSLK ngẫu nhiên) | 🟡 Medium | Chèn node copy xen kẽ tối ưu $O(1)$ bộ nhớ | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [GfG Practice](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1) |

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
- Trong mảng (hoặc mảng tĩnh kiểu C), các phần tử nằm liên tiếp nhau và chỉ tốn đúng kích thước của dữ liệu nguyên thủy (ví dụ $4$ hoặc $8$ bytes mỗi số).
- Trong singly linked list, mỗi phần tử được gói trong một `Node`. Trên hệ thống 64-bit, mỗi node bắt buộc phải chứa ít nhất 1 con trỏ `next` (8 bytes). Trong Python, mỗi đối tượng `Node` là một PyObject có phần header (`PyObject_HEAD`) chiếm thêm 16 bytes. Do đó, danh sách liên kết luôn có **memory overhead** lớn hơn đáng kể so với mảng liền khối.

</details>

---

### Quiz 02. Khả năng truy cập ngẫu nhiên (Random Access)
Tại sao phép truy cập phần tử thứ $i$ (`A[i]`) trên mảng có độ phức tạp $O(1)$, trong khi trên danh sách liên kết đơn lại là $O(n)$?

- [ ] A. Vì CPU không hỗ trợ đọc bộ nhớ của danh sách liên kết.
- [ ] B. Vì mảng lưu trữ các phần tử tại các ô nhớ vật lý liên tiếp nhau, cho phép tính địa chỉ trực tiếp qua công thức `Address(i) = Base + i * Size`, còn linked list phân tán rải rác trong bộ nhớ và buộc phải duyệt tuần tự từ `head`.
- [ ] C. Vì con trỏ `head` của linked list không biết kiểu dữ liệu của các node.
- [ ] D. Vì Python list được biên dịch thành mã máy tối ưu hơn class tự tạo.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Mảng sử dụng mô hình bộ nhớ liên tục (*contiguous memory allocation*). Địa chỉ của ô nhớ thứ $i$ được suy ra trực tiếp chỉ bằng một phép nhân và một phép cộng số học: $\text{Base} + i \times \text{SizeOfElement}$, đạt thời gian $O(1)$.
Linked list lưu trữ các node ở các vị trí bất kỳ trên bộ nhớ Heap. Địa chỉ của node thứ $i$ chỉ được biết khi ta đã đọc được con trỏ `next` của node thứ $i - 1$. Do đó, để đến được node thứ $i$, bắt buộc phải duyệt tuần tự qua $i$ bước liên kết từ `head`, dẫn tới chi phí trường hợp xấu nhất là $O(n)$.

</details>

---

### Quiz 03. Thứ tự gán con trỏ khi Chèn node sau một node đã biết
Cho một Singly Linked List và một node `p` đã biết trong danh sách. Ta muốn chèn một node mới `new_node` vào ngay sau node `p`. Thứ tự gán con trỏ nào sau đây là **đúng** để không làm mất phần danh sách phía sau?

- [ ] A. `p.next = new_node; new_node.next = p.next`
- [ ] B. `new_node.next = p.next; p.next = new_node`
- [ ] C. `p = new_node; new_node.next = p`
- [ ] D. `new_node.next = p; p.next = new_node.next`

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
- Bước 1: `new_node.next = p.next` (node mới móc nối vào phần danh sách phía sau `p`).
- Bước 2: `p.next = new_node` (node `p` đổi hướng liên kết trỏ tới node mới).
- Nếu làm theo phương án A (`p.next = new_node` trước), liên kết cũ đến phần danh sách phía sau sẽ bị ghi đè và mất vĩnh viễn (*memory leak* / lạc mất dữ liệu).

</details>

---

### Quiz 04. Ưu điểm nổi bật của Doubly Linked List so với Singly Linked List
Ưu điểm lớn nhất của Danh sách liên kết đôi (Doubly Linked List) so với Danh sách liên kết đơn là gì?

- [ ] A. Tiết kiệm bộ nhớ hơn vì không cần `None` ở cuối.
- [ ] B. Có thể duyệt theo cả hai chiều (tiến và lùi), đồng thời xóa một node đã biết trong $O(1)$ mà không cần duyệt tìm node đứng trước (*predecessor*).
- [ ] C. Cho phép truy cập phần tử thứ $i$ trong thời gian $O(1)$.
- [ ] D. Tự động sắp xếp các phần tử theo thứ tự tăng dần.

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
Dummy node là một node giả đứng trước `head` (`dummy = ListNode(0, head)`). Khi cần chèn hoặc xóa node ở đầu danh sách, thao tác này được đối xử giống hệt như chèn/xóa ở giữa danh sách (luôn có một node đứng trước là `dummy`), giúp loại bỏ hoàn toàn các trường hợp biên rắc rối và làm code ngắn gọn, không bị lỗi `AttributeError: 'NoneType' object has no attribute 'next'`.

</details>

---

### Quiz 07. Xóa node cuối trong Singly Linked List có con trỏ `tail`
Cho một Singly Linked List duy trì cả hai con trỏ `head` và `tail`. Độ phức tạp thời gian của thao tác xóa node cuối cùng (`delete_end`) là bao nhiêu?

- [ ] A. $O(1)$ vì ta đã có con trỏ `tail`.
- [ ] B. $O(n)$ vì mặc dù có `tail`, ta vẫn phải duyệt từ `head` đến node áp chót ($n-1$) để cập nhật con trỏ `next` của nó thành `None`.
- [ ] C. $O(\log n)$.
- [ ] D. $O(1)$ amortized.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: B**

**Giải thích:**
Đây là một cạm bẫy kinh điển:
- Trong Singly Linked List, các liên kết chỉ đi một chiều. Để xóa node cuối (`tail`), ta phải cập nhật con trỏ `next` của node đứng trước nó thành `None`, đồng thời dời `tail` về node đó.
- Nhưng con trỏ `tail` không thể lùi lại được! Ta bắt buộc phải duyệt từ `head` mất $n-1$ bước để tìm node áp chót. Do đó thao tác xóa cuối vẫn tốn $O(n)$ thời gian. (Trong Doubly Linked List, thao tác này mới đạt $O(1)$ nhờ `tail.prev`).

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
Do đó, Binary Search trên DSLK không đem lại bất kỳ cải thiện nào về bậc độ phức tạp so với Tìm kiếm tuyến tính ($O(n)$).

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
- Linked List: mỗi lần `curr = curr.next`, CPU phải nhảy tới một địa chỉ ngẫu nhiên trên Heap. Dữ liệu không nằm trong Cache $\to$ **Cache Miss** $\to$ CPU phải tạm dừng chu kỳ lệnh chờ nạp dữ liệu từ thanh RAM chính với độ trễ lớn.

</details>

---

### Quiz 10. Tìm node thứ k từ cuối bằng phương pháp Two-Pass
Cho một singly linked list có $n$ node ($n \ge k$). Nếu duyệt qua danh sách lần thứ nhất để đếm tổng số node là $n$, thì trong lần duyệt thứ hai, ta cần bước từ `head` thêm bao nhiêu bước để đến đúng node thứ $k$ từ cuối?

- [ ] A. $n - k$ bước
- [ ] B. $n - k + 1$ bước
- [ ] C. $k$ bước
- [ ] D. $k - 1$ bước

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: A**

**Giải thích:**
- Node đầu tiên (`head`) nằm ở vị trí chỉ số $0$ (cần 0 bước).
- Node thứ $k$ từ cuối nằm ở vị trí chỉ số $n - k$ (nếu đánh số từ 0).
- Do đó, bắt đầu từ `head`, ta chỉ cần bước tiếp đúng $n - k$ lần con trỏ `next` là sẽ chạm chính xác vào node thứ $k$ từ cuối.

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

### Quiz 12. So sánh Chèn đầu (Prepend) và Chèn cuối (Append)
Trong các khẳng định sau về thao tác chèn trên Singly Linked List (chỉ có `head`), khẳng định nào là **đúng**?

- [ ] A. Chèn đầu mất $O(1)$, chèn cuối mất $O(1)$.
- [ ] B. Chèn đầu mất $O(n)$, chèn cuối mất $O(1)$.
- [ ] C. Chèn đầu mất $O(1)$, chèn cuối mất $O(n)$ do phải duyệt từ `head` tới node cuối.
- [ ] D. Cả chèn đầu và chèn cuối đều mất $O(n)$.

<details>
<summary><strong>Đáp án & Giải thích chi tiết</strong></summary>

**Đáp án đúng: C**

**Giải thích:**
- Chèn đầu chỉ cần nối `new_node.next = self.head` và `self.head = new_node` $\to O(1)$ không phụ thuộc vào $n$.
- Chèn cuối khi chỉ giữ `head` bắt buộc phải chạy vòng lặp `while current.next is not None` đi qua tất cả $n$ node để tới được node đuôi $\to O(n)$.

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

## Bài T2. Phân tích Thuật toán Chèn và Xóa trong Doubly Linked List

### Đề bài
Cho một Doubly Linked List với cấu trúc node gồm `data`, `prev`, `next`.
1. Hãy viết 4 phép gán con trỏ chính xác để chèn `new_node` vào ngay sau node `p` (giả định `p` không phải là node cuối cùng).
2. Hãy viết 2 phép gán con trỏ để xóa node `curr` (giả định `curr` nằm ở giữa danh sách, có cả `curr.prev` và `curr.next`).
3. Vẽ sơ đồ trạng thái các liên kết trước và sau khi thực hiện thao tác xóa.

<details>
<summary><strong>Lời giải chi tiết</strong></summary>

### 1. Thao tác chèn sau node `p`
```python
new_node.next = p.next
new_node.prev = p
p.next.prev = new_node
p.next = new_node
```
*(Thứ tự này đảm bảo node đứng sau `p` nhận diện được `new_node` làm predecessor mới trước khi `p.next` bị đổi hướng).*

### 2. Thao tác xóa node `curr` ở giữa
```python
curr.prev.next = curr.next
curr.next.prev = curr.prev
```

### 3. Sơ đồ trạng thái khi xóa `curr`
```text
Ban đầu:
    [prev_node] <===> [curr] <===> [next_node]

Sau khi đổi liên kết:
    [prev_node] --------------------> [next_node]
    [prev_node] <-------------------- [next_node]
```
Node `curr` bị ngắt hoàn toàn khỏi mạch liên kết và sẽ được cơ chế Garbage Collection của Python thu hồi tự động.

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
| **Thao tác Partition của Quicksort** | Trên mảng, Quicksort duyệt từ hai đầu mảng vào giữa ($O(1)$ random access), swap cực nhanh. | Trên DSLK đơn, không thể duyệt lùi (`prev`), việc chọn pivot và phân hoạch Lomuto/Hoare rất kém hiệu quả và làm mất tính liên tục. |
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
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 02. Xóa Node theo Giá trị (Remove Linked List Elements)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 203 | GfG: Delete a Node in Single Linked List
- **Đường dẫn thực hành:** [LeetCode #203](https://leetcode.com/problems/remove-linked-list-elements/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một singly linked list và một số nguyên `val`. Hãy xóa tất cả các node có `node.val == val` trong danh sách và trả về `head` mới.

**Ví dụ:**
```text
Đầu vào: head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None, val = 6
Đầu ra:  1 -> 2 -> 3 -> 4 -> 5 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng **Dummy Node** đứng trước `head`. Điều này đảm bảo ta có thể xóa các node có giá trị `val` nằm ngay ở đầu danh sách mà không cần viết điều kiện đặc biệt:
- Duyệt bằng `curr = dummy`.
- Nếu `curr.next.val == val`: nhảy cóc qua node đó `curr.next = curr.next.next`.
- Ngược lại: tiến con trỏ `curr = curr.next`.

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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 03. Hợp nhất Hai Danh sách đã Sắp xếp (Merge Two Sorted Lists)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 21 | GfG: Merge two sorted linked lists
- **Đường dẫn thực hành:** [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

### Mô tả bài toán
Cho hai danh sách liên kết đơn đã được sắp xếp tăng dần `list1` và `list2`. Hãy hợp nhất chúng thành một danh sách duy nhất cũng được sắp xếp tăng dần bằng cách nối lại các node có sẵn.

**Ví dụ:**
```text
list1: 1 -> 2 -> 4 -> None
list2: 1 -> 3 -> 4 -> None
Đầu ra: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

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

- **Độ phức tạp thời gian:** $T(m, n) = O(m + n)$.
- **Bộ nhớ phụ:** $S(m, n) = O(1)$.

</details>

---

## Bài 04. Xóa Node khi không có Con trỏ Head (Delete Node in a Linked List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 237 | GfG: Delete without head pointer
- **Đường dẫn thực hành:** [LeetCode #237](https://leetcode.com/problems/delete-node-in-a-linked-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1)

### Mô tả bài toán
Cho tham chiếu đến một `node` cần xóa trong danh sách liên kết đơn (đảm bảo không phải node cuối). Bạn **không được cấp quyền truy cập** vào con trỏ `head`.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

```python
def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
```

- **Độ phức tạp thời gian:** $T(n) = O(1)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 05. Xóa Phần tử Trùng lặp trong Danh sách đã Sắp xếp (Remove Duplicates from Sorted List)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 83 | GfG: Remove duplicate element from sorted Linked List
- **Đường dẫn thực hành:** [LeetCode #83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một danh sách liên kết đã được sắp xếp tăng dần. Hãy xóa tất cả các phần tử trùng lặp sao cho mỗi giá trị chỉ xuất hiện đúng một lần.

**Ví dụ:**
```text
Đầu vào: 1 -> 1 -> 2 -> 3 -> 3 -> None
Đầu ra:  1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

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

## Bài 06. Chuyển đổi Số nhị phân dạng DSLK sang Số nguyên (Binary to Integer)

- **Mức độ:** 🟢 Easy
- **Mã bài:** LeetCode 1290 | GfG: Decimal Equivalent of Binary Linked List
- **Đường dẫn thực hành:** [LeetCode #1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/decimal-equivalent-of-binary-linked-list/1)

### Mô tả bài toán
Cho `head` của một linked list mà mỗi node chứa một giá trị là `0` hoặc `1`. Danh sách biểu diễn một số nhị phân (với `head` là bit có trọng số cao nhất). Hãy trả về giá trị thập phân tương ứng của số đó.

**Ví dụ:**
```text
Đầu vào: 1 -> 0 -> 1 -> None
Đầu ra:  5  (vì 1*2^2 + 0*2^1 + 1*2^0 = 5)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Duyệt qua danh sách và áp dụng thuật toán Horner (hoặc dịch bit):
$$\text{ans} = (\text{ans} \ll 1) + \text{curr.val} = 2 \times \text{ans} + \text{curr.val}$$

```python
def getDecimalValue(head: ListNode) -> int:
    ans = 0
    curr = head
    while curr is not None:
        ans = (ans << 1) | curr.val
        curr = curr.next
    return ans
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 07. Đảo ngược Danh sách Liên kết Đôi (Reverse a Doubly Linked List)

- **Mức độ:** 🟢 Easy
- **Nền tảng:** GeeksforGeeks: Reverse a Doubly Linked List
- **Đường dẫn thực hành:** [GeeksforGeeks Practice](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một Doubly Linked List. Hãy đảo ngược danh sách này ngay tại chỗ và trả về `head` mới.

**Ví dụ:**
```text
Đầu vào: None <- 1 <==> 2 <==> 3 <==> 4 -> None
Đầu ra:  None <- 4 <==> 3 <==> 2 <==> 1 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Với mỗi node trong doubly linked list, ta chỉ cần hoán đổi hai con trỏ `prev` và `next` của chính node đó:
```python
temp = curr.prev
curr.prev = curr.next
curr.next = temp
```
Sau đó, tiến sang node tiếp theo (chính là `curr.prev` cũ!). Khi kết thúc vòng lặp, node cuối cùng có `temp` khác `None` sẽ là `head` mới.

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
        # Hoán đổi prev và next
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        # Tiến sang node tiếp theo theo hướng ban đầu (nay là curr.prev)
        curr = curr.prev

    # Node đầu mới chính là node cuối cũ (đang trỏ bởi temp.prev)
    if temp is not None:
        head = temp.prev

    return head
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
Cho `headA` và `headB` của hai singly linked list, hãy tìm và trả về node mà tại đó hai danh sách bắt đầu giao nhau. Nếu không giao nhau, trả về `None`.

<details>
<summary><strong>Lời giải & Mã nguồn Python (Phương pháp đếm độ dài)</strong></summary>

### Phân tích thuật toán (Kỹ thuật so lệch độ dài)
1. Đếm độ dài $L_A$ của danh sách A và $L_B$ của danh sách B.
2. Tính độ lệch: $d = |L_A - L_B|$.
3. Cho con trỏ của danh sách dài hơn tiến trước $d$ bước.
4. Sau đó cho cả hai con trỏ cùng tiến từng bước một. Điểm chúng gặp nhau (`currA is currB`) chính là giao điểm!

```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    # Bước 1: Tính độ dài
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

    # Bước 2: Cân bằng điểm xuất phát
    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next

    # Bước 3: Cùng tiến tìm giao điểm
    while currA is not None and currB is not None:
        if currA is currB:
            return currA
        currA = currA.next
        currB = currB.next

    return None
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
Cho con trỏ `head` của một danh sách liên kết, hãy xóa node thứ $n$ tính từ cuối danh sách lên và trả về `head` mới sau khi xóa.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None, n = 2
Đầu ra:  1 -> 2 -> 3 -> 5 -> None (node 4 bị xóa)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python (Thuật toán Two-Pass)</strong></summary>

### Phân tích thuật toán (Kỹ thuật duyệt Two-Pass)
- **Lượt 1:** Duyệt qua danh sách để đếm tổng số node là $L$.
- Node cần xóa đứng ở vị trí chỉ số $L - n$ (tính từ 0). Node ngay trước nó đứng ở vị trí $L - n - 1$.
- **Lượt 2:** Dùng `dummy = ListNode(0, head)`, duyệt $L - n$ bước từ `dummy` để đến node ngay trước node cần xóa, rồi thực hiện: `curr.next = curr.next.next`.

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Lượt 1: Đếm tổng số node
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next

    # Lượt 2: Tìm và xóa
    dummy = ListNode(0, head)
    curr = dummy
    for _ in range(length - n):
        curr = curr.next

    curr.next = curr.next.next
    return dummy.next
```

- **Độ phức tạp thời gian:** $T(L) = O(L)$ (2 lượt duyệt tuyến tính).
- **Bộ nhớ phụ:** $S(L) = O(1)$.

</details>

---

## Bài 10. Xoay Danh sách Liên kết (Rotate List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 61 | GfG: Rotate a Linked List
- **Đường dẫn thực hành:** [LeetCode #61](https://leetcode.com/problems/rotate-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một danh sách liên kết, hãy xoay danh sách sang phải $k$ vị trí.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 4 -> 5 -> None, k = 2
Đầu ra:  4 -> 5 -> 1 -> 2 -> 3 -> None
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
1. Duyệt đến cuối danh sách để xác định độ dài $L$ và lưu lại con trỏ `tail`.
2. Tối ưu $k$: nếu $k \ge L$, ta lấy số vòng quay thực tế là $k = k \pmod L$. Nếu $k = 0$, trả về `head`.
3. Nối `tail.next = head` để biến danh sách thành một vòng tròn tạm thời.
4. Node đuôi mới sau khi xoay sẽ nằm ở vị trí thứ $L - k$ tính từ `head`. Ta duyệt $L - k$ bước, đặt `new_head = new_tail.next`, sau đó ngắt liên kết `new_tail.next = None`.

```python
def rotateRight(head: ListNode, k: int) -> ListNode:
    if head is None or head.next is None or k == 0:
        return head

    # Bước 1: Tính độ dài và tìm node cuối
    length = 1
    tail = head
    while tail.next is not None:
        length += 1
        tail = tail.next

    # Bước 2: Rút gọn k
    k = k % length
    if k == 0:
        return head

    # Bước 3: Nối vòng tạm thời
    tail.next = head

    # Bước 4: Tìm điểm cắt mới tại (length - k)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 11. Phân hoạch Danh sách Liên kết (Partition List)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 86 | GfG: Partition a Linked List
- **Đường dẫn thực hành:** [LeetCode #86](https://leetcode.com/problems/partition-list/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/partition-a-linked-list/1)

### Mô tả bài toán
Cho `head` của một danh sách liên kết và một giá trị $x$. Hãy sắp xếp lại danh sách sao cho tất cả các node có giá trị nhỏ hơn $x$ đứng trước các node có giá trị lớn hơn hoặc bằng $x$, trong khi vẫn bảo toàn thứ tự ban đầu của các phần tử trong từng nhóm.

**Ví dụ:**
```text
Đầu vào: head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Đầu ra:  1 -> 2 -> 2 -> 4 -> 3 -> 5
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng hai danh sách con độc lập với hai dummy node:
- `less_dummy`: gom các node có giá trị $< x$.
- `greater_dummy`: gom các node có giá trị $\ge x$.
Sau khi duyệt hết danh sách gốc, nối đuôi của danh sách `less` vào đầu của danh sách `greater`, và ngắt đuôi của danh sách `greater` bằng `None`.

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

    # Ngắt đuôi greater để tránh tạo chu trình
    greater.next = None
    # Nối hai danh sách
    less.next = greater_dummy.next

    return less_dummy.next
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
Cho `head` của một singly linked list. Hãy nhóm tất cả các node ở vị trí lẻ (node 1, 3, 5...) lại với nhau trước, theo sau là các node ở vị trí chẵn (node 2, 4, 6...).

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Tách hai luồng con trỏ `odd` và `even`:
- `odd` liên kết các node ở vị trí lẻ, `even` liên kết các node ở vị trí chẵn.
- Sau khi duyệt hết danh sách, nối `odd.next = even_head`.

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
Cho hai danh sách liên kết đại diện cho hai số nguyên không âm (các chữ số lưu theo thứ tự đảo ngược, hàng đơn vị ở `head`). Hãy cộng hai số đó và trả về kết quả dưới dạng danh sách liên kết.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Mô phỏng phép cộng số học tiểu học từ hàng đơn vị sang hàng cao hơn:
- Duyệt đồng thời qua hai danh sách, duy trì biến nhớ `carry`.
- Tại mỗi vị trí: $\text{total} = \text{val1} + \text{val2} + \text{carry}$, chữ số mới là $\text{total} \pmod{10}$, nhớ $\text{carry} = \lfloor \text{total} / 10 \rfloor$.

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
- **Bộ nhớ phụ:** $S(m, n) = O(\max(m, n))$.

</details>

---

## Bài 14. Hoán đổi Từng Cặp Node Liền kề (Swap Nodes in Pairs)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 24 | GfG: Pairwise swap elements of a linked list
- **Đường dẫn thực hành:** [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

### Mô tả bài toán
Cho một singly linked list, hãy hoán đổi vị trí của từng cặp node liền kề nhau bằng cách thay đổi con trỏ liên kết (không thay đổi giá trị).

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Sử dụng dummy node và 3 bước hoán đổi con trỏ:
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

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 15. Xóa Sạch Phần tử Trùng lặp (Remove Duplicates from Sorted List II)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 82 | GfG: Remove all occurrences of duplicates
- **Đường dẫn thực hành:** [LeetCode #82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/remove-all-occurences-of-duplicates-in-a-linked-list/1)

### Mô tả bài toán
Cho con trỏ `head` của một danh sách liên kết đã sắp xếp. Hãy xóa tất cả các node có giá trị bị trùng lặp, **chỉ giữ lại những node có giá trị xuất hiện duy nhất một lần**.

**Ví dụ:**
```text
Đầu vào: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> None
Đầu ra:  1 -> 2 -> 5 -> None (các số 3 và 4 bị xóa hoàn toàn)
```

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

### Phân tích thuật toán
Dùng `dummy = ListNode(0, head)` và `prev = dummy`:
- Kiểm tra xem `head` hiện tại có bị trùng với node liền sau (`head.val == head.next.val`) hay không.
- Nếu có trùng: chạy vòng lặp bỏ qua tất cả các node có giá trị này, sau đó nối `prev.next = head.next`.
- Nếu không trùng: tiến con trỏ `prev = prev.next`.

```python
def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while head is not None:
        if head.next is not None and head.val == head.next.val:
            # Nhảy cóc qua tất cả node có giá trị trùng lặp
            while head.next is not None and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next

    return dummy.next
```

- **Độ phức tạp thời gian:** $T(n) = O(n)$.
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

## Bài 16. Sao chép Danh sách có Con trỏ Ngẫu nhiên (Copy List with Random Pointer)

- **Mức độ:** 🟡 Medium
- **Mã bài:** LeetCode 138 | GfG: Clone a linked list with next and random pointer
- **Đường dẫn thực hành:** [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) \| [GeeksforGeeks](https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

### Mô tả bài toán
Một danh sách liên kết mà mỗi node ngoài con trỏ `next` còn chứa thêm con trỏ `random` có thể trỏ tới bất kỳ node nào trong danh sách hoặc `None`. Hãy tạo một bản sao sâu (**Deep Copy**) hoàn chỉnh trong $O(1)$ không gian bộ nhớ phụ.

<details>
<summary><strong>Lời giải & Mã nguồn Python</strong></summary>

```python
class NodeWithRandom:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'NodeWithRandom') -> 'NodeWithRandom':
    if head is None:
        return None

    # Bước 1: Nhân bản node xen kẽ A -> A' -> B -> B'
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
- **Bộ nhớ phụ:** $S(n) = O(1)$.

</details>

---

> © 2026 TS. Vũ Đức Minh – Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo, Trường Đại học Kinh tế Quốc dân (NEU).
