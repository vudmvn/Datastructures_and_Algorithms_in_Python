# 🐍 DSAI1002 – Cấu trúc dữ liệu và Giải thuật với Python (Data Structures and Algorithms in Python)

🌐 **Ngôn ngữ / Language:** 🇻🇳 **Tiếng Việt** | [🇬🇧 English Version (README-en.md)](README-en.md)

> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị phụ trách:** Khoa Khoa học dữ liệu và Trí tuệ nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)  
> **Số tín chỉ:** 3 Tín chỉ (45h lý thuyết, 22.5h thực hành, 90h tự học)  
> **Đề cương chi tiết học phần:** Xem tệp [syllabus-vn.md](syllabus-vn.md)

---

## 📌 1. Giới thiệu Học phần & Mục tiêu

Học phần **Cấu trúc dữ liệu và Giải thuật với Python (DSAI1002)** cung cấp kiến thức nền tảng và chuyên sâu về các cấu trúc dữ liệu cơ bản (Mảng, Danh sách liên kết, Ngăn xếp, Hàng đợi, Cây, Bảng băm) và các thuật toán cốt lõi (Tìm kiếm, Sắp xếp, Duyệt cây, Quy hoạch động, Chia để trị). 

Sinh viên được hướng dẫn tự cài đặt (implement from scratch) các cấu trúc dữ liệu và giải thuật bằng **Python**, phân tích độ phức tạp thời gian/bộ nhớ (Big-O notation) và áp dụng vào bài toán thực tế trong Kinh doanh & Tài chính.

### 🎯 Mục tiêu & Chuẩn đầu ra (CLOs):
1. **Phân tích độ phức tạp (G1):** Sử dụng ký hiệu Big-O đánh giá độ phức tạp thời gian và bộ nhớ của thuật toán.
2. **Cấu trúc dữ liệu & Thuật toán (G2):** Thành thạo các ADT, cấu trúc dữ liệu cơ bản & nâng cao và cài đặt từ đầu.
3. **Ứng dụng giải bài toán (G3):** Lựa chọn và thiết kế giải thuật tối ưu cho các bài toán thực tế.
4. **Năng lực tự chủ (G4):** Nâng cao tư duy độc lập, tự học và kỹ năng làm việc nhóm.

---

## 📚 2. Ma trận Bài giảng, Tài liệu & Bài tập Thực hành (Course Matrix by Parts)

Bảng dưới đây tổng hợp chi tiết tài liệu học tập, bài giảng Markdown, slide, bài tập thực hành và lời giải được tổ chức theo các **Phần học (Part)**:

| Phần | Chủ đề chính (Tiếng Việt) | Bài giảng & Bài đọc (.md) | Slide & Bài tập | Trạng thái |
|:---:|:---|:---|:---:|:---:|
| **Part 1** | **Giới thiệu Môn học** | • [Bài giảng: Giới thiệu Học phần & Phân tích Tổng quan](lectures/part-01-gioi-thieu-mon-hoc/introduction-1-vn.md) | - | ✅ *Đã sẵn sàng* |
| **Part 2** | **ADT & Lập trình Hướng đối tượng (OOP)** | - | • [Slide: L2. OOP 1](lectures/part-02-adt-va-oop/L2.%20OOP%201.pdf)<br>• [Slide: L3. OOP 2](lectures/part-02-adt-va-oop/L3.%20OOP%202.pdf)<br>• [Bài tập: Assignment 1](lectures/part-02-adt-va-oop/week_1_assignment.pdf) | ✅ *Đã sẵn sàng* |
| **Part 3** | **Thuật toán & Độ phức tạp tiệm cận** | • [Bài giảng: Thuật toán là gì? Nhập môn Phân tích Thuật toán](lectures/part-03-thuat-toan-va-do-phuc-tap/introduction-to-algorithm-1-vn.md)<br>• [Bài giảng: Độ phức tạp Thuật toán & Ký hiệu tiệm cận](lectures/part-03-thuat-toan-va-do-phuc-tap/complexity-analysis-2-vn.md)<br>• [Bài giảng: Master Theorem, Phương trình truy hồi & Phân tích Khấu hao](lectures/part-03-thuat-toan-va-do-phuc-tap/master-theorem-vn.md) | - | ✅ *Đã sẵn sàng* |
| **Part 4** | **Nền tảng Thuật toán & Phương pháp tiếp cận** | • [Part I: Nền tảng Thuật toán và Cấu trúc Dữ liệu](lectures/part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/part-1-vn.md)<br>• [Part II: Các phương pháp Tiếp cận Giải thuật](lectures/part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/part-2-vn.md)<br>• [Part III: Phân tích Thuật toán](lectures/part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/part-3-vn.md)<br>• [Part IV: Phân tích Thuật toán Đệ quy](lectures/part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/part-4-vn.md) | • [Bài tập: Problem Set 1 & Lời giải](lectures/part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/problem-set-1-vn.md) | ✅ *Đã sẵn sàng* |
| **Part 5** | **Thuật toán Tìm kiếm & Sắp xếp** | Linear Search, Binary Search, Insertion Sort, Bubble Sort, Selection Sort, Merge Sort, Quick Sort | - | ⏳ *Đang biên soạn* |
| **Part 6** | **Cấu trúc Dữ liệu Tuyến tính** | Mảng (Array), Danh sách liên kết (Singly/Doubly Linked List), Ngăn xếp (Stack), Hàng đợi (Queue) | - | ⏳ *Đang biên soạn* |
| **Part 7** | **Cấu trúc Dữ liệu Phi tuyến tính** | Cây tổng quát, Cây nhị phân, Cây tìm kiếm nhị phân (BST), Cây AVL, Heap & Priority Queue | - | ⏳ *Đang biên soạn* |
| **Part 8** | **Bảng băm & Giải thuật Nâng cao** | Bảng băm (Hash Table), Hàm băm, Xử lý đụng độ, Giải thuật đồ thị & Tổng kết môn học | - | ⏳ *Đang biên soạn* |

---

## 📖 3. Sách tham khảo (References & Textbooks)

| Bìa sách | Tài liệu | Tác giả | Nhà xuất bản | ISBN | Liên kết |
|:---:|:---|:---|:---|:---:|:---:|
| <img src="assets/images/data-structure-algorithmic-thinking-karumanchi-cover.jpg" alt="Data Structure and Algorithmic Thinking with Python" width="90" /> | **Data Structure and Algorithmic Thinking with Python** | Narasimha Karumanchi | CareerMonk Publications, 2020 | 9788194254003 | [Thông tin sách](https://careermonk.com/) |
| <img src="assets/images/fundamentals-python-data-structures-lambert-cover.jpg" alt="Fundamentals of Python: Data Structures" width="90" /> | **Fundamentals of Python: Data Structures**, 2nd Edition | Kenneth A. Lambert | Cengage Learning, 2019 | 9780357122754 | [Thông tin sách](https://www.cengage.com/c/fundamentals-of-python-data-structures-2e-lambert/9780357122754) |
| <img src="assets/images/data-structures-algorithms-goodrich-cover.jpg" alt="Data Structures and Algorithms in Python" width="90" /> | **Data Structures and Algorithms in Python** | Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser | Wiley, 2013 | 9781118290279 | [Thông tin sách](https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279) |
| <img src="assets/images/data-structures-algorithms-necaise-cover.jpg" alt="Data Structures and Algorithms Using Python" width="90" /> | **Data Structures and Algorithms Using Python** | Rance D. Necaise | Wiley, 2011 | 9780470618295 | [Thông tin sách](https://www.wiley.com/en-us/Data+Structures+and+Algorithms+Using+Python-p-9780470618295) |

---

> © 2026 TS. Vũ Đức Minh - Khoa Khoa học dữ liệu & Trí tuệ nhân tạo (NEU). Bản quyền tài liệu thuộc về tác giả.
