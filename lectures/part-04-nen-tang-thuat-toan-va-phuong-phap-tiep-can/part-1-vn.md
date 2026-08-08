---
title: "Part I — Foundations of Algorithms and Data Structures"
course: "Data Structures and Algorithmic Thinking with Python"
language: "vi"
version: "2.1"
---

# Part I — Foundations of Algorithms and Data Structures

**Cập nhật lần cuối:** 3 tháng 8 năm 2026

## 1. Mục tiêu học tập

Phần này cung cấp nền tảng khái niệm trước khi đi sâu vào các cấu trúc dữ liệu cụ thể và kỹ thuật phân tích thuật toán. Mục tiêu không chỉ là ghi nhớ các định nghĩa riêng lẻ, mà còn hiểu được mối quan hệ giữa bài toán, dữ liệu, thuật toán, chương trình và cấu trúc dữ liệu.

Sau phần này, người học có thể:

- phân biệt **problem**, **input**, **output**, **algorithm** và **program**;
- giải thích thuật toán là gì và nêu được các đặc tính cơ bản của một thuật toán;
- phân biệt **data type**, **data structure** và **Abstract Data Type — ADT**;
- nhận biết các cấu trúc dữ liệu cơ bản và mô tả được mục đích sử dụng điển hình của từng cấu trúc;
- giải thích rõ các thao tác thường gặp trên cấu trúc dữ liệu như access, search, insert, delete, update và traverse;
- giải thích mối quan hệ giữa thuật toán và cấu trúc dữ liệu;
- đánh giá một lời giải theo ba tiêu chí cơ bản: **correctness**, **efficiency** và **scalability**.

---

## 2. Problems, Inputs, Outputs, Algorithms, and Programs

Khi giải một bài toán bằng máy tính, ta thường đi qua một chuỗi các bước tư duy. Trước tiên cần xác định chính xác bài toán cần giải, tiếp theo là mô tả dữ liệu đầu vào và kết quả đầu ra, sau đó lựa chọn hoặc thiết kế thuật toán phù hợp, và cuối cùng hiện thực thuật toán đó bằng một chương trình cụ thể.

Có thể hình dung quá trình này như sau:

```text
Problem
    ↓
Input and Output Specification
    ↓
Algorithm
    ↓
Data Structures
    ↓
Program
```

Mỗi thành phần có một vai trò riêng. Nếu bài toán được mô tả không rõ, thuật toán có thể giải sai mục tiêu. Nếu input và output không được xác định chính xác, rất khó đánh giá tính đúng đắn. Nếu cấu trúc dữ liệu được chọn không phù hợp, một thuật toán đúng vẫn có thể hoạt động kém hiệu quả.

### 2.1. Problem

**Problem** là nhiệm vụ hoặc câu hỏi cần được giải quyết.

Một bài toán tính toán thường mô tả:

- dữ liệu nào được cung cấp;
- cần thực hiện phép xử lý nào;
- kết quả nào phải được tạo ra;
- các ràng buộc nào cần được thỏa mãn.

Ví dụ:

> Cho một danh sách số nguyên và một giá trị `target`. Hãy xác định vị trí đầu tiên của `target` trong danh sách. Nếu `target` không xuất hiện, trả về `-1`.

Đây là một bài toán tìm kiếm. Mô tả bài toán chưa phải là thuật toán, vì nó chỉ nói **cần tìm gì**, chưa nói **tìm bằng cách nào**.

### 2.2. Input

**Input** là dữ liệu được cung cấp cho thuật toán trước khi quá trình xử lý bắt đầu.

Trong ví dụ trên:

```text
arr = [7, 2, 9, 4, 1]
target = 4
```

Ta có hai input:

- `arr`: danh sách các số nguyên;
- `target`: giá trị cần tìm.

Khi mô tả input, nên làm rõ:

- kiểu dữ liệu;
- số lượng phần tử;
- miền giá trị;
- các ràng buộc đặc biệt.

Ví dụ:

```text
Input:
- n: số nguyên dương
- A: mảng gồm n số nguyên
- target: số nguyên cần tìm
```

Việc xác định input rõ ràng rất quan trọng vì thuật toán có thể được thiết kế khác nhau tùy theo đặc điểm dữ liệu. Chẳng hạn, tìm kiếm trên một mảng đã sắp xếp khác với tìm kiếm trên một mảng chưa sắp xếp.

### 2.3. Output

**Output** là kết quả mà thuật toán phải tạo ra sau khi xử lý input.

Với ví dụ:

```text
arr = [7, 2, 9, 4, 1]
target = 4
```

Output là:

```text
3
```

nếu chỉ số bắt đầu từ `0`.

Một đặc tả output tốt cần nói rõ:

- kiểu kết quả;
- ý nghĩa của kết quả;
- cách xử lý các trường hợp đặc biệt.

Ví dụ:

```text
Output:
- chỉ số đầu tiên i sao cho A[i] = target;
- trả về -1 nếu target không tồn tại.
```

### 2.4. Algorithm

**Algorithm** là một quy trình hữu hạn gồm các bước rõ ràng để biến input thành output.

Một thuật toán Linear Search có thể được mô tả bằng ý tưởng:

1. bắt đầu từ phần tử đầu tiên;
2. so sánh từng phần tử với `target`;
3. nếu tìm thấy, trả về vị trí;
4. nếu duyệt hết mà không tìm thấy, trả về `-1`.

Hiện thực bằng Python:

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

Điểm quan trọng là thuật toán mô tả **cách giải bài toán**, chứ không chỉ nêu yêu cầu đầu vào và đầu ra.

### 2.5. Program

**Program** là một hiện thực cụ thể của thuật toán bằng một ngôn ngữ lập trình.

Cùng một thuật toán Linear Search có thể được viết bằng:

- Python;
- C++;
- Java;
- Rust;
- hoặc nhiều ngôn ngữ khác.

Ý tưởng thuật toán không thay đổi, nhưng chương trình cụ thể có thể khác về:

- cú pháp;
- kiểu dữ liệu;
- cách quản lý bộ nhớ;
- thư viện sử dụng;
- chi tiết triển khai.

Có thể tóm tắt:

> **Algorithm là phương pháp giải; program là hiện thực cụ thể của phương pháp đó bằng một ngôn ngữ lập trình.**

---

## 3. What Is an Algorithm?

Một **thuật toán** là một dãy hữu hạn các chỉ dẫn được xác định rõ ràng nhằm giải quyết một bài toán hoặc thực hiện một phép tính.

Có thể mô tả trực quan quá trình này bằng sơ đồ:

```text
Input
    ↓
Finite sequence of well-defined steps
    ↓
Output
```

Hoặc viết ngắn gọn:

```text
Input → Algorithm → Output
```

Điểm cốt lõi là một thuật toán phải nhận dữ liệu, thực hiện một chuỗi bước có logic rõ ràng và tạo ra kết quả sau một số hữu hạn bước.

Ví dụ, xét bài toán tìm giá trị lớn nhất trong một mảng không rỗng:

```python
def find_max(arr):
    maximum = arr[0]

    for value in arr[1:]:
        if value > maximum:
            maximum = value

    return maximum
```

Thuật toán trên hoạt động theo nguyên tắc:

1. giả sử phần tử đầu tiên là lớn nhất;
2. lần lượt so sánh các phần tử còn lại với giá trị lớn nhất hiện tại;
3. cập nhật giá trị lớn nhất khi tìm thấy phần tử lớn hơn;
4. trả về kết quả sau khi duyệt hết mảng.

Ví dụ này cho thấy một thuật toán không chỉ là code. Trước khi viết chương trình, ta đã có một quy trình logic độc lập với ngôn ngữ lập trình.

---

## 4. Properties of Algorithms

Một quy trình muốn được xem là một thuật toán cần thỏa mãn một số đặc tính cơ bản. Các đặc tính này giúp đảm bảo rằng thuật toán được mô tả rõ ràng, có khả năng thực hiện và tạo ra kết quả đúng.

### 4.1. Input

Thuật toán có thể không nhận input hoặc nhận một hay nhiều input, nhưng dữ liệu đầu vào phải được xác định rõ.

Ví dụ:

```text
Input:
- n: số nguyên dương
- A: mảng gồm n số nguyên
```

Trong thực tế, việc mô tả input thường cần đi kèm ràng buộc. Ví dụ:

```text
1 ≤ n ≤ 100000
-10^9 ≤ A[i] ≤ 10^9
```

Các ràng buộc này có thể ảnh hưởng trực tiếp đến việc lựa chọn thuật toán và cấu trúc dữ liệu.

### 4.2. Output

Thuật toán phải tạo ra ít nhất một kết quả hoặc một trạng thái mới có thể quan sát được.

Ví dụ:

```text
Output:
- giá trị lớn nhất trong mảng A.
```

Một output được mô tả tốt phải đủ rõ để ta có thể kiểm tra thuật toán có trả về đúng kết quả hay không.

### 4.3. Definiteness

Mỗi bước của thuật toán phải rõ ràng và không mơ hồ.

Ví dụ không tốt:

```text
Chọn một số đủ lớn.
```

Câu này không chỉ ra thế nào là "đủ lớn".

Ví dụ tốt hơn:

```text
Đặt maximum bằng phần tử đầu tiên của mảng.
```

Một thuật toán càng phức tạp thì yêu cầu về tính rõ ràng càng quan trọng. Những mô tả mơ hồ có thể dẫn đến nhiều cách hiểu khác nhau và làm mất khả năng kiểm tra tính đúng đắn.

### 4.4. Finiteness

Thuật toán phải dừng sau một số hữu hạn bước đối với mọi input hợp lệ.

Ví dụ sau không kết thúc:

```python
while True:
    pass
```

Đối với thuật toán đệ quy, cần có một **base case** để đảm bảo quá trình gọi hàm không tiếp tục vô hạn.

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

### 4.5. Effectiveness

Mỗi bước của thuật toán phải đủ cơ bản để có thể thực hiện được trong một lượng thời gian hữu hạn.

Các thao tác như:

- gán giá trị;
- cộng, trừ, nhân, chia;
- so sánh;
- truy cập phần tử;
- gọi một thủ tục đã được xác định rõ;

đều là những thao tác có thể thực hiện.

Một mô tả như:

```text
Tìm ngay lời giải tối ưu của một bài toán bất kỳ.
```

không phải là một bước hiệu quả theo nghĩa thuật toán, vì nó không chỉ ra cách thực hiện cụ thể.

### 4.6. Correctness

Thuật toán phải trả về kết quả đúng cho mọi input hợp lệ.

Ví dụ, một thuật toán tìm giá trị lớn nhất phải trả về một phần tử không nhỏ hơn bất kỳ phần tử nào khác trong dữ liệu.

Tính đúng đắn có thể được đánh giá bằng:

- lập luận logic;
- chứng minh;
- loop invariant;
- induction;
- kiểm thử trên các trường hợp điển hình và biên.

Kiểm thử có thể giúp phát hiện lỗi, nhưng không phải lúc nào cũng đủ để chứng minh thuật toán đúng với mọi input.

### 4.7. Deterministic and Randomized Algorithms

Không phải mọi thuật toán đều deterministic.

- **Deterministic algorithm**: với cùng input, thuật toán luôn thực hiện cùng một chuỗi bước và tạo ra cùng kết quả.
- **Randomized algorithm**: thuật toán có thể sử dụng lựa chọn ngẫu nhiên trong quá trình thực thi.

Ví dụ, Randomized Quick Sort có thể chọn pivot ngẫu nhiên. Hai lần chạy trên cùng một input có thể tạo ra các chuỗi phân hoạch khác nhau.

Tuy nhiên, tính ngẫu nhiên không làm mất đi bản chất thuật toán. Điều quan trọng là quy trình phải được xác định rõ và có tiêu chí đúng đắn phù hợp.

---

## 5. What Is a Data Structure?

Khi lượng dữ liệu tăng lên, việc chỉ lưu các giá trị riêng lẻ trong các biến không còn đủ. Ta cần một cách có hệ thống để tổ chức dữ liệu sao cho các thao tác cần thiết được thực hiện hiệu quả.

Một **data structure** là cách tổ chức, lưu trữ và quản lý dữ liệu để hỗ trợ các thao tác như truy cập, tìm kiếm, chèn, xóa và duyệt.

Ví dụ:

- một danh sách các điểm số có thể được lưu bằng array;
- lịch sử thao tác undo có thể được quản lý bằng stack;
- hàng chờ khách hàng có thể được mô hình hóa bằng queue;
- mạng đường có thể được biểu diễn bằng graph;
- các cặp key-value có thể được lưu bằng hash table.

Điểm quan trọng là cùng một tập dữ liệu có thể được tổ chức theo nhiều cách khác nhau, và mỗi cách có ưu điểm riêng đối với các thao tác cụ thể.

> **Không tồn tại một cấu trúc dữ liệu tốt nhất cho mọi bài toán. Cấu trúc phù hợp là cấu trúc hỗ trợ hiệu quả nhất cho những thao tác được sử dụng thường xuyên nhất.**

---

## 6. Common Operations on Data Structures

Trước khi học từng cấu trúc dữ liệu, cần hiểu các thao tác cơ bản thường được thực hiện trên dữ liệu. Đây cũng là cơ sở để so sánh các cấu trúc dữ liệu với nhau.

### 6.1. Access

**Access** là thao tác lấy trực tiếp một phần tử tại một vị trí hoặc thông qua một địa chỉ xác định.

Ví dụ với array:

```python
values = [10, 20, 30, 40]
print(values[2])
```

Kết quả:

```text
30
```

Trong array, truy cập theo chỉ số thường là thao tác rất hiệu quả.

### 6.2. Search

**Search** là thao tác tìm một phần tử thỏa mãn một điều kiện hoặc có một giá trị cụ thể.

Ví dụ:

```python
def find_value(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

Search có thể được thực hiện theo nhiều cách khác nhau tùy cấu trúc dữ liệu, chẳng hạn Linear Search, Binary Search, hash lookup hoặc tree search.

### 6.3. Insert

**Insert** là thao tác thêm một phần tử mới vào cấu trúc dữ liệu.

Ví dụ:

```python
values = [10, 20, 30]
values.append(40)
```

Vị trí chèn có thể là:

- đầu;
- cuối;
- giữa;
- vị trí được xác định bởi key hoặc priority.

Chi phí chèn phụ thuộc mạnh vào cấu trúc dữ liệu.

### 6.4. Delete

**Delete** là thao tác loại bỏ một phần tử khỏi cấu trúc dữ liệu.

Ví dụ:

```python
values = [10, 20, 30, 40]
values.remove(30)
```

Một số cấu trúc hỗ trợ xóa hiệu quả khi đã biết vị trí hoặc node, trong khi các cấu trúc khác có thể cần dịch chuyển nhiều phần tử.

### 6.5. Update

**Update** là thao tác thay đổi giá trị của một phần tử đã tồn tại.

Ví dụ:

```python
scores = [7.5, 8.0, 9.0]
scores[1] = 8.5
```

Update khác với insert ở chỗ nó không làm tăng số lượng phần tử.

### 6.6. Traverse

**Traverse** là thao tác duyệt qua các phần tử của cấu trúc dữ liệu theo một thứ tự nhất định.

Ví dụ với list:

```python
for value in values:
    print(value)
```

Với tree hoặc graph, traverse có thể sử dụng các chiến lược khác nhau như DFS hoặc BFS.

### 6.7. Membership Test

**Membership test** kiểm tra xem một phần tử có thuộc cấu trúc dữ liệu hay không.

Ví dụ:

```python
visited = {1, 3, 5}

print(3 in visited)
```

Kết quả:

```text
True
```

Cùng một phép kiểm tra membership có thể có chi phí rất khác nhau trên list, set, hash table hoặc tree.

### 6.8. Find Minimum / Maximum

Thao tác này xác định phần tử nhỏ nhất hoặc lớn nhất theo một thứ tự hoặc tiêu chí ưu tiên.

Ví dụ:

```python
values = [7, 2, 9, 4]
print(min(values))
print(max(values))
```

Một heap hoặc priority queue được thiết kế đặc biệt để hỗ trợ việc lấy phần tử ưu tiên cao nhất hoặc thấp nhất hiệu quả.

### 6.9. Predecessor / Successor

Giả sử các phần tử có thứ tự.

- **Predecessor** của một phần tử là phần tử lớn nhất nhỏ hơn nó.
- **Successor** là phần tử nhỏ nhất lớn hơn nó.

Ví dụ, trong tập:

```text
{2, 5, 8, 12}
```

với phần tử `8`:

```text
Predecessor = 5
Successor = 12
```

Các thao tác này đặc biệt quan trọng trong ordered sets và balanced search trees.

### 6.10. Merge

**Merge** là thao tác hợp nhất hai cấu trúc dữ liệu hoặc hai tập dữ liệu thành một cấu trúc mới.

Ví dụ:

```text
A = [1, 3, 5]
B = [2, 4, 6]
```

Có thể merge thành:

```text
[1, 2, 3, 4, 5, 6]
```

Merge là một thao tác cốt lõi trong Merge Sort và nhiều cấu trúc dữ liệu nâng cao.

### 6.11. Split

**Split** là thao tác chia một cấu trúc dữ liệu thành hai hoặc nhiều phần theo một điều kiện.

Ví dụ:

```text
[1, 2, 3, 4, 5, 6]
```

chia tại vị trí giữa thành:

```text
[1, 2, 3]
[4, 5, 6]
```

Split xuất hiện trong divide-and-conquer, balanced trees và nhiều thuật toán phân hoạch.

### 6.12. Tóm tắt các thao tác

| Thao tác | Định nghĩa ngắn gọn |
|---|---|
| Access | Lấy trực tiếp một phần tử tại vị trí hoặc địa chỉ xác định |
| Search | Tìm phần tử thỏa điều kiện hoặc có giá trị cụ thể |
| Insert | Thêm một phần tử mới |
| Delete | Loại bỏ một phần tử |
| Update | Thay đổi giá trị phần tử đã tồn tại |
| Traverse | Duyệt qua các phần tử theo một thứ tự |
| Membership | Kiểm tra một phần tử có thuộc cấu trúc hay không |
| Min/Max | Tìm phần tử nhỏ nhất hoặc lớn nhất |
| Predecessor/Successor | Tìm phần tử liền trước hoặc liền sau theo thứ tự |
| Merge | Hợp nhất hai cấu trúc hoặc hai tập dữ liệu |
| Split | Chia một cấu trúc thành nhiều phần |

---

## 7. Abstract Data Types

Một **Abstract Data Type — ADT** là một mô hình trừu tượng mô tả dữ liệu và các phép toán được phép thực hiện trên dữ liệu đó.

Một ADT thường xác định:

1. tập các đối tượng dữ liệu;
2. tập các phép toán được hỗ trợ;
3. hành vi mong đợi của từng phép toán.

ADT tập trung vào câu hỏi:

> **Cấu trúc này cho phép làm gì và các thao tác phải có hành vi như thế nào?**

Trong khi implementation tập trung vào câu hỏi:

> **Dữ liệu được lưu trữ trong bộ nhớ ra sao và các thao tác được cài đặt bằng thuật toán nào?**

### Ví dụ: Stack ADT

Stack thường hỗ trợ:

- `push(x)`: thêm phần tử `x` lên đỉnh stack;
- `pop()`: lấy và xóa phần tử trên đỉnh;
- `top()` hoặc `peek()`: xem phần tử trên đỉnh mà không xóa;
- `is_empty()`: kiểm tra stack có rỗng hay không.

Stack hoạt động theo nguyên tắc:

```text
LIFO = Last-In, First-Out
```

Nghĩa là phần tử được thêm vào sau cùng sẽ được lấy ra trước tiên.

Stack có thể được cài đặt bằng:

- array;
- dynamic array;
- linked list.

Các cách cài đặt khác nhau vẫn có thể cung cấp cùng một giao diện Stack ADT, nhưng chi phí thời gian, bộ nhớ và cách quản lý dung lượng có thể khác nhau.

> **ADT mô tả giao diện và hành vi; data structure implementation mô tả cách dữ liệu được tổ chức và các thao tác được hiện thực.**

---

## 8. Basic and Commonly Used Data Structures

Các cấu trúc dữ liệu dưới đây xuất hiện thường xuyên trong lập trình, thuật toán, khoa học dữ liệu, trí tuệ nhân tạo và nghiên cứu vận hành. Mỗi cấu trúc phù hợp với một nhóm thao tác và dạng bài toán riêng.

### 8.1. Array / Dynamic Array

Array lưu các phần tử theo một thứ tự tuyến tính và thường hỗ trợ truy cập theo chỉ số.

Ví dụ:

```python
values = [10, 20, 30, 40]
print(values[2])
```

Kết quả:

```text
30
```

Array phù hợp khi cần:

- truy cập nhanh theo chỉ số;
- duyệt tuần tự;
- lưu dữ liệu theo thứ tự.

Dynamic array cho phép kích thước tăng hoặc giảm trong quá trình chạy. Python `list` là một ví dụ điển hình của dynamic array.

### 8.2. Linked List

Linked List gồm các node, trong đó mỗi node chứa dữ liệu và một hoặc nhiều liên kết đến node khác.

Linked List phù hợp khi:

- cần chèn hoặc xóa tại vị trí đã biết;
- không yêu cầu truy cập ngẫu nhiên nhanh theo index;
- kích thước cấu trúc thay đổi thường xuyên.

Điểm khác biệt quan trọng so với array là các node không nhất thiết nằm liên tiếp trong bộ nhớ.

### 8.3. Stack

Stack là cấu trúc tuyến tính hoạt động theo nguyên tắc:

```text
LIFO = Last-In, First-Out
```

Ví dụ trực giác là một chồng đĩa: chiếc đĩa đặt lên sau cùng sẽ được lấy ra trước.

Ứng dụng:

- DFS;
- backtracking;
- expression evaluation;
- undo operations;
- call stack.

### 8.4. Queue

Queue hoạt động theo nguyên tắc:

```text
FIFO = First-In, First-Out
```

Phần tử được đưa vào trước sẽ được lấy ra trước.

Ứng dụng:

- BFS;
- task scheduling;
- waiting lines;
- simulations;
- xử lý request theo thứ tự đến.

### 8.5. Deque

Deque, viết tắt của **double-ended queue**, cho phép chèn và xóa ở cả hai đầu.

Ứng dụng:

- sliding window;
- monotonic queue;
- palindrome processing;
- một số biến thể của BFS.

Deque linh hoạt hơn queue thông thường vì không giới hạn thao tác ở một đầu vào và một đầu ra.

### 8.6. Hash Table / Dictionary / Map

Hash Table lưu dữ liệu dưới dạng ánh xạ:

```text
key → value
```

Ví dụ trong Python:

```python
student = {
    "name": "Minh",
    "score": 9.0
}
```

Các thao tác tra cứu, chèn và xóa theo key thường có expected time gần `O(1)` trong điều kiện thông thường.

Hash table đặc biệt phù hợp khi cần:

- lookup nhanh theo key;
- đếm tần suất;
- caching;
- indexing.

### 8.7. Set

Set lưu các phần tử phân biệt và không cho phép lặp lại giá trị giống nhau theo nghĩa equality.

Ví dụ:

```python
visited = {1, 3, 5}
```

Ứng dụng:

- membership test;
- loại bỏ phần tử trùng;
- biểu diễn tập hợp;
- intersection, union và difference.

### 8.8. Priority Queue / Heap

Priority Queue quản lý các phần tử kèm theo mức ưu tiên. Phần tử được lấy ra không nhất thiết là phần tử được đưa vào trước, mà là phần tử có độ ưu tiên cao nhất hoặc thấp nhất tùy quy ước.

Heap là một cấu trúc phổ biến để cài đặt Priority Queue.

Ứng dụng:

- Dijkstra;
- A*;
- event simulation;
- scheduling;
- branch-and-bound;
- duy trì top-k.

### 8.9. Tree

Tree biểu diễn quan hệ phân cấp giữa các đối tượng.

Một node có thể có node cha và các node con.

Ví dụ ứng dụng:

- file system;
- organization hierarchy;
- syntax tree;
- decision tree.

Tree đặc biệt phù hợp với dữ liệu có cấu trúc phân cấp.

### 8.10. Binary Search Tree

Binary Search Tree — BST là một cây nhị phân có tính chất thứ tự.

Với một node có key `x`:

- các key trong cây con trái nhỏ hơn `x`;
- các key trong cây con phải lớn hơn `x`;

theo quy ước đơn giản khi không có key trùng.

Trong trường hợp cây cân bằng, các thao tác:

- search;
- insert;
- delete;

có thể đạt thời gian:

```text
O(log n)
```

Nếu cây mất cân bằng nghiêm trọng, chi phí có thể suy giảm tới `O(n)`.

### 8.11. Graph

Graph gồm:

- vertices hoặc nodes;
- edges biểu diễn quan hệ giữa các đối tượng.

Graph phù hợp để mô hình hóa:

- road networks;
- social networks;
- computer networks;
- routing;
- dependency graphs;
- supply-chain networks.

Nhiều bài toán thuật toán quan trọng như shortest path, connectivity và flow đều được mô hình hóa trên graph.

### 8.12. Disjoint Set / Union-Find

Disjoint Set, còn gọi là Union-Find, quản lý một tập các phần tử được chia thành các nhóm rời nhau.

Hai thao tác cơ bản:

- `find(x)`: xác định đại diện của nhóm chứa `x`;
- `union(x, y)`: hợp nhất hai nhóm.

Ứng dụng:

- Kruskal's algorithm;
- connectivity;
- clustering;
- dynamic component merging.

Với các kỹ thuật như path compression và union by rank/size, Union-Find có hiệu năng rất tốt trong thực tế.

---

## 9. Choosing a Data Structure Based on Operations

Việc chọn cấu trúc dữ liệu nên bắt đầu từ câu hỏi:

> **Những thao tác nào xuất hiện thường xuyên nhất trong thuật toán?**

Ví dụ:

- Nếu cần truy cập liên tục theo index, array thường phù hợp.
- Nếu cần push/pop theo LIFO, stack là lựa chọn tự nhiên.
- Nếu cần xử lý theo thứ tự đến trước phục vụ trước, queue phù hợp.
- Nếu cần tra cứu theo key nhiều lần, hash table thường là lựa chọn tốt.
- Nếu cần liên tục lấy phần tử có priority tốt nhất, priority queue phù hợp.
- Nếu dữ liệu biểu diễn mạng lưới quan hệ, graph là mô hình tự nhiên.

Bảng định hướng:

| Nhu cầu chính | Cấu trúc dữ liệu thường phù hợp |
|---|---|
| Random access | Array |
| Frequent insertion/deletion at known position | Linked List |
| LIFO processing | Stack |
| FIFO processing | Queue |
| Two-ended operations | Deque |
| Fast key lookup | Hash Table |
| Membership queries | Set |
| Maintain min/max priority | Heap / Priority Queue |
| Hierarchical data | Tree |
| Ordered search | Balanced BST |
| Network relationships | Graph |
| Dynamic connectivity | Union-Find |

Bảng này chỉ mang tính định hướng. Một bài toán thực tế có thể cần kết hợp nhiều cấu trúc dữ liệu cùng lúc.

---

## 10. The Relationship Between Algorithms and Data Structures

Thuật toán và cấu trúc dữ liệu không nên được xem xét tách rời.

Một thuật toán mô tả cách xử lý dữ liệu, trong khi cấu trúc dữ liệu quyết định dữ liệu được tổ chức như thế nào để hỗ trợ các thao tác đó.

Một thay đổi trong cách tổ chức dữ liệu có thể làm thay đổi đáng kể hiệu năng.

### Ví dụ: Membership Test

Giả sử cần kiểm tra nhiều lần xem một giá trị có xuất hiện trong tập dữ liệu hay không.

Với list:

```python
target in values
```

Trong worst case, có thể phải kiểm tra toàn bộ danh sách.

Với hash set:

```python
target in values_set
```

Việc tra cứu thường có expected time gần `O(1)`.

Như vậy, cùng một thao tác logic — kiểm tra membership — nhưng cấu trúc dữ liệu khác nhau có thể dẫn đến hiệu năng rất khác.

Có thể tóm tắt:

> **Algorithms transform data; data structures organize data so that algorithms can manipulate it efficiently.**

Một nguyên tắc quan trọng khi thiết kế thuật toán là:

> **Hãy xác định các thao tác chi phối trước, sau đó chọn cấu trúc dữ liệu hỗ trợ tốt nhất cho các thao tác đó.**

---

## 11. Correctness, Efficiency, and Scalability

Khi đánh giá một thuật toán, không nên chỉ hỏi "thuật toán có chạy được hay không". Ba tiêu chí quan trọng hơn là correctness, efficiency và scalability.

### 11.1. Correctness

**Correctness** trả lời câu hỏi:

> Thuật toán có luôn tạo ra kết quả đúng cho mọi input hợp lệ hay không?

Tính đúng đắn là điều kiện cơ bản nhất. Một thuật toán chạy rất nhanh nhưng trả về kết quả sai không có giá trị.

Ví dụ, với thuật toán tìm maximum, kết quả phải không nhỏ hơn bất kỳ phần tử nào khác trong dữ liệu.

### 11.2. Efficiency

**Efficiency** xem xét lượng tài nguyên mà thuật toán sử dụng, chủ yếu là:

- thời gian;
- bộ nhớ.

Hai thuật toán có thể cùng giải đúng một bài toán nhưng khác nhau đáng kể về hiệu năng.

Ví dụ:

```text
Linear Search:  Θ(n)
Binary Search:  Θ(log n)
```

Tuy nhiên, Binary Search yêu cầu dữ liệu phải được sắp xếp và hỗ trợ truy cập phù hợp.

Vì vậy, không nên đánh giá thuật toán chỉ bằng một ký hiệu complexity mà bỏ qua điều kiện áp dụng.

### 11.3. Scalability

**Scalability** mô tả khả năng duy trì hiệu năng khi kích thước input tăng lên.

Ví dụ:

```text
n = 100
n = 10^6
n = 10^9
```

Một thuật toán `O(n²)` có thể hoạt động tốt với `n = 100`, nhưng trở nên không khả thi khi `n` rất lớn.

Scalability phụ thuộc vào:

- tốc độ tăng trưởng của thời gian chạy;
- bộ nhớ cần thiết;
- đặc điểm dữ liệu;
- khả năng song song hóa;
- giới hạn phần cứng và hệ thống.

Điểm quan trọng là:

> **Correctness cho biết thuật toán có đúng hay không; efficiency cho biết nó sử dụng tài nguyên thế nào; scalability cho biết nó còn khả thi hay không khi bài toán lớn lên.**

---

## 12. Tóm tắt

Những ý chính cần nhớ:

- **Problem** xác định nhiệm vụ cần giải.
- **Input** mô tả dữ liệu được cung cấp.
- **Output** mô tả kết quả cần tạo ra.
- **Algorithm** là quy trình hữu hạn và rõ ràng để biến input thành output.
- **Program** là hiện thực cụ thể của thuật toán bằng một ngôn ngữ lập trình.
- Một thuật toán cần có các tính chất như definiteness, finiteness, effectiveness và correctness.
- **Data structure** tổ chức dữ liệu để hỗ trợ các thao tác hiệu quả.
- Các thao tác cơ bản gồm access, search, insert, delete, update, traverse, membership, min/max, predecessor/successor, merge và split.
- **ADT** mô tả dữ liệu và hành vi ở mức trừu tượng, độc lập với cách cài đặt cụ thể.
- Các cấu trúc dữ liệu phổ biến gồm Array, Linked List, Stack, Queue, Deque, Hash Table, Set, Heap, Tree, BST, Graph và Union-Find.
- Không có một cấu trúc dữ liệu tốt nhất cho mọi bài toán.
- Lựa chọn cấu trúc dữ liệu nên dựa trên các thao tác được thực hiện thường xuyên nhất.
- Thuật toán và cấu trúc dữ liệu có mối quan hệ chặt chẽ và cần được thiết kế cùng nhau.
- Correctness, efficiency và scalability là ba tiêu chí quan trọng để đánh giá một lời giải.