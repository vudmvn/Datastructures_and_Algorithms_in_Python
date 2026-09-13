# Bài tập và lời giải — Sorting, Selection và Searching

> **Phạm vi:** File này chỉ chọn các bài tập trong **Chương 10 (Sorting)** và **Chương 11 (Searching)** của *Data Structures and Algorithmic Thinking with Python* có nội dung trực tiếp liên quan đến hai phần bài giảng Lecture 4 đã cung cấp.
>
> Các chủ đề ngoài phạm vi hai phần bài giảng — ví dụ rotated sorted array, bitonic search, two-pointer cho pair-sum, các kỹ thuật đánh dấu mảng chuyên biệt, v.v. — **không được đưa vào**.
>
> Các phần **Lời giải / Gợi ý** được ẩn bằng thẻ `<details>`.

---

# Phần A. Sorting

## Bài 1. Tính ổn định của các thuật toán sắp xếp
*Phỏng theo Chương 10, Problem 12; chỉ giữ các thuật toán có trong bài giảng.*

Xét bốn thuật toán:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Giả sử hai bản ghi $R$ và $S$ có cùng khóa, và $R$ xuất hiện trước $S$ trong dữ liệu đầu vào.

1. Một thuật toán sắp xếp được gọi là **stable** khi nào?
2. Trong bốn thuật toán trên, thuật toán nào stable với cách cài đặt thông thường?
3. Vì sao Quick Sort có thể làm thay đổi thứ tự tương đối của hai bản ghi có cùng khóa?

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Một thuật toán sắp xếp là **stable** nếu các bản ghi có cùng khóa vẫn giữ nguyên thứ tự tương đối sau khi sắp xếp.

| Thuật toán | Stable? |
|---|---|
| Bubble Sort | Có |
| Insertion Sort | Có |
| Merge Sort | Có, nếu khi hai khóa bằng nhau ưu tiên phần tử ở nửa trái |
| Quick Sort | Thông thường không |

Quick Sort thực hiện các phép đổi chỗ trong quá trình partition. Hai bản ghi có cùng khóa có thể bị đổi thứ tự tương đối, nên cách cài đặt Quick Sort thông thường không stable.

</details>

---

## Bài 2. Thuật toán nào là in-place?
*Phỏng theo Chương 10, Problem 13; giới hạn theo các thuật toán trong bài giảng.*

Xét:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Hãy cho biết:

1. Thuật toán nào chỉ cần lượng nhỏ bộ nhớ phụ?
2. Thuật toán nào cần mảng phụ kích thước tỷ lệ với $n$?
3. So sánh auxiliary space của bốn thuật toán.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Với cách cài đặt trên mảng thường gặp:

| Thuật toán | Auxiliary space |
|---|---:|
| Bubble Sort | $\Theta(1)$ |
| Insertion Sort | $\Theta(1)$ |
| Merge Sort | $\Theta(n)$ |
| Quick Sort | khoảng $\Theta(\log n)$ expected cho recursion stack; có thể tới $\Theta(n)$ ở trường hợp xấu |

Bubble Sort và Insertion Sort rõ ràng là in-place.

Merge Sort trên mảng cần mảng phụ khi merge nên không in-place theo cách cài đặt chuẩn trong bài giảng.

Quick Sort partition trực tiếp trên mảng, nhưng vẫn cần recursion stack.

</details>

---

## Bài 3. So sánh worst-case complexity
*Phỏng theo Chương 10, Problem 49.*

Trong ba thuật toán sau:

- Merge Sort
- Bubble Sort
- Quick Sort

thuật toán nào có **worst-case time complexity thấp nhất**?

Giải thích dựa trên bảng độ phức tạp đã học.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Ta có:

$$
T_{\text{Merge}}(n)=\Theta(n\log n)
$$

trong cả best, average và worst case.

Trong khi đó:

$$
T_{\text{Bubble}}(n)=\Theta(n^2)
$$

ở worst case, và:

$$
T_{\text{Quick}}(n)=\Theta(n^2)
$$

ở worst case.

Vì vậy **Merge Sort** có worst-case complexity tốt nhất trong ba lựa chọn.

</details>

---

## Bài 4. Ảnh hưởng của cách chọn pivot trong Quick Sort
*Phỏng theo Chương 10, Problem 52.*

Một chương trình Quick Sort sắp xếp tăng dần và luôn chọn **phần tử đầu tiên** làm pivot.

Xét hai input:

```text
A = [1, 2, 3, 4, 5]
B = [4, 1, 5, 3, 2]
```

Gọi $t_1$ và $t_2$ là số phép so sánh của Quick Sort trên $A$ và $B$.

Hãy xác định quan hệ giữa $t_1$ và $t_2$ và giải thích.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Với $A$, mỗi pivot đều là phần tử nhỏ nhất của subarray hiện tại.

Các partition có dạng:

$$
0 \quad \text{và} \quad n-1.
$$

Sau đó tiếp tục:

$$
0 \quad \text{và} \quad n-2,
$$

v.v.

Đây là kiểu partition lệch nhất và dẫn đến worst case.

Input $B$ tạo các partition cân bằng hơn.

Do đó:

$$
\boxed{t_1>t_2}.
$$

</details>

---

## Bài 5. Recurrence của worst-case Quick Sort
*Phỏng theo Chương 10, Problem 56.*

Khi pivot luôn là phần tử nhỏ nhất hoặc lớn nhất của subarray, sau partition ta có:

- một subarray rỗng;
- pivot ở vị trí cuối cùng;
- một subarray có $n-1$ phần tử.

1. Viết recurrence cho thời gian chạy.
2. Giải recurrence để tìm asymptotic complexity.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Partition cần quét qua subarray nên tốn:

$$
\Theta(n).
$$

Recurrence:

$$
T(n)=T(n-1)+T(0)+cn.
$$

Bỏ các hằng số:

$$
T(n)=T(n-1)+\Theta(n).
$$

Khai triển:

$$
T(n)
=
\Theta(n+(n-1)+(n-2)+\cdots+1)
=
\Theta(n^2).
$$

Do đó worst case của Quick Sort là:

$$
\boxed{\Theta(n^2)}.
$$

</details>

---

## Bài 6. Các phần tử ngay sau median
*Phỏng theo Chương 10, Problem 11; liên hệ trực tiếp với phần Selection trong Lecture 4.*

Cho mảng $A$ gồm $n$ phần tử và một số nguyên $K<n/2$.

Hãy đề xuất cách xuất ra, theo thứ tự tăng dần, **$K$ phần tử đứng ngay sau median** trong thứ tự sắp xếp mà không cần sắp xếp toàn bộ mảng.

Mục tiêu:

$$
O(n+K\log K).
$$

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Ta không cần tạo toàn bộ thứ tự của $n$ phần tử.

Một hướng giải:

1. Tìm median bằng một thuật toán selection.
2. Partition mảng quanh median.
3. Xét phần chứa các phần tử lớn hơn median.
4. Dùng selection để cô lập $K$ phần tử nhỏ nhất trong phần này.
5. Chỉ sắp xếp $K$ phần tử cần xuất.

Chi phí selection và partition là tuyến tính theo $n$; sắp xếp phần kết quả cần:

$$
O(K\log K).
$$

Do đó tổng thời gian:

$$
\boxed{O(n+K\log K)}.
$$

Ý tưởng chính giống nguyên tắc trong bài giảng:

> Không sắp xếp nhiều hơn mức thứ tự mà output thực sự yêu cầu.

</details>

---

## Bài 7. Tìm đồng thời minimum và maximum
*Phỏng theo Chương 10, Problem 53; liên hệ với phần tìm extreme trong Lecture 4.*

Cho $n$ số phân biệt.

1. Nếu tìm minimum và maximum bằng hai lần quét độc lập, cần bao nhiêu phép so sánh?
2. Hãy thiết kế cách xử lý các phần tử theo từng cặp để giảm số phép so sánh.
3. Với $n=100$, phương pháp theo cặp cần bao nhiêu phép so sánh?

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Nếu tìm riêng:

- minimum cần $n-1$ phép so sánh;
- maximum cần $n-1$ phép so sánh.

Tổng:

$$
2n-2.
$$

### Xử lý theo cặp

Với hai phần tử $a,b$:

1. So sánh $a$ và $b$.
2. So sánh phần tử nhỏ hơn với `min`.
3. So sánh phần tử lớn hơn với `max`.

Sau khi dùng hai phần tử đầu để khởi tạo `min` và `max`, với $n$ chẵn số phép so sánh là:

$$
1+3\frac{n-2}{2}
=
\frac{3n}{2}-2.
$$

Với $n=100$:

$$
\frac{3(100)}{2}-2=148.
$$

Vì vậy:

$$
\boxed{148}
$$

phép so sánh.

> **Lưu ý về nguồn:** đáp án in trong bản sách cung cấp ghi 147 với công thức $\frac{3n}{2}-3$. Theo mô hình so sánh chuẩn và cách khởi tạo bằng hai phần tử đầu, kết quả đúng cho $n=100$ là 148.

</details>

---

# Phần B. Searching

## Bài 8. Kiểm tra phần tử lặp bằng brute force
*Chương 11, Problem 1.*

Cho mảng:

```text
A = [3, 2, 1, 2, 5, 3]
```

Hãy thiết kế thuật toán đơn giản để kiểm tra liệu mảng có chứa phần tử lặp hay không bằng cách so sánh các cặp phần tử.

Phân tích time complexity và auxiliary space.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Pseudocode:

```text
FOR i = 0 TO n - 2
    FOR j = i + 1 TO n - 1
        IF A[i] == A[j]
            RETURN TRUE

RETURN FALSE
```

Trong worst case phải xét:

$$
\frac{n(n-1)}{2}
$$

cặp.

Do đó:

$$
T(n)=\Theta(n^2),
\qquad
S(n)=\Theta(1).
$$

</details>

---

## Bài 9. Phát hiện duplicate bằng sorting
*Chương 11, Problem 2.*

Cải thiện Bài 8 bằng cách sử dụng kiến thức Sorting.

Hãy mô tả thuật toán và phân tích độ phức tạp.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Sau khi sort:

```text
A.sort()
```

các giá trị bằng nhau sẽ nằm cạnh nhau.

Chỉ cần một lần scan:

```text
FOR i = 0 TO n - 2
    IF A[i] == A[i + 1]
        RETURN TRUE

RETURN FALSE
```

Nếu dùng sorting algorithm có thời gian:

$$
O(n\log n),
$$

thì tổng thời gian là:

$$
O(n\log n)+O(n)
=
\boxed{O(n\log n)}.
$$

Bài này minh họa trực tiếp ý trong Lecture 4:

> Sorting thường không phải mục tiêu cuối cùng; nó tạo cấu trúc để thao tác tiếp theo dễ hơn.

</details>

---

## Bài 10. Phát hiện duplicate bằng hash set
*Chương 11, Problem 3.*

Giải lại bài toán duplicate bằng `set` hoặc hash table.

So sánh với hai cách ở Bài 8 và Bài 9.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Ví dụ Python:

```python
def has_duplicate(A):
    seen = set()

    for x in A:
        if x in seen:
            return True
        seen.add(x)

    return False
```

Với hash table:

- lookup expected:
  $$
  O(1);
  $$
- insert expected:
  $$
  O(1).
  $$

Với $n$ phần tử:

$$
T(n)=O(n)
$$

expected, nhưng cần:

$$
S(n)=O(n).
$$

So sánh:

| Cách | Time | Extra space |
|---|---:|---:|
| Brute force | $O(n^2)$ | $O(1)$ |
| Sort + scan | $O(n\log n)$ | phụ thuộc sort |
| Hash set | expected $O(n)$ | $O(n)$ |

Đây là trade-off giữa thời gian, bộ nhớ và cách tổ chức dữ liệu.

</details>

---

## Bài 11. First occurrence bằng Binary Search
*Chương 11, Problem 46.*

Cho mảng đã sắp xếp, có thể chứa duplicate:

```text
A = [2, 4, 4, 4, 4, 7, 9, 11]
```

Hãy tìm **index đầu tiên** của `4` trong:

$$
O(\log n)
$$

thời gian.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Khi tìm thấy `target`, không dừng ngay. Ta ghi nhớ vị trí và tiếp tục tìm bên trái.

```text
FUNCTION FIRST_OCCURRENCE(A, target)
    low = 0
    high = LENGTH(A) - 1
    answer = NONE

    WHILE low <= high
        mid = low + (high - low) DIV 2

        IF A[mid] >= target
            IF A[mid] == target
                answer = mid
            high = mid - 1
        ELSE
            low = mid + 1

    RETURN answer
```

Mỗi vòng lặp loại bỏ khoảng một nửa search interval:

$$
T(n)=\boxed{O(\log n)}.
$$

Với ví dụ trên, kết quả là index `1` nếu đánh số từ 0.

</details>

---

## Bài 12. Last occurrence bằng Binary Search
*Chương 11, Problem 47.*

Với:

```text
A = [2, 4, 4, 4, 4, 7, 9, 11]
```

hãy tìm **index cuối cùng** của `4` trong:

$$
O(\log n).
$$

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Khi tìm thấy `target`, ghi nhớ vị trí nhưng tiếp tục tìm bên phải.

```text
FUNCTION LAST_OCCURRENCE(A, target)
    low = 0
    high = LENGTH(A) - 1
    answer = NONE

    WHILE low <= high
        mid = low + (high - low) DIV 2

        IF A[mid] == target
            answer = mid
            low = mid + 1
        ELSE IF A[mid] < target
            low = mid + 1
        ELSE
            high = mid - 1

    RETURN answer
```

Độ phức tạp:

$$
\boxed{O(\log n)}.
$$

Kết quả của ví dụ là index `4`.

</details>

---

## Bài 13. Đếm số lần xuất hiện bằng hai Binary Search
*Phỏng theo Chương 11, Problems 48--50.*

Cho mảng đã sắp xếp:

```text
A = [1, 2, 2, 2, 2, 5, 8]
```

Hãy đếm số lần `target = 2` xuất hiện trong:

$$
O(\log n)
$$

thời gian.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Dùng hai kết quả:

- `first` = vị trí xuất hiện đầu tiên;
- `last` = vị trí xuất hiện cuối cùng.

Nếu không tìm thấy target:

```text
count = 0
```

Ngược lại:

$$
\text{count}
=
\text{last}-\text{first}+1.
$$

Trong ví dụ:

```text
first = 1
last  = 4
```

nên:

$$
\text{count}=4-1+1=4.
$$

Hai lần Binary Search vẫn chỉ tốn:

$$
O(\log n)+O(\log n)
=
\boxed{O(\log n)}.
$$

</details>

---

## Bài 14. Linear Search hay Binary Search?
*Phỏng theo Chương 11, Problem 81.*

So sánh:

- Linear Search trên 1000 phần tử bằng máy 5 GHz;
- Binary Search trên 1,000,000 phần tử bằng máy 1 GHz.

Giả sử đơn giản rằng mỗi phép so sánh tốn xấp xỉ một chu kỳ CPU.

1. Worst case của Linear Search cần bao nhiêu phép so sánh?
2. Worst case của Binary Search cần khoảng bao nhiêu phép so sánh?
3. Sau khi tính đến chênh lệch tốc độ CPU, phương án nào vẫn nhanh hơn?

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

### Linear Search

Worst case:

$$
1000
$$

phép so sánh.

Trên máy 5 GHz:

$$
t_L
\approx
\frac{1000}{5\times10^9}
=
2\times10^{-7}\text{ s}.
$$

### Binary Search

Số bước xấp xỉ:

$$
\lceil\log_2(1\,000\,000)\rceil
\approx 20.
$$

Trên máy 1 GHz:

$$
t_B
\approx
\frac{20}{10^9}
=
2\times10^{-8}\text{ s}.
$$

Do đó, theo mô hình đơn giản này:

$$
\frac{t_L}{t_B}
\approx 10.
$$

Binary Search trên **một triệu phần tử** vẫn nhanh hơn khoảng 10 lần trong worst-case comparison count, mặc dù chạy trên CPU có clock thấp hơn.

Bài tập minh họa khác biệt tăng trưởng:

$$
\Theta(n)
\quad \text{so với} \quad
\Theta(\log n).
$$

</details>

---

# Phần C. Tổng hợp đúng phạm vi hai bài giảng

## Bài 15. Chọn phương pháp dựa trên tổ chức dữ liệu

Với từng tình huống, hãy chọn phương pháp thích hợp nhất trong số:

- Linear Search
- Binary Search
- Sorting + scan
- Hash set
- Quickselect
- Merge Sort
- Quick Sort

### Tình huống

1. Chỉ cần tìm một phần tử trong một list chưa sắp xếp và chỉ truy vấn một lần.
2. Có một mảng đã sắp xếp và cần tìm target nhiều lần.
3. Cần kiểm tra duplicate, có thể dùng thêm $O(n)$ bộ nhớ.
4. Cần tìm median một lần mà không cần sorted output đầy đủ.
5. Cần worst-case $\Theta(n\log n)$ và stable sorting.
6. Muốn sorting in-place và chấp nhận worst-case $\Theta(n^2)$.

<details>
<summary><strong>Lời giải / Gợi ý</strong></summary>

Một lựa chọn hợp lý:

| Tình huống | Phương pháp |
|---|---|
| 1 | Linear Search |
| 2 | Binary Search |
| 3 | Hash set |
| 4 | Quickselect |
| 5 | Merge Sort |
| 6 | Quick Sort |

Cần luôn xét cả:

- input đã có thứ tự hay chưa;
- có cần stable hay không;
- có cần toàn bộ sorted order hay chỉ một rank;
- giới hạn bộ nhớ;
- số lượng truy vấn;
- worst-case guarantee.

</details>

---


