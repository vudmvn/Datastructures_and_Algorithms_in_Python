---
title: "Part III — Algorithm Analysis"
course: "Data Structures and Algorithmic Thinking with Python"
language: "vi"
version: "2.1"
---

# Part III — Algorithm Analysis

**Cập nhật lần cuối:** 3 tháng 8 năm 2026

## 1. Mục tiêu học tập

Phần này giới thiệu các công cụ cơ bản để đánh giá hiệu quả của thuật toán. Trọng tâm không phải là đo số giây chạy trên một máy cụ thể, mà là nghiên cứu cách tài nguyên tăng lên khi kích thước input tăng.

Sau phần này, người học có thể:

- giải thích vì sao cần phân tích thuật toán;
- xác định input size phù hợp;
- xác định basic operation và đếm số lần thực hiện;
- phân biệt time complexity và auxiliary space complexity;
- phân biệt best, average và worst cases;
- so sánh các growth rates;
- giải thích asymptotic analysis;
- sử dụng đúng Big-O, Big-Omega và Big-Theta;
- phân tích các đoạn code chứa vòng lặp, nhánh điều kiện và các cấu trúc cơ bản.

---

## 2. Why Analyze Algorithms?

Có thể đo thời gian thực tế bằng cách chạy chương trình. Tuy nhiên, kết quả phụ thuộc vào:

- CPU;
- RAM;
- hệ điều hành;
- programming language;
- compiler hoặc interpreter;
- thư viện;
- implementation details;
- dữ liệu cụ thể;
- các tiến trình khác đang chạy.

Vì vậy, phát biểu:

```text
Algorithm A takes 0.2 seconds.
```

không đủ để kết luận A tốt hơn B trong mọi trường hợp.

Phân tích thuật toán tập trung vào câu hỏi:

> **Khi kích thước input tăng, lượng thời gian và bộ nhớ cần thiết tăng theo quy luật nào?**

Mục tiêu chính là đánh giá:

- efficiency;
- scalability;
- khả năng so sánh giữa các thuật toán.

---

## 3. Input Size

Trước khi phân tích complexity, cần xác định rõ kích thước input.

Ký hiệu `n` không có ý nghĩa cố định cho mọi bài toán.

| Bài toán | Input size thường dùng |
|---|---|
| Array | số phần tử `n` |
| String | độ dài `n` |
| Matrix | số hàng `r`, số cột `c` |
| Graph | số đỉnh `V`, số cạnh `E` |
| Big integer | số bit hoặc số chữ số |
| Polynomial | số hệ số hoặc bậc |
| TSP | số thành phố |

Ví dụ với graph:

```text
T(V, E) = Θ(V + E)
```

thường rõ hơn:

```text
T(n) = Θ(n)
```

Nếu chọn sai input size, kết luận complexity có thể gây hiểu nhầm.

---

## 4. Basic Operations and Operation Counting

Một cách cơ bản để phân tích thuật toán:

1. xác định thao tác cơ bản;
2. đếm số lần thao tác được thực hiện;
3. biểu diễn số lần đó theo input size.

Ví dụ:

```python
for i in range(n):
    print(i)
```

Nếu xem mỗi lần `print(i)` có chi phí hằng số, thân vòng lặp chạy `n` lần.

Có thể viết:

```text
T(n) = c1 × n + c2
```

Do đó:

```text
T(n) = Θ(n)
```

Điểm quan trọng là không cần đếm chính xác mọi instruction ở mức máy. Ta quan tâm chủ yếu đến tốc độ tăng trưởng.

---

## 5. Time Complexity

**Time complexity** mô tả cách thời gian thực hiện tăng theo input size.

Ví dụ:

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

Nếu:

```text
n = len(arr)
```

thì vòng lặp chạy `n` lần.

Do đó:

```text
T(n) = Θ(n)
```

Time complexity không nhất thiết là số giây thực tế. Nó mô tả tốc độ tăng trưởng về mặt toán học.

---

## 6. Space and Auxiliary Space Complexity

**Space complexity** mô tả lượng bộ nhớ cần dùng.

Cần phân biệt:

- **Input space**: bộ nhớ dùng để lưu input.
- **Auxiliary space**: bộ nhớ bổ sung ngoài input.

Ví dụ:

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

Thuật toán chỉ dùng thêm một số biến cố định.

Do đó:

```text
Auxiliary space = Θ(1)
```

Ngược lại, nếu thuật toán tạo một list mới có `n` phần tử:

```python
def copy_array(arr):
    result = []

    for x in arr:
        result.append(x)

    return result
```

thì auxiliary space là:

```text
Θ(n)
```

---

## 7. Best, Average, and Worst Cases

Thời gian chạy có thể khác nhau giữa các input cùng kích thước.

Xét Linear Search:

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

### 7.1. Best Case

Best case là lớp input làm cực tiểu hóa chi phí.

Nếu target ở vị trí đầu tiên:

```text
T_best(n) = Θ(1)
```

### 7.2. Worst Case

Worst case là lớp input làm cực đại hóa chi phí.

Nếu target:

- ở vị trí cuối;
- hoặc không tồn tại;

thì:

```text
T_worst(n) = Θ(n)
```

### 7.3. Average Case

Average-case analysis xét kỳ vọng chi phí dưới một distribution xác định.

Giả sử target chắc chắn tồn tại và có xác suất bằng nhau tại mỗi vị trí.

Số phép so sánh trung bình:

```text
(1 + 2 + ... + n) / n
= (n + 1) / 2
= Θ(n)
```

Average-case analysis không thể xác định chính xác nếu không nêu mô hình xác suất.

---

## 8. Growth Rates

Các bậc tăng trưởng phổ biến:

| Complexity | Tên gọi | Ví dụ |
|---|---|---|
| `Θ(1)` | Constant | array indexing |
| `Θ(log n)` | Logarithmic | binary search |
| `Θ(n)` | Linear | linear scan |
| `Θ(n log n)` | Linearithmic | merge sort |
| `Θ(n²)` | Quadratic | xét mọi cặp |
| `Θ(n³)` | Cubic | ba vòng lặp độc lập |
| `Θ(2^n)` | Exponential | duyệt mọi subset |
| `Θ(n!)` | Factorial | duyệt mọi permutation |

Thứ tự điển hình:

```text
1 < log n < n < n log n < n² < n³ < 2^n < n!
```

Growth rate càng lớn, thuật toán càng khó mở rộng khi input tăng.

---

## 9. Why Growth Rate Matters

Giả sử cùng một máy có thể thực hiện khoảng:

```text
100,000,000 operations per second
```

Một thuật toán `Θ(n)` có thể xử lý input rất lớn.

Một thuật toán `Θ(n²)` nhanh chóng trở nên chậm.

Một thuật toán `Θ(2^n)` có thể không khả thi ngay cả khi `n` chỉ khoảng vài chục.

Do đó:

> **Complexity là công cụ để đánh giá scalability.**

---

## 10. Asymptotic Analysis

Asymptotic analysis nghiên cứu hành vi của hàm chi phí khi input size trở nên rất lớn.

Ta thường:

- bỏ constant factors;
- bỏ lower-order terms;
- giữ dominant term.

Ví dụ:

```text
T(n) = 5n² + 100n + 200
```

Khi `n` lớn, `n²` chi phối.

Do đó:

```text
T(n) = Θ(n²)
```

Ví dụ khác:

```text
T(n) = 100n log n + n
```

suy ra:

```text
T(n) = Θ(n log n)
```

---

## 11. Big-O Notation

Big-O mô tả một asymptotic upper bound.

Ta nói:

```text
f(n) = O(g(n))
```

nếu tồn tại các hằng số:

```text
c > 0
n0 > 0
```

sao cho với mọi `n ≥ n0`:

```text
0 ≤ f(n) ≤ c × g(n)
```

### Ví dụ

Xét:

```text
f(n) = 3n + 8
```

Với `n ≥ 8`:

```text
3n + 8 ≤ 4n
```

Do đó:

```text
3n + 8 = O(n)
```

Một hàm có thể có nhiều upper bounds:

```text
3n + 8 = O(n)
3n + 8 = O(n²)
3n + 8 = O(n³)
```

Nhưng `O(n)` là cận chặt hơn.

---

## 12. Big-Omega Notation

Big-Omega mô tả một asymptotic lower bound.

Ta nói:

```text
f(n) = Ω(g(n))
```

nếu tồn tại `c > 0`, `n0 > 0` sao cho:

```text
0 ≤ c × g(n) ≤ f(n)
```

với mọi `n ≥ n0`.

Ví dụ:

```text
5n² = Ω(n²)
```

vì có thể chọn `c = 5`.

---

## 13. Big-Theta Notation

Big-Theta mô tả một asymptotically tight bound.

Ta nói:

```text
f(n) = Θ(g(n))
```

nếu tồn tại `c1 > 0`, `c2 > 0`, `n0 > 0` sao cho:

```text
0 ≤ c1 × g(n) ≤ f(n) ≤ c2 × g(n)
```

với mọi `n ≥ n0`.

Tương đương:

```text
f(n) = O(g(n))
```

và:

```text
f(n) = Ω(g(n))
```

Ví dụ:

```text
6n³ = Θ(n³)
```

---

## 14. Important Distinction: Cases vs Bounds

Không nên đồng nhất:

```text
Big-O = Worst Case
Big-Omega = Best Case
```

Best, average và worst case nói về **loại input**.

`O`, `Ω`, `Θ` mô tả **cận của một hàm complexity**.

Ví dụ:

```text
T_worst(n) = Θ(n)
```

thì đồng thời:

```text
T_worst(n) = O(n)
```

và:

```text
T_worst(n) = Ω(n)
```

---

## 15. Rules for Analyzing Loops and Code Fragments

### 15.1. Constant Operations

```python
x = a + b
```

Nếu xem phép cộng là constant-time:

```text
Θ(1)
```

### 15.2. Single Loop

```python
for i in range(n):
    print(i)
```

Thân lặp chạy `n` lần:

```text
Θ(n)
```

### 15.3. Consecutive Loops

```python
for i in range(n):
    work_a()

for j in range(n):
    work_b()
```

Tổng:

```text
Θ(n) + Θ(n) = Θ(n)
```

Không phải `Θ(n²)`.

### 15.4. Nested Independent Loops

```python
for i in range(n):
    for j in range(n):
        work()
```

Thân trong chạy `n × n` lần:

```text
Θ(n²)
```

### 15.5. Dependent Loops

```python
for i in range(n):
    for j in range(i):
        work()
```

Số lần thực hiện:

```text
0 + 1 + 2 + ... + (n - 1)
```

Dùng công thức:

```text
0 + 1 + ... + (n - 1) = n(n - 1) / 2
```

Do đó:

```text
Θ(n²)
```

### 15.6. If-Else

```python
if n == 1:
    print("Wrong Value")
else:
    for i in range(n):
        print(i)
```

Worst-case time:

```text
Θ(n)
```

Tổng quát:

```text
cost(condition) + max(cost(if-branch), cost(else-branch))
```

### 15.7. Logarithmic Loop

```python
i = 1

while i < n:
    i *= 2
```

Giá trị:

```text
1, 2, 4, 8, 16, ...
```

Sau `k` vòng:

```text
i = 2^k
```

Dừng khi:

```text
2^k ≥ n
```

Do đó:

```text
k = Θ(log n)
```

### 15.8. Halving Loop

```python
i = n

while i > 1:
    i //= 2
```

Dãy:

```text
n, n/2, n/4, n/8, ...
```

Số vòng:

```text
Θ(log n)
```

---

## 16. Useful Mathematical Sums

### 16.1. Arithmetic Sum

```text
1 + 2 + ... + n = n(n + 1) / 2 = Θ(n²)
```

### 16.2. Geometric Sum

Với `x ≠ 1`:

```text
1 + x + x² + ... + x^n
= (x^(n + 1) - 1) / (x - 1)
```

Ví dụ:

```text
1 + 2 + 4 + ... + 2^k
= 2^(k + 1) - 1
= Θ(2^k)
```

### 16.3. Harmonic Sum

```text
1 + 1/2 + 1/3 + ... + 1/n = Θ(log n)
```

### 16.4. Logarithmic Sum

```text
Σ log k = log(n!) = Θ(n log n)
```

### 16.5. Power Sum

Với `p > -1`:

```text
Σ k^p = Θ(n^(p + 1))
```

---

## 17. Common Mistakes

### Mistake 1: Two loops always mean `O(n²)`

Sai.

Hai vòng nối tiếp có thể chỉ là `O(n)`.

### Mistake 2: One line means `O(1)`

Sai.

```python
result = sorted(arr)
```

là một dòng code nhưng không phải constant-time.

### Mistake 3: Ignore operation cost

```python
arr[:k]
```

tốn thời gian theo số phần tử được sao chép.

### Mistake 4: Ignore input size definition

Với graph, `O(V + E)` thường chính xác hơn `O(n)`.

### Mistake 5: Use only `O` when `Θ` is known

Nếu:

```text
T(n) = 3n + 7
```

thì nên viết:

```text
T(n) = Θ(n)
```

---

## 18. Tóm tắt

- Phân tích thuật toán nghiên cứu cách tài nguyên tăng theo input size.
- Input size phải được xác định rõ.
- Basic operation counting là một công cụ cơ bản.
- Time complexity và auxiliary space complexity là hai đại lượng chính.
- Best, average và worst case là các loại input.
- Growth rate quyết định scalability.
- Big-O là upper bound, Big-Omega là lower bound, Big-Theta là tight bound.
- Không nên đồng nhất Big-O với worst case hoặc Big-Omega với best case.
- Không thể chỉ đếm số vòng lặp; phải tính số lần thao tác thực sự được thực hiện.