---
title: "Bài giảng: Độ phức tạp thuật toán và Ký hiệu tiệm cận"
course: "Data Structures and Algorithms"
language: "vi"
version: "1.0"
---

# Bài giảng: Độ phức tạp thuật toán và Ký hiệu tiệm cận

## 1. Mục tiêu học tập

Sau bài học này, người học có thể:

1. Định nghĩa và giải thích ý nghĩa của phân tích tiệm cận (*asymptotic analysis*).
2. Phân biệt được ba ký hiệu tiệm cận phổ biến: Big $O$ (Chặn trên), Big $\Omega$ (Chặn dưới), và Big $\Theta$ (Chặn chặt).
3. Sử dụng thành thạo các quy tắc toán học (quy tắc cộng, quy tắc nhân) để tính độ phức tạp thời gian cho các đoạn code có vòng lặp đơn, vòng lặp lồng nhau và tuần tự.
4. Thiết lập hệ thức truy hồi cho thuật toán đệ quy và giải quyết bằng phương pháp cây đệ quy hoặc định lý Master (*Master Theorem*).
5. Phân biệt rõ ràng giữa **Độ phức tạp bộ nhớ** (*Space Complexity*) và **Bộ nhớ phụ trợ** (*Auxiliary Space*).

---

## 2. Vì sao cần Phân tích Tiệm cận?

Trong Bài 1, chúng ta đã biết rằng thời gian chạy bằng giây của một chương trình phụ thuộc rất nhiều vào cấu hình phần cứng, ngôn ngữ lập trình và trình biên dịch. Để đánh giá thuật toán một cách khách quan và độc lập với máy móc, chúng ta sử dụng **Phân tích Tiệm cận** (*Asymptotic Analysis*).

> **Ý tưởng cốt lõi:** Phân tích tiệm cận tập trung vào cách thức thời gian chạy (hoặc bộ nhớ) của thuật toán tăng lên khi kích thước đầu vào ($n$) tiến dần tới vô cùng lớn ($n \to \infty$).

Khi $n$ rất lớn, các hằng số hoặc các số hạng bậc thấp trở nên không đáng kể. 

Ví dụ, nếu một thuật toán thực hiện $f(n) = 3n^2 + 5n + 100$ phép tính:
- Khi $n = 10$: $f(10) = 300 + 50 + 100 = 450$ (số hạng $100$ đóng góp đáng kể).
- Khi $n = 10,000$: $f(10,000) = 300,000,000 + 50,000 + 100 \approx 3 \times 10^8$ (phần $5n + 100$ chỉ chiếm chưa đầy $0.02\%$ tổng số phép tính).

Do đó, ta nói tốc độ tăng trưởng của thuật toán này tỉ lệ với $n^2$.

---

## 3. Ba Ký hiệu Tiệm cận Cơ bản

Để mô tả mối quan hệ toán học giữa kích thước đầu vào và lượng tài nguyên tiêu thụ, ta sử dụng các ký hiệu tiệm cận: $O$, $\Omega$, và $\Theta$.

```text
  Tài nguyên (y)
      |         f(n) = O(g(n))  [Chặn trên - Trầm trọng nhất]
      |         f(n) = Θ(g(n))  [Chặn chặt - Trung bình]
      |         f(n) = Ω(g(n))  [Chặn dưới - Tốt nhất]
      +------------------------------> Kích thước đầu vào n (x)
```

### 3.1. Ký hiệu Big $O$ (Chặn trên - *Upper Bound*)

Ký hiệu Big $O$ (đọc là "Big Oh") mô tả trường hợp xấu nhất (*worst-case scenario*). Nó đưa ra giới hạn trên cho tốc độ tăng trưởng của thuật toán: thời gian chạy thực tế sẽ không bao giờ vượt quá mức này.

*   **Định nghĩa toán học:** $f(n) = O(g(n))$ nếu tồn tại các hằng số dương $c$ và $n_0$ sao cho:
    $$0 \le f(n) \le c \cdot g(n) \quad \text{với mọi } n \ge n_0$$

*   **Ý nghĩa:** Thuật toán chạy nhanh hơn hoặc bằng tốc độ của $g(n)$ khi đầu vào đủ lớn.
*   **Ví dụ:** Tìm kiếm tuyến tính có độ phức tạp trường hợp xấu nhất là $O(n)$ (phải duyệt hết mảng).

### 3.2. Ký hiệu Big $\Omega$ (Chặn dưới - *Lower Bound*)

Ký hiệu Big $\Omega$ (đọc là "Big Omega") mô tả trường hợp tốt nhất (*best-case scenario*). Nó đưa ra giới hạn dưới: thuật toán chắc chắn cần ít nhất chừng này bước để hoàn thành.

*   **Định nghĩa toán học:** $f(n) = \Omega(g(n))$ nếu tồn tại các hằng số dương $c$ và $n_0$ sao cho:
    $$0 \le c \cdot g(n) \le f(n) \quad \text{với mọi } n \ge n_0$$

*   **Ý nghĩa:** Thuật toán chạy chậm hơn hoặc bằng tốc độ của $g(n)$ trong mọi tình huống khi đầu vào đủ lớn.
*   **Ví dụ:** Dù mảng có kích thước bao nhiêu, thuật toán sắp xếp dựa trên so sánh luôn cần ít nhất $\Omega(n \log n)$ phép so sánh trong trường hợp xấu nhất.

### 3.3. Ký hiệu Big $\Theta$ (Chặn chặt - *Tight Bound*)

Ký hiệu Big $\Theta$ (đọc là "Big Theta") mô tả trường hợp trung bình hoặc mô tả chính xác tốc độ tăng trưởng của thuật toán khi giới hạn trên và giới hạn dưới trùng nhau.

*   **Định nghĩa toán học:** $f(n) = \Theta(g(n))$ nếu tồn tại các hằng số dương $c_1, c_2$ và $n_0$ sao cho:
    $$0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \text{với mọi } n \ge n_0$$

*   **Ý nghĩa:** $f(n) = \Theta(g(n))$ khi và chỉ khi $f(n) = O(g(n))$ và $f(n) = \Omega(g(n))$.
*   **Ví dụ:** Duyệt qua toàn bộ mảng có kích thước $n$ để in các phần tử luôn tốn chính xác $\Theta(n)$ bước.

---

## 4. Các Quy tắc Tính Độ phức tạp Thời gian

Khi phân tích một chương trình, bạn có thể áp dụng các quy tắc đơn giản sau để rút gọn biểu thức Big $O$.

### 4.1. Quy tắc cộng (Tuần tự)
Nếu chương trình gồm hai khối lệnh chạy tuần tự độc lập: Khối lệnh 1 tốn $O(f(n))$, Khối lệnh 2 tốn $O(g(n))$, thì tổng độ phức tạp là:
$$T(n) = O(f(n) + g(n)) = O(\max(f(n), g(n)))$$

**Ví dụ:**
```python
# Đoạn code 1: O(n)
for i in range(n):
    print(i)

# Đoạn code 2: O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)
```
Tổng thời gian là $O(n + n^2) = O(n^2)$.

### 4.2. Quy tắc nhân (Lồng nhau)
Nếu một vòng lặp ngoài chạy $f(n)$ lần, bên trong chứa một vòng lặp chạy $g(n)$ lần, thì độ phức tạp tổng cộng là:
$$T(n) = O(f(n) \times g(n))$$

**Ví dụ:**
```python
# Vòng lặp ngoài chạy n lần, vòng lặp trong chạy m lần
for i in range(n):
    for j in range(m):
        # công việc O(1)
        sum += i * j
```
Độ phức tạp thời gian là $O(n \times m)$. Nếu $n = m$, độ phức tạp sẽ là $O(n^2)$.

---

## 5. Phân tích các Cấu trúc Vòng lặp Kinh điển

### 5.1. Vòng lặp tăng/giảm tuyến tính: $O(n)$
```python
i = 0
while i < n:
    # công việc O(1)
    i += 2  # Hoặc i += c với c là hằng số
```
Vòng lặp thực hiện khoảng $n / 2$ bước. Vì hằng số $1/2$ bị bỏ qua, độ phức tạp là $O(n)$.

### 5.2. Vòng lặp nhân/chia lũy thừa: $O(\log n)$
```python
i = 1
while i < n:
    # công việc O(1)
    i *= 2  # Hoặc i *= c
```
Giá trị của `i` qua các bước: $1, 2, 4, 8, \dots, 2^k$. Vòng lặp dừng khi $2^k \ge n \implies k \ge \log_2 n$. Số bước thực hiện tỉ lệ với $\log n$.

```python
i = n
while i > 0:
    # công việc O(1)
    i //= 2
```
Tương tự, giá trị của `i` bị chia đôi liên tục cho đến khi bằng 0. Độ phức tạp là $O(\log n)$.

### 5.3. Vòng lặp lồng nhau dạng tam giác: $O(n^2)$
```python
for i in range(n):
    for j in range(i, n):
        # công việc O(1)
        print(i, j)
```
- Khi $i = 0$, vòng trong chạy $n$ lần.
- Khi $i = 1$, vòng trong chạy $n-1$ lần.
- ...
- Khi $i = n-1$, vòng trong chạy $1$ lần.

Tổng số lần lặp:
$$S = n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2} = \frac{1}{2}n^2 + \frac{1}{2}n$$
Bỏ qua hằng số và số hạng bậc thấp, độ phức tạp thời gian là $O(n^2)$.

---

## 6. Phân tích Đệ quy và Định lý Master

Khi một hàm tự gọi lại chính nó, chúng ta không thể đếm vòng lặp thông thường mà phải thiết lập **hệ thức truy hồi** (*recurrence relation*).

### 6.1. Ví dụ hệ thức truy hồi của Tìm kiếm Nhị phân
Mỗi lần gọi đệ quy, ta chia đôi kích thước mảng và thực hiện một lượng công việc không đổi ($O(1)$) để so sánh phần tử giữa:
$$T(n) = T\left(\frac{n}{2}\right) + c$$
Sử dụng phương pháp cây đệ quy hoặc phân tích, ta thu được độ phức tạp $O(\log n)$.

### 6.2. Định lý Master (Master Theorem)
Định lý Master là công cụ cực kỳ mạnh mẽ để giải nhanh các hệ thức truy hồi dạng chia để trị:
$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$
Trong đó:
*   $a \ge 1$ là số lượng nhánh đệ quy con.
*   $b > 1$ là hệ số chia nhỏ kích thước đầu vào.
*   $f(n)$ là công việc thực hiện ở bước chia và gộp kết quả.

Để tìm độ phức tạp, ta so sánh hàm $f(n)$ với biểu thức $n^{\log_b a}$:

| Trường hợp | Điều kiện | Độ phức tạp $T(n)$ | Ví dụ |
| :--- | :--- | :--- | :--- |
| **Trường hợp 1** | $f(n) < n^{\log_b a}$ (đệ quy chiếm ưu thế) | $T(n) = \Theta(n^{\log_b a})$ | $T(n) = 8T(n/2) + n^2 \implies \Theta(n^3)$ |
| **Trường hợp 2** | $f(n) = \Theta(n^{\log_b a})$ (cân bằng) | $T(n) = \Theta(n^{\log_b a} \log n)$ | $T(n) = 2T(n/2) + n \implies \Theta(n \log n)$ (Merge Sort) |
| **Trường hợp 3** | $f(n) > n^{\log_b a}$ (gộp chiếm ưu thế)* | $T(n) = \Theta(f(n))$ | $T(n) = 2T(n/2) + n^2 \implies \Theta(n^2)$ |

*\*Lưu ý đối với Trường hợp 3: Cần thỏa mãn điều kiện đều đặn (regularity condition): $a \cdot f(n/b) \le c \cdot f(n)$ với hằng số $c < 1$.*

---

## 7. Phân tích Độ phức tạp Bộ nhớ (Space Complexity)

Độ phức tạp bộ nhớ đánh giá tổng lượng bộ nhớ mà thuật toán cần dùng để chạy hoàn tất, bao gồm cả dữ liệu đầu vào. Tuy nhiên, trong phân tích giải thuật, chúng ta thường quan tâm hơn đến **Bộ nhớ phụ trợ** (*Auxiliary Space*).

*   **Bộ nhớ phụ trợ (Auxiliary Space):** Lượng bộ nhớ bổ sung hoặc tạm thời mà thuật toán tự khởi tạo (biến phụ, mảng động phụ trợ, stack đệ quy).
*   **Độ phức tạp bộ nhớ (Space Complexity):** Bằng Bộ nhớ đầu vào + Bộ nhớ phụ trợ.

### 7.1. Ví dụ về Bộ nhớ phụ trợ $O(1)$
```python
def swap(a, b):
    temp = a  # Cần thêm 1 ô nhớ cố định
    a = b
    b = temp
```
Lượng bộ nhớ không thay đổi bất kể giá trị đầu vào lớn bao nhiêu $\implies$ Auxiliary Space: $O(1)$.

### 7.2. Bộ nhớ đệ quy (Stack Frame)
Khi hàm đệ quy được gọi, hệ thống phải lưu các tham số và địa chỉ quay lui vào **Call Stack**. Độ sâu lớn nhất của cây đệ quy chính là lượng bộ nhớ phụ trợ tiêu thụ.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
Hàm `factorial(n)` gọi đệ quy tuyến tính $n$ lần trước khi chạm tới điều kiện cơ sở. Call stack sẽ chứa đồng thời $n$ khung hàm (stack frames).
$$\implies \text{Auxiliary Space: } O(n)$$

---

## 8. Các lỗi tư duy thường gặp

1.  **Nhầm lẫn giữa $O(1)$ và "Không có vòng lặp":** Một đoạn lệnh không chứa vòng lặp nào nhưng gọi các hàm thư viện bên trong (ví dụ: `list.sort()` trong Python) vẫn có độ phức tạp tùy thuộc vào hàm thư viện đó ($O(n \log n)$).
2.  **Coi hằng số là biến số:** Vòng lặp chạy cố định $1,000,000$ lần luôn có độ phức tạp thời gian là $O(1)$ chứ không phải $O(n)$, vì số bước không đổi khi kích thước đầu vào thay đổi.
3.  **Bỏ qua bộ nhớ Call Stack trong đệ quy:** Nhiều người cho rằng hàm tính Giai thừa đệ quy ở phần 7.2 có độ phức tạp bộ nhớ là $O(1)$ vì chỉ sử dụng các phép nhân số nguyên. Thực tế là call stack của đệ quy chiếm dụng $O(n)$ không gian bộ nhớ.

---

## 9. Câu hỏi ôn tập

1.  Định nghĩa ý nghĩa của $O(g(n))$, $\Omega(g(n))$ và $\Theta(g(n))$. Tại sao Big $O$ lại là ký hiệu được lập trình viên sử dụng nhiều nhất?
2.  Một thuật toán chạy mất $100n^2$ bước và một thuật toán khác chạy mất $2^n$ bước. Với giá trị nào của $n$ thì thuật toán thứ hai bắt đầu chạy chậm hơn thuật toán thứ nhất?
3.  Hệ thức truy hồi sau đây mô tả thuật toán nào và độ phức tạp của nó là bao nhiêu?
    $$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$
4.  Điểm khác biệt chính giữa Space Complexity và Auxiliary Space là gì? Khi so sánh hai thuật toán sắp xếp, ta nên dùng tiêu chí nào?

---

## 10. Bài tập thực hành

### Bài 1 — Phân tích thời gian đoạn code sau:
```python
def print_patterns(n):
    i = n
    while i > 0:
        for j in range(i):
            print(j)
        i = i // 2
```
*Hướng dẫn giải:* 
- Vòng lặp ngoài chia đôi `i` sau mỗi bước: $i = n, n/2, n/4, \dots$
- Vòng lặp trong chạy `i` lần.
- Tổng số bước: $n + n/2 + n/4 + n/8 + \dots \le 2n$.
- Do đó, độ phức tạp thời gian là $O(n)$ chứ không phải $O(n \log n)$ hay $O(n^2)$.

### Bài 2 — Sử dụng Định lý Master để tìm độ phức tạp:
Giải hệ thức truy hồi sau:
$$T(n) = 4T\left(\frac{n}{2}\right) + n$$
*Hướng dẫn giải:*
- So sánh các hệ số: $a = 4, b = 2, f(n) = n$.
- Tính $n^{\log_b a} = n^{\log_2 4} = n^2$.
- Vì $f(n) = n < n^2$, ta rơi vào **Trường hợp 1** của Định lý Master.
- Kết luận: $T(n) = \Theta(n^2)$.

### Bài 3 — Phân tích độ phức tạp bộ nhớ và bộ nhớ phụ trợ:
Đánh giá thuật toán tạo mảng cộng dồn từ mảng gốc:
```python
def prefix_sums(arr):
    n = len(arr)
    result = [0] * n
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        result[i] = current_sum
    return result
```
*Hướng dẫn giải:*
- Thuật toán nhận vào mảng kích thước $n$.
- Khởi tạo thêm mảng `result` kích thước $n$ để trả về kết quả.
- Độ phức tạp bộ nhớ tổng cộng (Space Complexity) là $O(n) + O(n) = O(n)$.
- Bộ nhớ phụ trợ cần thiết (Auxiliary Space) để thực hiện tính toán là $O(n)$ (mảng kết quả mới tạo thêm).

---

## 11. Tài liệu tham khảo gợi ý

1.  *Introduction to Algorithms* (CLRS) - Chương 3: Growth of Functions & Chương 4: Divide-and-Conquer.
2.  GeeksforGeeks: *Analysis of Algorithms* (https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/).
