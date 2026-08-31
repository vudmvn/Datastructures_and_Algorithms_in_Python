# Bài tập — Phân tích độ phức tạp thuật toán

**Cập nhật lần cuối:** 31 tháng 8 năm 2026

> **Mục tiêu:** luyện tập cách xác định kích thước đầu vào, đếm số lần thực hiện thao tác, phân tích vòng lặp, nhận diện tốc độ tăng trưởng, sử dụng ký hiệu $O$, $\Omega$, $\Theta$, thiết lập và giải recurrence, và làm quen với amortized analysis.
>
> Các bài tập được biên soạn theo các chủ đề của **Chương 1 — Introduction** trong *Data Structures and Algorithmic Thinking with Python*, đặc biệt các phần về running-time analysis, rate of growth, asymptotic notation, guidelines for asymptotic analysis, logarithms/summations, recurrence relations và amortized analysis.

---

## Quy ước khi đếm thao tác

Trừ khi đề bài nói khác:

- Mỗi phép **gán**, **so sánh**, **cộng/trừ/nhân/chia** được xem là một thao tác cơ bản.
- Khi chỉ hỏi **số lần câu lệnh được thực hiện**, chỉ đếm đúng câu lệnh được chỉ ra.
- Khi hỏi **độ phức tạp**, bỏ qua hằng số nhân và các số hạng bậc thấp.
- Có thể giả sử $n$ là số nguyên dương.
- Với các bài chia đôi, có thể giả sử $n$ là lũy thừa của 2 nếu điều đó giúp đơn giản hóa phép tính.

---

## Phần A. Đếm số thao tác cơ bản

### Bài 1. Một vòng lặp tuyến tính

Cho đoạn mã:

```python
count = 0
for i in range(n):
    count = count + 1
```

1. Câu lệnh `count = count + 1` được thực hiện bao nhiêu lần?
2. Nếu xem phép cộng và phép gán là hai thao tác riêng biệt, phần thân vòng lặp thực hiện bao nhiêu thao tác?
3. Độ phức tạp thời gian theo $\Theta$ là gì?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

1. Câu lệnh được thực hiện đúng $n$ lần.
2. Mỗi lần có 1 phép cộng và 1 phép gán, nên có $2n$ thao tác trong phần thân.
3. Bỏ qua hằng số:

$$T(n) = \Theta(n).$$

</details>

---

### Bài 2. Hai vòng lặp liên tiếp

```python
count = 0

for i in range(n):
    count += 1

for i in range(n):
    for j in range(n):
        count += 1
```

1. `count += 1` được thực hiện tổng cộng bao nhiêu lần?
2. Viết $T(n)$ theo dạng đa thức.
3. Xác định $\Theta(T(n))$.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Vòng thứ nhất thực hiện $n$ lần.

Hai vòng lặp lồng nhau thực hiện:

$$n \cdot n = n^2$$

lần.

Do đó:

$$T(n) = n + n^2.$$

Số hạng bậc cao nhất là $n^2$, nên:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 3. Vòng lặp tam giác

```python
count = 0

for i in range(n):
    for j in range(i + 1):
        count += 1
```

1. Với một giá trị cố định của $i$, câu lệnh `count += 1` chạy bao nhiêu lần?
2. Tính chính xác tổng số lần câu lệnh này được thực hiện.
3. Suy ra độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Với $i = 0, 1, \dots, n-1$, số lần chạy của vòng trong lần lượt là:

$$1, 2, 3, \dots, n.$$

Do đó:

$$T(n) = 1 + 2 + \dots + n = \frac{n(n+1)}{2}.$$

Vì vậy:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 4. Tam giác theo chiều ngược lại

```python
count = 0

for i in range(n):
    for j in range(i, n):
        count += 1
```

Tính chính xác số lần `count += 1` được thực hiện và xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Số lần chạy của vòng trong là:

$$n, (n-1), (n-2), \dots, 1.$$

Do đó:

$$T(n) = n + (n-1) + \dots + 1 = \frac{n(n+1)}{2}.$$

Suy ra:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 5. Bước nhảy bằng 2

```python
count = 0

for i in range(n):
    for j in range(0, n, 2):
        count += 1
```

1. Vòng trong thực hiện bao nhiêu lần?
2. Tổng số lần tăng `count` là bao nhiêu?
3. Độ phức tạp là gì?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Vòng trong duyệt các giá trị:

$$0, 2, 4, \dots$$

nhỏ hơn $n$, nên chạy khoảng $n/2$ lần, chính xác là:

$$\lceil n/2 
ceil.$$

Tổng số lần tăng `count`:

$$n \lceil n/2 
ceil.$$

Do đó:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 6. Tổng bình phương

```python
count = 0

for i in range(1, n + 1):
    for j in range(i * i):
        count += 1
```

1. Viết tổng biểu diễn số lần thực hiện `count += 1`.
2. Dùng công thức tổng bình phương để tính.
3. Xác định $\Theta$.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Ta có:

$$T(n) = \sum_{i=1}^n i^2.$$

Sử dụng:

$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}.$$

Số hạng bậc cao nhất là $\frac{1}{3}n^3$, nên:

$$T(n) = \Theta(n^3).$$

</details>

---

## Phần B. Phân tích vòng lặp logarithmic

### Bài 7. Nhân đôi biến điều khiển

```python
i = 1
while i < n:
    i = i * 2
```

1. Sau $k$ vòng lặp, `i` có giá trị bằng bao nhiêu?
2. Vòng lặp dừng khi nào?
3. Suy ra số vòng lặp và độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Sau $k$ lần:

$$i = 2^k.$$

Ta cần giá trị nhỏ nhất của $k$ sao cho:

$$2^k \ge n.$$

Do đó:

$$k = \lceil \log_2 n 
ceil.$$

Vì vậy:

$$T(n) = \Theta(\log n).$$

Cơ số logarithm không ảnh hưởng đến lớp độ phức tạp.

</details>

---

### Bài 8. Chia đôi biến điều khiển

```python
i = n
while i > 1:
    i = i // 2
```

Xác định số vòng lặp theo $n$ và độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Sau $k$ lần:

$$i \approx \frac{n}{2^k}.$$

Vòng lặp dừng khi:

$$\frac{n}{2^k} \le 1 \implies 2^k \ge n.$$

Vì vậy số vòng lặp là xấp xỉ:

$$\log_2 n$$

và:

$$T(n) = \Theta(\log n).$$

</details>

---

### Bài 9. Hai vòng logarithmic lồng nhau

```python
count = 0
i = 1

while i <= n:
    j = n
    while j > 0:
        count += 1
        j = j // 2
    i = i * 2
```

Xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Vòng ngoài chạy:

$$\Theta(\log n)$$

lần.

Ở mỗi lần của vòng ngoài, vòng trong cũng chạy:

$$\Theta(\log n)$$

lần.

Do đó:

$$T(n) = \Theta(\log n \cdot \log n) = \Theta(\log^2 n).$$

</details>

---

### Bài 10. Tuyến tính nhân logarithmic

```python
count = 0

for i in range(n):
    j = 1
    while j <= n:
        count += 1
        j = j * 2
```

1. Vòng `while` chạy bao nhiêu lần cho mỗi $i$?
2. Độ phức tạp tổng cộng là gì?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Vòng `while` tạo dãy:

$$1, 2, 4, 8, \dots, 2^k \le n.$$

Số vòng là:

$$\lfloor \log_2 n 
floor + 1.$$

Vòng ngoài chạy $n$ lần, nên:

$$T(n) = n \cdot (\lfloor \log_2 n 
floor + 1) = \Theta(n \log n).$$

</details>

---

### Bài 11. Tổng cấp số nhân trong vòng lặp

```python
count = 0
i = n

while i >= 1:
    for j in range(i):
        count += 1
    i = i // 2
```

Không được chỉ lấy “số vòng ngoài × chi phí vòng đầu tiên”. Hãy viết tổng chi phí và xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Chi phí qua các mức xấp xỉ:

$$n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \dots$$

Đây là cấp số nhân có tổng nhỏ hơn:

$$2n.$$

Do đó:

$$T(n) = \Theta(n).$$

Đây là ví dụ quan trọng cho thấy một vòng logarithmic ở bên ngoài **không nhất thiết** tạo ra $O(n \log n)$.

</details>

---

## Phần C. Vòng lặp phụ thuộc chỉ số

### Bài 12. Tổng harmonic

```python
count = 0

for i in range(1, n + 1):
    j = i
    while j <= n:
        count += 1
        j += i
```

1. Với mỗi $i$, vòng `while` chạy khoảng bao nhiêu lần?
2. Viết tổng số lần thực hiện.
3. Suy ra độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Với một $i$ cố định, `j` nhận các giá trị:

$$i, 2i, 3i, \dots$$

đến $n$, nên vòng trong chạy khoảng:

$$\lfloor n/i 
floor$$

lần.

Tổng:

$$T(n) = \sum_{i=1}^n \lfloor n/i 
floor.$$

Bỏ phần làm tròn:

$$T(n) \approx n \cdot \sum_{i=1}^n \frac{1}{i}.$$

Mà:

$$\sum_{i=1}^n \frac{1}{i} = \Theta(\log n).$$

Do đó:

$$T(n) = \Theta(n \log n).$$

</details>

---

### Bài 13. Biến tăng với tốc độ tăng dần

```python
i = 1
s = 1

while s < n:
    i = i + 1
    s = s + i
```

Hãy xác định độ phức tạp của vòng lặp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Sau $k$ vòng, $s$ có độ lớn bằng tổng của các số nguyên đầu tiên:

$$s = \Theta(k^2).$$

Vòng lặp kết thúc khi:

$$k^2 \approx n.$$

Do đó:

$$k = \Theta(\sqrt{n}).$$

Suy ra:

$$T(n) = \Theta(\sqrt{n}).$$

</details>

---

### Bài 14. Điều kiện bình phương

```python
i = 1
count = 0

while i * i < n:
    count += 1
    i += 1
```

Xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Vòng lặp dừng khi:

$$i^2 \ge n.$$

Suy ra:

$$i \approx \sqrt{n}.$$

Do đó:

$$T(n) = \Theta(\sqrt{n}).$$

</details>

---

## Phần D. Best case, worst case và nhánh điều kiện

### Bài 15. Tìm kiếm tuyến tính

```python
def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1
```

Giả sử `len(A) = n`.

1. Best case xảy ra khi nào? Độ phức tạp?
2. Worst case xảy ra khi nào? Độ phức tạp?
3. Nếu xác suất `x` nằm ở mỗi vị trí là như nhau, số phép so sánh trung bình xấp xỉ bao nhiêu?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

1. Best case: `x` nằm ngay ở `A[0]`.

$$T_{\text{best}}(n) = \Theta(1).$$

2. Worst case: `x` không có trong mảng hoặc nằm ở cuối mảng.

$$T_{\text{worst}}(n) = \Theta(n).$$

3. Nếu `x` chắc chắn tồn tại và các vị trí có xác suất như nhau:

$$\frac{1 + 2 + \dots + n}{n} = \frac{n+1}{2}.$$

Do đó average case vẫn là:

$$\Theta(n).$$

</details>

---

### Bài 16. Nhánh có chi phí khác nhau

```python
count = 0

for i in range(n):
    if A[i] == 0:
        count += 1
    else:
        for j in range(n):
            count += 1
```

Xác định:

1. Best-case complexity.
2. Worst-case complexity.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

### Best case

Nếu mọi `A[i] == 0`, mỗi lần vòng ngoài chỉ thực hiện công việc hằng số.

$$T_{\text{best}}(n) = \Theta(n).$$

### Worst case

Nếu mọi `A[i] != 0`, với mỗi $i$ ta thực hiện thêm vòng lặp $n$ lần.

$$T_{\text{worst}}(n) = n \cdot n = \Theta(n^2).$$

</details>

---

### Bài 17. `break` làm thay đổi độ phức tạp

```python
for i in range(n):
    j = 0
    while j < n:
        break
        j += 1
```

Độ phức tạp của đoạn mã là gì? Giải thích tại sao không phải $O(n^2)$.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Mỗi lần vòng ngoài chạy, vòng `while` chỉ thực hiện đúng một lượt vì gặp `break` ngay lập tức.

Do đó:

$$T(n) = n \cdot O(1) = \Theta(n).$$

Không thể chỉ nhìn vào điều kiện `j < n` để kết luận vòng trong chạy $n$ lần; cần xem **luồng điều khiển thực tế**.

</details>

---

## Phần E. Rate of growth và ký hiệu tiệm cận

### Bài 18. Bỏ số hạng bậc thấp

Xác định $\Theta$ cho các hàm:

1. $5n + 100$
2. $3n^2 + 20n + 7$
3. $n^4 + 100n^2 + 500$
4. $9$
5. $n \log n + 20n$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

1. $\Theta(n)$
2. $\Theta(n^2)$
3. $\Theta(n^4)$
4. $\Theta(1)$
5. $\Theta(n \log n)$

Nguyên tắc: khi $n$ lớn, giữ lại số hạng có tốc độ tăng trưởng nhanh nhất và bỏ hệ số hằng.

</details>

---

### Bài 19. Chứng minh bằng định nghĩa Big-O

Chứng minh:

$$5n + 12 = O(n).$$

Hãy đưa ra một cặp hằng số $c > 0$ và $n_0 > 0$ phù hợp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Ta cần:

$$5n + 12 \le c \cdot n$$

với mọi $n \ge n_0$.

Ví dụ, nếu $n \ge 12$:

$$12 \le n.$$

Do đó:

$$5n + 12 \le 6n.$$

Có thể chọn:

$$c = 6, \quad n_0 = 12.$$

Vậy:

$$5n + 12 = O(n).$$

Lưu ý: $c$ và $n_0$ **không duy nhất**.

</details>

---

### Bài 20. Chứng minh một cận chặt

Chứng minh:

$$4n^2 + 3n + 2 = \Theta(n^2).$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Ta cần tìm $c_1, c_2, n_0 > 0$ sao cho:

$$c_1 n^2 \le 4n^2 + 3n + 2 \le c_2 n^2.$$

Với $n \ge 1$:

$$4n^2 \le 4n^2 + 3n + 2.$$

Mặt khác:

$$3n \le 3n^2, \quad 2 \le 2n^2.$$

Nên:

$$4n^2 + 3n + 2 \le 9n^2.$$

Có thể chọn:

$$c_1 = 4, \quad c_2 = 9, \quad n_0 = 1.$$

Suy ra:

$$4n^2 + 3n + 2 = \Theta(n^2).$$

</details>

---

### Bài 21. Đúng hay sai?

Xác định mỗi phát biểu sau là đúng hay sai.

1. $2^{n+1} = O(2^n)$
2. $2^{2n} = O(2^n)$
3. $n \log n = O(n^2)$
4. $n^2 = \Omega(n \log n)$
5. $100n + 1 = \Theta(n)$
6. $n = \Theta(n^2)$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

1. **Đúng**, vì $2^{n+1} = 2 \cdot 2^n$.
2. **Sai**, vì $2^{2n} = 4^n$ tăng nhanh hơn $2^n$.
3. **Đúng**.
4. **Đúng**.
5. **Đúng**.
6. **Sai**.

</details>

---

### Bài 22. Xếp hạng tốc độ tăng trưởng

Sắp xếp các hàm sau từ tăng chậm nhất đến tăng nhanh nhất:

$$1, \quad \log n, \quad \sqrt{n}, \quad n, \quad n \log n, \quad 4^{\log_2 n}, \quad n^3, \quad 2^n, \quad n!.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Ta có:

$$4^{\log_2 n} = (2^2)^{\log_2 n} = n^2.$$

Thứ tự:

$$1 < \log n < \sqrt{n} < n < n \log n < n^2 < n^3 < 2^n < n!.$$

</details>

---

## Phần F. Viết recurrence từ mã đệ quy

### Bài 23. Một lời gọi đệ quy giảm 1

```python
def f(n):
    if n <= 0:
        return
    do_constant_work()
    f(n - 1)
```

1. Viết recurrence cho thời gian chạy.
2. Giải recurrence.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Recurrence:

$$T(n) = T(n-1) + \Theta(1).$$

Khai triển:

$$T(n) = T(n-2) + 2\Theta(1) = \dots = T(0) + n\Theta(1).$$

Do đó:

$$T(n) = \Theta(n).$$

</details>

---

### Bài 24. Một lời gọi đệ quy và công việc tuyến tính

```python
def f(n):
    if n <= 0:
        return

    for i in range(n):
        do_constant_work()

    f(n - 1)
```

Viết recurrence và xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Mỗi lời gọi làm $\Theta(n)$ công việc trước khi gọi `f(n-1)`:

$$T(n) = T(n-1) + \Theta(n).$$

Khai triển:

$$T(n) = n + (n-1) + \dots + 1.$$

Do đó:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 25. Giảm kích thước đi 3

```python
def f(n):
    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            do_constant_work()

    f(n - 3)
```

1. Viết recurrence.
2. Xác định số mức đệ quy.
3. Suy ra độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Mỗi lời gọi có chi phí:

$$\Theta(n^2).$$

Recurrence:

$$T(n) = T(n-3) + \Theta(n^2).$$

Số mức đệ quy là khoảng $n/3 = \Theta(n)$.

Tổng công việc:

$$n^2 + (n-3)^2 + (n-6)^2 + \dots$$

Đây là tổng của $\Theta(n)$ số hạng bậc $n^2$ giảm dần, tương đương về bậc với tổng bình phương.

Do đó:

$$T(n) = \Theta(n^3).$$

</details>

---

### Bài 26. Ba lời gọi với cùng bài toán con

```python
def f(n):
    if n <= 0:
        return

    f(n - 1)
    f(n - 1)
    f(n - 1)
```

Viết recurrence và xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Recurrence:

$$T(n) = 3T(n-1) + \Theta(1).$$

Cây đệ quy có hệ số phân nhánh 3 và độ sâu xấp xỉ $n$.

Số nút tăng theo:

$$1 + 3 + 3^2 + \dots + 3^n.$$

Do đó:

$$T(n) = \Theta(3^n).$$

</details>

---

### Bài 27. Hai bài toán con bằng một nửa

```python
def f(n):
    if n <= 1:
        return

    f(n // 2)
    f(n // 2)
    do_constant_work()
```

Viết recurrence và xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Recurrence:

$$T(n) = 2T(n/2) + \Theta(1).$$

Theo Master Theorem:

$$a = 2, \quad b = 2, \quad n^{\log_b a} = n.$$

Phần công việc ngoài đệ quy chỉ là $\Theta(1)$, nhỏ hơn $n$.

Do đó:

$$T(n) = \Theta(n).$$

</details>

---

## Phần G. Master Theorem

### Bài 28.

Giải recurrence:

$$T(n) = 2T(n/2) + n.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Có:

$$a = 2, \quad b = 2.$$

Do đó:

$$n^{\log_b a} = n^{\log_2 2} = n.$$

Phần ngoài đệ quy là:

$$f(n) = n.$$

Hai phần cùng bậc, nên:

$$T(n) = \Theta(n \log n).$$

</details>

---

### Bài 29.

Giải:

$$T(n) = 4T(n/2) + n.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

$$a = 4, \quad b = 2,$$

nên:

$$n^{\log_2 4} = n^2.$$

Vì:

$$f(n) = n$$

nhỏ hơn $n^2$, phần các bài toán con chi phối.

Do đó:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 30.

Giải:

$$T(n) = 2T(n/4) + n.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

$$a = 2, \quad b = 4.$$

Ta có:

$$n^{\log_4 2} = n^{1/2}.$$

Trong khi:

$$f(n) = n.$$

$n$ tăng nhanh hơn $n^{1/2}$, nên phần combine chi phối.

Do đó:

$$T(n) = \Theta(n).$$

</details>

---

### Bài 31.

Giải:

$$T(n) = 3T(n/2) + n^2.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

$$a = 3, \quad b = 2,$$

nên:

$$n^{\log_2 3} \approx n^{1.585}.$$

Trong khi:

$$f(n) = n^2.$$

$n^2$ tăng nhanh hơn, nên:

$$T(n) = \Theta(n^2).$$

</details>

---

### Bài 32.

Giải:

$$T(n) = 8T(n/2) + n^3.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

$$a = 8, \quad b = 2,$$

nên:

$$n^{\log_2 8} = n^3.$$

Phần ngoài đệ quy cũng là:

$$f(n) = n^3.$$

Hai phần cùng bậc nên xuất hiện thêm một nhân tử logarithm:

$$T(n) = \Theta(n^3 \log n).$$

</details>

---

## Phần H. Recurrence không ở dạng Master Theorem chuẩn

### Bài 33. Giảm từ $n$ xuống $\sqrt{n}$

Giải recurrence:

$$T(n) = T(\sqrt{n}) + 1.$$

Gợi ý: đặt $n = 2^m$.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Đặt:

$$n = 2^m \implies m = \log_2 n.$$

Định nghĩa:

$$S(m) = T(2^m).$$

Khi đó:

$$\sqrt{n} = 2^{m/2}.$$

Suy ra:

$$S(m) = S(m/2) + 1.$$

Recurrence này có độ phức tạp:

$$S(m) = \Theta(\log m).$$

Thay $m = \log n$:

$$T(n) = \Theta(\log \log n).$$

</details>

---

### Bài 34. Hai lời gọi với $\sqrt{n}$

Giải:

$$T(n) = 2T(\sqrt{n}) + 1.$$

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Tiếp tục đặt:

$$n = 2^m, \quad S(m) = T(2^m).$$

Ta được:

$$S(m) = 2S(m/2) + 1.$$

Theo Master Theorem:

$$S(m) = \Theta(m).$$

Do $m = \log n$:

$$T(n) = \Theta(\log n).$$

</details>

---

## Phần I. Phân tích một số đoạn mã tổng hợp

### Bài 35.

```python
count = 0

for i in range(n // 2, n):
    j = 1
    while j <= n // 2:
        k = 1
        while k <= n:
            count += 1
            k *= 2
        j += 1
```

Giả sử $n$ chẵn. Xác định độ phức tạp.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

- Vòng ngoài: $n/2 = \Theta(n)$ lần.
- Vòng giữa: $n/2 = \Theta(n)$ lần.
- Vòng trong: $\Theta(\log n)$ lần.

Nhân các chi phí:

$$T(n) = \Theta(n) \cdot \Theta(n) \cdot \Theta(\log n) = \Theta(n^2 \log n).$$

</details>

---

### Bài 36.

```python
count = 0

for i in range(n):
    j = 1
    while j <= n:
        k = j
        while k > 0:
            count += 1
            k //= 2
        j *= 2
```

Hãy phân tích cẩn thận tổng chi phí của vòng `k`, không chỉ lấy ba số vòng lặp nhân với nhau.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Với:

$$j = 1, 2, 4, \dots, 2^r \le n,$$

vòng `k` chạy khoảng:

$$\log_2 j + 1$$

lần.

Nếu đặt $j = 2^r$, chi phí theo $r$ là:

$$1 + 2 + \dots + (\log_2 n + 1).$$

Do đó, với mỗi $i$:

$$\Theta((\log n)^2).$$

Vòng ngoài chạy $n$ lần:

$$T(n) = \Theta(n \log^2 n).$$

</details>

---

## Phần J. Amortized analysis

### Bài 37. Dynamic array tăng gấp đôi

Một dynamic array ban đầu có sức chứa 1. Mỗi khi đầy, ta tạo một mảng mới có sức chứa gấp đôi và sao chép toàn bộ phần tử cũ sang mảng mới.

Giả sử thực hiện $n$ phép `append`.

1. Một phép `append` riêng lẻ có worst case là bao nhiêu?
2. Tổng số lần sao chép phần tử do resize sau $n$ lần `append` có bậc bao nhiêu?
3. Amortized complexity của một phép `append` là gì?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Một lần `append` gây resize có thể phải sao chép $\Theta(n)$ phần tử, nên worst case của **một phép** có thể là:

$$O(n).$$

Tuy nhiên các lần resize chỉ xảy ra tại các kích thước:

$$1, 2, 4, 8, \dots$$

Tổng số phần tử được sao chép:

$$1 + 2 + 4 + \dots < 2n.$$

Vì vậy tổng chi phí của $n$ lần `append` là:

$$\Theta(n).$$

Amortized cost của mỗi `append`:

$$\Theta(1).$$

</details>

---

## Phần K. Bài tự luyện nâng cao

### Bài 38.

Xác định độ phức tạp:

```python
count = 0

for i in range(1, n + 1):
    j = 1
    while j <= i:
        count += 1
        j *= 2
```

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Với mỗi $i$, vòng trong chạy:

$$\Theta(\log i).$$

Do đó:

$$T(n) = \sum_{i=1}^n \Theta(\log i).$$

Mà:

$$\sum_{i=1}^n \log i = \log(n!).$$

Ta có:

$$\log(n!) = \Theta(n \log n).$$

Suy ra:

$$T(n) = \Theta(n \log n).$$

</details>

---

### Bài 39.

Xác định độ phức tạp:

```python
count = 0
i = 1

while i <= n:
    for j in range(i):
        count += 1
    i *= 2
```

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Chi phí lần lượt là:

$$1 + 2 + 4 + 8 + \dots + n.$$

Đây là tổng cấp số nhân:

$$T(n) < 2n.$$

Do đó:

$$T(n) = \Theta(n).$$

</details>

---

### Bài 40.

Cho:

$$T(n) = T(n/2) + T(n/4) + T(n/8) + n.$$

Không cần tìm hằng số chính xác. Hãy dự đoán và giải thích bậc tăng trưởng của $T(n)$.

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Tổng kích thước các bài toán con ở một mức là:

$$\frac{n}{2} + \frac{n}{4} + \frac{n}{8} = \frac{7}{8}n < n.$$

Công việc ngoài đệ quy ở gốc là $\Theta(n)$, và tổng công việc ở mỗi mức tiếp theo giảm theo một hệ số nhỏ hơn 1.

Ta nhận được một tổng dạng cấp số nhân:

$$n + \frac{7}{8}n + \left(\frac{7}{8}
ight)^2 n + \dots$$

Do đó:

$$T(n) = \Theta(n).$$

</details>

---

## Phần L. Câu hỏi ngắn kiểm tra tư duy

### Bài 41.

Một thuật toán A mất:

$$T_A(n) = 1000n$$

và thuật toán B mất:

$$T_B(n) = n^2.$$

1. Thuật toán nào có tốc độ tăng trưởng tốt hơn?
2. Có nhất thiết A luôn chạy nhanh hơn B với mọi $n$ không?
3. Tại sao phân tích tiệm cận vẫn hữu ích?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

1. A có tốc độ tăng trưởng tốt hơn vì:

$$1000n = \Theta(n)$$

trong khi:

$$n^2 = \Theta(n^2).$$

2. Không. Với $n$ nhỏ, hệ số 1000 có thể khiến A chậm hơn B.
3. Phân tích tiệm cận tập trung vào hành vi khi $n$ lớn và giúp so sánh thuật toán độc lập hơn với phần cứng, ngôn ngữ và hằng số triển khai.

</details>

---

### Bài 42.

Tại sao không nên dùng riêng “thời gian chạy bằng giây” trên một máy tính cụ thể để kết luận thuật toán nào tốt hơn về mặt độ phức tạp?

<details>
<summary><strong>Nhấn để hiển thị hướng dẫn / lời giải</strong></summary>

Thời gian chạy thực tế phụ thuộc vào nhiều yếu tố:

- CPU và bộ nhớ;
- trình thông dịch / compiler;
- ngôn ngữ lập trình;
- cách hiện thực;
- dữ liệu đầu vào;
- tải của hệ thống tại thời điểm chạy.

Phân tích độ phức tạp biểu diễn running time theo **kích thước đầu vào $n$** và tập trung vào tốc độ tăng trưởng, nên phù hợp hơn để so sánh bản chất của các thuật toán.

</details>

---

# Gợi ý sử dụng bộ bài tập

Có thể chia thành ba mức:

- **Cơ bản:** Bài 1–17
- **Trung bình:** Bài 18–32
- **Nâng cao:** Bài 33–42

Một cách tổ chức trên lớp:

1. Yêu cầu sinh viên **đếm số lần thực hiện** trước khi dùng Big-O.
2. Từ tổng chính xác, rút gọn sang $\Theta$.
3. Với vòng lặp `while`, yêu cầu viết dãy giá trị của biến điều khiển.
4. Với recursion, luôn thực hiện theo trình tự:
   - xác định số lời gọi đệ quy;
   - xác định kích thước bài toán con;
   - xác định extra work;
   - viết recurrence;
   - sau đó mới giải recurrence.
5. Chỉ sử dụng Master Theorem khi recurrence thực sự phù hợp với dạng của định lý.
