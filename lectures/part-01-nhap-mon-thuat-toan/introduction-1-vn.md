---
title: "Bài giảng: Giới thiệu Thuật toán và Phân tích Độ phức tạp"
course: "Data Structures and Algorithmic Thinking with Python"
language: "vi"
version: "1.3"
---

# Bài giảng: Giới thiệu Thuật toán và Phân tích Độ phức tạp

**Cập nhật lần cuối:** 3 tháng 8 năm 2026

## 1. Mục tiêu và kiến thức nền

Bài học này giới thiệu các khái niệm nền tảng nhất trước khi đi sâu vào cấu trúc dữ liệu và thuật toán. Mục tiêu không chỉ là hiểu một thuật toán hoạt động như thế nào, mà còn biết cách **so sánh các thuật toán**, đánh giá thuật toán nào phù hợp hơn khi kích thước dữ liệu tăng lên.

Sau bài học, người học có thể:

- Giải thích được mối quan hệ giữa **biến, kiểu dữ liệu, cấu trúc dữ liệu và kiểu dữ liệu trừu tượng**.
- Nêu được định nghĩa và các đặc trưng cơ bản của một thuật toán.
- Giải thích vì sao cần phân tích thuật toán.
- Xác định kích thước input phù hợp cho từng bài toán.
- So sánh tốc độ tăng trưởng của các hàm thường gặp.
- Phân biệt **best case, average case và worst case**.
- Dùng đúng các ký hiệu tiệm cận `O`, `Ω` và `Θ`.
- Phân tích được các đoạn code đơn giản chứa vòng lặp, vòng lặp lồng nhau, câu lệnh nối tiếp, điều kiện và vòng lặp logarit.
- Sử dụng các công thức logarit và tổng cơ bản trong phân tích độ phức tạp.

Các kiến thức cần có trước khi học:

- Biến, phép gán và biểu thức.
- `if`, `for`, `while`.
- Hàm và lời gọi hàm.
- Mảng/list cơ bản.
- Lũy thừa và logarit ở mức nhập môn.

---

## 2. Từ biến và kiểu dữ liệu đến cấu trúc dữ liệu và ADT

Trong toán học, ta thường viết các phương trình như `x² + 2y − 2 = 1`. Ở đây, `x` và `y` là các tên đại diện cho một giá trị nào đó. Trong lập trình, biến cũng có vai trò tương tự: tên biến là một **placeholder** dùng để biểu diễn dữ liệu.

Ví dụ:

```python
x = 10
y = 25
total = x + y
```

Tên biến không phải bản thân dữ liệu, mà là cách để ta truy cập và thao tác với dữ liệu.

Một biến không thể nhận mọi loại giá trị theo cách giống nhau. Ta cần biết dữ liệu thuộc loại nào:

- số nguyên,
- số thực,
- ký tự,
- chuỗi,
- giá trị logic,
- hoặc một kiểu dữ liệu do người dùng định nghĩa.

Ví dụ:

```python
age = 20 # int
price = 19.95 # float
name = "Minh" # str
is_valid = True # bool
```

Kiểu dữ liệu quyết định:

- miền giá trị có thể biểu diễn;
- lượng bộ nhớ cần dùng;
- những phép toán nào hợp lệ.

Một kiểu nguyên 16 bit có thể biểu diễn ít giá trị hơn kiểu nguyên 32 bit. Tuy nhiên, trong Python, số nguyên có thể tự mở rộng kích thước theo nhu cầu và không bị giới hạn cố định như các kiểu nguyên chuẩn trong C/C++.

Ngoài các kiểu có sẵn, ta có thể xây dựng kiểu dữ liệu do người dùng định nghĩa:

```python
class NewType:
 def __init__(self, data1, data2, data3):
 self.data1 = data1
 self.data2 = data2
 self.data3 = data3
```

Việc tự định nghĩa kiểu dữ liệu giúp mô hình hóa những đối tượng phức tạp hơn trong bài toán.

Khi dữ liệu ngày càng nhiều, ta cần một cơ chế tổ chức dữ liệu để việc truy cập và xử lý hiệu quả hơn. Đó là vai trò của **cấu trúc dữ liệu**.

Một cấu trúc dữ liệu là cách tổ chức và lưu trữ dữ liệu trong bộ nhớ sao cho dữ liệu có thể được sử dụng hiệu quả.


Một **ADT — Abstract Data Type** mô tả một cấu trúc dữ liệu thông qua:

1. tập dữ liệu được quản lý;
2. tập các phép toán được phép thực hiện.

ADT chỉ mô tả **cái gì có thể làm**, không quy định chi tiết **làm bằng cách nào**.


> **ADT mô tả giao diện và hành vi; cấu trúc dữ liệu cụ thể mô tả cách cài đặt.**

## Kiểu dữ liệu trừu tượng và các cấu trúc dữ liệu phổ biến

Một **kiểu dữ liệu trừu tượng** (*Abstract Data Type — ADT*) là một mô hình toán học hoặc mô hình logic mô tả:

1. **Tập các đối tượng dữ liệu** được quản lý;
2. **Tập các phép toán** có thể thực hiện trên các đối tượng đó;
3. **Hành vi mong đợi** của từng phép toán.

ADT tập trung vào câu hỏi:

> **Cấu trúc này cung cấp những thao tác nào và các thao tác đó phải hoạt động như thế nào?**

ADT không quy định trực tiếp dữ liệu được lưu trữ trong bộ nhớ ra sao hoặc thuật toán nào được sử dụng để thực hiện từng phép toán.

Ngược lại, một **cấu trúc dữ liệu cụ thể** (*data structure implementation*) xác định cách dữ liệu thực sự được tổ chức trong bộ nhớ và cách các thao tác của ADT được hiện thực.

Ví dụ, Stack ADT định nghĩa nguyên tắc **Last-In, First-Out — LIFO** và thường cung cấp các phép toán như `push`, `pop` và `top`. Tuy nhiên, Stack có thể được cài đặt bằng:

- mảng tĩnh;
- mảng động;
- linked list.

Các cách cài đặt này đều cung cấp cùng giao diện của Stack ADT nhưng có thể khác nhau về chi phí thời gian, bộ nhớ và cách quản lý dung lượng.

Có thể tóm tắt mối quan hệ như sau:

> **ADT xác định dữ liệu có thể được sử dụng như thế nào; cấu trúc dữ liệu xác định dữ liệu được tổ chức và xử lý trong bộ nhớ như thế nào.**

---

## Các ADT và cấu trúc dữ liệu phổ biến

Các cấu trúc dữ liệu thường gặp bao gồm:

- Array / Dynamic Array
- Linked List
- Stack
- Queue
- Deque
- Priority Queue
- Binary Tree
- Binary Search Tree
- Heap
- Dictionary / Map
- Hash Table
- Set
- Graph
- Disjoint Set / Union-Find

Mỗi cấu trúc phù hợp với những loại thao tác và dạng bài toán khác nhau.

<p align="center">
  <img src="images/image-5.png" alt="alt text" width="800" />
</p>
## So sánh các thao tác thường gặp giữa các cấu trúc dữ liệu

Ký hiệu:

- **✓**: thao tác được hỗ trợ trực tiếp và là một trong những chức năng điển hình của cấu trúc dữ liệu;
- **△**: có thể thực hiện nhưng không phải thao tác cốt lõi hoặc có thể không hiệu quả;
- **—**: không được hỗ trợ trực tiếp hoặc không phù hợp với bản chất của cấu trúc dữ liệu.

| Thao tác | Mô tả ngắn | Array | Linked List | Stack | Queue | Deque | Priority Queue / Heap | BST | Hash Table / Map | Set | Graph | Union-Find |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Truy cập theo chỉ số | Lấy phần tử ở vị trí `i` | ✓ | △ | — | — | △ | △ | — | — | — | — | — |
| Duyệt tuần tự | Truy cập lần lượt các phần tử | ✓ | ✓ | △ | △ | ✓ | △ | ✓ | ✓ | ✓ | ✓ | △ |
| Tìm kiếm theo giá trị | Kiểm tra một giá trị có tồn tại hay không | △ | △ | △ | △ | △ | △ | ✓ | ✓ | ✓ | △ | — |
| Chèn phần tử | Thêm một phần tử mới | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ |
| Xóa phần tử | Loại bỏ một phần tử | △ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Thêm/xóa ở đầu | Thao tác tại đầu cấu trúc | △ | ✓ | — | ✓ | ✓ | — | — | — | — | — | — |
| Thêm/xóa ở cuối | Thao tác tại cuối cấu trúc | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — |
| Lấy phần tử ưu tiên cao nhất | Lấy phần tử nhỏ nhất hoặc lớn nhất theo tiêu chí ưu tiên | △ | △ | — | — | — | ✓ | ✓ | △ | △ | — | — |
| Tra cứu theo khóa | Lấy giá trị tương ứng với một khóa | — | — | — | — | — | — | ✓ | ✓ | △ | △ | — |
| Kiểm tra membership | Kiểm tra một phần tử có thuộc cấu trúc hay không | △ | △ | △ | △ | △ | △ | ✓ | ✓ | ✓ | △ | — |
| Tìm phần tử nhỏ nhất/lớn nhất | Xác định phần tử cực trị | △ | △ | — | — | — | ✓ | ✓ | △ | △ | — | — |
| Tìm predecessor/successor | Tìm phần tử liền trước hoặc liền sau theo thứ tự | — | — | — | — | — | — | ✓ | — | △ | — | — |
| Duyệt BFS | Mở rộng theo từng mức | — | — | — | ✓ | ✓ | — | — | — | — | ✓ | — |
| Duyệt DFS | Đi sâu trước khi quay lui | — | — | ✓ | — | △ | — | — | — | — | ✓ | — |
| Biểu diễn quan hệ giữa các đối tượng | Lưu các node và quan hệ giữa chúng | △ | △ | — | — | — | — | ✓ | △ | △ | ✓ | — |
| Hợp nhất hai thành phần | Gộp hai nhóm phần tử rời nhau | — | — | — | — | — | — | — | — | △ | △ | ✓ |
| Kiểm tra hai phần tử có cùng nhóm | Xác định hai phần tử có thuộc cùng một thành phần hay không | — | — | — | — | — | — | — | — | △ | △ | ✓ |
---


## Mối liên hệ với Data Science, AI, Machine Learning và Operations Research

Các cấu trúc dữ liệu không chỉ là nội dung nền tảng của lập trình mà còn là thành phần cốt lõi của nhiều thuật toán trong Data Science, AI, Machine Learning và Operations Research. Mối liên hệ giữa cấu trúc dữ liệu và thuật toán thường xuất phát từ loại thao tác cần được thực hiện với tần suất cao nhất.

Trong Data Science, Array, Matrix, Dictionary và Set thường được dùng để biểu diễn bảng dữ liệu, vector đặc trưng, thống kê tần suất và tập giá trị phân biệt. Trong Machine Learning, Tree là nền tảng của Decision Tree, Random Forest và Gradient Boosted Trees; Heap có thể duy trì các ứng viên tốt nhất; Hash Table hỗ trợ xử lý đặc trưng thưa và dữ liệu categorical. Trong Deep Learning, tensor là dạng mở rộng nhiều chiều của array, còn graph được dùng để biểu diễn computational graph hoặc dữ liệu có quan hệ.

Trong AI, lựa chọn cấu trúc dữ liệu ảnh hưởng trực tiếp đến chiến lược tìm kiếm. BFS sử dụng Queue để mở rộng trạng thái theo từng mức; DFS và backtracking sử dụng Stack; A* và uniform-cost search sử dụng Priority Queue để chọn trạng thái có giá trị ưu tiên tốt nhất. Với các bài toán constraint satisfaction, stack hoặc các cấu trúc lưu trạng thái hỗ trợ quá trình thử, phát hiện mâu thuẫn và quay lui.

Trong Operations Research, Graph là mô hình tự nhiên cho shortest path, flow, routing, assignment, scheduling và network design. Priority Queue xuất hiện trong Dijkstra, label-setting algorithms, event simulation và branch-and-bound; Union-Find được sử dụng trong Kruskal và các bài toán connectivity; Array, Matrix và Hash Table thường được dùng để lưu trạng thái của dynamic programming hoặc các thông tin tạm thời trong heuristic và metaheuristic. Trong simulation, Queue biểu diễn các đối tượng chờ phục vụ, còn Priority Queue quản lý thứ tự các sự kiện theo thời gian xảy ra.

Điểm cốt lõi là:

> **Không có một cấu trúc dữ liệu tốt nhất cho mọi bài toán. Cấu trúc phù hợp là cấu trúc hỗ trợ hiệu quả nhất cho các thao tác chi phối của thuật toán đang xét.**

---

## 3. Khái niệm thuật toán và nhu cầu phân tích thuật toán

Hãy xét một công việc đời thường: làm món trứng tráng.

Một quy trình có thể là:

```text
1. Lấy chảo.
2. Lấy dầu.
3. Nếu không còn dầu:
 - đi mua dầu;
 - quay lại bếp.
4. Đổ dầu vào chảo.
5. Bật bếp.
6. Đập trứng và nấu.
7. Kết thúc.
```

Đây là một quy trình từng bước để đạt được một mục tiêu.

Một **thuật toán** là một dãy hữu hạn các bước được mô tả rõ ràng và không mơ hồ nhằm giải quyết một bài toán hoặc thực hiện một phép tính.

Khi học thuật toán, ta không chỉ quan tâm:

> Thuật toán có cho ra đáp án đúng không?

Mà còn phải quan tâm:

> Thuật toán cần bao nhiêu thời gian và bao nhiêu bộ nhớ?

Cùng một bài toán có thể được giải bằng nhiều thuật toán khác nhau. Có thể hình dung tương tự việc di chuyển từ thành phố A đến thành phố B bằng nhiều phương tiện khác nhau; các phương án đều đạt cùng mục tiêu nhưng khác nhau về thời gian, chi phí và mức độ khả thi.

Trong tính toán, tính đúng đắn là điều kiện cần nhưng chưa đủ; hiệu quả về thời gian, bộ nhớ và khả năng mở rộng cũng là các tiêu chí quan trọng khi lựa chọn thuật toán.

---

## 4. Mục tiêu phân tích thuật toán và xác định kích thước input

Mục tiêu của **phân tích thuật toán** là đánh giá và so sánh các thuật toán theo các tiêu chí tài nguyên, chủ yếu gồm:

- thời gian chạy;
- bộ nhớ sử dụng;
- đôi khi còn theo các tài nguyên khác.

Trong phạm vi bài này, trọng tâm được đặt vào **thời gian chạy** (*running time*).

Phân tích thời gian chạy xem xét câu hỏi:

> Khi kích thước input tăng lên, thời gian xử lý tăng theo quy luật nào?

Việc xác định đúng **kích thước input** là điều kiện cần để biểu diễn độ phức tạp một cách chính xác.

| Bài toán | Kích thước input thường dùng |
|---|---|
| Mảng | số phần tử `n` |
| Đa thức | bậc của đa thức |
| Ma trận | số phần tử hoặc số hàng/cột |
| Số nguyên rất lớn | số bit hoặc số chữ số |
| Đồ thị | số đỉnh `V` và số cạnh `E` |

Không phải mọi bài toán đều được mô tả đầy đủ bởi một tham số duy nhất `n`.

Ví dụ:

```text
Graph algorithm → thường cần biểu diễn theo V và E
Matrix algorithm → có thể cần biểu diễn theo r và c
```

Nếu ta chọn sai kích thước input, kết luận về độ phức tạp có thể trở nên không rõ ràng hoặc gây hiểu nhầm.

---

## 5. So sánh thuật toán và tốc độ tăng trưởng

Có nhiều tiêu chí để so sánh thuật toán, tuy nhiên một số tiêu chí không phản ánh tốt khả năng mở rộng theo kích thước input.

### Hạn chế của việc chỉ sử dụng thời gian thực nghiệm

Thời gian thực tế phụ thuộc vào:

- CPU,
- RAM,
- ngôn ngữ lập trình,
- compiler/interpreter,
- hệ điều hành,
- thư viện,
- dữ liệu cụ thể.

Do đó, nói:

```text
Thuật toán A mất 0.2 giây.
```

chưa đủ để kết luận A tốt hơn B một cách tổng quát.

### Hạn chế của việc sử dụng số dòng mã nguồn

Một chương trình ít dòng hơn chưa chắc nhanh hơn.

Ví dụ:

```python
result = sorted(arr)
```

chỉ có một dòng, nhưng bên trong vẫn có cả một thuật toán sắp xếp.

### So sánh thông qua tốc độ tăng trưởng

Thời gian chạy có thể được mô tả bằng một hàm của kích thước input, ký hiệu là `T(n)`. Ví dụ, có thể gặp `T₁(n) = n`, `T₂(n) = n log n` hoặc `T₃(n) = n²`.

Khi `n` tăng rất lớn, bậc tăng trưởng quan trọng hơn hằng số.

Ví dụ, với `T(n) = n⁴ + 2n² + 100n + 500`, khi `n` lớn thì `n⁴` chi phối hoàn toàn các số hạng còn lại. Do đó, `T(n) = Θ(n⁴)`.

Trong phân tích tiệm cận, các hệ số hằng và các số hạng bậc thấp thường được lược bỏ, do không quyết định bậc tăng trưởng khi kích thước input đủ lớn:

```text
3n + 20 → Θ(n)
7n² + 5n + 100 → Θ(n²)
100n log n + n → Θ(n log n)
```

---

## 6. Các bậc tăng trưởng thường gặp

Các bậc tăng trưởng phổ biến:

| Độ phức tạp | Tên gọi | Ví dụ |
|---|---|---|
| `Θ(1)` | Hằng số | truy cập phần tử theo chỉ số |
| `Θ(log n)` | Logarit | binary search |
| `Θ(n)` | Tuyến tính | duyệt một mảng |
| `Θ(n log n)` | Tuyến tính-logarit | merge sort |
| `Θ(n²)` | Bậc hai | xét mọi cặp phần tử |
| `Θ(n³)` | Bậc ba | ba vòng lặp độc lập |
| `Θ(2^n)` | Mũ | duyệt các tập con theo mô hình nhị phân |
| `Θ(n!)` | Giai thừa | duyệt mọi hoán vị |

Thứ tự tăng trưởng điển hình, từ chậm đến nhanh, được biểu diễn như sau:

<p align="center">
  <img src="images/image-4.png" alt="alt text" width="800" />
</p>

Một số quan hệ cần chú ý là `2^(log₂ n) = n` và `log(n!) = Θ(n log n)`.

Các hàm có tốc độ tăng trưởng lớn hơn thường dẫn đến khả năng mở rộng kém hơn khi kích thước input tăng.

---

## 7. Best case, average case và worst case

Thời gian chạy của một thuật toán có thể khác nhau đáng kể giữa các input có cùng kích thước.

Vì vậy, phân tích thường xét ba trường hợp: tốt nhất, trung bình và xấu nhất.

### Worst case

Trường hợp xấu nhất (*worst case*) là lớp input có cùng kích thước làm cực đại hóa chi phí thực hiện của thuật toán.

Ví dụ với linear search:

```python
def linear_search(arr, target):
 for i, x in enumerate(arr):
 if x == target:
 return i
 return -1
```

Worst case xảy ra khi:

- `target` nằm ở cuối mảng;
- hoặc không tồn tại trong mảng.

Số phép so sánh là `n`, do đó **worst case có độ phức tạp `Θ(n)`**.

### Best case

Trường hợp tốt nhất (*best case*) là lớp input có cùng kích thước làm cực tiểu hóa chi phí thực hiện của thuật toán.

Với linear search, nếu phần tử cần tìm nằm ngay vị trí đầu tiên thì **best case có độ phức tạp `Θ(1)`**.

### Average case

Trường hợp trung bình (*average case*) mô tả kỳ vọng về chi phí thực hiện dưới một phân phối xác suất xác định trên tập input.

Giá trị average case không thể được suy ra đơn giản bằng cách lấy trung bình số học giữa best case và worst case.

Ta phải mô tả input được sinh như thế nào.

Ví dụ, nếu target chắc chắn tồn tại và có xác suất bằng nhau ở mỗi vị trí, số so sánh trung bình là:

```text
(1 + 2 + ... + n) / n
= (n + 1) / 2
= Θ(n)
```

Một cách khái quát, ta có quan hệ `Lower Bound ≤ Average Time ≤ Upper Bound`.

Tuy nhiên cần phân biệt:

- best/worst/average case là nói về các loại input;
- `O`, `Ω`, `Θ` là ký hiệu tiệm cận mô tả cận của hàm.

Hai khái niệm này liên quan nhưng không đồng nhất.

---

## 8. Phân tích tiệm cận và các ký hiệu O, Ω, Θ

Phân tích tiệm cận nghiên cứu hành vi của hàm chi phí khi `n → ∞`, qua đó tập trung vào bậc tăng trưởng dài hạn và bỏ qua các khác biệt do hệ số hằng hoặc các số hạng bậc thấp.

### Big-O: cận trên tiệm cận

Ta nói `f(n) = O(g(n))` nếu tồn tại hai hằng số dương `c` và `n₀` sao cho `0 ≤ f(n) ≤ c·g(n)` với mọi `n ≥ n₀`.

Diễn giải trực quan:

> `g(n)` là một cận trên cho tốc độ tăng trưởng của `f(n)`.

<p align="center">
  <img src="images/image-1.png" alt="alt text" width="800" />
</p>

Ví dụ, xét `f(n) = 3n + 8`. Với `n ≥ 8`, ta có `3n + 8 ≤ 3n + n = 4n`; do đó `3n + 8 = O(n)`.

Một hàm có thể thỏa mãn đồng thời nhiều cận trên tiệm cận:

```text
3n + 8 = O(n)
3n + 8 = O(n²)
3n + 8 = O(n³)
```

Tuy nhiên, trong các cận trên trên, `O(n)` cung cấp mô tả chặt hơn về bậc tăng trưởng.

Tương tự, do `n² + 1 ≤ 2n²` với mọi `n ≥ 1`, suy ra `n² + 1 = O(n²)`.

#### Các ví dụ về Big-O

Các ví dụ dưới đây minh họa cách áp dụng trực tiếp định nghĩa Big-O thông qua việc lựa chọn các hằng số `c` và `n₀` phù hợp.

**Ví dụ 1. Tìm cận trên của `f(n) = 3n + 8`.**

Với mọi `n ≥ 8`, ta có `3n + 8 ≤ 3n + n = 4n`. Chọn `c = 4` và `n₀ = 8`, suy ra `3n + 8 = O(n)`.

**Ví dụ 2. Tìm cận trên của `f(n) = n² + 1`.**

Với mọi `n ≥ 1`, ta có `n² + 1 ≤ 2n²`. Chọn `c = 2` và `n₀ = 1`, do đó `n² + 1 = O(n²)`.

**Ví dụ 3. Tìm cận trên của `f(n) = n⁴ + 100n² + 50`.**

Với `n ≥ 11`, ta có `n⁴ + 100n² + 50 ≤ 2n⁴`. Chọn `c = 2` và `n₀ = 11`, suy ra `n⁴ + 100n² + 50 = O(n⁴)`.

**Ví dụ 4. Tìm cận trên của `f(n) = 2n³ - 2n²`.**

Với mọi `n ≥ 1`, ta có `2n³ - 2n² ≤ 2n³`. Chọn `c = 2` và `n₀ = 1`, do đó `2n³ - 2n² = O(n³)`.

**Ví dụ 5. Tìm cận trên của `f(n) = n`.**

Với mọi `n ≥ 1`, hiển nhiên `n ≤ n`. Chọn `c = 1` và `n₀ = 1`, suy ra `n = O(n)`.

**Ví dụ 6. Tìm cận trên của hàm hằng `f(n) = 410`.**

Với mọi `n ≥ 1`, ta có `410 ≤ 410`. Chọn `g(n) = 1`, `c = 410` và `n₀ = 1`, suy ra `410 = O(1)`.

**Ví dụ 7. Cặp hằng số `c` và `n₀` không duy nhất**

Xét `100n + 5 = O(n)`. Một cách chọn là dùng bất đẳng thức `100n + 5 ≤ 100n + 5n = 105n` với mọi `n ≥ 1`; khi đó có thể chọn `c = 105` và `n₀ = 1`.

Lựa chọn này không phải là duy nhất. Chẳng hạn, nếu chọn `c` lớn hơn thì có thể vẫn tìm được một `n₀` thích hợp. Điều quan trọng là **tồn tại** ít nhất một cặp hằng số dương `c, n₀` thỏa định nghĩa.

---

### Big-Ω: cận dưới tiệm cận

Ta nói `f(n) = Ω(g(n))` nếu tồn tại `c > 0` và `n₀` sao cho `0 ≤ c·g(n) ≤ f(n)` với mọi `n ≥ n₀`.

Diễn giải trực quan:

> `g(n)` là một cận dưới cho tốc độ tăng trưởng của `f(n)`.

<p align="center">
  <img src="images/image-2.png" alt="alt text" width="800" />
</p>

Ví dụ, với `f(n) = 5n²`, chọn `c = 5` thì `5n² ≥ 5n²`, nên `5n² = Ω(n²)`.

Ví dụ khác, `100n + 5 = Ω(n)` vì `100n + 5 ≥ 100n`.

#### Các ví dụ về Big-Ω

**Ví dụ 1. Tìm cận dưới của `f(n) = 5n²`.**

Với mọi `n ≥ 1`, ta có `5n² ≥ 5n²`. Chọn `c = 5` và `n₀ = 1`, suy ra `5n² = Ω(n²)`.

**Ví dụ 2. Chứng minh `100n + 5 ∉ Ω(n²)`.**

Giả sử ngược lại rằng tồn tại `c > 0` và `n₀` sao cho `cn² ≤ 100n + 5` với mọi `n ≥ n₀`. Với `n ≥ 1`, ta lại có `100n + 5 ≤ 100n + 5n = 105n`, nên `cn² ≤ 105n`, hay tương đương `n ≤ 105/c`.

Nhưng `105/c` là một hằng số hữu hạn, trong khi `n` có thể lớn tùy ý. Mâu thuẫn. Vì vậy, `100n + 5 ∉ Ω(n²)`.

**Ví dụ 3. Một số quan hệ đơn giản.**

Các quan hệ sau đều đúng: `2n = Ω(n)`, `n³ = Ω(n³)` và `log n = Ω(log n)`.

---

### Theta: cận chặt tiệm cận

Ta nói `f(n) = Θ(g(n))` nếu `f(n)` vừa là `O(g(n))` vừa là `Ω(g(n))`. Tức là tồn tại `c₁ > 0`, `c₂ > 0` và `n₀ > 0` sao cho `0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n)` với mọi `n ≥ n₀`.

<p align="center">
  <img src="images/image-3.png" alt="alt text" width="800" />
</p>

Ví dụ, với `f(n) = 6n³`, ta có đồng thời `6n³ = O(n³)` và `6n³ = Ω(n³)`, nên `6n³ = Θ(n³)`.

Một ví dụ khác là `f(n) = (n² - n)/2`; hàm này có bậc tăng trưởng `Θ(n²)`.

Cách diễn đạt ngắn gọn:

- `O(g(n))`: không tăng nhanh hơn `g(n)` về mặt tiệm cận.
- `Ω(g(n))`: không tăng chậm hơn `g(n)` về mặt tiệm cận.
- `Θ(g(n))`: tăng cùng bậc với `g(n)`.

---

#### Các ví dụ về Theta

**Ví dụ 1. Chứng minh `f(n) = n²/2 - n/2 = Θ(n²)`.**

Với `n ≥ 2`, ta có thể chọn các hằng số dương sao cho `(1/5)n² ≤ n²/2 - n/2 ≤ n²`. Do đó có thể lấy `c₁ = 1/5`, `c₂ = 1` và `n₀ = 2`, suy ra `n²/2 - n/2 = Θ(n²)`.

**Ví dụ 2. Chứng minh `n ∉ Θ(n²)`.**

Nếu `n = Θ(n²)`, phải tồn tại `c₁, c₂ > 0` sao cho `c₁n² ≤ n ≤ c₂n²` với mọi `n` đủ lớn. Tuy nhiên, bất đẳng thức bên trái `c₁n² ≤ n` tương đương với `n ≤ 1/c₁`, điều không thể đúng với mọi `n` đủ lớn. Vậy `n ∉ Θ(n²)`.

**Ví dụ 3. Chứng minh `6n³ ∉ Θ(n²)`.**

Nếu điều này đúng, phải tồn tại `c₁, c₂ > 0` sao cho `c₁n² ≤ 6n³ ≤ c₂n²` với mọi `n` đủ lớn. Từ bất đẳng thức phải `6n³ ≤ c₂n²`, suy ra `n ≤ c₂/6`, điều không thể đúng với mọi `n` đủ lớn. Do đó `6n³ ∉ Θ(n²)`.

**Ví dụ 4. Chứng minh `n ∉ Θ(log n)`.**

Nếu `n = Θ(log n)`, phải tồn tại `c₁, c₂ > 0` sao cho `c₁ log n ≤ n ≤ c₂ log n` với mọi `n` đủ lớn. Từ `n ≤ c₂ log n`, suy ra `c₂ ≥ n/log n`. Nhưng `n/log n → ∞` khi `n → ∞`, nên không tồn tại một hằng số hữu hạn `c₂` thỏa điều kiện cho mọi `n` đủ lớn. Vậy `n ∉ Θ(log n)`.

---

## 9. Một số tính chất của ký hiệu tiệm cận

Các tính chất sau thường được dùng khi rút gọn biểu thức.

### Tính truyền

Nếu `f(n) = O(g(n))` và `g(n) = O(h(n))` thì `f(n) = O(h(n))`. Tính chất tương tự cũng đúng cho `Ω` và `Θ`.

### Tính phản xạ

Luôn đúng rằng `f(n) = O(f(n))`, `f(n) = Ω(f(n))` và `f(n) = Θ(f(n))`.

### Tính đối xứng của Theta

Quan hệ `f(n) = Θ(g(n)) ⇔ g(n) = Θ(f(n))` luôn đúng.

### Quan hệ giữa O và Ω

Quan hệ `f(n) = O(g(n)) ⇔ g(n) = Ω(f(n))` luôn đúng.

### Quy tắc cộng

Nếu `f₁(n) = O(g₁(n))` và `f₂(n) = O(g₂(n))` thì `f₁(n) + f₂(n) = O(max(g₁(n), g₂(n)))`. Chẳng hạn, `n² + n log n = Θ(n²)`.

### Quy tắc nhân

Nếu `f₁(n) = O(g₁(n))` và `f₂(n) = O(g₂(n))` thì `f₁(n)f₂(n) = O(g₁(n)g₂(n))`. Ví dụ, `n × log n = Θ(n log n)`.

---

## 10. Quy tắc phân tích các đoạn code phổ biến

### Vòng lặp đơn

```python
for i in range(n):
 print(i)
```

Thân vòng lặp chạy `n` lần. Nếu mỗi lần mất `Θ(1)` thì tổng thời gian là `T(n) = n · Θ(1) = Θ(n)`.

### Vòng lặp lồng nhau

```python
for i in range(n):
 for j in range(n):
 print(i, j)
```

Vòng ngoài chạy `n` lần. Mỗi lần của vòng ngoài, vòng trong chạy `n` lần.

Do đó `T(n) = n × n = Θ(n²)`. Nếu ba vòng lặp độc lập cùng chạy `n` lần thì độ phức tạp là `Θ(n³)`.

### Các câu lệnh nối tiếp

```python
for i in range(n):
 work_a()

for j in range(n):
 work_b()
```

Tổng chi phí là `Θ(n) + Θ(n) = Θ(2n) = Θ(n)`.

Nếu `T₁(n) = Θ(n)` và `T₂(n) = Θ(n²)` thì `T(n) = Θ(n + n²) = Θ(n²)`.

### Câu lệnh if-else

Ví dụ:

```python
if n == 1:
 print("Wrong Value")
else:
 for i in range(n):
 print(i)
```

Worst-case time là `Θ(n)` vì khi phân tích worst case, ta xét nhánh tốn nhiều thời gian hơn.

Tổng quát, với worst case, ta có `T_ifelse = cost(condition) + max(cost(then), cost(else))`.

### Vòng lặp logarit

Ví dụ:

```python
i = 1
while i < n:
 i *= 2
```

Giá trị của `i`:
 `1, 2, 4, 8, 16, ...` 
Sau `k` vòng, ta có `i = 2^k`. Vòng lặp dừng khi `2^k ≥ n`, suy ra `k ≥ log₂n`; do đó `T(n) = Θ(log n)`.

Tương tự:

```python
i = n
while i > 1:
 i //= 2
```

cũng có độ phức tạp `Θ(log n)`.

### Vòng lặp phụ thuộc

Ví dụ:

```python
for i in range(n):
 for j in range(i):
 work()
```

Số lần thực hiện là `0 + 1 + 2 + ... + (n - 1)`. Ta có `0 + 1 + 2 + ... + (n - 1) = n(n - 1)/2 = Θ(n²)`.

Không thể xác định độ phức tạp chỉ dựa trên số lượng vòng lặp; cần tính số lần thân lặp thực sự được thực hiện.

---

### Các ví dụ phân tích mã nguồn

Các ví dụ sau minh họa các quy tắc phân tích phổ biến đối với vòng lặp, các câu lệnh nối tiếp, nhánh điều kiện và các quá trình có tốc độ giảm theo cấp số nhân.

**Ví dụ 1. Vòng lặp đơn**

```python
for i in range(0, n):
 print("Current Number:", i, sep="")
```

Nếu thân vòng lặp mất thời gian hằng số `c`, tổng thời gian là `T(n) = c × n = O(n)`.

**Ví dụ 2. Hai vòng lặp lồng nhau**

```python
for i in range(0, n):
 for j in range(0, n):
 print(i, j)
```

Tổng số lần thực hiện thân vòng lặp là `n × n = n²`, do đó `T(n) = O(n²)`.

**Ví dụ 3. Các câu lệnh nối tiếp**

```python
n = 100

for i in range(n):
 print("Current Number:", i, sep="")

for i in range(n):
 for j in range(n):
 print(i, j)
```

Có thể biểu diễn tổng thời gian dưới dạng `T(n) = c₀ + c₁n + c₂n²`. Số hạng chi phối là `n²`, nên `T(n) = O(n²)`.

**Ví dụ 4. Câu lệnh `if-else`**

```python
if n == 1:
 print("Wrong Value")
 print(n)
else:
 for i in range(n):
 print("Current Number:", i, sep="")
```

- Nhánh `if`: thời gian hằng số.
- Nhánh `else`: chạy `n` lần.

Trong worst case, ta có `T(n) = c₀ + c₁n = O(n)`.

**Ví dụ 5. Vòng lặp logarit tăng gấp đôi**

```python
def logarithms(n):
 i = 1
 while i < n:
 i = i * 2
 print(i)

logarithms(100)
```

Giá trị `i` lần lượt là:
 `1, 2, 4, 8, 16, ...` 
Sau `k` bước, ta có `2^k ≈ n`, nên `k = log₂n`. Do đó `T(n) = O(log n)`.

**Ví dụ 6. Vòng lặp logarit giảm một nửa**

```python
def logarithms(n):
 i = n
 while i > 1:
 i = i // 2
 print(i)

logarithms(100)
```

Mỗi vòng giảm kích thước còn một nửa theo dãy `n, n/2, n/4, n/8, ...`, nên số vòng là `O(log n)`.

**Ví dụ 7. Tìm kiếm từ trong từ điển bằng cách chia đôi**

Giả sử cần tìm một từ trong từ điển có `n` trang:

1. Mở trang giữa.
2. Nếu từ cần tìm nằm ở phía bên trái, bỏ nửa bên phải.
3. Nếu nằm ở phía bên phải, bỏ nửa bên trái.
4. Lặp lại trên nửa còn lại.

Sau mỗi bước, số trang cần xét giảm còn một nửa theo dãy `n → n/2 → n/4 → n/8 → ...`; vì vậy số bước là `O(log n)`.

---

## 11. Các công thức logarit và tổng thường dùng

### Công thức logarit

Các quy tắc quan trọng gồm `log(xy) = log x + log y`, `log(x/y) = log x - log y`, `log(x^k) = k log x` và `log(log n) = log log n`. Khi đổi cơ số, ta dùng `log_b x = log_a x / log_a b`.

Trong phân tích tiệm cận, cơ số log thường không ảnh hưởng đến bậc tăng trưởng; chẳng hạn `log₂n = Θ(log₁₀n)`.

### Tổng số học

Ta có công thức `1 + 2 + 3 + ... + n = n(n + 1)/2 = Θ(n²)`.

### Tổng cấp số nhân

Với `x ≠ 1`, ta có `1 + x + x² + ... + x^n = (x^(n+1) - 1)/(x - 1)`. Chẳng hạn, `1 + 2 + 4 + ... + 2^k = 2^(k+1) - 1 = Θ(2^k)`.

### Tổng điều hòa

Tổng điều hòa thỏa `1 + 1/2 + 1/3 + ... + 1/n = Θ(log n)`.

Điều này xuất hiện trong nhiều thuật toán có tổng dạng `n/1 + n/2 + n/3 + ... + n/n`. Khi đó, `n(1 + 1/2 + ... + 1/n) = Θ(n log n)`.

### Tổng logarit

Với tổng logarit, ta có `Σ log k = log(n!) = Θ(n log n)` khi `k` chạy từ `1` đến `n`.

### Tổng lũy thừa

Với `p > -1`, ta có `Σ k^p = Θ(n^(p+1))`. Ví dụ, `1² + 2² + ... + n² = Θ(n³)`.

---

## 12. Các nhầm lẫn thường gặp trong phân tích độ phức tạp

### Nhầm số vòng lặp với độ phức tạp

Hai vòng lặp không phải lúc nào cũng là `Θ(n²)`.

Nếu hai vòng lặp chạy nối tiếp thì `Θ(n) + Θ(n) = Θ(n)`; nếu chúng lồng nhau độc lập thì thường có `Θ(n × n) = Θ(n²)`.

### Nhầm best case với Big-Ω

`best case` là một loại input. `Ω` là ký hiệu cận dưới.

Không nên đồng nhất một cách máy móc `Big-O = worst case` và `Big-Omega = best case`.

Ví dụ, nếu một hàm có `Worst-case time = Θ(n²)` thì đồng thời cũng đúng rằng `Worst-case time = O(n²)` và `Worst-case time = Ω(n²)`.

### Chỉ nhìn code mà bỏ qua chi phí thao tác

Ví dụ:

```python
arr[:k]
```

không phải lúc nào là `O(1)`; trong Python, slicing tạo list mới và tốn thời gian theo số phần tử được sao chép.

Tương tự:

```python
x in list
```

thường có worst case `Θ(n)`.

### Quên xác định input size

Không thể phân tích đúng nếu không biết `n` đại diện cho gì.

Ví dụ với đồ thị, biểu diễn `O(V + E)` thường chính xác hơn viết đơn giản `O(n)`.

### Chỉ dùng O khi có thể dùng Θ

Nếu biết chính xác bậc tăng trưởng, chẳng hạn `T(n) = 3n + 7`, thì viết `T(n) = Θ(n)` thường mạnh và chính xác hơn chỉ viết `T(n) = O(n)`.

---

## 13. Ví dụ tổng hợp

### Ví dụ 1: vòng lặp đơn

```python
def example1(n):
 total = 0
 for i in range(n):
 total += i
 return total
```

Thân lặp chạy `n` lần, nên **time complexity là `Θ(n)` và auxiliary space là `Θ(1)`**.

### Ví dụ 2: hai vòng lặp nối tiếp

```python
def example2(n):
 for i in range(n):
 print(i)

 for j in range(n):
 print(j)
```

Tổng thời gian là `Θ(n) + Θ(n) = Θ(n)`.

### Ví dụ 3: vòng lặp lồng nhau

```python
def example3(n):
 count = 0
 for i in range(n):
 for j in range(n):
 count += 1
 return count
```

Tổng số lần tăng `count` là `n²`, do đó **time complexity là `Θ(n²)`**.

### Ví dụ 4: vòng lặp logarit

```python
def example4(n):
 i = 1
 count = 0

 while i < n:
 i *= 2
 count += 1

 return count
```

Sau `k` vòng, `i = 2^k`. Vòng lặp dừng khi `2^k ≥ n`, nên `k = Θ(log n)`.

### Ví dụ 5: tổng điều hòa

```python
def example5(n):
 count = 0

 for i in range(1, n + 1):
 j = i
 while j <= n:
 count += 1
 j += i

 return count
```

Với mỗi `i`, vòng trong chạy khoảng `n/i` lần. Tổng số lần lặp là `n/1 + n/2 + ... + n/n = nH_n = Θ(n log n)`.

---

## 14. Quiz tự kiểm tra

### Phần A — Trắc nghiệm

1. Phát biểu nào mô tả đúng nhất về ADT?

 A. Một ngôn ngữ lập trình. 
 B. Một cách mô tả dữ liệu và các phép toán, độc lập với cài đặt cụ thể. 
 C. Một biến nguyên. 
 D. Một thuật toán sắp xếp.

2. Với `T(n) = 5n² + 2n + 100`, bậc tăng trưởng là:

 A. `Θ(1)` 
 B. `Θ(n)` 
 C. `Θ(n²)` 
 D. `Θ(n³)`

3. Hai vòng lặp nối tiếp, mỗi vòng chạy `n` lần, có tổng độ phức tạp:

 A. `Θ(n)` 
 B. `Θ(n²)` 
 C. `Θ(log n)` 
 D. `Θ(2n²)`

4. Đoạn code sau có độ phức tạp nào?

 ```python
 i = 1
 while i < n:
 i *= 2
 ```

 A. `Θ(1)` 
 B. `Θ(log n)` 
 C. `Θ(n)` 
 D. `Θ(n²)`

5. Với linear search, worst case xảy ra khi:

 A. Phần tử ở đầu mảng. 
 B. Phần tử ở vị trí ngẫu nhiên. 
 C. Phần tử ở cuối hoặc không tồn tại. 
 D. Mảng chỉ có một phần tử.

6. `f(n) = O(g(n))` nghĩa là:

 A. `f(n)` luôn bằng `g(n)`. 
 B. `f(n)` bị chặn trên tiệm cận bởi một hằng số nhân với `g(n)`. 
 C. `f(n)` luôn nhỏ hơn `g(n)` với mọi `n`. 
 D. `f(n)` là best case.

7. Nếu `f(n) = Θ(g(n))` thì:

 A. Chỉ có cận trên. 
 B. Chỉ có cận dưới. 
 C. Có cả cận trên và cận dưới cùng bậc. 
 D. Không thể so sánh.

8. Tổng `1 + 2 + ... + n` có bậc:

 A. `Θ(log n)` 
 B. `Θ(n)` 
 C. `Θ(n log n)` 
 D. `Θ(n²)`

9. Tổng điều hòa `1 + 1/2 + ... + 1/n` có bậc:

 A. `Θ(1)` 
 B. `Θ(log n)` 
 C. `Θ(n)` 
 D. `Θ(n²)`

10. Phát biểu nào sai?

 A. `n = O(n²)`. 
 B. `n² = Ω(n)`. 
 C. `n = Θ(n²)`. 
 D. `3n + 5 = Θ(n)`.

<details>
<summary><strong>Đáp án Quiz</strong></summary>

| Câu | Đáp án |
|---:|:---:|
| 1 | B |
| 2 | C |
| 3 | A |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | D |
| 9 | B |
| 10 | C |

</details>

---

## 15. Bài tập thực hành

### Bài 1

Phân tích:

```python
for i in range(n):
 print(i)
```

### Bài 2

Phân tích:

```python
for i in range(n):
 for j in range(n):
 print(i, j)
```

### Bài 3

Phân tích:

```python
for i in range(n):
 print(i)

for j in range(n * n):
 print(j)
```

### Bài 4

Phân tích:

```python
i = n
while i > 1:
 i //= 2
```

### Bài 5

Phân tích:

```python
for i in range(n):
 for j in range(i):
 print(i, j)
```

### Bài 6

Chứng minh `3n + 8 = O(n)` bằng định nghĩa Big-O.

### Bài 7

Chứng minh `5n² = Ω(n²)` bằng định nghĩa Big-Ω.

### Bài 8

Chứng minh `6n³ + 4n = Θ(n³)`.

### Bài 9

Cho `f(n) = n² + n log n + 100`. Hãy xác định bậc tăng trưởng.

### Bài 10

Với linear search:

- nêu best case;
- worst case;
- average case;
- và giải thích vì sao average case cần một giả định xác suất.

---

## 16. Tóm tắt

Những ý chính cần nhớ:

- Biến lưu giá trị; kiểu dữ liệu mô tả miền giá trị và phép toán.
- Cấu trúc dữ liệu tổ chức dữ liệu; ADT mô tả dữ liệu và các phép toán ở mức trừu tượng.
- Thuật toán là một quy trình hữu hạn, rõ ràng để giải quyết bài toán.
- Phân tích thuật toán tập trung vào cách thời gian và bộ nhớ tăng theo kích thước input.
- Không nên chỉ dùng giây chạy thực tế hoặc số dòng code để so sánh thuật toán.
- Trọng tâm của phân tích tiệm cận là tốc độ tăng trưởng theo kích thước input.
- Các bậc thường gặp có thứ tự tăng dần: `1 < log n < n < n log n < n² < n³ < 2^n < n!`.

- Best, average và worst case phụ thuộc vào loại input.
- `O` là cận trên, `Ω` là cận dưới, `Θ` là cận chặt.
- Vòng lặp nối tiếp thường cộng chi phí; vòng lặp lồng nhau thường nhân hoặc cần tính tổng.
- Vòng lặp nhân đôi/chia đôi thường dẫn đến `Θ(log n)`.
- Các công thức tổng số học, cấp số nhân, tổng điều hòa và logarit là công cụ cơ bản trong phân tích độ phức tạp.