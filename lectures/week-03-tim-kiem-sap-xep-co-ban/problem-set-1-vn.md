---
title: "Bài giảng: Phân tích thuật toán — Bài tập và lời giải"
course: "Data Structures and Algorithmic Thinking with Python"
language: "vi"
version: "1.2"
---

# Bài giảng: Phân tích thuật toán — Bài tập và lời giải

**Cập nhật lần cuối:** 3 tháng 8 năm 2026

## 1. Mục tiêu học tập

Phần này tập trung vào việc luyện tập phân tích độ phức tạp thông qua các dạng bài thường gặp: giải phương trình truy hồi, phân tích vòng lặp có bước tăng không tuyến tính, phân tích hàm đệ quy, sử dụng Master Theorem, phương pháp thế, recursion tree và so sánh tốc độ tăng trưởng của các hàm.

Sau khi hoàn thành phần này, người học có thể:

- giải các truy hồi dạng `T(n) = aT(n-b) + f(n)` bằng phép thế hoặc định lý thích hợp;
- phân tích các vòng lặp có biến điều khiển tăng theo tổng tích lũy, cấp số nhân hoặc căn bậc hai;
- thiết lập truy hồi từ mã nguồn đệ quy;
- nhận biết khi nào Master Theorem áp dụng được và khi nào cần đổi biến hoặc sử dụng recursion tree;
- phân biệt cận trên, cận dưới và cận chặt;
- so sánh bậc tăng trưởng của các hàm đa thức, hàm mũ, giai thừa và logarithm.

Một nguyên tắc quan trọng là không suy luận độ phức tạp chỉ từ hình thức bề ngoài của đoạn mã hoặc truy hồi. Hai biểu thức có vẻ tương tự có thể dẫn tới các kết quả hoàn toàn khác nhau do sự triệt tiêu, cấu trúc đệ quy hoặc quy luật tăng của biến điều khiển.

> **Cách sử dụng:** Mỗi bài được trình bày với đề bài đầy đủ. Phần lời giải được ẩn mặc định và chỉ hiển thị khi nhấn vào dấu tam giác cạnh dòng **Hiện lời giải**.

---

## 2. Truy hồi dạng subtract-and-conquer và phép thế

### Bài 1. Truy hồi `T(n) = 3T(n-1)`

**Đề bài.** Hãy xác định độ phức tạp thời gian của truy hồi sau:

```text
T(n) = 3T(n - 1), nếu n > 0
T(0) = 1
```

Giải truy hồi bằng phương pháp thế hoặc khai triển trực tiếp.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```text
T(n) = 3T(n-1),  nếu n > 0
T(0) = 1
```

Khai triển liên tiếp:

```text
T(n) = 3T(n-1)
     = 3²T(n-2)
     = 3³T(n-3)
     = ...
     = 3ⁿT(0)
     = 3ⁿ
```

Do đó:

`T(n) = Θ(3ⁿ)`.

Bài toán này cũng có thể được xem là một trường hợp subtract-and-conquer với hệ số phân nhánh lớn hơn `1`.


</details>

### Bài 2. Truy hồi có triệt tiêu

**Đề bài.** Hãy xác định độ phức tạp thời gian của truy hồi sau:

```text
T(n) = 2T(n - 1) - 1, nếu n > 0
T(0) = 1
```

Giải truy hồi bằng phương pháp thế và lưu ý khả năng xuất hiện sự triệt tiêu giữa các số hạng.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```text
T(n) = 2T(n-1) - 1,  nếu n > 0
T(0) = 1
```

Khai triển:

```text
T(n) = 2T(n-1) - 1
     = 2(2T(n-2) - 1) - 1
     = 2²T(n-2) - 2 - 1
```

Tiếp tục:

```text
T(n) = 2ⁿT(0) - (2ⁿ⁻¹ + 2ⁿ⁻² + ... + 2 + 1)
```

Vì `T(0) = 1` và `2ⁿ⁻¹ + ... + 2 + 1 = 2ⁿ - 1`, suy ra:

```text
T(n) = 2ⁿ - (2ⁿ - 1) = 1
```

Do đó:

`T(n) = Θ(1)`.

Ví dụ này cho thấy không thể kết luận rằng một truy hồi có hệ số `2` trước lời gọi đệ quy nhất thiết phải có độ phức tạp mũ; phần còn lại của truy hồi có thể tạo ra sự triệt tiêu chính xác.


</details>

## 3. Phân tích vòng lặp với bước tăng không tuyến tính

### Bài 3. Biến tích lũy tăng theo tổng `1 + 2 + ... + k`

**Đề bài.** Hãy xác định độ phức tạp thời gian của hàm sau theo kích thước input `n`:

```python
def function(n):
    i = 1
    s = 1

    while s < n:
        i = i + 1
        s = s + i

    print("*")

function(20)
```

Cần xác định số lần vòng `while` được thực hiện khi giá trị `s` tăng theo tổng tích lũy `1 + 2 + ... + k`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Sau `k` vòng lặp, giá trị của `s` có bậc:

```text
s = 1 + 2 + ... + k = k(k+1)/2
```

Vòng lặp dừng khi `s ≥ n`, tức là:

`k(k+1)/2 ≥ n`.

Suy ra `k = Θ(√n)`, nên:

`T(n) = Θ(√n)`.

Điểm cần chú ý là biến `s` không tăng mỗi lần một đơn vị; nó tăng theo tổng các số nguyên liên tiếp.


</details>

### Bài 4. Bước nhảy tăng dần

**Đề bài.** Hãy xác định độ phức tạp thời gian của hàm sau:

```python
def function(n):
    i = 1
    count = 0

    while i < n:
        count = count + 1
        i = i + count
        print(count)

function(20)
```

Phân tích số vòng lặp dựa trên quy luật tăng của `i`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    i = 1
    count = 0

    while i < n:
        count = count + 1
        i = i + count
        print(count)
```

Sau `k` vòng:

```text
i ≈ 1 + 1 + 2 + ... + k
```

Do đó `i = Θ(k²)`. Vòng lặp dừng khi `i ≥ n`, nên:

`k = Θ(√n)`.

Vì vậy:

`T(n) = Θ(√n)`.


</details>

### Bài 5. Ba vòng lặp với một vòng logarithmic

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            k = 1

            while k <= n:
                count = count + 1
                k = k * 2

            j = j + 1

    print(count)

function(20)
```

Phân tích riêng số lần thực hiện của vòng ngoài, vòng giữa và vòng trong.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                count = count + 1
                k = k * 2
            j = j + 1

    print(count)
```

Vòng ngoài chạy `Θ(n)` lần. Vòng giữa chạy `Θ(n)` lần. Vòng trong nhân đôi `k`, nên chạy `Θ(log n)` lần.

Do đó:

`T(n) = Θ(n² log n)`.


</details>

### Bài 6. Hai vòng logarithmic lồng trong một vòng tuyến tính

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            k = 1

            while k <= n:
                count = count + 1
                k = k * 2

            j = j * 2

    print(count)

function(20)
```

Chú ý rằng cả `j` và `k` đều tăng theo cấp số nhân.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                count = count + 1
                k = k * 2
            j = j * 2

    print(count)
```

Vòng ngoài chạy `Θ(n)` lần. Biến `j` tăng gấp đôi nên vòng giữa chạy `Θ(log n)` lần. Vòng trong cũng chạy `Θ(log n)` lần.

Vì vậy:

`T(n) = Θ(n log² n)`.


</details>

### Bài 7. Ảnh hưởng của `break`

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1

        while j + n // 2 <= n:
            break
            j = j * 2

        print(count)

function(20)
```

Giải thích ảnh hưởng của lệnh `break` đến số lần thực hiện vòng `while`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    count = 0

    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            break
            j = j * 2

        print(count)
```

Mặc dù điều kiện của vòng `while` có thể đúng, lệnh `break` khiến vòng lặp kết thúc ngay trong lần lặp đầu tiên. Do đó, mỗi lần của vòng `for` chỉ chịu chi phí hằng số.

Vì vòng ngoài chạy `Θ(n)` lần:

`T(n) = Θ(n)`.


</details>

## 4. Thiết lập truy hồi từ hàm đệ quy

### Bài 8. Hai vòng lặp bậc hai và lời gọi `n-3`

**Đề bài.** Xét hàm đệ quy sau:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            count = count + 1

    function(n - 3)
    print(count)

function(20)
```

Hãy:

1. thiết lập phương trình truy hồi cho thời gian chạy `T(n)`;
2. chứng minh bằng phương pháp khai triển rằng `T(n) = Θ(n³)`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        for j in range(n):
            count = count + 1

    function(n - 3)
    print(count)
```

Mỗi lời gọi thực hiện `Θ(n²)` công việc và gọi lại với kích thước `n-3`. Do đó:

`T(n) = T(n-3) + Θ(n²)`.

Khai triển:

```text
T(n) = Θ(n² + (n-3)² + (n-6)² + ...)
```

Có `Θ(n)` mức đệ quy và tổng các bình phương có bậc `Θ(n³)`. Vì vậy:

`T(n) = Θ(n³)`.


</details>

### Bài 9. Truy hồi có `n log n`

**Đề bài.** Hãy xác định cận chặt `Θ` cho truy hồi:

`T(n) = 2T(n/2) + n log n`.

Có thể sử dụng Master Theorem hoặc dạng mở rộng thích hợp.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = 2T(n/2) + n log n`.

Với `a = 2`, `b = 2`, ta có `n^(log₂2) = n`. Vì:

`f(n) = Θ(n log n)`,

Master Theorem mở rộng cho:

`T(n) = Θ(n log² n)`.


</details>

### Bài 10. Ba bài toán con có tổng kích thước nhỏ hơn `n`

**Đề bài.** Hãy xác định cận `Θ` cho truy hồi:

`T(n) = T(n/2) + T(n/4) + T(n/8) + n`.

Phân tích tổng kích thước các bài toán con hoặc sử dụng recursion tree.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = T(n/2) + T(n/4) + T(n/8) + n`.

Tổng tỷ lệ kích thước của các bài toán con là:

`1/2 + 1/4 + 1/8 = 7/8 < 1`.

Do đó tổng công việc trên mỗi mức của recursion tree giảm theo cấp số nhân:

```text
n + (7/8)n + (7/8)²n + ...
```

Tổng chuỗi là `Θ(n)`, nên:

`T(n) = Θ(n)`.


</details>

### Bài 11. Truy hồi giảm một nửa với chi phí hằng số

**Đề bài.** Hãy xác định cận `Θ` cho truy hồi:

`T(n) = T(⌊n/2⌋) + 7`.

Giải thích số mức đệ quy trước khi kích thước bài toán trở thành hằng số.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = T(⌊n/2⌋) + 7`.

Sau `Θ(log n)` lần chia đôi, kích thước trở thành hằng số. Mỗi mức có chi phí `Θ(1)`, do đó:

`T(n) = Θ(log n)`.


</details>

### Bài 12. Chứng minh cận dưới `Ω(log n)`

**Đề bài.** Chứng minh rằng thời gian chạy của đoạn mã sau có cận dưới `Ω(log n)`; đồng thời xác định cận chặt nếu có thể:

```python
def Read(n):
    k = 1

    while k < n:
        k = 3 * k
```

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def Read(n):
    k = 1
    while k < n:
        k = 3 * k
```

Sau `t` vòng:

`k = 3^t`.

Vòng lặp dừng khi `3^t ≥ n`, nên:

`t ≥ log₃n`.

Vì vậy:

`T(n) = Θ(log n)`,

và đặc biệt:

`T(n) = Ω(log n)`.


</details>

### Bài 13. Truy hồi có chi phí `n(n-1)`

**Đề bài.** Giải truy hồi sau bằng phương pháp khai triển:

```text
T(1) = 1
T(n) = T(n - 1) + n(n - 1), với n ≥ 2
```

Hãy xác định cận chặt `Θ` của `T(n)`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```text
T(1) = 1
T(n) = T(n-1) + n(n-1), với n ≥ 2
```

Khai triển:

```text
T(n) = T(1) + Σ[i=2..n] i(i-1)
```

Ta có:

```text
Σ i(i-1) = Σ i² - Σ i = Θ(n³)
```

Do đó:

`T(n) = Θ(n³)`.


</details>

### Bài 14. Fibonacci đệ quy trực tiếp

**Đề bài.** Xét chương trình tính số Fibonacci bằng đệ quy trực tiếp:

```python
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)

print(Fib(3))
```

Hãy:

1. thiết lập truy hồi thời gian chạy;
2. phân tích độ phức tạp của chương trình;
3. nêu cả một cận trên đơn giản và, nếu có thể, một cận chặt hơn.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
```

Truy hồi thời gian:

`T(n) = T(n-1) + T(n-2) + Θ(1)`.

Một cận trên đơn giản là `O(2^n)`. Phân tích chặt hơn cho thấy số lời gọi tăng theo số Fibonacci, nên:

`T(n) = Θ(φ^n)`,

trong đó `φ = (1 + √5)/2`.


</details>

## 5. Tổng điều hòa, tổng logarithm và các lỗi cần lưu ý

### Bài 15. Vòng lặp với bước tăng `i`

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
def function(n):
    count = 0

    if n <= 0:
        return

    for i in range(n):
        j = 1

        while j <= n:
            j = j + i
            count = count + 1

    print(count)

function(20)
```

Trước khi phân tích độ phức tạp, cần kiểm tra chương trình có luôn kết thúc hay không. Nếu phát hiện lỗi khiến chương trình không dừng, hãy chỉ rõ lỗi và phân tích phiên bản sửa hợp lý.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Nếu sửa vòng ngoài thành:

```python
for i in range(1, n):
```

thì với mỗi `i`, vòng trong chạy khoảng `n/i` lần. Tổng số lần lặp là:

```text
n/1 + n/2 + ... + n/(n-1) = Θ(n log n)
```

Do đó, phiên bản đã sửa có:

`T(n) = Θ(n log n)`.


</details>

### Bài 16. Tổng `Σ log i`

**Đề bài.** Hãy xác định độ phức tạp của tổng:

`Σ[i=1..n] log i`.

Rút gọn tổng bằng các tính chất của logarithm và xác định cận chặt `Θ`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`Σ[i=1..n] log i`.

Sử dụng tính chất logarithm:

```text
log 1 + log 2 + ... + log n
= log(1 × 2 × ... × n)
= log(n!)
```

Theo Stirling:

`log(n!) = Θ(n log n)`.

Vì vậy:

`Σ[i=1..n] log i = Θ(n log n)`.


</details>

## 6. Các mẫu đệ quy đặc biệt

### Bài 17. Ba lời gọi trên kích thước `n/3`

**Đề bài.** Xét hàm đệ quy sau:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n / 3)

function(20)
```

Hãy:

1. thiết lập phương trình truy hồi thời gian;
2. xác định độ phức tạp bằng Master Theorem.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n / 3)
```

Truy hồi:

`T(n) = 3T(n/3) + Θ(1)`.

Theo Master Theorem:

`T(n) = Θ(n)`.


</details>

### Bài 18. Ba lời gọi trên `n-1`

**Đề bài.** Xét hàm đệ quy sau:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n - 1)

function(20)
```

Hãy:

1. thiết lập phương trình truy hồi;
2. giải truy hồi bằng phương pháp khai triển hoặc subtract-and-conquer;
3. xác định cận chặt `Θ`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    if n <= 0:
        return

    for i in range(3):
        function(n - 1)
```

Truy hồi:

`T(n) = 3T(n-1) + Θ(1)`.

Số lời gọi tăng theo cấp số nhân:

`T(n) = Θ(3^n)`.


</details>

### Bài 19. Ba lời gọi trên `0.8n`

**Đề bài.** Xét hàm đệ quy sau:

```python
def function3(n):
    if n <= 0:
        return

    for i in range(3):
        function3(0.8 * n)

function3(20)
```

Hãy thiết lập đúng phương trình truy hồi và xác định độ phức tạp thời gian theo `n`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function3(n):
    if n <= 0:
        return

    for i in range(3):
        function3(0.8 * n)
```

Truy hồi đúng là:

`T(n) = 3T(0.8n) + Θ(1)`.

Viết `0.8n = n/1.25`, ta có `a = 3`, `b = 1.25`. Theo Master Theorem:

`T(n) = Θ(n^(log_{1.25} 3))`.

Vì `log_{1.25}3 ≈ 4.923`, nên:

`T(n) = Θ(n^4.923...)`.


</details>

### Bài 20. Truy hồi `2T(√n) + log n`

**Đề bài.** Hãy xác định độ phức tạp của truy hồi:

`T(n) = 2T(√n) + log n`.

Gợi ý: sử dụng phép đổi biến `m = log n` để biến truy hồi thành dạng phù hợp với Master Theorem.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = 2T(√n) + log n`.

Đặt:

`m = log n`

và:

`S(m) = T(2^m)`.

Vì `√n = 2^(m/2)`, suy ra:

`S(m) = 2S(m/2) + m`.

Theo Master Theorem:

`S(m) = Θ(m log m)`.

Thay `m = log n`:

`T(n) = Θ(log n · log log n)`.


</details>

### Bài 21. Truy hồi `T(√n) + 1`

**Đề bài.** Hãy xác định độ phức tạp của truy hồi:

`T(n) = T(√n) + 1`.

Có thể sử dụng phép đổi biến `m = log n`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = T(√n) + 1`.

Đặt `m = log n` và `S(m) = T(2^m)`, ta được:

`S(m) = S(m/2) + 1`.

Do đó:

`S(m) = Θ(log m)`,

nên:

`T(n) = Θ(log log n)`.


</details>

### Bài 22. Truy hồi `2T(√n) + 1`

**Đề bài.** Hãy xác định độ phức tạp của truy hồi:

`T(n) = 2T(√n) + 1`.

Có thể sử dụng phép đổi biến `m = log n` và Master Theorem trên truy hồi mới.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = 2T(√n) + 1`.

Với phép đổi biến `m = log n`:

`S(m) = 2S(m/2) + 1`.

Theo Master Theorem:

`S(m) = Θ(m)`.

Vì vậy:

`T(n) = Θ(log n)`.


</details>

### Bài 23. Hàm đệ quy trên `√n`

**Đề bài.** Hãy xác định độ phức tạp thời gian của hàm sau:

```python
import math

count = 0

def function(n):
    global count

    if n <= 2:
        return 1
    else:
        function(round(math.sqrt(n)))
        count = count + 1
        return count

print(function(200))
```

Thiết lập truy hồi thời gian và xác định số lần có thể liên tiếp lấy căn bậc hai trước khi đối số trở thành hằng số.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
import math

count = 0

def function(n):
    global count

    if n <= 2:
        return 1
    else:
        function(round(math.sqrt(n)))
        count = count + 1
        return count
```

Mỗi lời gọi chỉ tạo một lời gọi mới với kích thước xấp xỉ `√n`, nên:

`T(n) = T(√n) + Θ(1)`.

Do đó:

`T(n) = Θ(log log n)`.


</details>

### Bài 24. Tám lời gọi `n/2` và một vòng lặp bậc ba

**Đề bài.** Phân tích thời gian chạy của hàm đệ quy sau theo `n`:

```python
def function(n):
    if n < 2:
        return

    counter = 0

    for i in range(8):
        function(n / 2)

    for i in range(n ** 3):
        counter = counter + 1
```

Hãy thiết lập phương trình truy hồi và giải bằng Master Theorem.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Truy hồi:

`T(n) = 8T(n/2) + Θ(n³)`.

Vì `n^(log₂8) = n³`, đây là trường hợp cân bằng:

`T(n) = Θ(n³ log n)`.


</details>

## 7. Các bài toán vòng lặp và truy hồi tiếp theo

### Bài 25. Hai vòng tuyến tính lồng nhau

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
def function(n):
    for i in range(0, n // 3):
        j = 1

        while j <= n:
            j = j + 4
            print("*")

function(20)
```

Phân tích số lần thực hiện của từng vòng lặp.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    for i in range(0, n // 3):
        j = 1
        while j <= n:
            j = j + 4
            print("*")
```

Vòng ngoài chạy `Θ(n)` lần. Vòng trong tăng `j` thêm `4` nên cũng chạy `Θ(n)` lần.

Do đó:

`T(n) = Θ(n²)`.


</details>

### Bài 26. Hai lời gọi `n/2`

**Đề bài.** Hãy xác định độ phức tạp thời gian của hàm đệ quy sau:

```python
def function(n):
    if n <= 0:
        return

    print("*")
    function(n / 2)
    function(n / 2)
    print("*")

function(20)
```

Thiết lập phương trình truy hồi và giải bằng Master Theorem.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    if n <= 0:
        return

    print("*")
    function(n / 2)
    function(n / 2)
    print("*")
```

Truy hồi:

`T(n) = 2T(n/2) + Θ(1)`.

Theo Master Theorem:

`T(n) = Θ(n)`.


</details>

### Bài 27. Hai vòng logarithmic lồng nhau

**Đề bài.** Hãy xác định độ phức tạp thời gian của chương trình sau:

```python
count = 0

def logarithms(n):
    i = 1
    global count

    while i <= n:
        j = i

        while j > 0:
            j = j // 2
            count = count + 1

        i = i * 2

    return count

print(logarithms(10))
```

Cần tính tổng số lần thực hiện của vòng trong qua tất cả các giá trị của `i`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
count = 0

def logarithms(n):
    i = 1
    global count

    while i <= n:
        j = i

        while j > 0:
            j = j // 2
            count = count + 1

        i = i * 2

    return count
```

Giá trị `i` lần lượt là `1, 2, 4, ..., 2^k`, với `k = Θ(log n)`.

Ở mức `i = 2^r`, vòng trong chạy `Θ(r)` lần. Tổng chi phí:

```text
1 + 2 + ... + Θ(log n) = Θ(log² n)
```

Do đó:

`T(n) = Θ(log² n)`.


</details>

## 8. Các câu hỏi về ký hiệu tiệm cận

### Bài 28. Tổng của `n` số hạng `O(n)`

**Đề bài.** Xét biểu thức:

`Σ[i=1..n] O(n)`,

trong đó mỗi số hạng là một hàm có bậc `O(n)`. Hãy chọn cận trên phù hợp cho toàn bộ tổng:

A. `O(n)`  
B. `O(n²)`  
C. `O(n³)`  
D. `O(3n²)`  
E. `O(1.5n²)`

<details>
<summary><strong>Hiện lời giải</strong></summary>

Nếu:

`Σ[i=1..n] O(n)`,

thì có `n` số hạng, mỗi số hạng có cận `O(n)`. Vì vậy:

`Σ[i=1..n] O(n) = O(n²)`.

</details>

### Bài 29. Các mệnh đề đúng về Big-O

**Đề bài.** Xét ba mệnh đề sau, trong đó `k` và `m` là các hằng số:

I. `(n + k)^m = O(n^m)`  
II. `2^(n+1) = O(2^n)`  
III. `2^(2n+1) = O(2^n)`

Hãy xác định nhóm mệnh đề đúng:

A. I và II  
B. I và III  
C. II và III  
D. I, II và III

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét ba mệnh đề:

1. `(n+k)^m = O(n^m)`, với `k`, `m` là hằng số;
2. `2^(n+1) = O(2^n)`;
3. `2^(2n+1) = O(2^n)`.

Mệnh đề 1 đúng vì khi `n` lớn, `(n+k)^m` cùng bậc với `n^m`.

Mệnh đề 2 đúng vì:

`2^(n+1) = 2·2^n`.

Mệnh đề 3 sai vì:

`2^(2n+1) / 2^n = 2^(n+1) → ∞`.

Do đó, chỉ mệnh đề **I và II** đúng.

</details>

### Bài 30. So sánh `2^n`, `n!` và `n^(log n)`

**Đề bài.** Xét ba hàm:

```text
f(n) = 2^n
g(n) = n!
h(n) = n^(log n)
```

Mệnh đề nào sau đây mô tả đúng quan hệ tăng trưởng tiệm cận giữa ba hàm?

A. `f(n) = O(g(n))` và `g(n) = O(h(n))`  
B. `f(n) = Ω(g(n))` và `g(n) = O(h(n))`  
C. `g(n) = O(f(n))` và `h(n) = O(f(n))`  
D. `h(n) = O(f(n))` và `g(n) = Ω(f(n))`

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```text
f(n) = 2^n
g(n) = n!
h(n) = n^(log n)
```

Khi `n` đủ lớn:

`h(n) < f(n) < g(n)`.

Thật vậy:

```text
log h(n) = Θ((log n)²)
log f(n) = Θ(n)
log g(n) = Θ(n log n)
```

Do đó:

`h(n) = o(f(n))` và `f(n) = o(g(n))`.


</details>

### Bài 31. Số lần kiểm tra điều kiện trong vòng nhân đôi

**Đề bài.** Xét đoạn mã C sau:

```c
j = 1;
while (j <= n) {
    j = j * 2;
}
```

Với `n > 0`, hãy xác định:

1. số lần thực hiện thân vòng lặp;
2. số lần kiểm tra điều kiện `j <= n`.

Phân biệt rõ hai đại lượng này.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```c
j = 1;
while (j <= n) {
    j = j * 2;
}
```

Thân vòng lặp thực hiện `Θ(log n)` lần.

Nếu đếm **số lần thực hiện thân vòng lặp**, kết quả là `⌊log₂n⌋ + 1` với `n ≥ 1`.

Nếu đếm **số lần kiểm tra điều kiện `j <= n`**, cần cộng thêm lần kiểm tra cuối cùng thất bại.


</details>

### Bài 32. Kiểm tra số nguyên tố bằng thử chia đến `√n`

**Đề bài.** Xét hàm kiểm tra số nguyên tố:

```python
import math

def IsPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            print("Not Prime")
            return 0

    return 1
```

Mệnh đề nào sau đây đúng về độ phức tạp thời gian?

A. `T(n) = O(√n)` và `T(n) = Ω(√n)`  
B. `T(n) = O(√n)` và `T(n) = Ω(1)`  
C. `T(n) = O(√n)` và `T(n) = Ω(n)`  
D. Không có lựa chọn nào đúng

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
import math

def IsPrime(n):
    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            print("Not Prime")
            return 0

    return 1
```

Trong worst case, vòng lặp phải kiểm tra tới `Θ(√n)` giá trị, nên:

`T(n) = O(√n)`.

Trong best case, có thể phát hiện ước số ngay lập tức:

`T(n) = Ω(1)`.


</details>

### Bài 33. Thuật toán Euclid

**Đề bài.** Xét hàm Euclid tính ước chung lớn nhất:

```python
def gcd(m, n):
    if n % m == 0:
        return m

    m = n % m
    return gcd(m, n)
```

Hãy xác định phát biểu đúng về độ phức tạp thời gian của thuật toán và giải thích vì sao cận dưới logarithmic không nhất thiết đúng cho mọi input.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def gcd(m, n):
    if n % m == 0:
        return m
    m = n % m
    return gcd(m, n)
```

Độ phức tạp worst case của thuật toán Euclid là:

`O(log min(m,n))`.

Tuy nhiên, không thể khẳng định cận dưới chặt là `Ω(log m)` cho mọi input, vì có những trường hợp thuật toán kết thúc ngay sau một bước. Vì vậy, khi các lựa chọn chỉ đưa ra một cận dưới logarithmic bắt buộc cho mọi input, lựa chọn đó không chính xác.


</details>

### Bài 34. Nhận diện mệnh đề sai

**Đề bài.** Giả sử truy hồi:

`T(n) = 2T(n/2) + n`, với `T(0) = T(1) = 1`.

Mệnh đề nào sau đây là sai?

A. `T(n) = O(n²)`  
B. `T(n) = Θ(n log n)`  
C. `T(n) = Ω(n²)`  
D. `T(n) = O(n log n)`

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = 2T(n/2) + n`.

Theo Master Theorem:

`T(n) = Θ(n log n)`.

Do đó mọi mệnh đề cho rằng truy hồi này có cận chặt `Θ(n²)` là sai.


</details>

## 9. Phân tích vòng lặp nhiều tầng và lũy thừa

### Bài 35. Vòng lặp có điều kiện chia hết

**Đề bài.** Hãy xác định độ phức tạp thời gian chặt của hàm sau:

```python
def function(n):
    for i in range(1, n):
        j = i

        while j < i * i:
            j = j + 1

            if j % i == 0:
                for k in range(0, j):
                    print("*")

function(10)
```

Không chỉ đưa ra một cận trên thô; hãy phân tích tổng chi phí của vòng `for k` qua các giá trị của `j` và `i`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

```python
def function(n):
    for i in range(1, n):
        j = i

        while j < i * i:
            j = j + 1

            if j % i == 0:
                for k in range(0, j):
                    print("*")
```

Với mỗi `i`, vòng `while` chạy `Θ(i²)` lần. Tuy nhiên, vòng `for k` chỉ được thực hiện khi `j` là bội của `i`. Có `Θ(i)` giá trị như vậy trong đoạn từ `i` đến `i²`, và tổng chi phí của các vòng `for k` là:

```text
i(2 + 3 + ... + i) = Θ(i³)
```

Do đó chi phí cho một giá trị `i` là `Θ(i³)`, và tổng:

```text
Σ[i=1..n] Θ(i³) = Θ(n⁴)
```

Vì vậy, một phân tích chặt cho đoạn mã là:

`T(n) = Θ(n⁴)`.

Một cận thô hơn như `O(n⁵)` vẫn là cận trên đúng nhưng không chặt.


</details>

### Bài 36. Tính `9^n` bằng nhân lặp

**Đề bài.** Hãy thiết kế một thuật toán đơn giản để tính `9^n` bằng cách nhân lặp từ `1` và phân tích độ phức tạp thời gian của thuật toán đó.

<details>
<summary><strong>Hiện lời giải</strong></summary>


sử dụng `n` phép nhân, nên:

`T(n) = Θ(n)`.

Có thể cải thiện xuống `Θ(log n)` phép nhân bằng **fast exponentiation / exponentiation by squaring**.


</details>

### Bài 37. Cải thiện thuật toán tính lũy thừa

**Đề bài.** Với bài toán tính `9^n` ở Bài 58, hãy cải thiện độ phức tạp thời gian bằng kỹ thuật lũy thừa nhanh (*exponentiation by squaring*). Nêu ý tưởng và độ phức tạp của thuật toán cải tiến.

<details>
<summary><strong>Hiện lời giải</strong></summary>


Cách này giảm số phép nhân từ `Θ(n)` xuống:

`Θ(log n)`.


</details>

### Bài 38. Phân tích worst case của vòng lặp nhánh

**Đề bài.** Xét hàm sau:

```python
def function(n):
    sum = 0

    for i in range(0, n - 1):
        if i > j:
            sum = sum + 1
        else:
            for k in range(0, j):
                sum = sum - 1

    print(sum)

function(10)
```

Hãy phân tích độ phức tạp trong trường hợp xấu nhất. Đồng thời chỉ rõ rằng kết luận phụ thuộc vào giá trị hoặc miền giá trị của biến `j`, vốn chưa được xác định trong đoạn mã.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Trong worst case, nếu nhánh `else` được thực hiện `Θ(n)` lần và mỗi lần vòng trong chạy `Θ(n)` lần, thì:

`T(n) = Θ(n²)`.

Kết luận phụ thuộc vào giả thiết về `j`; vì vậy khi biến này không được xác định rõ, cần nêu điều kiện khi đưa ra độ phức tạp.


</details>

## 10. Recursion tree và các truy hồi có nhiều nhánh

### Bài 39. Truy hồi `T(n) = T(n/2) + T(2n/3) + n²`

**Đề bài.** Giải truy hồi sau bằng phương pháp cây đệ quy (*recursion tree*):

`T(n) = T(n/2) + T(2n/3) + n²`.

Hãy xác định lượng công việc tại từng mức và chứng minh cận `Θ` của tổng thời gian.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Xét:

`T(n) = T(n/2) + T(2n/3) + n²`.

Ở mức đầu tiên, chi phí ngoài đệ quy là `n²`.

Ở mức tiếp theo:

```text
(n/2)² + (2n/3)²
= (1/4 + 4/9)n²
= (25/36)n²
```

Ở mức `k`, tổng công việc bị chặn bởi:

`(25/36)^k n²`.

Vì `25/36 < 1`, tổng trên toàn bộ cây là một chuỗi hình học hội tụ:

```text
T(n) ≤ n² Σ[k≥0] (25/36)^k = Θ(n²)
```

Do đó:

`T(n) = Θ(n²)`.


</details>

### Bài 40. Truy hồi `T(n) = T(n/2) + T(n/4) + T(n/8) + n`

**Đề bài.** Xác định độ phức tạp của truy hồi:

`T(n) = T(n/2) + T(n/4) + T(n/8) + n`.

Có thể sử dụng phương pháp đoán và chứng minh hoặc recursion tree. Hãy giải thích vì sao tổng kích thước các bài toán con nhỏ hơn kích thước bài toán cha.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Tổng kích thước các bài toán con ở mỗi mức nhỏ hơn kích thước bài toán cha:

`n/2 + n/4 + n/8 = 7n/8`.

Do đó, tổng công việc theo các mức bị chặn bởi:

```text
n + (7/8)n + (7/8)²n + ...
```

Suy ra:

`T(n) = Θ(n)`.


</details>

## 11. Xếp hạng tốc độ tăng trưởng

### Bài 41. Sắp xếp các hàm theo thứ tự giảm dần

**Đề bài.** Sắp xếp các hàm sau theo thứ tự giảm dần về tốc độ tăng trưởng tiệm cận:

```text
(n + 1)!
n!
4^n
n·3^n
3^n + n^3 + 20n
3^n
(3/2)^n
4n²
4^(log n)
n² + 200
20n + 500
2^(log n)
n^(2/3)
1
```

Khi cần, hãy giả sử `log` có cơ số `2` và chỉ ra các hàm có cùng bậc tăng trưởng.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Khi `log` có cơ số `2`:

`4^(log₂n) = n²`

và:

`2^(log₂n) = n`.

Vì vậy, trong ký hiệu tiệm cận, một số hàm trong danh sách có cùng bậc.


</details>

### Bài 42. Có phải `3^(n^5) = O(3^n)`?

**Đề bài.** Xác định mệnh đề sau đúng hay sai và chứng minh:

`3^(n^5) = O(3^n)`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Khi `n → ∞`, tỷ số này tiến tới vô hạn. Do đó:

`3^(n^5) ∉ O(3^n)`.


</details>

### Bài 43. Có phải `3^n = O(2^n)`?

**Đề bài.** Xác định mệnh đề sau đúng hay sai và chứng minh:

`3^n = O(2^n)`.

<details>
<summary><strong>Hiện lời giải</strong></summary>

Do đó:

`3^n ∉ O(2^n)`.


</details>

## 12. Tóm tắt các kỹ thuật chính

Các dạng bài trong phần này có thể quy về một số kỹ thuật cốt lõi.

**Với vòng lặp**, cần xác định chính xác quy luật thay đổi của biến điều khiển. Nếu biến tăng tuyến tính, số vòng thường là `Θ(n)`; nếu nhân hoặc chia bởi một hằng số, số vòng thường là `Θ(log n)`; nếu biến tích lũy theo `1 + 2 + ... + k`, số vòng có thể là `Θ(√n)`.

**Với các vòng lặp lồng nhau**, không nên chỉ nhân số vòng lặp một cách máy móc. Khi số lần của vòng trong phụ thuộc vào biến của vòng ngoài, cần viết thành tổng và rút gọn tổng đó.

**Với đệ quy**, bước đầu tiên là thiết lập đúng phương trình truy hồi. Sau đó mới quyết định dùng Master Theorem, phép thế, đổi biến, recursion tree hay một công cụ khác.

**Với các truy hồi chứa `√n`**, phép đổi biến `m = log n` thường biến chúng thành truy hồi quen thuộc trên `m`.

**Với các câu hỏi Big-O, Big-Ω và Theta**, cần phân biệt cận đúng với cận chặt. Một biểu thức `O(n^5)` có thể đúng nhưng vẫn rất lỏng nếu độ phức tạp thực sự là `Θ(n^4)`.

**Với mã nguồn**, cần kiểm tra tính kết thúc trước khi phân tích độ phức tạp. Một vòng lặp có biến không thay đổi, chẳng hạn bước tăng bằng `0`, có thể không kết thúc.

---

## 13. Bài tập tự luyện

1. Phân tích `T(n) = 4T(n-1) - 3` với `T(0) = 1`.
2. Phân tích vòng lặp trong đó `i` tăng lần lượt thêm `1, 2, 3, ...`.
3. Giải `T(n) = 3T(n/3) + n log²n`.
4. Giải `T(n) = T(√n) + log log n`.
5. Phân tích `T(n) = 4T(√n) + log n` bằng phép đổi biến.
6. Dùng recursion tree để giải `T(n) = T(n/3) + T(2n/3) + n²`.
7. Chứng minh `Σ[i=1..n] log i = Θ(n log n)`.
8. Phân tích chặt đoạn mã có vòng ngoài `i = 1..n` và vòng trong chạy `n/i` lần.
9. So sánh `n!`, `2^n`, `n^(log n)` và `n^100`.
10. Giải thích sự khác biệt giữa một cận trên đúng và một cận chặt.