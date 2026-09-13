# 🔍 Part 04: Thuật toán Tìm kiếm, Chọn lọc và Sắp xếp (Searching, Selection, and Sorting Algorithms)

> **Học phần:** Cấu trúc dữ liệu và Giải thuật với Python (DSAI1002)  
> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị:** Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)

---

## 📚 Danh mục Tài liệu & Học liệu (Learning Resources)

Thư mục này cung cấp toàn bộ tài liệu học tập, ghi chú bài giảng lý thuyết, slide trình chiếu và hệ thống bài tập thực hành cho **Part 04**:

### 1. Ghi chú Bài giảng Toàn diện (Comprehensive Lecture Notes)
- 📄 **[part04-lecture-notes-en.pdf](part04-lecture-notes-en.pdf)** *(24 trang, ấn bản PDF chuẩn xuất bản)*:
  - Tổng hợp lý thuyết chuyên sâu, chứng minh toán học, cây đệ quy, bảng so sánh và bài toán phỏng vấn / tổng hợp.
  - Tích hợp code Python chuẩn mực và hướng dẫn từng bước (step-by-step traces) cho tất cả các thuật toán.
  - Bản sao liên kết: **[part04-lecture-notes.pdf](part04-lecture-notes.pdf)**
  - Mã nguồn LaTeX: **[part04-lecture-notes-en.tex](part04-lecture-notes-en.tex)**

### 2. Slide Bài giảng (Lecture Slides)
- 📊 **[part04-sorting-en.pdf](part04-sorting-en.pdf)**: Slide bài giảng về các thuật toán sắp xếp cơ bản và nâng cao (Bubble, Selection, Insertion, Merge Sort, Quicksort, Counting Sort, Radix Sort, Timsort).
- 📊 **[part04-selection-searching.pdf](part04-selection-searching.pdf)**: Slide bài giảng về bài toán Chọn lọc (Quickselect, Median of Medians, Streaming Top-$k$) và Tìm kiếm (Linear, Binary, Ternary Search).

### 3. Bài tập Thực hành & Ôn tập (Practice Problems)
- 📖 **[part04-practice-vn.md](part04-practice-vn.md)**: Hệ thống bài tập thực hành, câu hỏi tự luận và bài tập trắc nghiệm giải thích bằng Tiếng Việt.
- 📖 **[part04-practice-en.md](part04-practice-en.md)**: English version of practice problems and conceptual self-check exercises.

---

## 🧠 Nội dung Trọng tâm (Key Topics Covered)

```
Part 04: Searching, Selection & Sorting
├── 1. Elementary Sorts
│   ├── Bubble Sort (Early-exit optimization, O(n) best-case)
│   ├── Selection Sort (Instability proof & minimal swaps)
│   └── Insertion Sort (Adaptive online capability, O(n) on nearly-sorted data)
├── 2. Divide-and-Conquer Sorts
│   ├── Merge Sort (Guaranteed O(n log n), recursive tree, O(n) auxiliary space)
│   ├── Quicksort (Lomuto vs Hoare partitioning, pivot strategies)
│   └── Dutch National Flag Partitioning (3-way partition for duplicate-heavy arrays)
├── 3. Non-Comparison Linear-Time Sorts
│   ├── The Information-Theoretic Lower Bound Ω(n log n)
│   ├── Counting Sort (Frequency histogram, prefix sums, stable right-to-left placement)
│   └── Radix Sort (LSD multi-pass sorting)
├── 4. Python Sorting Internals & Practical Engineering
│   ├── Timsort mechanics (Run detection, natural merges, stability)
│   ├── Multi-criteria sorting with tuple keys
│   └── Adapting custom comparators via functools.cmp_to_key
├── 5. The Selection Problem & Order Statistics
│   ├── Quickselect (Expected O(n) time, O(1) space)
│   ├── Streaming Top-k extraction via Min-Heap (O(n log k) time, O(k) memory)
│   └── Median of Medians (BFPRT, deterministic worst-case O(n))
└── 6. Searching Algorithms
    ├── Binary Search (Loop invariants, safe midpoint calculation low + (high-low)//2)
    ├── Boundary Search (First occurrence / lower bound, last occurrence)
    ├── Ternary Search on Unimodal Functions
    └── Advanced Applications (Binary Search on Answer, Rotated Sorted Array search)
```

---

## 💻 Hướng dẫn Biên dịch Mã nguồn LaTeX (LaTeX Compilation Guide)

Tài liệu ghi chú bài giảng được định dạng chuẩn với MiKTeX / TeX Live. Để biên dịch:

```bash
# Biên dịch Ghi chú Bài giảng (2 lượt để cập nhật mục lục và liên kết)
pdflatex -interaction=nonstopmode part04-lecture-notes-en.tex
pdflatex -interaction=batchmode part04-lecture-notes-en.tex
```

---

> © 2026 TS. Vũ Đức Minh – Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo, Trường Đại học Kinh tế Quốc dân (NEU).
