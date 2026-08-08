# Lập trình hướng đối tượng trong Python

## Giới thiệu bài học

Bài học này giới thiệu các khái niệm nền tảng của **lập trình hướng đối tượng** (*Object-Oriented Programming – OOP*) trong Python. Người học bắt đầu từ hai khái niệm trung tâm là **class** và **object**, sau đó tìm hiểu cách một đối tượng lưu dữ liệu thông qua **attributes** và cung cấp hành vi thông qua **methods**.

Bài học tiếp tục làm rõ vai trò của `self`, `__init__()`, class attribute và instance attribute trước khi giới thiệu bốn trụ cột quan trọng của OOP: **Encapsulation**, **Inheritance**, **Polymorphism** và **Abstraction**. Phần cuối liên hệ các khái niệm OOP với việc mô tả và triển khai **Abstract Data Type (ADT)** và cấu trúc dữ liệu trong Python.

Các ví dụ được xây dựng ở mức cơ bản để người học vừa hiểu khái niệm, vừa có thể đọc và viết các class Python đơn giản. Cuối bài có **quiz**, bài đọc mã và **bài tập tự luyện** để củng cố kiến thức.

## Kiến thức và kỹ năng sẽ đạt được

Sau khi hoàn thành bài học, người học có thể:

- Giải thích được khái niệm **class** và **object**, đồng thời phân biệt được hai khái niệm này.
- Nhận biết được **state**, **behavior** và **identity** của một object.
- Phân biệt được **class attribute** và **instance attribute**.
- Giải thích được vai trò của method, `self` và `__init__()` trong một class Python.
- Tạo class, khởi tạo object và truy cập attribute/method bằng toán tử `.`.
- Giải thích được ý nghĩa của **Encapsulation, Inheritance, Polymorphism** và **Abstraction**.
- Sử dụng inheritance để xây dựng một class mới từ class đã có.
- Nhận biết và triển khai **method overriding** ở mức cơ bản.
- Giải thích được **duck typing** và cách polymorphism xuất hiện trong Python.
- Sử dụng `ABC` và `@abstractmethod` ở mức cơ bản để mô tả một abstract class.
- Giải thích được mối liên hệ giữa **ADT, interface và implementation**.
- Triển khai một cấu trúc dữ liệu đơn giản như `Stack` bằng class Python.
- Đọc, phân tích và dự đoán kết quả của các đoạn mã OOP cơ bản.

## Cấu trúc bài học

Bài học gồm các nội dung chính sau:

1. Giới thiệu về lập trình hướng đối tượng.
2. Class và Object.
3. Thuộc tính và phương thức.
4. `self` và `__init__()`.
5. Truy cập thuộc tính bằng toán tử `.`.
6. Bốn trụ cột của OOP:
   - Encapsulation;
   - Inheritance;
   - Polymorphism;
   - Abstraction.
7. Ví dụ tổng hợp.
8. Class và Object trong cấu trúc dữ liệu.
9. Phân biệt các khái niệm quan trọng.
10. Một số lỗi thường gặp.
11. Tóm tắt bài học.
12. Quiz và câu hỏi ôn tập.
13. Bài tập tự luyện.
14. Đáp án quiz.

---

## 1. Giới thiệu về lập trình hướng đối tượng

**Lập trình hướng đối tượng** (**Object-Oriented Programming – OOP**) là một cách tổ chức chương trình dựa trên các **đối tượng** (**objects**) và **lớp** (**classes**).

Thay vì chỉ tổ chức chương trình thành các hàm xử lý dữ liệu riêng lẻ, OOP cho phép chúng ta đặt **dữ liệu** và các **thao tác liên quan đến dữ liệu đó** trong cùng một đối tượng.

Một đối tượng thường có:

- **State – trạng thái:** dữ liệu đang được lưu trong đối tượng.
- **Behavior – hành vi:** những thao tác mà đối tượng có thể thực hiện.
- **Identity – định danh:** mỗi đối tượng là một thực thể riêng biệt trong chương trình.

Ví dụ, một đối tượng `Dog` có thể có:

- trạng thái: `name`, `age`;
- hành vi: `bark()`, `eat()`, `sleep()`;
- định danh: hai đối tượng `dog1` và `dog2` có thể có cùng dữ liệu nhưng vẫn là hai đối tượng khác nhau.

OOP đặc biệt hữu ích khi chương trình có nhiều loại đối tượng và mỗi đối tượng có dữ liệu cùng các thao tác riêng.

Các lợi ích chính của OOP gồm:

- tổ chức chương trình thành các thành phần rõ ràng;
- đóng gói dữ liệu và các thao tác liên quan;
- tái sử dụng mã nguồn;
- hỗ trợ mở rộng chương trình;
- mô hình hóa các thực thể trong bài toán;
- giúp chương trình dễ đọc, dễ kiểm thử và dễ bảo trì hơn.

Bốn khái niệm quan trọng thường được xem là các trụ cột của OOP gồm:

1. **Encapsulation – đóng gói**;
2. **Inheritance – kế thừa**;
3. **Polymorphism – đa hình**;
4. **Abstraction – trừu tượng hóa**.

<p align="center">
  <img src="images/oop-pillars-overview.png" alt="Bốn trụ cột của lập trình hướng đối tượng (OOP)" width="800" />
</p>

---

## 2. Class và Object

### 2.1. Class là gì?

**Class – lớp** là một khuôn mẫu dùng để tạo ra các đối tượng.

Một class thường định nghĩa:

- dữ liệu mà đối tượng cần lưu;
- các thao tác mà đối tượng có thể thực hiện.

Trong Python, một class được khai báo bằng từ khóa `class`.

Ví dụ:

```python
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Ở đây:

- `Dog` là tên class;
- `species` là **class attribute**;
- `name` và `age` là **instance attributes**;
- `__init__()` được sử dụng để thiết lập trạng thái ban đầu cho đối tượng;
- `self` tham chiếu tới đối tượng hiện tại.

Có thể hình dung:

```text
Class Dog
   |
   +-- species
   +-- name
   +-- age
   +-- các phương thức
```

Class **không phải là một đối tượng cụ thể**. Nó là mô tả chung cho các đối tượng sẽ được tạo ra.

---

### 2.2. Object là gì?

**Object – đối tượng** là một **instance** của một class.

Ví dụ:

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
```

`dog1` và `dog2` đều được tạo từ class `Dog`, nhưng chúng là hai đối tượng khác nhau.

```python
print(dog1.name)
print(dog2.name)
```

Kết quả:

```text
Buddy
Max
```

Ta có thể hình dung:

```text
             Dog
              |
        +-----+-----+
        |           |
      dog1        dog2
   name=Buddy    name=Max
   age=3         age=5
```

Hai đối tượng sử dụng cùng một class nhưng có thể lưu trạng thái khác nhau.

---

## 3. Thuộc tính và phương thức

### 3.1. Instance attribute

**Instance attribute** là thuộc tính thuộc về từng đối tượng riêng biệt.

Ví dụ:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Khi tạo:

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
```

thì:

```python
print(dog1.age)   # 3
print(dog2.age)   # 5
```

Mỗi đối tượng có một giá trị `age` riêng.

---

### 3.2. Class attribute

**Class attribute** là thuộc tính được khai báo trực tiếp bên trong class và bên ngoài các instance method.

Ví dụ:

```python
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name
```

Các đối tượng có thể cùng truy cập thuộc tính này:

```python
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)
print(dog2.species)
```

Kết quả:

```text
Canine
Canine
```

Có thể truy cập trực tiếp qua class:

```python
print(Dog.species)
```

Thông thường, nếu một giá trị mô tả **đặc điểm chung cho tất cả các instance**, ta có thể cân nhắc sử dụng class attribute.

---

### 3.3. Method

**Method – phương thức** là hàm được định nghĩa bên trong class.

Ví dụ:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking")
```

Sử dụng:

```python
dog1 = Dog("Buddy")
dog1.bark()
```

Kết quả:

```text
Buddy is barking
```

Method có thể truy cập và thay đổi trạng thái của đối tượng thông qua `self`.

Ví dụ:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1
```

```python
counter = Counter()

counter.increase()
counter.increase()

print(counter.value)
```

Kết quả:

```text
2
```

---

## 4. `self` và `__init__`

### 4.1. `self`

Trong instance method, tham số đầu tiên thường được đặt tên là `self`.

Ví dụ:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
```

Khi gọi:

```python
student = Student("An")
student.show_name()
```

Python về bản chất truyền đối tượng `student` vào tham số `self`.

Có thể hiểu gần tương đương với:

```python
Student.show_name(student)
```

Do đó:

```python
self.name
```

có nghĩa là:

> thuộc tính `name` của chính đối tượng đang thực hiện phương thức.

`self` không phải là từ khóa bắt buộc của Python, nhưng đây là quy ước chuẩn và nên luôn sử dụng tên này.

---

### 4.2. `__init__()`

`__init__()` là một **special method** được Python gọi sau khi một instance mới được tạo.

Nó thường được dùng để gán giá trị ban đầu cho các thuộc tính của đối tượng.

Ví dụ:

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```

Khi viết:

```python
student = Student("An", "SV001")
```

Python sẽ gọi:

```python
student.__init__("An", "SV001")
```

và đối tượng nhận được:

```text
name       = "An"
student_id = "SV001"
```

Trong các tài liệu nhập môn, `__init__()` thường được gọi đơn giản là **constructor**. Chính xác hơn trong Python, `__new__()` chịu trách nhiệm tạo instance, còn `__init__()` chịu trách nhiệm **khởi tạo trạng thái** của instance sau khi nó được tạo.

---

## 5. Truy cập thuộc tính bằng toán tử `.`

Thuộc tính và phương thức thường được truy cập thông qua toán tử dấu chấm `.`.

Ví dụ:

```python
class Student:
    university = "NEU"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")
```

```python
student = Student("An")

print(student.name)
print(student.university)
student.introduce()
```

Trong đó:

```python
student.name
```

truy cập instance attribute,

```python
student.university
```

truy cập class attribute,

và:

```python
student.introduce()
```

gọi một method của đối tượng.

---

## 6. Bốn trụ cột của OOP

### 6.1. Encapsulation – Đóng gói

**Encapsulation** là việc đặt dữ liệu và các thao tác liên quan vào trong cùng một class.

<p align="center">
  <img src="images/oop-encapsulation.png" alt="Tính đóng gói (Encapsulation) trong OOP" width="800" />
</p>

Ví dụ:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
```

Ở đây:

- `balance` biểu diễn trạng thái của tài khoản;
- `deposit()` và `withdraw()` là các thao tác làm thay đổi trạng thái đó;
- toàn bộ dữ liệu và hành vi liên quan tới tài khoản được đặt trong class `BankAccount`.

Sử dụng:

```python
account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)
```

Kết quả:

```text
1300
```

#### Mức độ truy cập trong Python

Khác với một số ngôn ngữ như Java hoặc C++, Python không thực thi `public`, `protected`, `private` theo cùng cơ chế.

Thông thường Python sử dụng quy ước:

```python
name       # thuộc tính thông thường
_name      # quy ước: chỉ nên sử dụng nội bộ
__name     # kích hoạt name mangling
```

Ví dụ:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

```python
account = BankAccount(1000)

print(account.get_balance())
```

`__balance` không phải là một private field tuyệt đối. Python thực hiện **name mangling** để hạn chế việc vô tình truy cập trực tiếp từ bên ngoài class.

Mục tiêu quan trọng của encapsulation không chỉ là "giấu dữ liệu", mà là:

> kiểm soát cách dữ liệu của đối tượng được sử dụng và thay đổi.

---

### 6.2. Inheritance – Kế thừa

**Inheritance** cho phép một class mới sử dụng lại hoặc mở rộng dữ liệu và hành vi của một class đã có.

<p align="center">
  <img src="images/oop-inheritance.png" alt="Tính kế thừa (Inheritance) trong OOP" width="800" />
</p>

Ví dụ:

```python
class Animal:
    def eat(self):
        print("Animal is eating")
```

Ta có thể xây dựng class `Dog` kế thừa từ `Animal`:

```python
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
```

Sử dụng:

```python
dog = Dog()

dog.eat()
dog.bark()
```

Kết quả:

```text
Animal is eating
Dog is barking
```

`Dog` không định nghĩa lại `eat()`, nhưng vẫn sử dụng được method này vì `Dog` kế thừa từ `Animal`.

Có thể hình dung:

```text
Animal
  |
  +-- eat()
  |
  v
 Dog
  |
  +-- bark()
```

Trong đó:

- `Animal`: **parent class**, **base class** hoặc **superclass**;
- `Dog`: **child class**, **derived class** hoặc **subclass**.

Inheritance giúp:

- tái sử dụng code;
- biểu diễn quan hệ phân cấp;
- xây dựng các class chuyên biệt từ class tổng quát.

---

#### Ghi đè phương thức

Class con có thể cung cấp một cách triển khai khác cho method của class cha.

Ví dụ:

```python
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")
```

```python
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Kết quả:

```text
Woof
Meow
```

Đây được gọi là **method overriding**.

---

### 6.3. Polymorphism – Đa hình

**Polymorphism** có thể hiểu là:

> cùng một thao tác hoặc giao diện nhưng có thể tạo ra hành vi khác nhau tùy theo loại đối tượng.

<p align="center">
  <img src="images/oop-polymorphism.png" alt="Tính đa hình (Polymorphism) trong OOP" width="800" />
</p>

Xét các class:

```python
class Dog:
    def sound(self):
        return "Woof"


class Cat:
    def sound(self):
        return "Meow"
```

Một hàm có thể làm việc với cả hai loại đối tượng:

```python
def make_sound(animal):
    print(animal.sound())
```

```python
dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
```

Kết quả:

```text
Woof
Meow
```

Hàm:

```python
make_sound()
```

không cần biết chính xác đối tượng là `Dog` hay `Cat`. Nó chỉ cần đối tượng cung cấp method:

```python
sound()
```

Đây cũng thể hiện đặc điểm **duck typing** thường gặp trong Python:

> nếu một đối tượng cung cấp các thao tác mà chương trình cần, chương trình có thể sử dụng đối tượng đó mà không nhất thiết phải kiểm tra chính xác class của nó.

Một ví dụ rất quen thuộc là hàm `len()`:

```python
print(len("Python"))
print(len([1, 2, 3]))
print(len({"a": 1, "b": 2}))
```

Cùng một thao tác `len()` có thể áp dụng cho nhiều loại dữ liệu khác nhau.

---

### 6.4. Abstraction – Trừu tượng hóa

**Abstraction** tập trung vào việc mô tả:

> đối tượng cần cung cấp chức năng gì,

thay vì bắt người sử dụng phải biết:

> chức năng đó được triển khai bên trong như thế nào.

Ví dụ, người sử dụng một stack chỉ cần biết các thao tác:

```text
push(x)
pop()
top()
is_empty()
```

Người sử dụng không nhất thiết phải biết stack bên trong được triển khai bằng:

- list;
- linked list;
- array;
- hoặc một cấu trúc dữ liệu khác.

Đây chính là ý tưởng quan trọng khi OOP được sử dụng để triển khai **Abstract Data Type – ADT**.

![alt text](images/oop-abstract.png)

Trong Python, module `abc` có thể được sử dụng để mô tả một abstract class.

Ví dụ:

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Class `Shape` quy định rằng các class cụ thể kế thừa từ nó phải cung cấp method `area()`.

Ví dụ:

```python
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

```python
rectangle = Rectangle(4, 5)

print(rectangle.area())
```

Kết quả:

```text
20
```

Người sử dụng chỉ cần biết:

```python
shape.area()
```

mà không cần quan tâm mỗi loại hình học tính diện tích bằng công thức nào.

---

## 7. Ví dụ tổng hợp

Xét một hệ thống quản lý nhân viên.

```python
class Employee:
    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
```

Ta xây dựng một class chuyên biệt:

```python
class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.salary * 0.2
```

Sử dụng:

```python
employee = Employee("An", 1000)
manager = Manager("Binh", 2000, 5)

print(employee.calculate_bonus())
print(manager.calculate_bonus())
```

Kết quả:

```text
100.0
400.0
```

Ví dụ trên thể hiện đồng thời nhiều khái niệm OOP:

- `Employee` và `Manager` là các **class**;
- `employee` và `manager` là các **object**;
- `name`, `salary`, `team_size` là các **instance attributes**;
- `company` là **class attribute**;
- `calculate_bonus()` và `display()` là các **methods**;
- dữ liệu và thao tác liên quan được **đóng gói** trong class;
- `Manager` **kế thừa** `Employee`;
- `Manager` **ghi đè** `calculate_bonus()`;
- lời gọi cùng tên `calculate_bonus()` tạo ra kết quả khác nhau tùy đối tượng, thể hiện **đa hình**.

---

## 8. Class và Object trong cấu trúc dữ liệu

OOP rất quan trọng khi triển khai các **Abstract Data Type – ADT** và **Data Structure – cấu trúc dữ liệu**.

Ví dụ, ta muốn mô tả ADT `Stack`.

Về mặt giao diện, stack cần hỗ trợ các thao tác cơ bản:

```text
push(x)
pop()
top()
is_empty()
```

Ta có thể triển khai stack bằng class:

```python
class Stack:

    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0
```

Sử dụng:

```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())
print(stack.pop())
```

Kết quả:

```text
30
30
```

Ở đây:

- `Stack` định nghĩa một loại đối tượng;
- `_data` lưu trạng thái của stack;
- các method mô tả các thao tác hợp lệ trên stack;
- người sử dụng không cần thao tác trực tiếp với list `_data`.

Đây là một ví dụ đơn giản về việc sử dụng OOP để **đóng gói cách triển khai một cấu trúc dữ liệu**.

---

## 9. Phân biệt một số khái niệm quan trọng

| Khái niệm | Ý nghĩa |
|---|---|
| Class | Khuôn mẫu để tạo đối tượng |
| Object | Một instance cụ thể của class |
| Attribute | Dữ liệu gắn với class hoặc object |
| Instance attribute | Thuộc tính riêng của từng object |
| Class attribute | Thuộc tính được định nghĩa ở cấp class |
| Method | Hàm được định nghĩa trong class |
| `self` | Tham chiếu tới instance hiện tại |
| `__init__()` | Khởi tạo trạng thái ban đầu của instance |
| Encapsulation | Đóng gói dữ liệu và thao tác liên quan |
| Inheritance | Xây dựng class mới từ class đã có |
| Polymorphism | Cùng giao diện nhưng có nhiều cách xử lý |
| Abstraction | Chỉ công khai chức năng cần thiết, ẩn chi tiết triển khai |

---

## 10. Một số lỗi thường gặp

### Nhầm class với object
Sai về cách hiểu:

```text
Dog là một con chó cụ thể.
```

Đúng hơn:

```text
Dog là class mô tả các đối tượng chó.
dog1 là một object cụ thể thuộc class Dog.
```

---

### Nhầm class attribute với instance attribute
```python
class Student:
    school = "NEU"

    def __init__(self, name):
        self.name = name
```

Trong đó:

```python
school
```

là class attribute, còn:

```python
self.name
```

là instance attribute.

---

### Quên `self`
Không nên viết:

```python
class Student:
    def show_name():
        print("Student")
```

Với instance method thông thường, cần:

```python
class Student:
    def show_name(self):
        print("Student")
```

---

### Thay đổi class attribute qua một instance
Xét:

```python
class Dog:
    species = "Canine"
```

```python
dog1 = Dog()
dog2 = Dog()

dog1.species = "Unknown"
```

Lúc này Python tạo hoặc gán một instance attribute `species` cho `dog1`; nó không nhất thiết thay đổi `Dog.species`.

Do đó:

```python
print(dog1.species)
print(dog2.species)
print(Dog.species)
```

có thể cho:

```text
Unknown
Canine
Canine
```

Đây là một điểm cần chú ý khi làm việc với class attribute.

---

## 11. Tóm tắt

OOP tổ chức chương trình xung quanh **class** và **object**.

Một class mô tả:

```text
Data + Operations
```

hay:

```text
Attributes + Methods
```

Một object là một instance cụ thể của class.

Ví dụ:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof")
```

```python
dog = Dog("Buddy")
dog.bark()
```

Trong OOP:

- **Encapsulation** giúp nhóm dữ liệu và phương thức liên quan;
- **Inheritance** giúp xây dựng class mới từ class có sẵn;
- **Polymorphism** cho phép cùng một giao diện có nhiều hành vi;
- **Abstraction** giúp tách chức năng cần sử dụng khỏi chi tiết triển khai.

Đối với cấu trúc dữ liệu, OOP cung cấp một cách tự nhiên để triển khai **ADT**:

```text
ADT
 |
 | specifies operations
 v
Class / Interface
 |
 | implemented by
 v
Concrete Data Structure
```

Ví dụ:

```text
Stack ADT
   |
   +-- push
   +-- pop
   +-- top
   +-- is_empty
          |
          v
   Stack implemented
   using Python list
```

---
---

## 12. Quiz và câu hỏi ôn tập

### 12.1. Câu hỏi trắc nghiệm

**Câu 1.** Phát biểu nào mô tả đúng nhất về `class`?

A. Một object cụ thể đang tồn tại trong chương trình.  
B. Một khuôn mẫu dùng để tạo các object.  
C. Một method đặc biệt của Python.  
D. Một biến được dùng chung cho mọi module.

**Câu 2.** Trong đoạn mã sau, `name` là gì?

```python
class Student:
    def __init__(self, name):
        self.name = name
```

A. Class attribute.  
B. Instance attribute.  
C. Global variable.  
D. Abstract method.

**Câu 3.** Trong đoạn mã sau, `school` là gì?

```python
class Student:
    school = "NEU"

    def __init__(self, name):
        self.name = name
```

A. Instance attribute.  
B. Local variable.  
C. Class attribute.  
D. Method.

**Câu 4.** `self` trong một instance method thường tham chiếu tới:

A. Class cha.  
B. Module hiện tại.  
C. Object hiện tại.  
D. Method đang được gọi.

**Câu 5.** `__init__()` thường được sử dụng để:

A. Xóa object.  
B. Thiết lập trạng thái ban đầu của object.  
C. Gọi class cha trong mọi trường hợp.  
D. Khai báo abstract method.

**Câu 6.** Khái niệm nào mô tả việc nhóm dữ liệu và các thao tác liên quan vào cùng một class?

A. Inheritance.  
B. Encapsulation.  
C. Polymorphism.  
D. Recursion.

**Câu 7.** Khái niệm nào cho phép `Dog` sử dụng method đã được định nghĩa trong `Animal`?

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

A. Encapsulation.  
B. Inheritance.  
C. Abstraction.  
D. Iteration.

**Câu 8.** Khi class con định nghĩa lại một method đã tồn tại trong class cha, ta gọi đó là:

A. Method overriding.  
B. Method nesting.  
C. Method hiding.  
D. Object instantiation.

**Câu 9.** Đoạn mã nào thể hiện rõ polymorphism?

A.

```python
x = 10
```

B.

```python
print(len("Python"))
print(len([1, 2, 3]))
```

C.

```python
for i in range(3):
    print(i)
```

D.

```python
import math
```

**Câu 10.** Duck typing nhấn mạnh rằng:

A. Object phải thuộc đúng một class đã chỉ định trước.  
B. Object có thể được sử dụng nếu nó cung cấp các thao tác mà chương trình cần.  
C. Mọi class phải kế thừa từ `ABC`.  
D. Mọi object phải có cùng tập attributes.

**Câu 11.** Abstraction chủ yếu giúp:

A. Hiển thị toàn bộ chi tiết triển khai cho người sử dụng.  
B. Tách chức năng cần sử dụng khỏi chi tiết triển khai bên trong.  
C. Thay thế hoàn toàn inheritance.  
D. Tạo nhiều object giống nhau.

**Câu 12.** Trong Python, `@abstractmethod` thường được sử dụng cùng với:

A. `abc`.  
B. `math`.  
C. `random`.  
D. `os`.

**Câu 13.** Trong ví dụ `Stack`, `_data` có vai trò gì?

A. Lưu trạng thái nội bộ của stack.  
B. Là một abstract method.  
C. Là class cha của `Stack`.  
D. Là tên của ADT.

**Câu 14.** Phát biểu nào đúng về ADT?

A. Một ADT bắt buộc chỉ có một cách triển khai.  
B. ADT mô tả các thao tác cần cung cấp mà không nhất thiết quy định cách triển khai bên trong.  
C. ADT và object là hai khái niệm hoàn toàn giống nhau.  
D. ADT không thể được triển khai bằng class.

**Câu 15.** Sau đoạn mã sau, giá trị nào được in ra?

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1


c = Counter()
c.increase()
c.increase()
print(c.value)
```

A. `0`  
B. `1`  
C. `2`  
D. Chương trình báo lỗi.

### 12.2. Đúng hay sai

Cho biết mỗi phát biểu sau là **Đúng** hay **Sai**.

1. Một class có thể được sử dụng để tạo nhiều object.
2. Hai object thuộc cùng một class bắt buộc phải có cùng giá trị của mọi instance attribute.
3. `self` thường tham chiếu tới object đang gọi instance method.
4. Class attribute là thuộc tính riêng biệt cho từng object.
5. Inheritance có thể giúp tái sử dụng code.
6. Method overriding xảy ra khi class con cung cấp cách triển khai mới cho method của class cha.
7. Abstraction yêu cầu người sử dụng phải biết toàn bộ chi tiết triển khai.
8. Một ADT có thể có nhiều implementation khác nhau.

### 12.3. Đọc mã và dự đoán kết quả

**Bài 1.**

```python
class Student:
    university = "NEU"

    def __init__(self, name):
        self.name = name


s1 = Student("An")
s2 = Student("Binh")

print(s1.name)
print(s2.university)
```

Yêu cầu:

- Dự đoán kết quả.
- Cho biết `name` và `university` thuộc loại attribute nào.

**Bài 2.**

```python
class Dog:
    species = "Canine"


dog1 = Dog()
dog2 = Dog()

dog1.species = "Unknown"

print(dog1.species)
print(dog2.species)
print(Dog.species)
```

Yêu cầu:

- Dự đoán ba dòng kết quả.
- Giải thích vì sao việc gán `dog1.species` không nhất thiết làm thay đổi `Dog.species`.

**Bài 3.**

```python
class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Woof"


a = Animal()
d = Dog()

print(a.sound())
print(d.sound())
```

Yêu cầu:

- Dự đoán kết quả.
- Xác định method nào đã được overriding.

**Bài 4.**

```python
class Dog:
    def sound(self):
        return "Woof"


class Cat:
    def sound(self):
        return "Meow"


def make_sound(animal):
    print(animal.sound())


make_sound(Dog())
make_sound(Cat())
```

Yêu cầu:

- Dự đoán kết quả.
- Giải thích vì sao `make_sound()` có thể làm việc với cả `Dog` và `Cat`.
- Xác định khái niệm polymorphism/duck typing trong ví dụ.

**Bài 5.**

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())
print(stack.pop())
print(stack.top())
```

Yêu cầu:

- Dự đoán kết quả.
- Ghi lại trạng thái của `_data` sau từng thao tác `push()` và `pop()`.

---

## 13. Bài tập tự luyện

Các bài tập dưới đây **không kèm lời giải**. Người học nên tự xây dựng chương trình, chạy thử với nhiều bộ dữ liệu và giải thích các khái niệm OOP xuất hiện trong lời giải của mình.

### 13.1. Bài 1 – Xây dựng class `Student`

Viết class `Student` có:

- instance attributes: `name`, `student_id`, `gpa`;
- method `display()` để hiển thị thông tin sinh viên;
- method `is_passed()` trả về `True` nếu `gpa >= 2.0`, ngược lại trả về `False`.

Yêu cầu:

1. Tạo ít nhất ba object `Student`.
2. Hiển thị thông tin từng sinh viên.
3. Kiểm tra sinh viên nào đạt yêu cầu.

### 13.2. Bài 2 – Class attribute và instance attribute

Xây dựng class `Product` có:

- class attribute `tax_rate = 0.1`;
- instance attributes `name`, `price`;
- method `final_price()` trả về giá sau thuế.

Tạo hai sản phẩm và so sánh:

```python
Product.tax_rate
product1.tax_rate
product2.tax_rate
```

Sau đó thực hiện:

```python
product1.tax_rate = 0.2
```

Tiếp tục quan sát:

```python
product1.tax_rate
product2.tax_rate
Product.tax_rate
```

Giải thích kết quả quan sát được.

### 13.3. Bài 3 – Encapsulation với `BankAccount`

Xây dựng class `BankAccount` có:

- thuộc tính `_balance`;
- method `deposit(amount)`;
- method `withdraw(amount)`;
- method `get_balance()`.

Yêu cầu:

- không cho nạp số tiền âm hoặc bằng 0;
- không cho rút số tiền âm hoặc bằng 0;
- không cho rút số tiền lớn hơn số dư;
- thử nghiệm với cả dữ liệu hợp lệ và không hợp lệ.

Cuối cùng, giải thích vì sao nên thay đổi số dư thông qua `deposit()` và `withdraw()` thay vì sửa `_balance` trực tiếp.

### 13.4. Bài 4 – Inheritance

Xây dựng class cha `Employee` có:

- `name`;
- `salary`;
- method `display()`.

Xây dựng hai class con:

```python
class Manager(Employee):
    ...

class Developer(Employee):
    ...
```

Trong đó:

- `Manager` có thêm `team_size`;
- `Developer` có thêm `programming_language`.

Tạo object của từng class và kiểm tra khả năng sử dụng lại dữ liệu/method từ `Employee`.

### 13.5. Bài 5 – Method overriding và polymorphism

Tiếp tục Bài 4.

Trong `Employee`, xây dựng:

```python
def calculate_bonus(self):
    return self.salary * 0.1
```

Trong `Manager`, overriding method trên để bonus bằng `20%` lương.

Trong `Developer`, overriding method trên để bonus bằng `15%` lương.

Tạo một danh sách gồm nhiều `Employee`, `Manager` và `Developer`, sau đó dùng một vòng lặp để gọi:

```python
employee.calculate_bonus()
```

cho từng object.

Giải thích vì sao đây là một ví dụ của polymorphism.

### 13.6. Bài 6 – Duck typing

Xây dựng ba class:

```python
Dog
Cat
Cow
```

Mỗi class cung cấp method:

```python
sound()
```

nhưng trả về kết quả khác nhau.

Viết hàm:

```python
def make_sound(animal):
    ...
```

sao cho hàm có thể hoạt động với cả ba loại object mà không cần kiểm tra:

```python
type(animal)
```

hoặc:

```python
isinstance(...)
```

### 13.7. Bài 7 – Abstract class `Shape`

Sử dụng:

```python
from abc import ABC, abstractmethod
```

để xây dựng abstract class:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Sau đó triển khai ít nhất ba class cụ thể:

- `Rectangle`;
- `Circle`;
- `Triangle`.

Mỗi class phải cung cấp implementation riêng cho `area()`.

Viết một hàm nhận một object `Shape` và in diện tích của object đó.

### 13.8. Bài 8 – Triển khai ADT `Stack`

Viết class `Stack` hỗ trợ các thao tác:

```text
push(x)
pop()
top()
is_empty()
```

Dùng Python `list` để lưu dữ liệu nội bộ.

Thực hiện lần lượt:

```text
push(10)
push(20)
push(30)
top()
pop()
top()
```

Ghi lại trạng thái stack sau từng thao tác.

### 13.9. Bài 9 – Hai implementation cho cùng một ADT

Giả sử ADT `Stack` quy định bốn thao tác:

```text
push(x)
pop()
top()
is_empty()
```

Xây dựng hai class khác nhau cùng cung cấp giao diện trên.

Ví dụ:

```python
ListStack
LinkedStack
```

Viết một hàm:

```python
def test_stack(stack):
    ...
```

có thể kiểm tra cả hai implementation mà không cần biết dữ liệu bên trong được lưu như thế nào.

Giải thích mối liên hệ giữa bài tập này với **abstraction** và **polymorphism**.

### 13.10. Bài 10 – Bài tập tổng hợp

Xây dựng một hệ thống đơn giản quản lý phương tiện.

Class cha `Vehicle` có:

- `brand`;
- `speed`;
- method `move()`;
- method `display()`.

Xây dựng các class con:

```python
Car
Bike
Truck
```

Yêu cầu:

1. Mỗi class con kế thừa `Vehicle`.
2. Mỗi class con overriding `move()` với hành vi khác nhau.
3. Tạo ít nhất một object từ mỗi class.
4. Đặt các object vào một list.
5. Dùng vòng lặp gọi `display()` và `move()` cho từng object.
6. Chỉ ra trong chương trình vị trí thể hiện:
   - encapsulation;
   - inheritance;
   - polymorphism;
   - abstraction (nếu có).

---

## 14. Đáp án quiz

<details>
<summary><strong>Xem đáp án câu hỏi trắc nghiệm</strong></summary>

| Câu | Đáp án | Câu | Đáp án | Câu | Đáp án |
|---|---|---|---|---|---|
| 1 | B | 6 | B | 11 | B |
| 2 | B | 7 | B | 12 | A |
| 3 | C | 8 | A | 13 | A |
| 4 | C | 9 | B | 14 | B |
| 5 | B | 10 | B | 15 | C |

</details>

<details>
<summary><strong>Xem đáp án phần Đúng/Sai</strong></summary>

1. Đúng.  
2. Sai.  
3. Đúng.  
4. Sai.  
5. Đúng.  
6. Đúng.  
7. Sai.  
8. Đúng.

</details>

<details>
<summary><strong>Xem đáp án phần đọc mã</strong></summary>

**Bài 1**

```text
An
NEU
```

`name` là instance attribute; `university` là class attribute.

**Bài 2**

```text
Unknown
Canine
Canine
```

Việc gán `dog1.species = "Unknown"` tạo/gán thuộc tính `species` ở instance `dog1`; class attribute `Dog.species` vẫn giữ giá trị `"Canine"`.

**Bài 3**

```text
Some sound
Woof
```

`Dog.sound()` overriding `Animal.sound()`.

**Bài 4**

```text
Woof
Meow
```

`make_sound()` chỉ cần object truyền vào cung cấp method `sound()`. Đây là ví dụ của polymorphism và duck typing.

**Bài 5**

```text
30
30
20
```

Trạng thái `_data` thay đổi:

```text
[]
[10]
[10, 20]
[10, 20, 30]
[10, 20]
```

</details>


## Tài liệu tham khảo
1. GeeksforGeeks, **Python OOP Concepts**, cập nhật ngày 8/6/2026:  
   https://www.geeksforgeeks.org/python/python-oops-concepts/

2. Python Documentation, **Classes**:  
   https://docs.python.org/3/tutorial/classes.html

3. Python Documentation, **abc — Abstract Base Classes**:  
   https://docs.python.org/3/library/abc.html