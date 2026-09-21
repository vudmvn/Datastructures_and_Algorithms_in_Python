# 🧱 Part 05: Cấu trúc Dữ liệu Tuyến tính (Linear Data Structures)

> **Học phần:** Cấu trúc dữ liệu và Giải thuật với Python (DSAI1002)  
> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị:** Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)

---

## 📚 Danh mục Tài liệu & Học liệu (Learning Resources)

Thư mục này cung cấp toàn bộ tài liệu học tập, bài giảng lý thuyết Markdown, slide trình chiếu và bài tập phân tích cho **Part 05**:

### 1. Bài giảng & Bài đọc Lý thuyết (Lecture Notes & Readings)
- 📖 **[part05-linked-list-vn.md](part05-linked-list-vn.md)** *(Chương 3: Danh sách liên kết - Linked Lists)*:
  - Tổng quan từ mảng đến danh sách liên kết, bản chất của node và liên kết tham chiếu.
  - Danh sách liên kết đơn (*Singly Linked List*), danh sách liên kết đôi (*Doubly Linked List*), danh sách liên kết vòng (*Circular Linked List*).
  - Cài đặt chi tiết các thao tác từ đầu (*from scratch*): duyệt, tìm kiếm, chèn (đầu/cuối/vị trí bất kỳ), xóa node, đếm số node.
  - Kỹ thuật nâng cao: Hai con trỏ (*Slow & Fast Pointers*), đảo ngược danh sách liên kết, tìm node thứ $k$ từ cuối, phát hiện chu trình (*Floyd's Cycle Detection*).
  - Hệ thống bài tập phân tích độ phức tạp, câu hỏi thảo luận và checklist ôn tập cuối bài.

### 2. Slide Bài giảng (Lecture Slides)
- 📊 **[part05-data-structures-review-slide-en.pdf](part05-data-structures-review-slide-en.pdf)** *(Slide Part 1: Data Structures as ADTs)*:
  - Khái niệm Cấu trúc dữ liệu (Data Structures) và Kiểu dữ liệu trừu tượng (Abstract Data Types - ADTs).
  - Phân loại thao tác dữ liệu (Access, Search, Insert, Delete, Traverse).
  - Ánh xạ giữa ADT và công cụ cài đặt cụ thể trong Python (`list`, `dict`, `set`, `deque`, `heapq`, node classes).
  - Mã nguồn LaTeX: `part05-data-structures-review-slide-en.tex`
- 📊 **[part05-array-linked-lists-slide-en.pdf](part05-array-linked-lists-slide-en.pdf)** *(Slide Part 2: Arrays and Linked Lists)*:
  - Cấu trúc tuần tự (Sequences) và các phương pháp biểu diễn trong bộ nhớ.
  - Mảng tĩnh vs. Mảng động (Dynamic Arrays, cơ chế Geometric Resizing và chi phí Amortized $O(1)$).
  - Danh sách liên kết (Singly, Doubly, Circular Linked Lists): Biểu diễn con trỏ, chèn, xóa và duyệt.
  - So sánh toàn diện giữa Cấu trúc dựa trên mảng (*Array-Based*) và Cấu trúc liên kết (*Linked Structures*).
  - Mã nguồn LaTeX: `part05-array-linked-lists-slide-en.tex`

### 3. Bài tập Thực hành & Ôn tập (Practice Problems)
- 📝 **[part05-linked-list-vn.md (Mục 32 & 33)](part05-linked-list-vn.md#32-bài-tập-phân-tích)**:
  - Hệ thống bài tập phân tích độ phức tạp thời gian/bộ nhớ và so sánh hiệu năng.
  - Câu hỏi thảo luận chuyên sâu về ứng dụng thực tế của Linked Lists vs Arrays trong kỹ thuật phần mềm và xử lý dữ liệu.

---

## 🧠 Nội dung Trọng tâm (Key Topics Covered)

```
Part 05: Linear Data Structures
├── 1. Overview of Data Structures & ADTs
│   ├── Data Structures vs Abstract Data Types (ADTs)
│   ├── Core operations: Access, Search, Insert, Delete, Traverse
│   └── Python ecosystem: Built-ins (list, dict, set) vs collections (deque)
├── 2. Arrays & Dynamic Arrays
│   ├── Contiguous memory representation & O(1) random access
│   ├── Dynamic array mechanics: Geometric resizing & amortized analysis
│   └── Trade-offs: Cache locality vs expensive insertions/deletions O(n)
├── 3. Singly Linked Lists
│   ├── Node anatomy (value, next pointer) & head reference
│   ├── Traversal, search, insertion, and deletion algorithms
│   └── Pythonic implementation & sentinel (dummy) node pattern
├── 4. Doubly & Circular Linked Lists
│   ├── Doubly Linked List: prev & next pointers, bidirectional traversal
│   └── Circular Linked List: Tail pointing to head, round-robin applications
├── 5. Algorithmic Techniques on Linked Lists
│   ├── Two-pointer techniques (Slow & Fast / Tortoise & Hare)
│   ├── Finding the middle element & kth node from end
│   ├── In-place list reversal (O(n) time, O(1) auxiliary space)
│   └── Cycle detection (Floyd's Algorithm)
└── 6. Comparative Analysis
    └── Arrays vs Linked Lists: Access time, insertion/deletion, memory overhead, cache efficiency
```

---

## 💻 Hướng dẫn Biên dịch Mã nguồn LaTeX (LaTeX Compilation Guide)

Các slide bài giảng Beamer được định dạng chuẩn với MiKTeX / TeX Live. Để biên dịch:

```bash
# Biên dịch Slide Part 1: Data Structures as ADTs
pdflatex -interaction=nonstopmode part05-data-structures-review-slide-en.tex

# Biên dịch Slide Part 2: Arrays & Linked Lists
pdflatex -interaction=nonstopmode part05-array-linked-lists-slide-en.tex
```

---

> © 2026 TS. Vũ Đức Minh – Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo, Trường Đại học Kinh tế Quốc dân (NEU).
