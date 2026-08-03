#!/usr/bin/env python3
"""
Script tự động quét các bài giảng trong `lectures/`, đối chiếu với đề cương `syllabus-vn.md`,
tạo/cập nhật Cổng thông tin môn học Song ngữ (Tiếng Việt `README.md` và Tiếng Anh `README-en.md`),
và thực hiện commit + push lên GitHub.

Quy tắc: Những mục chưa được biên soạn thực tế (chỉ là template khung hoặc thư mục rỗng)
sẽ hiển thị dấu gạch ngang '-' thay vì hiển thị link rỗng.
"""

import os
import sys
import re
import argparse
import subprocess

# Danh sách 15 tuần học chuẩn Song ngữ cho DSAI1002 (Bilingual Syllabus Mapping)
SYLLABUS_WEEKS = [
    {
        "week": "01",
        "topic_vn": "Giới thiệu học phần & ADT",
        "topic_en": "Course Intro & Abstract Data Types",
        "desc_vn": "Giới thiệu đề cương; Kiểu dữ liệu trừu tượng (ADT); Cấu trúc dữ liệu tích hợp trong Python; Thư viện mở rộng.",
        "desc_en": "Syllabus overview; Abstract Data Types (ADT); Python built-in data structures & external libraries."
    },
    {
        "week": "02",
        "topic_vn": "Độ phức tạp tiệm cận & Big-O",
        "topic_en": "Asymptotic Complexity & Big-O Notation",
        "desc_vn": "Phân tích thời gian chạy, số phép toán cơ bản, ký hiệu Big-O, đệ quy, Chia để trị & Định lý Master.",
        "desc_en": "Execution time analysis, basic operations, Big-O notation, recursion, Divide & Conquer & Master Theorem."
    },
    {
        "week": "03",
        "topic_vn": "Tìm kiếm & Sắp xếp cơ bản",
        "topic_en": "Searching & Simple Sorting Algorithms",
        "desc_vn": "Tìm kiếm tuyến tính, Tìm kiếm nhị phân; Sắp xếp chèn (Insertion), Sắp xếp nổi bọt (Bubble), Sắp xếp chọn (Selection).",
        "desc_en": "Linear Search, Binary Search; Insertion Sort, Bubble Sort, Selection Sort algorithms and implementations."
    },
    {
        "week": "04",
        "topic_vn": "Sắp xếp nâng cao & Phân tích",
        "topic_en": "Advanced Sorting & Complexity Analysis",
        "desc_vn": "Sắp xếp trộn (Merge sort), Sắp xếp nhanh (Quicksort); Đánh giá và so sánh độ phức tạp các thuật toán sắp xếp.",
        "desc_en": "Merge Sort, Quick Sort algorithms; Complexity analysis & comparative evaluation of sorting methods."
    },
    {
        "week": "05",
        "topic_vn": "Mảng & Danh sách liên kết (Phần 1)",
        "topic_en": "Array & Linked Structures (Part 1)",
        "desc_vn": "Cấu trúc dữ liệu Mảng (Array); Thao tác trên mảng; Danh sách liên kết đơn (Singly Linked List) và các phép toán.",
        "desc_en": "Array data structure & operations; Singly Linked List concepts, nodes, and operations."
    },
    {
        "week": "06",
        "topic_vn": "Danh sách liên kết (Phần 2)",
        "topic_en": "Linked Structures (Part 2)",
        "desc_vn": "Danh sách liên kết đôi (Doubly Linked List); Danh sách liên kết vòng (Circular Linked List) & thao tác thực hành.",
        "desc_en": "Doubly Linked List, Circular Linked List & practical implementation of list operations."
    },
    {
        "week": "07",
        "topic_vn": "Ngăn xếp (Stack) & Hàng đợi (Queue)",
        "topic_en": "Stack & Queue Data Structures",
        "desc_vn": "Cấu trúc Ngăn xếp (Stack), Hàng đợi (Queue), Hàng đợi hai đầu (Deque); Thao tác cơ bản & bài toán ứng dụng.",
        "desc_en": "Stack, Queue, Deque ADTs; Fundamental operations & application scenarios."
    },
    {
        "week": "08",
        "topic_vn": "Ứng dụng Stack/Queue & Ôn tập giữa kỳ",
        "topic_en": "Applications of Stack/Queue & Midterm Review",
        "desc_vn": "Ứng dụng thực tế của Stack/Queue (Undo/Redo, Parsing, Traversal); Ôn tập chuẩn bị giữa kỳ.",
        "desc_en": "Real-world applications of Stack/Queue (Undo/Redo, Expression Parsing, Traversal) & Midterm review."
    },
    {
        "week": "09",
        "topic_vn": "Thi giữa kỳ",
        "topic_en": "Midterm Examination",
        "desc_vn": "Bài kiểm tra giữa kỳ trên máy tính / tự luận đánh giá kiến thức Tuần 1 đến Tuần 8.",
        "desc_en": "Computer-based / Written Midterm Test evaluating topics from Week 1 to Week 8."
    },
    {
        "week": "10",
        "topic_vn": "Cây tổng quát & Cây nhị phân",
        "topic_en": "General Trees & Binary Trees",
        "desc_vn": "Khái niệm Cây (Tree), Cây nhị phân (Binary Tree); Cài đặt cây & các thuật toán duyệt cây (Pre-order, In-order, Post-order).",
        "desc_en": "Tree concepts & terminology; Binary Trees; Tree implementation & traversal algorithms (Pre-order, In-order, Post-order)."
    },
    {
        "week": "11",
        "topic_vn": "Cây tìm kiếm nhị phân (BST)",
        "topic_en": "Binary Search Trees (BST)",
        "desc_vn": "Cấu trúc Cây tìm kiếm nhị phân (BST); Các thuật toán tìm kiếm, chèn, xóa trên BST.",
        "desc_en": "Binary Search Tree structure; Searching, insertion, and deletion algorithms on BST."
    },
    {
        "week": "12",
        "topic_vn": "Cây cân bằng AVL",
        "topic_en": "AVL Balanced Search Trees",
        "desc_vn": "Khái niệm cân bằng cây; Cây AVL; Các phép quay cây (Single/Double Rotation) & cơ chế tự cân bằng.",
        "desc_en": "Tree balance concepts; AVL Trees; Single & Double Rotations & self-balancing mechanisms."
    },
    {
        "week": "13",
        "topic_vn": "Hàng đợi ưu tiên & Cấu trúc Heap",
        "topic_en": "Priority Queues & Heap Structure",
        "desc_vn": "ADT Hàng đợi ưu tiên (Priority Queue); Cấu trúc Heap (Min-Heap, Max-Heap); Thuật toán Heap Sort.",
        "desc_en": "Priority Queue ADT; Heap data structures (Min-Heap, Max-Heap); Heap Sort algorithm."
    },
    {
        "week": "14",
        "topic_vn": "Bảng băm & Hàm băm",
        "topic_en": "Hash Functions & Hash Tables",
        "desc_vn": "Hàm băm (Hash Function); Bảng băm (Hash Table); Các chiến lược xử lý đụng độ (Collision Handling Schemes).",
        "desc_en": "Hash functions; Hash Table structure; Collision handling schemes (Chaining, Open Addressing)."
    },
    {
        "week": "15",
        "topic_vn": "Tổng kết & Ôn tập cuối kỳ",
        "topic_en": "Course Summary & Final Review",
        "desc_vn": "Hệ thống hóa toàn bộ kiến thức môn học DSAI1002, giải đáp thắc mắc & hướng dẫn ôn tập thi cuối kỳ.",
        "desc_en": "Systematizing complete course knowledge of DSAI1002, Q&A session & final exam preparation."
    }
]

def is_valid_content_file(file_path, min_bytes=1500):
    """Kiểm tra tệp xem đã có nội dung thực tế chưa hay chỉ là template rỗng"""
    if not os.path.exists(file_path):
        return False
    size = os.path.getsize(file_path)
    return size >= min_bytes

def is_non_empty_dir(dir_path):
    """Kiểm tra thư mục xem có chứa tệp thực tế nào không"""
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        return False
    return len(os.listdir(dir_path)) > 0

def scan_lectures_dir(lectures_dir):
    """
    Quét thư mục lectures/ để tìm các thư mục tuần học và các file tài liệu bên trong.
    """
    lecture_map = {}
    if not os.path.exists(lectures_dir):
        return lecture_map

    for folder in os.listdir(lectures_dir):
        folder_path = os.path.join(lectures_dir, folder)
        if os.path.isdir(folder_path) and folder.startswith("week-"):
            parts = folder.split("-")
            if len(parts) >= 2:
                week_key = parts[1] # e.g. "01", "02"
                files = os.listdir(folder_path)

                # Kiểm tra từng loại tài nguyên
                lecture_file = os.path.join(folder_path, "lecture.ipynb")
                slides_file = os.path.join(folder_path, "slides.md")
                lab_file = os.path.join(folder_path, "lab_exercise.ipynb")
                solution_file = os.path.join(folder_path, "lab_solution.ipynb")
                data_dir_path = os.path.join(folder_path, "data")
                images_dir_path = os.path.join(folder_path, "images")
                
                notebook_link = f"[📘 Notebook](lectures/{folder}/lecture.ipynb)" if is_valid_content_file(lecture_file, 2000) else "-"
                slides_link = f"[📊 Slides](lectures/{folder}/slides.md)" if is_valid_content_file(slides_file, 1500) else "-"
                lab_link = f"[💻 Lab](lectures/{folder}/lab_exercise.ipynb)" if is_valid_content_file(lab_file, 1500) else "-"
                solution_link = f"[🔑 Đáp án / Solution](lectures/{folder}/lab_solution.ipynb)" if is_valid_content_file(solution_file, 1500) else "-"
                data_link = f"[📁 Data](lectures/{folder}/data/)" if is_non_empty_dir(data_dir_path) else "-"
                images_link = f"[🖼️ Images](lectures/{folder}/images/)" if is_non_empty_dir(images_dir_path) else "-"

                # Tìm các bài đọc bổ sung dạng .md (ngoại trừ README.md, README-en.md, slides.md, slides-en.md)
                extra_mds_vn = []
                extra_mds_en = []
                for f in sorted(files):
                    if f.endswith(".md") and f not in ["README.md", "README-en.md", "slides.md", "slides-en.md"]:
                        file_full_path = os.path.join(folder_path, f)
                        doc_title = f.replace(".md", "").replace("-vn", "").replace("-en", "").replace("_", " ").title()
                        try:
                            with open(file_full_path, "r", encoding="utf-8") as mdf:
                                for line in mdf:
                                    line_str = line.strip()
                                    if line_str.startswith("# "):
                                        doc_title = line_str.replace("# ", "").strip()
                                        break
                        except Exception:
                            pass

                        link_str = f"• [{doc_title}](lectures/{folder}/{f})"
                        if f.endswith("-en.md"):
                            extra_mds_en.append(link_str)
                        else:
                            extra_mds_vn.append(link_str)

                extra_docs_vn_str = "<br>".join(extra_mds_vn) if extra_mds_vn else ""
                extra_docs_en_str = "<br>".join(extra_mds_en) if extra_mds_en else ""

                lecture_map[week_key] = {
                    "folder": folder,
                    "notebook": notebook_link,
                    "slides": slides_link,
                    "lab": lab_link,
                    "solution": solution_link,
                    "data": data_link,
                    "images": images_link,
                    "extra_docs_vn": extra_docs_vn_str,
                    "extra_docs_en": extra_docs_en_str
                }
    return lecture_map

def generate_portal_readmes():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    readme_vn_path = os.path.join(root_dir, "README.md")
    readme_en_path = os.path.join(root_dir, "README-en.md")

    lecture_map = scan_lectures_dir(lectures_dir)

    # -------------------------------------------------------------
    # 1. TẠO FILE README.md (PHIÊN BẢN TIẾNG VIỆT CÓ DẤU CHUẨN)
    # -------------------------------------------------------------
    vn_content = """# 🐍 DSAI1002 – Cấu trúc dữ liệu và Giải thuật với Python (Data Structures and Algorithms in Python)

🌐 **Ngôn ngữ / Language:** 🇻🇳 **Tiếng Việt** | [🇬🇧 English Version (README-en.md)](README-en.md)

> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`) & ThS. Nguyễn Thành Hoàng (`hoangnt@neu.edu.vn`)  
> **Đơn vị phụ trách:** Khoa Khoa học dữ liệu và Trí tuệ nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)  
> **Chương trình đào tạo:** Data Science in Finance and E-commerce (DSFE / EP15)  
> **Số tín chỉ:** 3 Tín chỉ (30h lý thuyết, 15h thực hành, 90h tự học)  
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

## 📚 2. Ma trận Bài giảng, Tài liệu & Bài tập Thực hành (Course Matrix)

Bảng dưới đây tổng hợp chi tiết tài liệu học tập, bài giảng Notebook, slide, bài tập thực hành, tệp dữ liệu và đáp án cho **15 tuần học**:

| Tuần | Chủ đề chính (Tiếng Việt) | Bài giảng & Bài đọc (.md / .ipynb) | Slide | Bài tập Lab | Đáp án | Tài nguyên (Data / Images) | Trạng thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
"""

    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic_vn = item["topic_vn"]
        
        if w in lecture_map:
            info = lecture_map[w]
            theory_parts = []
            if info["notebook"] != "-":
                theory_parts.append(info["notebook"])
            if info["extra_docs_vn"]:
                theory_parts.append(info["extra_docs_vn"])
            
            theory_str = "<br>".join(theory_parts) if theory_parts else "-"
            resources_parts = []
            if info["data"] != "-":
                resources_parts.append(info["data"])
            if info["images"] != "-":
                resources_parts.append(info["images"])
            res_str = " | ".join(resources_parts) if resources_parts else "-"

            vn_content += f"| **Tuần {w}** | **{topic_vn}** | {theory_str} | {info['slides']} | {info['lab']} | {info['solution']} | {res_str} | ✅ *Đã sẵn sàng* |\n"
        else:
            vn_content += f"| **Tuần {w}** | {topic_vn} | - | - | - | - | - | ⏳ *Đang biên soạn* |\n"


    vn_content += """
---

## 🛠️ 3. Hướng dẫn Môi trường & Cài đặt (Setup Guide)

### 1. Cài đặt Python & Anaconda
Khuyến nghị cài đặt bản [Anaconda Distribution](https://www.anaconda.com/download) (Python 3.10+).

### 2. Cài đặt các thư viện phụ thuộc
Mở **Anaconda Prompt** hoặc **Terminal** và chạy lệnh:
```bash
pip install numpy pandas matplotlib seaborn jupyterlab
```

### 3. Mở JupyterLab làm việc
```bash
jupyter lab
```

---

## 📖 4. Tài liệu Quy trình & Quản lý Bài giảng

- 📋 **Đề cương chi tiết học phần:** Xem tệp [syllabus-vn.md](syllabus-vn.md)
- ⚙️ **Quy trình soạn bài giảng & Quản lý ảnh:** Xem tệp [QUY_TRINH_SOAN_BAI_GIANG.md](QUY_TRINH_SOAN_BAI_GIANG.md)

---

> © 2026 TS. Vũ Đức Minh & ThS. Nguyễn Thành Hoàng - Khoa Khoa học dữ liệu & Trí tuệ nhân tạo (NEU). Bản quyền tài liệu thuộc về tác giả.
"""

    with open(readme_vn_path, "w", encoding="utf-8") as f:
        f.write(vn_content)
    print("✅ Đã cập nhật file README.md (Tiếng Việt có dấu chuẩn)!")

    # -------------------------------------------------------------
    # 2. TẠO FILE README-en.md (BILINGUAL / ENGLISH VERSION)
    # -------------------------------------------------------------
    en_content = """# 🐍 DSAI1002 – Data Structures and Algorithms in Python

🌐 **Language:** [🇻🇳 Vietnamese Version (README.md)](README.md) | 🇬🇧 **English**

> **Lecturers:** Dr. Minh Duc Vu (`minhvd@neu.edu.vn`) & M.Sc. Thanh Hoang Nguyen (`hoangnt@neu.edu.vn`)  
> **Department:** School of Data Science and Artificial Intelligence – National Economics University (NEU)  
> **Academic Program:** Data Science in Finance and E-commerce (DSFE / EP15)  
> **Credits:** 3 Credits (30h Lectures, 15h Labs, 90h Self-study)  
> **Detailed Syllabus:** View [syllabus-en.md](syllabus-en.md)

---

## 📌 1. Course Description & Objectives

The course **Data Structures and Algorithms in Python (DSAI1002)** provides a comprehensive foundation and in-depth understanding of fundamental data structures (Arrays, Linked Lists, Stacks, Queues, Trees, Hash Tables) and core algorithms (Searching, Sorting, Tree Traversals, Divide & Conquer).

Students are guided to implement data structures and algorithms from scratch in **Python**, evaluate time/space complexity using Big-O notation, and solve practical business problems.

### 🎯 Course Learning Outcomes (CLOs):
1. **Complexity Analysis (G1):** Apply Big-O notation to evaluate time and space efficiency.
2. **Data Structures & Algorithms (G2):** Master ADTs, fundamental/advanced structures, and implement them from scratch.
3. **Problem Solving (G3):** Design optimal algorithms for real-world scenarios.
4. **Autonomy (G4):** Enhance independent learning and collaboration capabilities.

---

## 📚 2. Course Portal & Learning Matrix (15-Week Syllabus)

The table below summarizes lecture notebooks, reading materials, slides, lab assignments, sample datasets, and solutions for all **15 weeks**:

| Week | Main Topic (English) | Lecture & Reading Materials (.md / .ipynb) | Slides | Lab Exercise | Solutions | Resources (Data / Images) | Status |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
"""

    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic_en = item["topic_en"]
        
        if w in lecture_map:
            info = lecture_map[w]
            theory_parts = []
            if info["notebook"] != "-":
                theory_parts.append(info["notebook"])
            if info["extra_docs_en"]:
                theory_parts.append(info["extra_docs_en"])
            
            theory_str = "<br>".join(theory_parts) if theory_parts else "-"
            resources_parts = []
            if info["data"] != "-":
                resources_parts.append(info["data"])
            if info["images"] != "-":
                resources_parts.append(info["images"])
            res_str = " | ".join(resources_parts) if resources_parts else "-"

            en_content += f"| **Week {w}** | **{topic_en}** | {theory_str} | {info['slides']} | {info['lab']} | {info['solution']} | {res_str} | ✅ *Ready* |\n"
        else:
            en_content += f"| **Week {w}** | {topic_en} | - | - | - | - | - | ⏳ *In Progress* |\n"

    en_content += """
---

## 🛠️ 3. Environment & Installation Setup Guide

### 1. Python & Anaconda Installation
We recommend installing [Anaconda Distribution](https://www.anaconda.com/download) (Python 3.10+).

### 2. Dependency Package Installation
Open **Anaconda Prompt** or **Terminal** and execute:
```bash
pip install numpy pandas matplotlib seaborn jupyterlab
```

### 3. Launching JupyterLab
```bash
jupyter lab
```

---

## 📖 4. Workflow & Course Guidelines

- 📋 **Detailed Syllabus Document:** View [syllabus-en.md](syllabus-en.md)
- ⚙️ **Lecture Preparation & Image Workflow:** View [QUY_TRINH_SOAN_BAI_GIANG.md](QUY_TRINH_SOAN_BAI_GIANG.md)

---

> © 2026 Dr. Minh Duc Vu & M.Sc. Thanh Hoang Nguyen - School of Data Science & Artificial Intelligence (NEU). All rights reserved.
"""

    with open(readme_en_path, "w", encoding="utf-8") as f:
        f.write(en_content)
    print("✅ Đã cập nhật file README-en.md (Phiên bản Tiếng Anh / English Version)!")

def run_git_publish(message):
    print("Đang đẩy dữ liệu lên GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Đã xuất bản cập nhật Song ngữ lên GitHub thành công!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Lỗi khi xuất bản bằng git: {e}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Cập nhật Cổng thông tin môn học Song ngữ và đẩy bài giảng lên GitHub.")
    parser.add_argument("--message", "-m", default="docs(readme): Cập nhật Cổng thông tin môn học Song ngữ với quy định dấu gạch ngang '-' cho mục chưa có", help="Nội dung commit message")
    parser.add_argument("--no-push", action="store_true", help="Chỉ cập nhật README files, không git commit & push")
    args = parser.parse_args()

    generate_portal_readmes()

    if not args.no_push:
        run_git_publish(args.message)
