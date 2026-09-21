# Chương 3. Danh sách liên kết (Linked Lists)

> **Tài liệu nền:** Chương 3 — *Linked Lists* trong *Data Structures and Algorithmic Thinking with Python* của Narasimha Karumanchi (2020).  
> Bài giảng giữ cách tiếp cận chính của chương: bắt đầu từ hạn chế của mảng, xây dựng khái niệm Linked List ADT, sau đó lần lượt xét danh sách liên kết đơn, danh sách liên kết đôi và danh sách liên kết vòng.  
> Các đoạn mã Python được **chuẩn hóa lại cho mục đích giảng dạy**, nhưng vẫn bám sát các thao tác và phân tích độ phức tạp của chương.

---

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- Giải thích được vì sao cần danh sách liên kết bên cạnh mảng.
- Mô tả được cấu trúc của một **node**, vai trò của `head`, `tail` và liên kết `next`/`prev`.
- Phân biệt:
  - danh sách liên kết đơn (*singly linked list*);
  - danh sách liên kết đôi (*doubly linked list*);
  - danh sách liên kết vòng (*circular linked list*).
- Cài đặt các thao tác cơ bản:
  - duyệt danh sách;
  - tìm kiếm;
  - chèn;
  - xóa;
  - đếm số node.
- Phân tích độ phức tạp thời gian và bộ nhớ của các thao tác.
- Vận dụng các kỹ thuật con trỏ thường gặp như:
  - hai con trỏ `slow`–`fast`;
  - đảo ngược danh sách;
  - tìm node thứ $k$ từ cuối;
  - phát hiện chu trình.

---

# 1. Từ mảng đến danh sách liên kết

## 1.1. Nhắc lại về mảng

Mảng lưu các phần tử trong một vùng nhớ liên tiếp.

Ví dụ:

```text
Index:    0      1      2      3
        +----+ +----+ +----+ +----+
Array:  |  4 | | 15 | |  7 | | 40 |
        +----+ +----+ +----+ +----+
```

Nhờ các phần tử nằm liên tiếp trong bộ nhớ, địa chỉ của phần tử tại vị trí `i` có thể được tính trực tiếp từ địa chỉ đầu mảng.

Vì vậy:

$$\text{access}(i) = O(1)$$

Đây là một ưu điểm rất lớn của mảng.

Tuy nhiên, mảng cũng có một số hạn chế:

- kích thước thường phải được xác định trước hoặc phải cấp phát lại khi mở rộng;
- chèn/xóa ở đầu hoặc giữa mảng có thể phải dịch chuyển nhiều phần tử;
- một mảng lớn cần một vùng nhớ liên tục đủ lớn;
- việc mở rộng một dynamic array đôi khi phải tạo vùng nhớ mới và sao chép dữ liệu.

---

## 1.2. Ý tưởng của danh sách liên kết

Thay vì yêu cầu các phần tử nằm liên tiếp trong bộ nhớ, ta lưu mỗi phần tử trong một **node**.

Mỗi node lưu:

1. dữ liệu;
2. một liên kết đến node tiếp theo.

```text
head
 |
 v
+------+------+
| data | next | ----+
+------+------+     |
                   v
              +------+------+
              | data | next | ----+
              +------+------+     |
                                  v
                             +------+------+
                             | data | None |
                             +------+------+
```

Một danh sách:

```text
4 -> 15 -> 7 -> 40 -> None
```

có thể được hình dung như:

```text
head
 |
 v
+---+---+    +----+---+    +---+---+    +----+------+
| 4 | *----->| 15 | *----->| 7 | *----->| 40 | None |
+---+---+    +----+---+    +---+---+    +----+------+
```

Các node **không cần nằm cạnh nhau trong bộ nhớ**. Liên kết giữa chúng được xác định bởi tham chiếu `next`.

---

# 2. Khái niệm cơ bản

## 2.1. Node

Trong danh sách liên kết đơn, một node gồm:

```text
+------------+------------+
|    data    |    next    |
+------------+------------+
```

Trong Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Ví dụ:

```python
p = Node(15)
```

Tại thời điểm này:

```text
p
|
v
+----+------+
| 15 | None |
+----+------+
```

---

## 2.2. `head`

`head` là tham chiếu đến **node đầu tiên** của danh sách.

Quan trọng:

> `head` không phải là một node đặc biệt. Nó chỉ là biến giữ tham chiếu tới node đầu tiên.

Danh sách rỗng:

```python
head = None
```

Danh sách có node:

```text
head
 |
 v
[4] -> [15] -> [7] -> None
```

---

## 2.3. `tail`

Ta có thể giữ thêm một tham chiếu `tail` đến node cuối cùng:

```text
head                         tail
 |                             |
 v                             v
[4] -> [15] -> [7] -> [40] -> None
```

`tail` không bắt buộc.

Nếu **chỉ giữ `head`**, muốn tìm node cuối phải duyệt toàn bộ danh sách: $O(n)$.

Nếu **giữ thêm `tail`**, việc chèn vào cuối có thể thực hiện trong $O(1)$.

---

# 3. Linked List ADT

Theo cách trình bày của Chương 3, các thao tác chính của Linked List ADT gồm:

- `insert`: chèn phần tử;
- `delete`: xóa phần tử.

Các thao tác phụ thường gặp:

- xóa toàn bộ danh sách;
- đếm số phần tử;
- tìm kiếm;
- tìm node thứ $k$ từ cuối danh sách.

Một thiết kế tối thiểu có thể gồm:

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
```

---

# 4. So sánh mảng và danh sách liên kết

## 4.1. Khả năng truy cập

Với mảng, việc truy cập trực tiếp phần tử thứ $i$ qua `A[i]` chỉ mất:

$$T(n) = O(1)$$

Với danh sách liên kết, muốn đến node thứ $i$, ta phải duyệt tuần tự từ `head`:

```text
head -> node 0 -> node 1 -> node 2 -> ... -> node i
```

Do đó, trong trường hợp xấu nhất:

$$T(n) = O(n)$$

---

## 4.2. Chèn/xóa

Danh sách liên kết không cần dịch chuyển toàn bộ các phần tử phía sau.

Ví dụ muốn chèn `12` giữa `5` và `8`:

Trước:

```text
[5] --------> [8]
```

Sau:

```text
[5] ----> [12] ----> [8]
```

Ta chủ yếu thay đổi các liên kết.

Tuy nhiên cần phân biệt hai chi phí:

1. **tìm vị trí cần chèn/xóa**;
2. **thay đổi liên kết**.

Nếu đã có tham chiếu tới đúng node, thay đổi liên kết thường chỉ mất $O(1)$.

Nhưng nếu phải tìm node đó từ `head`, tổng thời gian có thể là $O(n)$.

---

## 4.3. Bảng so sánh

| Thao tác | Mảng / Dynamic Array | Singly Linked List |
|---|---:|---:|
| Truy cập phần tử thứ $i$ | $O(1)$ | $O(n)$ |
| Tìm kiếm không có thứ tự | $O(n)$ | $O(n)$ |
| Chèn ở đầu | $O(n)$ do dịch chuyển | $O(1)$ |
| Xóa ở đầu | $O(n)$ do dịch chuyển | $O(1)$ |
| Chèn ở cuối | thường $O(1)$ amortized với dynamic array | $O(n)$ nếu chỉ giữ `head` |
| Chèn ở cuối nếu có `tail` | — | $O(1)$ |
| Chèn sau một node đã biết | không áp dụng trực tiếp | $O(1)$ |
| Xóa sau một node đã biết | không áp dụng trực tiếp | $O(1)$ |
| Bộ nhớ phụ | có thể thừa dung lượng | thêm bộ nhớ cho các liên kết |

---

## 4.4. Một lưu ý quan trọng trong Python

`list` của Python:

```python
A = [4, 15, 7, 40]
```

**không phải** là linked list.

Python `list` về bản chất gần với **dynamic array** hơn.

Vì vậy:

```python
A[100]
```

có thể truy cập theo chỉ số nhanh, trong khi linked list không hỗ trợ random access như vậy.

---

# 5. Danh sách liên kết đơn — Singly Linked List

## 5.1. Cấu trúc

Mỗi node có:

- `data`;
- `next`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Danh sách:

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
```

---

# 6. Duyệt danh sách liên kết đơn

Giả sử:

```text
head
 |
 v
[4] -> [15] -> [7] -> [40] -> None
```

Ta bắt đầu từ `head`, sau đó liên tục:

```python
current = current.next
```

cho đến khi:

```python
current is None
```

Cài đặt:

```python
def traverse(self):
    current = self.head

    while current is not None:
        print(current.data)
        current = current.next
```

Do phải duyệt qua $n$ node và chỉ dùng một biến con trỏ `current`:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

## 6.1. Đếm số node

```python
def count_nodes(self):
    current = self.head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count
```

Độ phức tạp:

$$T(n) = O(n)$$

Nếu cấu trúc dữ liệu duy trì sẵn biến `length`, việc lấy số node chỉ cần:

```python
return self.length
```

khi đó:

$$T(n) = O(1)$$

---

# 7. Tìm kiếm trên singly linked list

```python
def search(self, value):
    current = self.head

    while current is not None:
        if current.data == value:
            return True

        current = current.next

    return False
```

Ví dụ tìm `7`:

```text
4 -> 15 -> 7 -> 40
^
```

```text
4 -> 15 -> 7 -> 40
     ^
```

```text
4 -> 15 -> 7 -> 40
           ^
           found
```

Trường hợp xấu nhất phải duyệt toàn bộ danh sách:

$$T(n) = O(n)$$

---

# 8. Chèn node trong singly linked list

Có ba trường hợp cơ bản:

1. chèn ở đầu;
2. chèn ở cuối;
3. chèn ở giữa.

---

## 8.1. Chèn ở đầu

Ban đầu:

```text
head
 |
 v
[4] -> [15] -> [7] -> None
```

Chèn `2`.

### Bước 1

Tạo node mới:

```text
new
 |
 v
[2] -> None
```

### Bước 2

Cho `new.next` trỏ tới head cũ:

```text
new
 |
 v
[2] ------+
          |
          v
         [4] -> [15] -> [7] -> None
          ^
          |
        head
```

### Bước 3

Đưa `head` sang node mới:

```text
head
 |
 v
[2] -> [4] -> [15] -> [7] -> None
```

Cài đặt:

```python
def insert_front(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

    self.length += 1
```

Không phụ thuộc vào $n$:

$$T(n) = O(1)$$

---

## 8.2. Chèn ở cuối

Nếu chỉ có `head`, trước hết phải tìm node cuối.

```text
head
 |
 v
[4] -> [15] -> [7] -> None
                     ^
                     current
```

Sau đó:

```text
[4] -> [15] -> [7] -> [40] -> None
```

Cài đặt:

```python
def insert_end(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        self.length += 1
        return

    current = self.head

    while current.next is not None:
        current = current.next

    current.next = new_node
    self.length += 1
```

Do phải tìm node cuối:

$$T(n) = O(n)$$

### Nếu duy trì thêm `tail`

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
```

thì append có thể trở thành:

```python
def insert_end(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1
```

Khi đó:

$$T(n) = O(1)$$

---

## 8.3. Chèn sau một node đã biết

Giả sử cần chèn `12` sau node `5`.

Trước:

```text
          p
          |
          v
[2] -> [5] --------> [8] -> None
```

### Bước 1

```python
new_node.next = p.next
```

```text
          p
          |
          v
[2] -> [5] --------> [8] -> None
          \
           \--> [12] ---+
                        |
                        +----> [8]
```

### Bước 2

```python
p.next = new_node
```

Kết quả:

```text
[2] -> [5] -> [12] -> [8] -> None
```

Cài đặt:

```python
def insert_after(self, node, data):
    if node is None:
        return

    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

    self.length += 1
```

Nếu `node` đã được cho trước:

$$T(n) = O(1)$$

---

## 8.4. Chèn tại vị trí `index`

Giả sử vị trí bắt đầu từ `0`.

```python
def insert_at(self, index, data):
    if index < 0 or index > self.length:
        raise IndexError("index out of range")

    if index == 0:
        self.insert_front(data)
        return

    previous = self.head

    for _ in range(index - 1):
        previous = previous.next

    new_node = Node(data)
    new_node.next = previous.next
    previous.next = new_node

    self.length += 1
```

Phần nối node chỉ là $O(1)$, nhưng việc đi đến vị trí `index - 1` có thể mất $O(n)$. Vì vậy, trong trường hợp xấu nhất:

$$T(n) = O(n)$$

---

# 9. Xóa node trong singly linked list

Tương tự thao tác chèn, ta xét:

1. xóa node đầu;
2. xóa node cuối;
3. xóa node ở giữa.

---

## 9.1. Xóa node đầu

Ban đầu:

```text
head
 |
 v
[4] -> [15] -> [7] -> None
```

Chỉ cần:

```python
self.head = self.head.next
```

Kết quả:

```text
head
 |
 v
[15] -> [7] -> None
```

Cài đặt:

```python
def delete_front(self):
    if self.head is None:
        return None

    removed = self.head
    self.head = self.head.next

    removed.next = None
    self.length -= 1

    return removed.data
```

Độ phức tạp:

$$T(n) = O(1)$$

---

## 9.2. Xóa node cuối

Muốn xóa node cuối trong singly linked list, ta cần node đứng trước nó.

```text
head
 |
 v
[4] -> [15] -> [7] -> [40] -> None
              previous  current
```

Sau đó:

```python
previous.next = None
```

Cài đặt:

```python
def delete_end(self):
    if self.head is None:
        return None

    if self.head.next is None:
        value = self.head.data
        self.head = None
        self.length = 0
        return value

    previous = None
    current = self.head

    while current.next is not None:
        previous = current
        current = current.next

    previous.next = None
    self.length -= 1

    return current.data
```

Do phải duyệt danh sách:

$$T(n) = O(n)$$

---

## 9.3. Xóa node sau một node đã biết

Giả sử:

```text
          p
          |
          v
[2] -> [5] -> [12] -> [8] -> None
```

Muốn xóa node `12`:

```python
p.next = p.next.next
```

Kết quả:

```text
[2] -> [5] ----------> [8] -> None
```

Cài đặt:

```python
def delete_after(self, node):
    if node is None or node.next is None:
        return None

    removed = node.next
    node.next = removed.next

    removed.next = None
    self.length -= 1

    return removed.data
```

Nếu `node` đã được biết:

$$T(n) = O(1)$$

---

## 9.4. Xóa theo giá trị

```python
def delete_value(self, value):
    if self.head is None:
        return False

    if self.head.data == value:
        self.delete_front()
        return True

    previous = self.head
    current = self.head.next

    while current is not None:
        if current.data == value:
            previous.next = current.next
            current.next = None
            self.length -= 1
            return True

        previous = current
        current = current.next

    return False
```

Trường hợp xấu nhất:

$$T(n) = O(n)$$

---

# 10. Cài đặt hoàn chỉnh một singly linked list đơn giản

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        self.length += 1

    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False

    def delete_front(self):
        if self.head is None:
            return None

        removed = self.head
        self.head = self.head.next
        removed.next = None
        self.length -= 1

        return removed.data

    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.delete_front()
            return True

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                previous.next = current.next
                current.next = None
                self.length -= 1
                return True

            previous = current
            current = current.next

        return False

    def to_list(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result
```

Ví dụ sử dụng:

```python
linked_list = SinglyLinkedList()

linked_list.insert_end(4)
linked_list.insert_end(15)
linked_list.insert_end(7)

linked_list.insert_front(2)

print(linked_list.to_list())
# [2, 4, 15, 7]

linked_list.delete_value(15)

print(linked_list.to_list())
# [2, 4, 7]
```

---

# 11. Danh sách liên kết đôi — Doubly Linked List

## 11.1. Ý tưởng

Trong singly linked list:

```text
[4] -> [15] -> [7]
```

mỗi node chỉ biết node tiếp theo.

Trong doubly linked list, mỗi node có:

- `prev`: node trước;
- `next`: node sau.

```text
None <- [4] <-> [15] <-> [7] -> None
```

Cấu trúc node:

```text
+--------+--------+--------+
|  prev  |  data  |  next  |
+--------+--------+--------+
```

Python:

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

---

## 11.2. Ưu điểm

Có thể di chuyển theo cả hai hướng:

```text
next:  ---->
prev:  <----
```

Nếu đã có tham chiếu trực tiếp đến một node, ta có thể truy cập node đứng trước qua:

```python
node.prev
```

Điều này giúp thao tác xóa node thuận tiện hơn so với singly linked list.

---

## 11.3. Nhược điểm

Mỗi node phải lưu thêm một tham chiếu:

```python
prev
```

nên tốn thêm bộ nhớ.

Ngoài ra, chèn/xóa cần cập nhật nhiều liên kết hơn.

---

# 12. Duyệt doubly linked list

Giả sử có cả `head` và `tail`.

```text
head                         tail
 |                             |
 v                             v
[4] <-> [15] <-> [7] <-> [40]
```

Duyệt xuôi:

```python
current = self.head

while current is not None:
    print(current.data)
    current = current.next
```

Duyệt ngược:

```python
current = self.tail

while current is not None:
    print(current.data)
    current = current.prev
```

Cả hai đều có:

$$T(n) = O(n)$$

---

# 13. Chèn trong doubly linked list

## 13.1. Chèn ở đầu

Trước:

```text
None <- [4] <-> [15] <-> [7] -> None
         ^
         |
        head
```

Chèn `2`:

```text
None <- [2] <-> [4] <-> [15] <-> [7] -> None
         ^
         |
        head
```

Các liên kết cần cập nhật:

```python
new_node.next = self.head
self.head.prev = new_node
self.head = new_node
```

Cài đặt:

```python
def insert_front(self, data):
    new_node = DoublyNode(data)

    if self.head is None:
        self.head = self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    self.length += 1
```

Độ phức tạp:

$$T(n) = O(1)$$

---

## 13.2. Chèn ở cuối

```python
def insert_end(self, data):
    new_node = DoublyNode(data)

    if self.tail is None:
        self.head = self.tail = new_node
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1
```

Nếu có `tail`:

$$T(n) = O(1)$$

---

## 13.3. Chèn sau một node

Trước:

```text
[5] <----------> [12]
 ^
 |
 p
```

Chèn `8` sau `p`:

```text
[5] <-> [8] <-> [12]
```

Cần cập nhật:

```python
new_node.prev = p
new_node.next = p.next

if p.next is not None:
    p.next.prev = new_node

p.next = new_node
```

Nếu chèn sau `tail`, cần cập nhật `tail`.

---

# 14. Xóa trong doubly linked list

Đây là một trong những ưu điểm quan trọng của doubly linked list.

Giả sử:

```text
[4] <-> [8] <-> [12]
          ^
          |
          p
```

Muốn xóa `p`.

Ta cần nối:

```text
[4] <----------> [12]
```

Hai phía được cập nhật:

```python
p.prev.next = p.next
p.next.prev = p.prev
```

Cần xử lý riêng khi `p` là `head` hoặc `tail`.

Cài đặt tổng quát:

```python
def delete_node(self, node):
    if node is None:
        return None

    if node.prev is None:
        self.head = node.next
    else:
        node.prev.next = node.next

    if node.next is None:
        self.tail = node.prev
    else:
        node.next.prev = node.prev

    node.prev = None
    node.next = None

    self.length -= 1

    return node.data
```

Nếu đã có trực tiếp `node`:

$$T(n) = O(1)$$

Đây là khác biệt đáng chú ý so với singly linked list: nếu chỉ có con trỏ đến node cần xóa, singly linked list thường còn cần biết node trước đó.

---

# 15. Cài đặt doubly linked list tối giản

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_front(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def insert_end(self, data):
        new_node = DoublyNode(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def delete_node(self, node):
        if node is None:
            return None

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

        self.length -= 1
        return node.data

    def forward(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result

    def backward(self):
        result = []
        current = self.tail

        while current is not None:
            result.append(current.data)
            current = current.prev

        return result
```

---

# 16. Singly linked list và doubly linked list

| Đặc điểm | Singly Linked List | Doubly Linked List |
|---|---|---|
| Liên kết mỗi node | `next` | `prev`, `next` |
| Duyệt xuôi | Có | Có |
| Duyệt ngược | Không trực tiếp | Có |
| Bộ nhớ mỗi node | ít hơn | nhiều hơn |
| Xóa node khi đã có chính node đó | thường cần biết predecessor | $O(1)$ nhờ `prev` |
| Số liên kết phải cập nhật | ít hơn | nhiều hơn |

---

# 17. Danh sách liên kết vòng — Circular Linked List

## 17.1. Khái niệm

Trong linked list thông thường, node cuối có:

```python
next = None
```

Trong circular linked list, node cuối liên kết ngược lại node đầu.

```text
head
 |
 v
[4] -> [15] -> [7] -> [40]
 ^                       |
 |_______________________|
```

Do đó:

```python
tail.next == head
```

Không có node cuối nào có `next = None`.

---

## 17.2. Vì sao phải cẩn thận khi duyệt?

Đoạn mã sau là sai:

```python
while current is not None:
    current = current.next
```

Với circular linked list, `current` không trở thành `None`.

Ta phải dừng khi quay lại `head`.

Ví dụ:

```python
def traverse_circular(head):
    if head is None:
        return

    current = head

    while True:
        print(current.data)
        current = current.next

        if current == head:
            break
```

---

## 17.3. Ứng dụng

Một ứng dụng điển hình được nêu trong chương là cơ chế **round robin**.

Ví dụ có các tiến trình:

```text
P1 -> P2 -> P3 -> P4
^                 |
|_________________|
```

Sau `P4`, hệ thống quay lại `P1`.

Ý tưởng này phù hợp với các bài toán trong đó các phần tử cần được xử lý tuần hoàn.

---

# 18. Một circular singly linked list đơn giản

Ta giữ `tail`.

Khi danh sách không rỗng:

```python
tail.next == head
```

Cài đặt:

```python
class CircularLinkedList:
    def __init__(self):
        self.tail = None

    @property
    def head(self):
        if self.tail is None:
            return None
        return self.tail.next
```

---

## 18.1. Chèn vào cuối

### Danh sách rỗng

Tạo node duy nhất:

```text
    +-------+
    |       |
    v       |
   [5] -----+
```

Node đó vừa là `head` vừa là `tail`.

```python
new_node.next = new_node
self.tail = new_node
```

### Danh sách không rỗng

Trước:

```text
head
 |
 v
[4] -> [15] -> [7]
 ^              |
 |______________|
                ^
                |
               tail
```

Chèn `40`:

```python
new_node.next = self.tail.next
self.tail.next = new_node
self.tail = new_node
```

Cài đặt:

```python
def append(self, data):
    new_node = Node(data)

    if self.tail is None:
        new_node.next = new_node
        self.tail = new_node
        return

    new_node.next = self.tail.next
    self.tail.next = new_node
    self.tail = new_node
```

Nếu giữ `tail`:

$$T(n) = O(1)$$

---

# 19. Bảng độ phức tạp quan trọng

Giả sử singly linked list cơ bản chỉ giữ `head`, trừ khi ghi chú khác.

| Thao tác | Singly LL | Doubly LL với `head`, `tail` |
|---|---:|---:|
| Truy cập node thứ $i$ | $O(n)$ | $O(n)$ |
| Tìm kiếm | $O(n)$ | $O(n)$ |
| Duyệt toàn bộ | $O(n)$ | $O(n)$ |
| Chèn đầu | $O(1)$ | $O(1)$ |
| Xóa đầu | $O(1)$ | $O(1)$ |
| Chèn cuối | $O(n)$ | $O(1)$ |
| Chèn cuối nếu singly LL có `tail` | $O(1)$ | — |
| Xóa cuối | $O(n)$ | $O(1)$ nếu có `tail` |
| Chèn sau node đã biết | $O(1)$ | $O(1)$ |
| Xóa node đã biết | cần predecessor hoặc tìm từ `head` | $O(1)$ |

Điểm cần nhớ:

> Linked list không tự động làm mọi thao tác chèn/xóa trở thành $O(1)$.  
> Thao tác **nối/xóa liên kết** có thể là $O(1)$, nhưng **tìm đúng vị trí** vẫn có thể cần $O(n)$.

---

# 20. Kỹ thuật hai con trỏ

Chương Linked Lists có nhiều bài toán có thể giải hiệu quả bằng cách dùng hai con trỏ.

---

## 20.1. Tìm node giữa

Dùng:

- `slow`: mỗi lần đi 1 node;
- `fast`: mỗi lần đi 2 node.

```python
def middle_node(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
```

Ví dụ:

```text
1 -> 2 -> 3 -> 4 -> 5
S
F
```

Sau mỗi vòng lặp:

```text
1 -> 2 -> 3 -> 4 -> 5
     S    F
```

```text
1 -> 2 -> 3 -> 4 -> 5
          S         F
```

Khi `fast` tới cuối, `slow` ở giữa.

$$T(n) = O(n), \quad S(n) = O(1)$$

---

## 20.2. Kiểm tra số node chẵn hay lẻ

Cho một con trỏ nhảy 2 node mỗi lần.

```python
def is_even_length(head):
    current = head

    while current is not None and current.next is not None:
        current = current.next.next

    return current is None
```

Nếu cuối cùng:

```python
current is None
```

thì độ dài chẵn.

Nếu `current` dừng tại node cuối:

```python
current.next is None
```

thì độ dài lẻ.

---

# 21. Tìm node thứ $k$ từ cuối

Ví dụ:

```text
10 -> 20 -> 30 -> 40 -> 50 -> None
```

Node thứ `2` từ cuối là `40`.

Không cần đếm tổng số node trước.

Ta dùng hai con trỏ:

- `fast`;
- `slow`.

Đầu tiên cho `fast` đi trước $k$ bước.

Sau đó cho cả hai đi cùng tốc độ.

```python
def kth_from_end(head, k):
    if k <= 0:
        return None

    slow = head
    fast = head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow
```

Khoảng cách giữa hai con trỏ luôn là $k$.

Khi `fast` chạm cuối, `slow` chính là node thứ $k$ từ cuối. Độ phức tạp:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

# 22. Đảo ngược singly linked list

Ban đầu:

```text
head
 |
 v
[1] -> [2] -> [3] -> [4] -> None
```

Mục tiêu:

```text
head
 |
 v
[4] -> [3] -> [2] -> [1] -> None
```

Ta dùng ba tham chiếu:

- `previous`;
- `current`;
- `next_node`.

```python
def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next

        current.next = previous

        previous = current
        current = next_node

    return previous
```

Điểm quan trọng:

```python
next_node = current.next
```

phải thực hiện **trước khi** đổi:

```python
current.next = previous
```

nếu không ta có thể làm mất phần còn lại của danh sách.

Độ phức tạp:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

# 23. Phát hiện chu trình — Floyd's Cycle Detection

Một linked list bình thường:

```text
1 -> 2 -> 3 -> 4 -> None
```

Một linked list có chu trình:

```text
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

Dùng:

- `slow`: đi 1 bước;
- `fast`: đi 2 bước.

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
```

Nếu tồn tại chu trình, `fast` cuối cùng sẽ bắt kịp `slow`.

Độ phức tạp:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

# 24. Ghép hai danh sách đã sắp xếp

Ví dụ:

```text
L1: 1 -> 4 -> 7
L2: 2 -> 3 -> 8
```

Kết quả:

```text
1 -> 2 -> 3 -> 4 -> 7 -> 8
```

Ta dùng một node giả `dummy`.

```python
def merge_sorted_lists(a, b):
    dummy = Node(0)
    tail = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return dummy.next
```

Nếu hai danh sách có lần lượt $m$ và $n$ node:

$$T(m, n) = O(m + n), \quad S(m, n) = O(1)$$

(do có thể nối lại trực tiếp các node cũ mà không cần cấp phát thêm bộ nhớ).

---

# 25. Kiểm tra palindrome

Ví dụ:

```text
1 -> 2 -> 3 -> 2 -> 1
```

là palindrome.

Một cách hiệu quả:

1. tìm giữa danh sách bằng `slow`/`fast`;
2. đảo nửa sau;
3. so sánh hai nửa;
4. nếu cần, đảo lại nửa sau để khôi phục danh sách.

Ý tưởng:

```text
1 -> 2 -> 3 -> 2 -> 1
          ^
        middle
```

Đảo nửa sau:

```text
1 -> 2 -> 3     1 -> 2
```

sau đó so sánh:

```text
1 == 1
2 == 2
```

Độ phức tạp:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

# 26. Những lỗi thường gặp

## 26.1. Làm mất phần còn lại của danh sách

Sai:

```python
current.next = previous
current = current.next
```

Sau dòng đầu, `current.next` đã thay đổi.

Đúng:

```python
next_node = current.next
current.next = previous
current = next_node
```

---

## 26.2. Quên xử lý danh sách rỗng

Ví dụ:

```python
current = self.head
while current.next is not None:
    ...
```

sẽ lỗi nếu:

```python
self.head is None
```

Cần kiểm tra trước:

```python
if self.head is None:
    return
```

---

## 26.3. Quên cập nhật `head`

Khi chèn hoặc xóa node đầu, `head` phải được cập nhật.

Ví dụ chèn đầu:

```python
new_node.next = self.head
self.head = new_node
```

---

## 26.4. Quên cập nhật cả hai hướng trong doubly linked list

Khi thay:

```text
A <-> B <-> C
```

thành:

```text
A <-> C
```

phải cập nhật cả:

```python
A.next = C
C.prev = A
```

Chỉ cập nhật một phía sẽ làm cấu trúc không còn nhất quán.

---

## 26.5. Duyệt circular linked list bằng điều kiện `None`

Sai:

```python
while current is not None:
    current = current.next
```

Có thể chạy vô hạn.

Phải dừng khi quay lại node ban đầu.

---

# 27. Khi nào nên sử dụng linked list?

Linked list phù hợp khi:

- số phần tử thay đổi thường xuyên;
- cần chèn/xóa ở đầu nhiều;
- thường xuyên chèn/xóa sau một node đã biết;
- không cần truy cập ngẫu nhiên theo chỉ số;
- cần cấu trúc tuần hoàn, ví dụ round robin;
- linked list được dùng làm cấu trúc nền cho một ADT khác.

Linked list không phù hợp khi:

- thao tác phổ biến là `A[i]`;
- cần binary search;
- hiệu năng cache rất quan trọng;
- mỗi node rất nhỏ nhưng số lượng cực lớn, khiến overhead của liên kết trở nên đáng kể.

---

# 28. Linked list là nền tảng của nhiều cấu trúc khác

Ý tưởng node + liên kết sẽ xuất hiện lại trong:

- Stack;
- Queue;
- Trees;
- Graph adjacency lists;
- Hash table với separate chaining.

Do đó linked list không chỉ là một cấu trúc dữ liệu riêng lẻ, mà còn giúp sinh viên làm quen với tư duy:

> dữ liệu có thể được tổ chức bằng **quan hệ liên kết giữa các object**, thay vì chỉ bằng vị trí trong một vùng nhớ liên tục.

---

# 29. Tóm tắt

Một linked list gồm các node được nối với nhau bằng các tham chiếu.

Singly linked list:

```text
[data | next] -> [data | next] -> ...
```

Doubly linked list:

```text
[prev | data | next] <-> [prev | data | next]
```

Circular linked list:

```text
node cuối -> node đầu
```

Ba ý quan trọng nhất:

1. Linked list **không hỗ trợ random access** nên truy cập theo vị trí thường là $O(n)$.
2. Nếu đã có đúng node hoặc predecessor cần thao tác, nhiều phép chèn/xóa chỉ cần $O(1)$.
3. Phần khó nhất của linked list không phải dữ liệu trong node mà là **cập nhật các liên kết đúng thứ tự**.

---

# 30. Tự kiểm tra

### Câu 1

Cho danh sách:

```text
head -> 5 -> 8 -> 12 -> None
```

Giá trị của:

```python
head.next.next.data
```

là bao nhiêu?

<details>
<summary>Đáp án</summary>

`12`.

- `head` là node `5`;
- `head.next` là node `8`;
- `head.next.next` là node `12`.

</details>

---

### Câu 2

Vì sao truy cập node thứ $i$ của singly linked list là $O(n)$ trong trường hợp xấu nhất?

<details>
<summary>Đáp án</summary>

Vì linked list không lưu các node liên tiếp để có thể tính trực tiếp địa chỉ node thứ $i$. Ta phải bắt đầu từ `head` và đi qua các liên kết `next` cho tới node cần tìm.

</details>

---

### Câu 3

Cho:

```text
head -> 4 -> 7 -> 9 -> None
```

Muốn chèn `5` sau node `4`, hai phép gán quan trọng là gì?

<details>
<summary>Đáp án</summary>

Giả sử `p` trỏ tới node `4`:

```python
new_node.next = p.next
p.next = new_node
```

Thứ tự này giúp không làm mất phần danh sách bắt đầu từ node `7`.

</details>

---

### Câu 4

Trong doubly linked list, mỗi node cần thêm trường nào so với singly linked list?

<details>
<summary>Đáp án</summary>

`prev`, dùng để trỏ đến node đứng trước.

</details>

---

### Câu 5

Tại sao không thể dùng:

```python
while current is not None:
```

để duyệt circular linked list?

<details>
<summary>Đáp án</summary>

Vì trong circular linked list, node cuối trỏ về node đầu nên `current` không trở thành `None`. Điều kiện dừng phải dựa vào việc con trỏ quay lại `head` hoặc node xuất phát.

</details>

---

### Câu 6

Một singly linked list chỉ giữ `head`. Độ phức tạp của `insert_end` là gì?

<details>
<summary>Đáp án</summary>

- **Độ phức tạp:** $O(n)$, vì phải duyệt đến node cuối trước khi nối node mới.
- Nếu giữ thêm `tail`, thao tác này có thể giảm xuống $O(1)$.

</details>

---

### Câu 7

Một doubly linked list có `head` và `tail`. Nếu đã có trực tiếp tham chiếu đến node cần xóa, độ phức tạp của việc xóa là gì?

<details>
<summary>Đáp án</summary>

- **Độ phức tạp:** $O(1)$, vì có thể truy cập cả `node.prev` và `node.next` để nối hai node lân cận mà không cần duyệt tìm kiếm.

</details>

---

# 31. Bài tập lập trình ngắn

## Bài 1. In toàn bộ phần tử

Viết hàm:

```python
def print_list(head):
    pass
```

để in các phần tử của singly linked list từ đầu đến cuối.

Ví dụ:

```text
2 -> 5 -> 8 -> None
```

Kết quả:

```text
2 5 8
```

<details>
<summary>Gợi ý</summary>

Bắt đầu từ `current = head`, sau đó liên tục cập nhật:

```python
current = current.next
```

cho đến khi `current is None`.

</details>

---

## Bài 2. Tính tổng các phần tử

Viết:

```python
def sum_list(head):
    pass
```

Ví dụ:

```text
2 -> 5 -> 8 -> None
```

trả về:

```python
15
```

<details>
<summary>Gợi ý</summary>

Duyệt danh sách một lần và cộng:

```python
total += current.data
```

Độ phức tạp mong đợi: $O(n)$.

</details>

---

## Bài 3. Đếm số lần xuất hiện

Viết:

```python
def count_value(head, x):
    pass
```

để đếm số node có giá trị bằng `x`.

Ví dụ:

```text
3 -> 7 -> 3 -> 5 -> 3 -> None
```

với `x = 3`, kết quả là `3`.

---

## Bài 4. Chèn sau node đầu tiên có giá trị `x`

Viết:

```python
def insert_after_value(head, x, value):
    pass
```

Nếu tìm thấy node đầu tiên có `data == x`, chèn `value` ngay sau node đó.

Ví dụ:

```text
2 -> 5 -> 8
```

với:

```python
x = 5
value = 7
```

kết quả:

```text
2 -> 5 -> 7 -> 8
```

---

## Bài 5. Xóa node đầu tiên có giá trị `x`

Viết:

```python
def delete_first_value(head, x):
    pass
```

Chú ý trường hợp node cần xóa chính là `head`.

---

## Bài 6. Tìm node giữa

Viết hàm sử dụng hai con trỏ:

```python
def middle_node(head):
    pass
```

Không được đếm số node trước.

Độ phức tạp mong đợi: $T(n) = O(n)$ thời gian và $S(n) = O(1)$ bộ nhớ phụ.

---

## Bài 7. Tìm phần tử thứ $k$ từ cuối

Viết:

```python
def kth_from_end(head, k):
    pass
```

Chỉ được duyệt danh sách một lần theo nghĩa mỗi con trỏ chỉ tiến về phía trước.

---

## Bài 8. Đảo ngược danh sách

Viết:

```python
def reverse_list(head):
    pass
```

Không tạo một linked list mới.

Yêu cầu:

$$T(n) = O(n), \quad S(n) = O(1)$$

---

# 32. Bài tập phân tích

## Bài 1

Cho singly linked list chỉ có `head`.

Phân tích độ phức tạp của:

```python
def get_last(head):
    current = head

    while current.next is not None:
        current = current.next

    return current
```

<details>
<summary>Đáp án</summary>

- Trường hợp xấu nhất phải đi qua tất cả $n$ node: $T(n) = O(n)$.
- Bộ nhớ phụ: $S(n) = O(1)$.

</details>

---

## Bài 2

Cho node `p` đã biết thuộc singly linked list.

```python
new_node.next = p.next
p.next = new_node
```

Độ phức tạp là bao nhiêu?

<details>
<summary>Đáp án</summary>

- **Độ phức tạp:** $O(1)$, vì chỉ có một số hữu hạn phép gán tham chiếu và không cần duyệt danh sách.

</details>

---

## Bài 3

Tại sao tìm kiếm trên **sorted linked list** vẫn thường là $O(n)$, mặc dù dữ liệu đã có thứ tự?

<details>
<summary>Đáp án</summary>

Vì linked list không hỗ trợ truy cập trực tiếp node giữa theo chỉ số. Do đó không thể áp dụng binary search theo cách như trên mảng. Ta vẫn phải đi tuần tự qua các liên kết.

</details>

---

# 33. Câu hỏi thảo luận

1. Nếu một ứng dụng có rất nhiều thao tác đọc `A[i]` nhưng rất ít chèn/xóa, nên ưu tiên mảng hay linked list? Vì sao?
2. Nếu một hệ thống liên tục chèn phần tử vào đầu, linked list có lợi thế gì?
3. Tại sao doubly linked list thường dùng nhiều bộ nhớ hơn singly linked list?
4. Nếu ta luôn cần chèn ở cuối singly linked list, nên thay đổi cấu trúc dữ liệu như thế nào?
5. Circular linked list phù hợp với bài toán lập lịch round robin ở điểm nào?
6. Tại sao thao tác xóa node trong linked list phải đặc biệt cẩn thận với các tham chiếu?
7. Có thể dùng linked list để cài đặt Stack và Queue như thế nào?

---

# 34. Nội dung mở rộng của Chương 3

Chương 3 của tài liệu còn trình bày các hướng nâng cao như:

- memory-efficient doubly linked list;
- skip list;
- nhiều bài toán linked list trong phần *Problems & Solutions*.

Các chủ đề này phù hợp để học sau khi đã thành thạo:

- singly linked list;
- doubly linked list;
- circular linked list;
- các thao tác chèn/xóa;
- kỹ thuật hai con trỏ.

---

# 35. Checklist cuối bài

Sinh viên nên tự kiểm tra xem mình có thể làm được các việc sau mà không nhìn tài liệu hay không:

- [ ] Vẽ một singly linked list gồm 4 node.
- [ ] Giải thích `head` là gì.
- [ ] Viết lớp `Node`.
- [ ] Duyệt linked list bằng `while`.
- [ ] Chèn node ở đầu.
- [ ] Chèn node sau một node đã biết.
- [ ] Xóa node đầu.
- [ ] Xóa node sau một node đã biết.
- [ ] Giải thích vì sao truy cập theo index là $O(n)$.
- [ ] Phân biệt singly và doubly linked list.
- [ ] Giải thích circular linked list.
- [ ] Viết thuật toán tìm node giữa bằng `slow` và `fast`.
- [ ] Đảo ngược singly linked list trong $O(n)$ thời gian và $O(1)$ bộ nhớ phụ.
- [ ] Phát hiện cycle bằng Floyd's algorithm.

---

# Tài liệu tham khảo

Narasimha Karumanchi, *Data Structures and Algorithmic Thinking with Python: Data Structures and Algorithmic Puzzles*, CareerMonk Publications, 2020, Chapter 3: Linked Lists.
