# Lập trình hướng đối tượng trong Python

## 1. Giới thiệu về lập trình hướng đối tượng

**Lập trình hướng đối tượng** (*Object-Oriented Programming – OOP*) là một cách tổ chức chương trình dựa trên các **đối tượng** (*objects*) và **lớp** (*classes*).

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
        |           |
      dog1        dog2
   name=Buddy    name=Max
   age=3         age=5
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
print(dog1.age)   # 3
print(dog2.age)   # 5
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
name       = "An"
student_id = "SV001"
```

Trong các tài liệu nhập môn, `__init__()` thường được gọi đơn giản là *constructor*. Chính xác hơn trong Python, `__new__()` chịu trách nhiệm tạo instance, còn `__init__()` chịu trách nhiệm **khởi tạo trạng thái** của instance sau khi nó được tạo.

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

# 6. Bốn trụ cột của OOP

## 6.1. Encapsulation – Đóng gói

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

### Mức độ truy cập trong Python

Khác với một số ngôn ngữ như Java hoặc C++, Python không thực thi `public`, `protected`, `private` theo cùng cơ chế.

Thông thường Python sử dụng quy ước:

```python
name       # thuộc tính thông thường
_name      # quy ước: chỉ nên sử dụng nội bộ
__name     # kích hoạt name mangling
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

## 6.2. Inheritance – Kế thừa

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

### Ghi đè phương thức

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

## 6.3. Polymorphism – Đa hình

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

## 6.4. Abstraction – Trừu tượng hóa

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

# 7. Ví dụ tổng hợp

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

# 8. Class và Object trong cấu trúc dữ liệu

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

# 9. Phân biệt một số khái niệm quan trọng

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

# 10. Một số lỗi thường gặp

## Nhầm class với object

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

## Nhầm class attribute với instance attribute

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

## Quên `self`

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

## Thay đổi class attribute qua một instance

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

# 11. Tóm tắt

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

# Tài liệu tham khảo

1. GeeksforGeeks, **Python OOP Concepts**, cập nhật ngày 8/6/2026:  
   https://www.geeksforgeeks.org/python/python-oops-concepts/

2. Python Documentation, **Classes**:  
   https://docs.python.org/3/tutorial/classes.html

3. Python Documentation, **abc — Abstract Base Classes**:  
   https://docs.python.org/3/library/abc.html
