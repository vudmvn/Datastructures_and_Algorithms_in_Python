---
title: "Part IV — Analysis of Recursive Algorithms"
course: "Data Structures and Algorithmic Thinking with Python"
language: "vi"
version: "2.1"
---

# Part IV — Analysis of Recursive Algorithms

## 1. Mục tiêu học tập

Nhiều thuật toán đệ quy không thể được phân tích trực tiếp bằng cách đếm vòng lặp. Thay vào đó, thời gian chạy thường được mô tả bằng recurrence relation.

Sau phần này, người học có thể:

- thiết lập recurrence relation từ cấu trúc của thuật toán đệ quy;
- giải recurrence bằng expansion/iteration;
- sử dụng recursion tree để quan sát chi phí theo từng mức;
- sử dụng substitution method để chứng minh cận;
- áp dụng Master Theorem cho các recurrence dạng chuẩn;
- nhận biết các trường hợp Master Theorem không áp dụng trực tiếp.

---

## 2. Recurrence Relations

Một **recurrence relation** mô tả chi phí của bài toán kích thước `n` thông qua chi phí của một hoặc nhiều bài toán con nhỏ hơn.

Ví dụ:

### Factorial

```text
T(n) = T(n - 1) + Θ(1)
```

### Binary Search

```text
T(n) = T(n / 2) + Θ(1)
```

### Merge Sort

```text
T(n) = 2T(n / 2) + Θ(n)
```

Recurrence thể hiện hai thành phần:

1. chi phí của các lời gọi đệ quy;
2. chi phí ngoài đệ quy.

Mục tiêu là xác định tốc độ tăng trưởng của `T(n)`.

---

## 3. From Recursive Algorithm to Recurrence

Ví dụ Binary Search recursive:

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search_recursive(
            arr,
            target,
            mid + 1,
            right
        )

    return binary_search_recursive(
        arr,
        target,
        left,
        mid - 1
    )
```

Mỗi bước:

- chỉ tiếp tục trên một nửa;
- thực hiện một lượng công việc hằng số ngoài recursion.

Do đó:

```text
T(n) = T(n / 2) + Θ(1)
```

---

## 4. Expansion / Iteration Method

Expansion method liên tục thay recurrence vào chính nó để phát hiện quy luật.

Xét:

```text
T(n) = 2T(n / 2) + n
```

Khai triển một lần:

```text
T(n)
= 2[2T(n / 4) + n / 2] + n
= 4T(n / 4) + 2n
```

Khai triển tiếp:

```text
T(n)
= 8T(n / 8) + 3n
```

Sau `k` bước:

```text
T(n)
= 2^k T(n / 2^k) + kn
```

Dừng khi:

```text
n / 2^k = 1
```

Suy ra:

```text
k = log2(n)
```

Do đó:

```text
T(n)
= nT(1) + n log2(n)
= Θ(n log n)
```

Expansion method phù hợp khi recurrence có cấu trúc dễ khai triển và xuất hiện pattern rõ ràng.

---

## 5. Recursion Tree

Recursion tree biểu diễn mỗi lời gọi đệ quy như một node trong cây.

Xét:

```text
T(n) = 2T(n / 2) + n
```

Chi phí mỗi mức:

```text
Level 0: n
Level 1: n/2 + n/2 = n
Level 2: 4 × n/4 = n
...
```

Số mức:

```text
log2(n)
```

Mỗi mức có tổng chi phí `n`.

Do đó:

```text
T(n) = Θ(n log n)
```

Recursion tree hữu ích để:

- quan sát số lượng subproblems;
- thấy kích thước subproblem theo từng mức;
- tính total cost per level;
- đoán nghiệm trước khi chứng minh.

---

## 6. Substitution Method

Substitution method thường gồm bốn bước:

1. đoán một cận;
2. giả sử cận đúng cho bài toán con;
3. thay giả thuyết vào recurrence;
4. chứng minh bằng induction.

Xét:

```text
T(n) = 2T(n / 2) + n
```

Đoán:

```text
T(n) = O(n log n)
```

Giả sử:

```text
T(n / 2) ≤ c × (n / 2) × log(n / 2)
```

Khi đó:

```text
T(n)
≤ 2 × c × (n / 2) × log(n / 2) + n
```

Suy ra:

```text
T(n)
≤ cn(log n - 1) + n
```

Hay:

```text
T(n)
≤ cn log n - (c - 1)n
```

Nếu `c ≥ 1`:

```text
T(n) ≤ cn log n
```

Do đó:

```text
T(n) = O(n log n)
```

Để kết luận `Θ(n log n)`, cần thêm cận dưới.

---

## 7. Master Theorem

Master Theorem áp dụng cho recurrence dạng:

```text
T(n) = aT(n / b) + f(n)
```

Trong đó:

- `a`: số bài toán con;
- `n / b`: kích thước mỗi bài toán con;
- `f(n)`: chi phí ngoài recursion.

Đại lượng cần so sánh:

```text
n^(log_b a)
```

Ý tưởng là xác định thành phần nào chi phối tổng chi phí:

- recursive work;
- non-recursive work;
- hoặc hai thành phần cân bằng.

---

## 8. Master Theorem — Case 1

Nếu tồn tại `ε > 0` sao cho:

```text
f(n) = O(n^(log_b a - ε))
```

thì:

```text
T(n) = Θ(n^(log_b a))
```

Phần recursive work chi phối.

### Ví dụ

```text
T(n) = 8T(n / 2) + n²
```

Ta có:

```text
n^(log_2 8) = n³
```

Vì `n²` nhỏ hơn đa thức so với `n³`:

```text
T(n) = Θ(n³)
```

---

## 9. Master Theorem — Case 2

Nếu:

```text
f(n) = Θ(n^(log_b a) × log^k n)
```

với `k ≥ 0`, thì:

```text
T(n)
= Θ(n^(log_b a) × log^(k + 1) n)
```

### Ví dụ: Merge Sort

```text
T(n) = 2T(n / 2) + n
```

Ta có:

```text
n^(log_2 2) = n
```

Hai thành phần cân bằng.

Do đó:

```text
T(n) = Θ(n log n)
```

---

## 10. Master Theorem — Case 3

Nếu tồn tại `ε > 0` sao cho:

```text
f(n) = Ω(n^(log_b a + ε))
```

và thỏa regularity condition:

```text
a × f(n / b) ≤ c × f(n)
```

với một hằng số `c < 1`, thì:

```text
T(n) = Θ(f(n))
```

### Ví dụ

```text
T(n) = 2T(n / 2) + n²
```

Ta có:

```text
n^(log_2 2) = n
```

Trong khi:

```text
f(n) = n²
```

Do đó:

```text
T(n) = Θ(n²)
```

---

## 11. Extended Form for `n^k log^p n`

Xét:

```text
T(n)
= aT(n / b)
+ Θ(n^k × log^p n)
```

So sánh `a` với `b^k`.

### Nếu `a > b^k`

```text
T(n) = Θ(n^(log_b a))
```

### Nếu `a = b^k` và `p > -1`

```text
T(n) = Θ(n^k × log^(p + 1) n)
```

### Nếu `a = b^k` và `p = -1`

```text
T(n) = Θ(n^k × log log n)
```

### Nếu `a = b^k` và `p < -1`

```text
T(n) = Θ(n^k)
```

### Nếu `a < b^k`

Trong các trường hợp thông thường, non-recursive work chi phối; cần kiểm tra điều kiện áp dụng để kết luận tight bound.

---

## 12. Workflow for Applying Master Theorem

Khi gặp:

```text
T(n) = aT(n / b) + f(n)
```

có thể làm theo bốn bước.

### Step 1. Identify Parameters

Xác định:

```text
a, b, f(n)
```

### Step 2. Compute Critical Function

Tính:

```text
n^(log_b a)
```

### Step 3. Compare

So sánh `f(n)` với `n^(log_b a)`.

### Step 4. Conclude

Chọn case phù hợp và viết kết luận.

---

## 13. Representative Examples

| Recurrence | Result |
|---|---|
| `T(n) = 2T(n/2) + n` | `Θ(n log n)` |
| `T(n) = 4T(n/2) + n²` | `Θ(n² log n)` |
| `T(n) = 8T(n/2) + n²` | `Θ(n³)` |
| `T(n) = 2T(n/2) + n²` | `Θ(n²)` |
| `T(n) = 2T(n/2) + n log n` | `Θ(n log² n)` |
| `T(n) = 2T(n/2) + n/log n` | `Θ(n log log n)` |

---

## 14. When Master Theorem Does Not Apply Directly

Master Theorem không áp dụng trực tiếp cho mọi recurrence.

Các trường hợp thường gặp:

- số lượng subproblems phụ thuộc vào `n`;
- các subproblems có kích thước không đồng đều;
- kích thước không có dạng `n / b`;
- recurrence có dạng subtract-and-conquer;
- `f(n)` không thỏa điều kiện cần thiết.

Ví dụ:

```text
T(n) = T(n - 1) + n
```

```text
T(n) = T(n / 3) + T(2n / 3) + n
```

```text
T(n) = sqrt(n) × T(sqrt(n)) + n
```

Khi đó có thể sử dụng:

- expansion;
- recursion tree;
- substitution;
- direct summation;
- change of variables;
- Akra–Bazzi.

---

## 15. Example Outside Standard Master Theorem

Xét:

```text
T(n) = T(n - 1) + n
```

Khai triển:

```text
T(n)
= n + T(n - 1)
= n + (n - 1) + T(n - 2)
= ...
```

Suy ra:

```text
T(n)
= 1 + 2 + ... + n
= Θ(n²)
```

Ví dụ này cho thấy recurrence không cần Master Theorem vẫn có thể giải bằng expansion.

---

## 16. Tóm tắt

- Recursive algorithms thường dẫn đến recurrence relations.
- Expansion liên tục khai triển recurrence để tìm pattern.
- Recursion tree giúp quan sát cost theo level.
- Substitution method dùng để đoán và chứng minh bound.
- Master Theorem áp dụng cho dạng `T(n) = aT(n/b) + f(n)`.
- Ba case của Master Theorem phụ thuộc vào việc so sánh `f(n)` với `n^(log_b a)`.
- Không phải mọi recurrence đều phù hợp với Master Theorem.