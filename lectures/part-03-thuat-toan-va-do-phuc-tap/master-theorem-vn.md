# Bài giảng: Master Theorem, Phương trình truy hồi và Phân tích khấu hao

**Cập nhật lần cuối:** 31 tháng 8 năm 2026

## 1. Mục tiêu học tập và kiến thức nền

Nhiều thuật toán đệ quy không thể được phân tích chỉ bằng cách đếm trực tiếp số vòng lặp. Thời gian chạy của chúng thường được mô tả bởi một **phương trình truy hồi** (*recurrence relation*), trong đó chi phí của bài toán kích thước `n` được biểu diễn thông qua chi phí của một hoặc nhiều bài toán con nhỏ hơn.

Sau bài học này, người học có thể:

- thiết lập phương trình truy hồi cho các thuật toán đệ quy và chia để trị;
- áp dụng Master Theorem cho truy hồi dạng `T(n) = aT(n/b) + f(n)`;
- sử dụng dạng mở rộng khi `f(n) = Θ(n^k log^p n)`;
- nhận biết các trường hợp Master Theorem không áp dụng được;
- phân tích các truy hồi subtract-and-conquer;
- sử dụng phương pháp đoán nghiệm và chứng minh bằng quy nạp;
- phân biệt amortized analysis với worst-case analysis và average-case analysis.

Kiến thức nền cần có gồm đệ quy, logarithm, ký hiệu tiệm cận `O`, `Ω`, `Θ`, tổng cấp số nhân, cây đệ quy và quy nạp toán học.

---

## 2. Từ thuật toán chia để trị đến phương trình truy hồi

Thuật toán chia để trị (*divide and conquer*) thường gồm ba bước:

1. **Divide:** chia bài toán ban đầu thành các bài toán con nhỏ hơn;
2. **Conquer:** giải các bài toán con, thường bằng đệ quy;
3. **Combine:** kết hợp lời giải của các bài toán con để tạo lời giải cho bài toán ban đầu.

Nếu một bài toán kích thước `n` được chia thành `a` bài toán con, mỗi bài toán con có kích thước khoảng `n/b`, và chi phí ngoài các lời gọi đệ quy là `f(n)`, thì thời gian chạy thường có dạng `T(n) = aT(n/b) + f(n)`.

Trong đó, `a` là số bài toán con, `n/b` là kích thước của mỗi bài toán con, và `f(n)` là chi phí để chia bài toán, kết hợp kết quả và thực hiện các công việc khác ngoài đệ quy.

### Ví dụ: Merge Sort

Merge Sort chia mảng kích thước `n` thành hai nửa, sắp xếp đệ quy từng nửa và hợp nhất hai dãy đã sắp xếp trong thời gian tuyến tính. Do đó, `T(n) = 2T(n/2) + Θ(n)`, và kết quả là `T(n) = Θ(n log n)`.

### Ví dụ: Binary Search

Binary Search chỉ tiếp tục trên một nửa của mảng và mỗi bước thực hiện một lượng công việc hằng số. Khi đó, `T(n) = T(n/2) + Θ(1)`, suy ra `T(n) = Θ(log n)`.

Phương trình truy hồi chỉ mô tả cấu trúc tự lặp của thuật toán. Mục tiêu của phân tích là xác định bậc tăng trưởng của `T(n)`. Các công cụ thường dùng gồm cây đệ quy, phép thế và chứng minh bằng quy nạp, Master Theorem, Akra–Bazzi theorem và phân tích trực tiếp bằng tổng.

---

## 3. Master Theorem cho divide-and-conquer recurrences

Xét truy hồi `T(n) = aT(n/b) + f(n)`, với `a ≥ 1`, `b > 1` và `f(n)` là hàm không âm đối với `n` đủ lớn.

Đại lượng quan trọng cần so sánh là `n^(log_b a)`. Đây là bậc tăng trưởng biểu thị tổng số lượng công việc do cấu trúc phân nhánh đệ quy tạo ra.

### Trường hợp 1: phần đệ quy chi phối

Nếu tồn tại `ε > 0` sao cho `f(n) = O(n^(log_b a - ε))`, thì `T(n) = Θ(n^(log_b a))`.

Trong trường hợp này, công việc sinh ra từ các lời gọi đệ quy chi phối tổng thời gian.

**Ví dụ.** Với `T(n) = 8T(n/2) + n²`, ta có `n^(log₂8) = n³`. Vì `n²` nhỏ hơn đa thức so với `n³`, suy ra `T(n) = Θ(n³)`.

### Trường hợp 2: hai thành phần cân bằng

Nếu `f(n) = Θ(n^(log_b a) log^k n)` với `k ≥ 0`, thì `T(n) = Θ(n^(log_b a) log^(k+1) n)`.

**Ví dụ.** Với `T(n) = 2T(n/2) + n`, ta có `n^(log₂2) = n`. Hai thành phần cùng bậc nên `T(n) = Θ(n log n)`.

### Trường hợp 3: phần công việc ngoài đệ quy chi phối

Nếu tồn tại `ε > 0` sao cho `f(n) = Ω(n^(log_b a + ε))` và thỏa điều kiện chính quy `a f(n/b) ≤ c f(n)` với một hằng số `c < 1` và `n` đủ lớn, thì `T(n) = Θ(f(n))`.

**Ví dụ.** Với `T(n) = 2T(n/2) + n²`, ta có `n^(log₂2) = n`, trong khi `f(n) = n²`. Điều kiện chính quy được thỏa mãn vì `2(n/2)² = n²/2`. Do đó `T(n) = Θ(n²)`.

---

## 4. Dạng mở rộng với `f(n) = Θ(n^k log^p n)`

Một dạng thường gặp trong bài tập là `T(n) = aT(n/b) + Θ(n^k log^p n)`, trong đó `a > 1`, `b > 1`, `k ≥ 0` và `p` là số thực.

Thay vì so sánh trực tiếp `f(n)` với `n^(log_b a)`, có thể so sánh `a` với `b^k`.

### Khi `a > b^k`

Phần đệ quy chi phối và `T(n) = Θ(n^(log_b a))`.

Ví dụ, với `T(n) = 3T(n/2) + n`, ta có `a = 3`, `b^k = 2`, nên `T(n) = Θ(n^(log₂3))`.

### Khi `a = b^k`

Đây là trường hợp cân bằng. Kết quả phụ thuộc vào `p`.

- Nếu `p > -1`, thì `T(n) = Θ(n^k log^(p+1) n)`.
- Nếu `p = -1`, thì `T(n) = Θ(n^k log log n)`.
- Nếu `p < -1`, thì `T(n) = Θ(n^k)`.

Các ví dụ tiêu biểu:

- `T(n) = 2T(n/2) + n log n` có nghiệm `Θ(n log² n)`;
- `T(n) = 2T(n/2) + n/log n` có nghiệm `Θ(n log log n)`;
- `T(n) = 2T(n/2) + n/log² n` có nghiệm `Θ(n)`.

### Khi `a < b^k`

Nếu `p ≥ 0`, phần công việc ngoài đệ quy chi phối và `T(n) = Θ(n^k log^p n)`.

Nếu `p < 0`, cận thường gặp là `O(n^k)`. Để kết luận bằng `Θ`, cần kiểm tra thêm các điều kiện cụ thể của truy hồi và định lý đang áp dụng.

### Bảng tóm tắt

| Điều kiện | Kết quả |
|---|---|
| `a > b^k` | `Θ(n^(log_b a))` |
| `a = b^k`, `p > -1` | `Θ(n^k log^(p+1) n)` |
| `a = b^k`, `p = -1` | `Θ(n^k log log n)` |
| `a = b^k`, `p < -1` | `Θ(n^k)` |
| `a < b^k`, `p ≥ 0` | `Θ(n^k log^p n)` |
| `a < b^k`, `p < 0` | thường có cận `O(n^k)`; cần kiểm tra thêm để kết luận cận chặt |

---

## 5. Quy trình áp dụng Master Theorem

Khi gặp truy hồi `T(n) = aT(n/b) + f(n)`, có thể thực hiện theo bốn bước.

**Bước 1. Xác định `a`, `b` và `f(n)`.** Ví dụ, với `T(n) = 4T(n/2) + n²`, ta có `a = 4`, `b = 2` và `f(n) = n²`.

**Bước 2. Tính `n^(log_b a)`.** Trong ví dụ trên, `n^(log₂4) = n²`.

**Bước 3. So sánh `f(n)` với `n^(log_b a)`.** Hai hàm cùng bậc, do đó thuộc trường hợp cân bằng.

**Bước 4. Kết luận.** Vì `f(n) = Θ(n²)`, suy ra `T(n) = Θ(n² log n)`.

Một lỗi phổ biến là chỉ nhìn vào số lượng bài toán con mà bỏ qua `f(n)`. Một lỗi khác là áp dụng Master Theorem khi `a` không phải hằng số, kích thước các bài toán con không đồng đều hoặc `f(n)` không thỏa các điều kiện cần thiết.

---

## 6. Các ví dụ Master Theorem tiêu biểu

Bảng sau tổng hợp một số truy hồi điển hình.

| Bài | Truy hồi | Kết quả | Nhận xét |
|---|---|---|---|
| 1 | `T(n) = 3T(n/2) + n²` | `Θ(n²)` | Phần ngoài đệ quy chi phối |
| 2 | `T(n) = 4T(n/2) + n²` | `Θ(n² log n)` | Trường hợp cân bằng |
| 3 | `T(n) = T(n/2) + n²` | `Θ(n²)` | Phần ngoài đệ quy chi phối |
| 4 | `T(n) = 2^n T(n/2) + n^n` | Không áp dụng trực tiếp | `a` không phải hằng số |
| 5 | `T(n) = 16T(n/4) + n` | `Θ(n²)` | Phần đệ quy chi phối |
| 6 | `T(n) = 2T(n/2) + n log n` | `Θ(n log² n)` | Cân bằng với `p = 1` |
| 7 | `T(n) = 2T(n/2) + n/log n` | `Θ(n log log n)` | Trường hợp biên `p = -1` |
| 8 | `T(n) = 2T(n/4) + n^0.51` | `Θ(n^0.51)` | Phần ngoài đệ quy chi phối |
| 9 | `T(n) = 0.5T(n/2) + 1/n` | Không áp dụng dạng chuẩn | `a < 1` |
| 10 | `T(n) = 6T(n/3) + n² log n` | `Θ(n² log n)` | Phần ngoài đệ quy chi phối |
| 11 | `T(n) = 64T(n/8) - n² log n` | Không áp dụng trực tiếp | `f(n)` không dương |
| 12 | `T(n) = 7T(n/3) + n²` | `Θ(n²)` | Phần ngoài đệ quy chi phối |
| 13 | `T(n) = 4T(n/2) + log n` | `Θ(n²)` | Phần đệ quy chi phối |
| 14 | `T(n) = 16T(n/4) + n!` | `Θ(n!)` dưới điều kiện chính quy phù hợp | Không thuộc dạng đa thức-log |
| 15 | `T(n) = √2 T(n/2) + log n` | `Θ(√n)` | Phần đệ quy chi phối |
| 16 | `T(n) = 3T(n/2) + n` | `Θ(n^(log₂3))` | Phần đệ quy chi phối |
| 17 | `T(n) = 3T(n/3) + √n` | `Θ(n)` | Phần đệ quy chi phối |
| 18 | `T(n) = 4T(n/2) + cn` | `Θ(n²)` | Phần đệ quy chi phối |
| 19 | `T(n) = 3T(n/4) + n log n` | `Θ(n log n)` | Phần ngoài đệ quy chi phối |
| 20 | `T(n) = 3T(n/3) + n/2` | `Θ(n log n)` | Trường hợp cân bằng |

### Phân tích một số ví dụ

**Ví dụ 1.** Với `T(n) = 3T(n/2) + n²`, ta có `n^(log₂3) ≈ n^1.585`. Vì `n²` lớn hơn đa thức so với `n^1.585`, phần công việc ngoài đệ quy chi phối. Kết quả là `Θ(n²)`.

**Ví dụ 2.** Với `T(n) = 4T(n/2) + n²`, ta có `n^(log₂4) = n²`. Hai thành phần cân bằng, nên xuất hiện thêm một thừa số `log n`, cho kết quả `Θ(n² log n)`.

**Ví dụ 6.** Với `T(n) = 2T(n/2) + n log n`, ta có `a = 2`, `b = 2`, `k = 1` và `p = 1`. Vì `a = b^k`, kết quả là `Θ(n log² n)`.

**Ví dụ 7.** Với `T(n) = 2T(n/2) + n/log n`, ta có `p = -1`. Đây là trường hợp biên đặc biệt, dẫn đến `Θ(n log log n)`.

**Ví dụ 16.** Với `T(n) = 3T(n/2) + n`, ta có `a = 3 > 2 = b^k`; do đó phần đệ quy chi phối và `T(n) = Θ(n^(log₂3))`.

---

## 7. Khi nào Master Theorem không áp dụng được?

Master Theorem rất hữu ích nhưng không phải là công cụ tổng quát cho mọi truy hồi. Một số trường hợp không thể áp dụng trực tiếp gồm:

- số lượng bài toán con phụ thuộc vào `n`, chẳng hạn `2^n T(n/2)`;
- các bài toán con có kích thước không đồng nhất, chẳng hạn `T(n/3) + T(2n/3) + n`;
- kích thước bài toán con không có dạng `n/b`;
- hệ số trước lời gọi đệ quy nhỏ hơn `1` trong dạng chuẩn;
- `f(n)` âm hoặc không thỏa điều kiện chính quy;
- truy hồi chứa nhiều kiểu giảm kích thước khác nhau;
- truy hồi có dạng `T(n-1)`, `T(n-2)` hoặc một dạng subtract-and-conquer.

Trong các trường hợp này, có thể sử dụng cây đệ quy, phép đổi biến, substitution, Akra–Bazzi hoặc phân tích trực tiếp.

---

## 8. Master Theorem cho subtract-and-conquer recurrences

Không phải mọi thuật toán đệ quy đều chia kích thước bài toán theo một tỷ lệ. Trong subtract-and-conquer, kích thước thường giảm đi một lượng cố định.

Xét truy hồi `T(n) = aT(n-b) + f(n)`, với `a > 0`, `b > 0`, và giả sử `f(n) = O(n^k)`.

Một số cận trên thường dùng là:

| Điều kiện | Cận trên |
|---|---|
| `a < 1` | `O(n^k)` |
| `a = 1` | `O(n^(k+1))` |
| `a > 1` | `O(n^k a^(n/b))` |

### Ví dụ 1

Với `T(n) = T(n-1) + 1`, mỗi bước giảm `n` đi `1`, nên có khoảng `n` mức đệ quy. Kết quả là `T(n) = Θ(n)`.

### Ví dụ 2

Với `T(n) = T(n-1) + n`, khai triển cho `T(n) = n + (n-1) + ... + 1 = Θ(n²)`.

### Ví dụ 3

Với `T(n) = 2T(n-1) + 1`, số lời gọi đệ quy tăng theo cấp số nhân, dẫn đến `T(n) = Θ(2^n)`.

### Một biến thể phân chia không đều

Xét `T(n) = T(αn) + T((1-α)n) + βn`, với `0 < α < 1` và `β > 0`. Dưới các giả thiết thông thường, truy hồi này có bậc `Θ(n log n)`.

---

## 9. Phương pháp đoán nghiệm và chứng minh bằng quy nạp

Khi truy hồi không phù hợp với Master Theorem, một phương pháp quan trọng là:

> **Đoán dạng của nghiệm, sau đó chứng minh bằng quy nạp.**

Quy trình gồm bốn bước:

1. quan sát truy hồi và dự đoán bậc tăng trưởng;
2. giả sử giả thuyết đúng với các bài toán con;
3. thay giả thuyết vào truy hồi;
4. kiểm tra xem bất đẳng thức cần chứng minh có đúng với `n` đủ lớn hay không.

Nếu chứng minh thất bại, điều đó không nhất thiết có nghĩa là nghiệm đoán hoàn toàn sai; đôi khi cần thay đổi hằng số, bổ sung số hạng hiệu chỉnh hoặc chọn một dạng giả thuyết mạnh hơn.

### Ví dụ: `T(n) = √n T(√n) + n`

Truy hồi này không thuộc dạng Master Theorem chuẩn vì số lượng bài toán con là `√n`, không phải một hằng số.

Một cách phân tích thuận tiện là chia hai vế cho `n`. Đặt `U(n) = T(n)/n`. Khi đó `U(n) = U(√n) + 1`.

Mỗi lần áp dụng truy hồi, đối số biến đổi theo chuỗi `n → √n → n^(1/4) → n^(1/8) → ...`.

Sau `k` bước, kích thước còn `n^(1/2^k)`. Quá trình dừng khi giá trị này trở thành hằng số, tức là khi `2^k = Θ(log n)`. Do đó `k = Θ(log log n)`.

Mỗi mức đóng góp `Θ(1)` vào `U(n)`, nên `U(n) = Θ(log log n)`. Suy ra `T(n) = Θ(n log log n)`.

### Vì sao một số dự đoán thất bại?

Nếu đoán `T(n) = Θ(n log n)`, cận này quá lớn. Nếu đoán `Θ(n)`, cận này quá nhỏ. Các dạng trung gian như `Θ(n√log n)` cũng không phù hợp. Dạng `Θ(n log log n)` phản ánh đúng số lần có thể lấy căn bậc hai trước khi kích thước bài toán trở thành hằng số.

---

## 10. Phân tích khấu hao — Amortized Analysis

Amortized analysis nghiên cứu **chi phí trung bình trên một chuỗi thao tác**, nhưng không dựa trên giả định xác suất về input.

Cần phân biệt ba khái niệm:

- **Worst-case analysis:** xét chi phí lớn nhất của một thao tác riêng lẻ;
- **Average-case analysis:** xét kỳ vọng dựa trên một phân phối xác suất của input;
- **Amortized analysis:** xét tổng chi phí của một chuỗi thao tác trong trường hợp xấu nhất rồi phân bổ chi phí đó cho các thao tác trong chuỗi.

Vì vậy, amortized analysis vẫn cung cấp một worst-case guarantee cho toàn bộ chuỗi thao tác.

### Động cơ của phân tích khấu hao

Một số cấu trúc dữ liệu có đặc điểm rằng phần lớn thao tác rất rẻ, một số ít thao tác có thể rất đắt, và các thao tác đắt chỉ xảy ra hiếm khi. Trong những trường hợp như vậy, chỉ nhìn worst-case của từng thao tác có thể cho một cận quá bi quan.

### Ví dụ: dynamic array

Giả sử một dynamic array tăng gấp đôi dung lượng khi đầy.

Phần lớn thao tác `append` có chi phí `O(1)`. Tuy nhiên, khi mảng đầy, cần cấp phát vùng nhớ mới và sao chép toàn bộ phần tử cũ, nên một thao tác đơn lẻ có thể tốn `O(n)`.

Nếu bắt đầu từ dung lượng `1`, tổng số phần tử được sao chép trong các lần mở rộng là `1 + 2 + 4 + 8 + ... < 2n`.

Vì vậy, thực hiện `n` thao tác `append` có tổng chi phí `O(n)`, và chi phí khấu hao mỗi thao tác là `O(1)`.

Điều này không có nghĩa mọi thao tác `append` đều có worst-case `O(1)`; nó có nghĩa tổng chi phí của một chuỗi `n` thao tác append là `O(n)`.

---

## 11. Ba phương pháp phân tích khấu hao

### Phương pháp tổng hợp — Aggregate Method

Phương pháp aggregate tính trực tiếp tổng chi phí của `m` thao tác, sau đó chia cho `m`.

Nếu tổng chi phí là `T(m)`, thì chi phí khấu hao mỗi thao tác là `T(m)/m`.

Ví dụ, nếu `m` thao tác trên dynamic array có tổng chi phí `O(m)`, thì chi phí khấu hao mỗi thao tác là `O(1)`.

### Phương pháp kế toán — Accounting Method

Phương pháp accounting gán cho mỗi thao tác một **chi phí nhân tạo** (*amortized cost*). Một số thao tác có thể bị tính cao hơn chi phí thực tế; phần chênh lệch được coi như tín dụng để thanh toán cho các thao tác đắt trong tương lai.

Yêu cầu quan trọng là tổng tín dụng tích lũy không được âm.

### Phương pháp thế năng — Potential Method

Phương pháp potential gán cho trạng thái dữ liệu một hàm thế năng `Φ`.

Chi phí khấu hao của thao tác thứ `i` được định nghĩa bởi `ĉ_i = c_i + Φ(D_i) - Φ(D_(i-1))`, trong đó `c_i` là chi phí thực tế, `D_i` là trạng thái sau thao tác thứ `i`, và `Φ(D_i)` là thế năng của trạng thái mới.

Nếu `Φ(D_0) = 0` và `Φ(D_i) ≥ 0`, thì tổng chi phí thực tế không vượt quá tổng chi phí khấu hao.

---

## 12. Ví dụ về amortized analysis

### Ví dụ 1: sắp xếp một lần, truy vấn nhiều lần

Giả sử có `n` phần tử và cần thực hiện `n` truy vấn tìm phần tử nhỏ thứ `k`.

Nếu sắp xếp trước với chi phí `O(n log n)`, mỗi truy vấn sau đó có thể trả lời trong `O(1)`.

Tổng chi phí của `n` truy vấn là `O(n log n) + O(n) = O(n log n)`.

Do đó, chi phí trung bình trên mỗi truy vấn, nếu tính cả chi phí tiền xử lý, là `O(log n)`.

Ví dụ này minh họa nguyên tắc rằng một thao tác đắt ban đầu có thể làm giảm đáng kể chi phí của nhiều thao tác sau.

### Ví dụ 2: Stack với MultiPop

Giả sử stack hỗ trợ ba thao tác: thêm một phần tử, xóa một phần tử, và `MultiPop(k)` để xóa tối đa `k` phần tử.

Một thao tác `MultiPop(k)` riêng lẻ có thể tốn `O(k)`, nhưng mỗi phần tử chỉ có thể bị xóa một lần. Trong một chuỗi `m` thao tác, tổng số lần pop không thể vượt quá tổng số lần push.

Do đó, tổng chi phí của cả chuỗi là `O(m)`, và chi phí khấu hao mỗi thao tác là `O(1)`.

---

## 13. Bài tập thực hành

### Bài 1

Giải truy hồi `T(n) = 8T(n/2) + n²` bằng Master Theorem.

### Bài 2

Giải truy hồi `T(n) = 2T(n/2) + n log² n`.

### Bài 3

Giải truy hồi `T(n) = 2T(n/2) + n/log n`.

### Bài 4

Giải truy hồi `T(n) = 4T(n/2) + log n`.

### Bài 5

Giải truy hồi `T(n) = T(n-1) + n`.

### Bài 6

Phân tích truy hồi `T(n) = √n T(√n) + n`.

### Bài 7

Giải thích vì sao `T(n) = T(n/3) + T(2n/3) + n` không áp dụng trực tiếp Master Theorem chuẩn.

### Bài 8

Một dynamic array tăng gấp đôi dung lượng mỗi khi đầy. Chứng minh rằng `n` thao tác append có tổng chi phí `O(n)`.

### Bài 9

Một stack hỗ trợ `Push`, `Pop` và `MultiPop(k)`. Chứng minh chi phí khấu hao mỗi thao tác là `O(1)`.

### Bài 10

Phân biệt ba khái niệm worst-case complexity, average-case complexity và amortized complexity bằng các ví dụ thích hợp.

---

## 14. Quiz tự kiểm tra

1. Với truy hồi `T(n) = 4T(n/2) + n²`, kết quả là:

   A. `Θ(n²)`  
   B. `Θ(n² log n)`  
   C. `Θ(n³)`  
   D. `Θ(n log n)`

2. Với `T(n) = 2T(n/2) + n/log n`, kết quả là:

   A. `Θ(n)`  
   B. `Θ(n log n)`  
   C. `Θ(n log log n)`  
   D. `Θ(n log² n)`

3. Truy hồi nào sau đây không thuộc dạng Master Theorem chuẩn?

   A. `2T(n/2) + n`  
   B. `4T(n/2) + n²`  
   C. `T(n/3) + T(2n/3) + n`  
   D. `8T(n/2) + n³`

4. Với `T(n) = T(n-1) + n`, độ phức tạp là:

   A. `Θ(n)`  
   B. `Θ(n log n)`  
   C. `Θ(n²)`  
   D. `Θ(2^n)`

5. Amortized analysis:

   A. luôn dựa trên phân phối xác suất của input;  
   B. xét chi phí trung bình trên một chuỗi thao tác trong trường hợp xấu nhất;  
   C. chỉ áp dụng cho sorting;  
   D. giống hoàn toàn average-case analysis.

6. Một thao tác append của dynamic array có worst-case `O(n)` nhưng amortized cost `O(1)` vì:

   A. resize không bao giờ xảy ra;  
   B. resize xảy ra hiếm và tổng số phần tử được sao chép qua nhiều lần resize là tuyến tính;  
   C. mọi thao tác đều có chi phí hằng số;  
   D. dynamic array không sử dụng bộ nhớ phụ.

7. Với `T(n) = √n T(√n) + n`, kết quả là:

   A. `Θ(n)`  
   B. `Θ(n log n)`  
   C. `Θ(n log log n)`  
   D. `Θ(n²)`

8. Phương pháp accounting trong amortized analysis:

   A. gán một chi phí nhân tạo cho mỗi thao tác;  
   B. yêu cầu mọi thao tác có cùng chi phí thực tế;  
   C. luôn sử dụng xác suất;  
   D. chỉ dùng cho graph.

<details>
<summary><strong>Đáp án Quiz</strong></summary>

| Câu | Đáp án |
|---:|:---:|
| 1 | B |
| 2 | C |
| 3 | C |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | C |
| 8 | A |

</details>

---

## 15. Tóm tắt

Các điểm chính của bài học:

- Thuật toán chia để trị thường dẫn tới truy hồi dạng `T(n) = aT(n/b) + f(n)`.
- Master Theorem xác định độ phức tạp bằng cách so sánh `f(n)` với `n^(log_b a)`.
- Dạng mở rộng `f(n) = Θ(n^k log^p n)` cho phép xử lý nhiều truy hồi có chứa logarithm.
- Không phải mọi truy hồi đều phù hợp với Master Theorem; cần nhận biết các trường hợp có hệ số không hằng, kích thước bài toán con không đồng đều hoặc dạng subtract-and-conquer.
- Phương pháp đoán và chứng minh bằng quy nạp là công cụ quan trọng khi không có định lý áp dụng trực tiếp.
- Amortized analysis đánh giá chi phí trung bình trên một chuỗi thao tác mà không giả định phân phối xác suất của input.
- Aggregate, accounting và potential là ba phương pháp chuẩn của amortized analysis.
- Một thao tác riêng lẻ có thể rất đắt nhưng chi phí khấu hao vẫn nhỏ nếu thao tác đắt xảy ra hiếm và chi phí được phân bổ trên toàn bộ chuỗi thao tác.