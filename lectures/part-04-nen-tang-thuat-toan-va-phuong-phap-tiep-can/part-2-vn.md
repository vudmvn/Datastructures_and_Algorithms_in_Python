# Part II — Algorithmic Approaches

**Cập nhật lần cuối:** 3 tháng 8 năm 2026

## 1. Mục tiêu học tập

Phần này giới thiệu một số cách tiếp cận cơ bản để mô tả, thiết kế và tổ chức việc thực thi thuật toán. Mục tiêu không phải là xem mọi thuật toán như các lớp tách biệt hoàn toàn, mà là hiểu rằng iteration, recursion, Divide and Conquer, sequential execution và parallel execution thuộc các góc nhìn khác nhau.

Sau phần này, người học có thể:

- giải thích iterative algorithm là gì;
- giải thích recursive algorithm là gì;
- phân biệt base case và recursive case;
- so sánh iteration và recursion trên cùng một bài toán;
- giải thích paradigm Divide and Conquer;
- phân biệt recursion với Divide and Conquer;
- hiểu vai trò của sequential execution và parallel execution ở mức nhập môn;
- nhận biết khi nào một bài toán có thể được chia thành các bài toán con độc lập.

---

## 2. Overview of Algorithmic Approaches

Các thuật ngữ thường gặp như:

- iterative;
- recursive;
- Divide and Conquer;
- sequential;
- parallel;

không nằm trên cùng một tiêu chí phân loại.

Có thể hiểu khái quát như sau:

| Khái niệm | Bản chất |
|---|---|
| Iteration | Kỹ thuật lặp bằng vòng lặp |
| Recursion | Kỹ thuật giải bài toán bằng lời gọi chính nó |
| Divide and Conquer | Paradigm thiết kế thuật toán |
| Sequential execution | Mô hình thực thi tuần tự |
| Parallel execution | Mô hình thực thi đồng thời |

Vì vậy, một thuật toán có thể vừa recursive, vừa Divide and Conquer, đồng thời được thực thi tuần tự hoặc song song tùy implementation.

---

## 3. Iterative Algorithms

Một **iterative algorithm** sử dụng vòng lặp để lặp lại một chuỗi thao tác cho đến khi đạt điều kiện dừng.

Các cấu trúc lặp phổ biến gồm:

- `for`;
- `while`;
- nested loops.

Ví dụ tính giai thừa:

```python
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
```

Ý tưởng của thuật toán:

1. khởi tạo `result = 1`;
2. lần lượt nhân với các số từ `1` đến `n`;
3. trả về kết quả.

Với input `n`, vòng lặp chạy `n` lần.

Do đó:

```text
Time complexity: Θ(n)
Auxiliary space: Θ(1)
```

Iteration thường phù hợp khi:

- quá trình xử lý có thể mô tả tự nhiên bằng một vòng lặp;
- không cần chia bài toán thành các bài toán con;
- muốn tránh chi phí call stack;
- cần kiểm soát trực tiếp trạng thái qua từng vòng lặp.

---

## 4. Recursive Algorithms

Một **recursive algorithm** giải bài toán bằng cách gọi lại chính nó trên một bài toán nhỏ hơn.

Một thuật toán đệ quy thường cần hai thành phần:

1. **Base case**: trường hợp cơ sở, không gọi đệ quy thêm.
2. **Recursive case**: lời gọi hàm trên một input nhỏ hơn.

Ví dụ tính giai thừa:

```python
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)
```

Quá trình gọi hàm với `n = 4`:

```text
factorial_recursive(4)
    ↓
4 × factorial_recursive(3)
    ↓
4 × 3 × factorial_recursive(2)
    ↓
4 × 3 × 2 × factorial_recursive(1)
    ↓
4 × 3 × 2 × 1
```

Recurrence:

```text
T(n) = T(n - 1) + Θ(1)
```

Do đó:

```text
Time complexity: Θ(n)
Auxiliary space: Θ(n)
```

Phần auxiliary space tăng do call stack lưu trạng thái của các lời gọi hàm chưa hoàn tất.

---

## 5. Base Case and Recursive Case

### 5.1. Base Case

Base case là điều kiện dừng của thuật toán đệ quy.

Ví dụ:

```python
if n <= 1:
    return 1
```

Nếu không có base case phù hợp, thuật toán có thể tiếp tục gọi chính nó cho đến khi gây lỗi stack overflow hoặc recursion depth exceeded.

### 5.2. Recursive Case

Recursive case là bước biến bài toán hiện tại thành một bài toán nhỏ hơn.

Ví dụ:

```python
return n * factorial_recursive(n - 1)
```

Input giảm từ `n` xuống `n - 1`.

Một recursive algorithm đúng cần đảm bảo rằng sau hữu hạn bước, quá trình luôn tiến tới base case.

---

## 6. Iteration and Recursion

Iteration và recursion có thể được dùng để giải cùng một bài toán.

### Ví dụ: Factorial

#### Iterative version

```python
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
```

#### Recursive version

```python
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)
```

So sánh:

| Tiêu chí | Iterative | Recursive |
|---|---|---|
| Cơ chế | Loop | Function calls |
| Điều kiện dừng | Điều kiện vòng lặp | Base case |
| Call stack | Không tăng theo `n` trong ví dụ | Tăng theo `n` |
| Time complexity | `Θ(n)` | `Θ(n)` |
| Auxiliary space | `Θ(1)` | `Θ(n)` |
| Khả năng biểu diễn cây/phân rã | Thường ít trực quan hơn | Thường tự nhiên hơn |

Điểm quan trọng:

> **Hai thuật toán có thể có cùng time complexity nhưng khác space complexity.**

Không nên mặc định rằng recursion luôn tốt hơn iteration hoặc ngược lại. Lựa chọn phụ thuộc vào:

- cấu trúc bài toán;
- độ rõ ràng của lời giải;
- giới hạn stack;
- chi phí function calls;
- khả năng tối ưu của ngôn ngữ.

---

## 7. Divide and Conquer

**Divide and Conquer** là một algorithmic paradigm trong đó bài toán lớn được chia thành các bài toán con nhỏ hơn, các bài toán con được giải, sau đó kết quả được kết hợp để tạo lời giải cho bài toán ban đầu.

Ba bước cơ bản:

1. **Divide**: chia bài toán thành các bài toán con.
2. **Conquer**: giải các bài toán con.
3. **Combine**: kết hợp kết quả.

Có thể mô tả:

```text
Original problem
      ↓
Divide into smaller subproblems
      ↓
Solve subproblems
      ↓
Combine partial solutions
      ↓
Final solution
```

Các ví dụ điển hình:

- Binary Search;
- Merge Sort;
- Quick Sort;
- Karatsuba multiplication;
- Closest pair of points.

---

## 8. Recursion Is Not the Same as Divide and Conquer

Recursion và Divide and Conquer có liên quan nhưng không đồng nhất.

Factorial:

```text
factorial(n) = n × factorial(n - 1)
```

là recursive vì hàm gọi lại chính nó.

Tuy nhiên, nó không chia bài toán thành nhiều bài toán con độc lập.

Ngược lại, Merge Sort:

```text
Divide array into two halves
        ↓
Sort left half recursively
        ↓
Sort right half recursively
        ↓
Merge two sorted halves
```

Recurrence:

```text
T(n) = 2T(n / 2) + Θ(n)
```

Đây là một ví dụ điển hình của Divide and Conquer.

Điểm cần nhớ:

> **Một thuật toán Divide and Conquer thường dùng recursion, nhưng một recursive algorithm không nhất thiết là Divide and Conquer.**

---

## 9. Example: Binary Search

Binary Search áp dụng trên dữ liệu đã được sắp xếp.

Mỗi bước:

1. chọn phần tử giữa;
2. so sánh với target;
3. bỏ đi một nửa không thể chứa target;
4. tiếp tục trên nửa còn lại.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Không gian tìm kiếm giảm theo dãy:

```text
n → n/2 → n/4 → n/8 → ...
```

Do đó:

```text
Time complexity: Θ(log n)
```

Binary Search minh họa một dạng Divide and Conquer trong đó chỉ một bài toán con được tiếp tục xử lý sau mỗi bước.

---

## 10. Example: Merge Sort

Merge Sort hoạt động theo ba bước:

1. chia mảng thành hai nửa;
2. sắp xếp đệ quy từng nửa;
3. merge hai dãy đã sắp xếp.

Cấu trúc:

```text
Array of size n
      ↓
Two arrays of size n/2
      ↓
Sort both recursively
      ↓
Merge in linear time
```

Recurrence:

```text
T(n) = 2T(n / 2) + Θ(n)
```

Kết quả:

```text
T(n) = Θ(n log n)
```

Merge Sort là một ví dụ quan trọng vì nó kết nối trực tiếp giữa:

- recursion;
- Divide and Conquer;
- recurrence relations;
- Master Theorem.

---

## 11. Sequential Execution Model

Trong **sequential execution**, các bước được thực hiện lần lượt theo một thứ tự xác định.

```text
Step 1 → Step 2 → Step 3 → Step 4
```

Ví dụ:

```python
def sequential_example(arr):
    total = sum(arr)
    maximum = max(arr)
    average = total / len(arr)

    return total, maximum, average
```

Trong implementation này:

1. tính tổng;
2. tìm maximum;
3. tính average.

Các bước được thực hiện theo thứ tự.

Sequential execution là mô hình phổ biến nhất trong các chương trình cơ bản và là nền tảng để phân tích thuật toán nhập môn.

---

## 12. Parallel Execution Model

Trong **parallel execution**, nhiều tác vụ có thể được thực hiện đồng thời nếu chúng độc lập hoặc có thể phối hợp được.

Ví dụ trực quan:

```text
           ┌── Task A ──┐
Input ─────┼── Task B ──┼────→ Combine
           └── Task C ──┘
```

Ví dụ tính tổng một mảng lớn:

1. chia mảng thành nhiều block;
2. tính tổng từng block đồng thời;
3. cộng các tổng cục bộ.

Các khái niệm thường gặp:

- number of processors;
- work;
- span;
- synchronization;
- communication cost;
- speedup;
- scalability.

Parallel execution không đảm bảo chương trình nhanh hơn trong mọi trường hợp. Cần tính đến:

- overhead chia việc;
- chi phí đồng bộ;
- chi phí truyền dữ liệu;
- mức độ độc lập giữa các task.

Trong một môn nhập môn DSA, phần này chỉ nên được xem là giới thiệu để người học hiểu rằng thuật toán và mô hình thực thi là hai vấn đề khác nhau.

---

## 13. Sequential vs Parallel Execution

| Tiêu chí | Sequential | Parallel |
|---|---|---|
| Số tác vụ thực hiện đồng thời | Một | Có thể nhiều |
| Mô hình đơn giản | Có | Thường phức tạp hơn |
| Đồng bộ | Ít | Có thể cần |
| Communication overhead | Thường không đáng kể | Có thể đáng kể |
| Khả năng tăng tốc | Bị giới hạn bởi một luồng thực thi | Có thể tận dụng nhiều processor |

Không phải mọi bài toán đều song song hóa tốt.

Một số bài toán có phụ thuộc mạnh giữa các bước, do đó mức độ parallelism bị hạn chế.

---

## 14. Tóm tắt

- Iteration sử dụng loop.
- Recursion sử dụng lời gọi chính nó.
- Recursive algorithm cần base case và recursive case.
- Iteration và recursion có thể có cùng time complexity nhưng khác auxiliary space.
- Divide and Conquer gồm Divide, Conquer và Combine.
- Recursion không đồng nghĩa với Divide and Conquer.
- Binary Search và Merge Sort là hai ví dụ điển hình.
- Sequential và Parallel là execution models, không phải cùng một loại phân loại với recursion hay Divide and Conquer.
- Parallel execution có thể tăng tốc nhưng đi kèm overhead và chi phí đồng bộ.