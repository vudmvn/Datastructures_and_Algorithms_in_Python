# Quy trình Soạn bài giảng, Quản lý Hình ảnh & Xuất bản lên GitHub (Cấu trúc dữ liệu và Giải thuật với Python - DSAI1002)

Tài liệu này hướng dẫn chi tiết quy trình chuẩn bị bài giảng, tạo tài liệu thực hành (Markdown bài giảng song ngữ, Slides PDF, Assignments), sinh/quản lý dữ liệu và hình ảnh minh họa trong thư mục `images/`, đồng thời tự động xuất bản lên GitHub bằng công cụ **Antigravity Skill** và các bộ script hỗ trợ.

---

## 🏗️ 1. Cấu trúc Quản lý Bài giảng trong Repository

Mỗi phần học sẽ nằm trong một thư mục riêng biệt tại đường dẫn `lectures/part-XX-<ten-chu-de>`:

```text
Datastructures_and_Algorithms_in_Python/
├── skills/                         # THƯ MỤC QUẢN LÝ TẤT CẢ CUSTOM SKILLS
│   ├── python-lecture-prep/        # Skill chuẩn bị bài giảng, lab & quản lý ảnh
│   │   └── SKILL.md
│   └── course-syllabus-updater/    # Skill cập nhật trang chủ syllabus & ma trận bài giảng
│       └── SKILL.md
├── lectures/
│   ├── part-01-gioi-thieu-mon-hoc/
│   │   ├── introduction-1-vn.md                  # Bài giảng Tiếng Việt
│   │   ├── introduction-1-en.md                  # Bài giảng Tiếng Anh
│   │   ├── part-01-slide-course-introduction.pdf # Slide bài giảng PDF
│   │   ├── part-01-practice-set-1.pdf            # Bài tập thực hành PDF
│   │   ├── part-01-assignment-1.pdf              # Bài tập về nhà PDF
│   │   ├── data/                                 # Bộ dữ liệu dùng trong Part 1
│   │   └── images/                               # THƯ MỤC LƯU HÌNH ẢNH MINH HỌA CỦA PART 1
│   │       ├── image-1.png
│   │       └── diagram.png
│   ├── part-02-adt-va-oop/
│   ├── part-03-thuat-toan-va-do-phuc-tap/
│   ├── part-04-nen-tang-thuat-toan-va-phuong-phap-tiep-can/
│   ├── part-05-tim-kiem-va-sap-xep/
│   ├── part-06-cau-truc-du-lieu-tuyen-tinh/
│   ├── part-07-cau-truc-du-lieu-phi-tuyen-tinh/
│   └── part-08-bang-bam-va-giai-thuat-nang-cao/
├── scripts/
│   ├── create_lecture.py           # Script khởi tạo khung bài giảng mới
│   └── publish_lecture.py          # Script tự động cập nhật README & push GitHub
├── syllabus-vn.md                  # Đề cương chi tiết học phần DSAI1002 (Tiếng Việt)
├── syllabus-en.md                  # Đề cương chi tiết học phần DSAI1002 (Tiếng Anh)
├── README-en.md                    # Trang chủ repo (Tiếng Anh) + Ma trận bài giảng
└── README.md                       # Trang chủ repo (Tiếng Việt) + Ma trận bài giảng
```

---

## 🖼️ 2. Quy chuẩn Quản lý, Căn giữa & Bảo vệ Hình ảnh (Image Preservation & Centering Rules)

1. **Vị trí lưu trữ**: Tất cả ảnh minh họa, sơ đồ cấu trúc dữ liệu, infographic hoặc biểu đồ được tạo/export cho phần học nào sẽ nằm trong thư mục `lectures/part-XX-<slug>/images/`.
2. **Quy tắc Không Ghi đè & Tự động Đổi tên (No-Overwrite & Auto-Rename Rule)**:
   - **Tuyệt đối không xóa hoặc ghi đè** lên các tệp ảnh đã tồn tại trong thư mục `images/`.
   - Nếu tên tệp ảnh mới định lưu bị trùng tên với tệp ảnh đã có sẵn, Antigravity Skill sẽ tự động thêm số thứ tự phân biệt (ví dụ `image-1.png`, `image-2.png` hoặc `chart-v2.png`) để đảm bảo không làm mất ảnh cũ.
3. **Quy tắc Bắt buộc Căn giữa (Image Centering Rule)**:
   - **TẤT CẢ HÌNH ẢNH** trong các tệp Markdown (`README.md`, các bài đọc `.md`) và slide **PHẢI ĐƯỢC CĂN GIỮA (CENTERED)** để hiển thị trực quan và đẹp mắt.
   - Cú pháp HTML Căn giữa Chuẩn:
     ```html
     <p align="center">
       <img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="800" />
     </p>
     ```
4. **Tự động hóa**: Antigravity Skill sẽ tự động chuyển tệp ảnh vào `images/`, đổi tên chống trùng, căn giữa ảnh và cập nhật lại đường dẫn tương đối chính xác trong các tệp `.md`.

5. **Quy tắc Cập nhật Ngày chỉnh sửa (Auto Last-Updated Date Rule)**:
   - Mỗi tệp bài giảng Markdown (`.md`) bắt buộc phải có dòng thông tin ngày cập nhật ngay dưới tiêu đề bài học.
   - Khi tạo mới bài giảng hoặc bất kỳ khi nào chỉnh sửa, cập nhật nội dung của tệp bài giảng `.md`, Antigravity Skill sẽ tự động cập nhật dòng ngày này về ngày hiện tại (`**Cập nhật lần cuối:** <ngày> tháng <tháng> năm <năm>` cho Tiếng Việt hoặc `**Last updated:** <Month> <Day>, <Year>` cho Tiếng Anh).

6. **Quy chuẩn Slide TeX/PDF & Đặt tên tệp PDF chuẩn hóa**:
   - **Quy chuẩn đặt tên tệp PDF:**
     - Slide bài giảng: `part-XX-slide-<topic>.pdf`
     - Bài tập thực hành: `part-XX-practice-set-<N>.pdf`
     - Bài tập về nhà: `part-XX-assignment-<N>.pdf`
   - **Kiểm tra đường dẫn ảnh trong `.tex`:** Mọi hình ảnh chèn vào Slide LaTeX Beamer phải được đối chiếu tồn tại thực tế tại thư mục `images/`. Macro `\imageplaceholder` được thiết lập tự động render hình ảnh thật qua `\IfFileExists`.
   - **Biên dịch XeLaTeX & Xóa tệp tạm:** Biên dịch bằng `xelatex -interaction=nonstopmode <filename>.tex` (2 lượt). Ngay sau khi xuất xong tệp PDF, Antigravity Skill **bắt buộc dọn dẹp xóa các tệp tạm** (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.vrb`) để repo luôn sạch sẽ.

7. **Quy tắc Cập nhật Link Slide PDF & Assignment vào `README.md` & `README-en.md`**:
   - Cập nhật liên kết slide PDF và tệp bài tập vào đúng 2 cột tương ứng (**Slide bài giảng** và **Bài tập & Thực hành**) thuộc bảng Ma trận bài giảng ở cả 2 tệp `README.md` và `README-en.md`.
   - **Dùng liên kết Markdown chuẩn:** Trỏ trực tiếp tới đường dẫn tương đối của tệp PDF (ví dụ: `lectures/part-01-gioi-thieu-mon-hoc/part-01-slide-course-introduction.pdf`).

---

## ⚡ 3. Quy trình Soạn Bài giảng Chi tiết

### Bước 1: Khởi tạo khung bài giảng phần mới
Chạy script Python để sinh nhanh bộ file mẫu (bao gồm cả thư mục `images/` và `data/`):
```bash
python scripts/create_lecture.py --part <Số_phần> --title "<Tên_chủ_đề>"
```
*Ví dụ:*
```bash
python scripts/create_lecture.py --part 3 --title "Thuật toán và Độ phức tạp tiệm cận"
```

### Bước 2: Nhờ AI Assistant (Antigravity Agent) biên soạn nội dung
Khi Antigravity được kích hoạt, bạn chỉ cần ra lệnh cho AI bằng tiếng Việt:
> *"Soạn bài giảng Part 3 về Thuật toán và Độ phức tạp tiệm cận theo đề cương syllabus-vn.md. Tạo thêm sơ đồ minh họa đặt vào folder images và nhúng đường dẫn tương đối vào file markdown bài giảng."*

Agent sẽ tự động đọc `syllabus-vn.md`, áp dụng `python-lecture-prep` skill để:
1. Điền lý thuyết chi tiết vào các bài giảng `.md` (Song ngữ Tiếng Việt và Tiếng Anh).
2. Lưu các bức ảnh minh họa vào `images/` và chèn đường dẫn `images/<filename>` vào các file `.md`.
3. Tạo mã nguồn ví dụ Python từ đầu (from scratch) có chú thích Tiếng Việt, chuẩn PEP8.
4. Tạo dữ liệu/mẫu thử nghiệm chất lượng cao lưu vào thư mục `data/`.
5. Sinh slide PDF và bài tập thực hành/assignment theo quy chuẩn tên tệp `part-XX-...pdf`.

### Bước 3: Xuất bản tự động lên GitHub
Sau khi biên soạn xong, bạn chỉ cần chạy:
```bash
python scripts/publish_lecture.py -m "feat(lecture): Hoàn thành bài giảng Part 03"
```
Script sẽ tự động:
1. Đọc tất cả thư mục trong `lectures/`.
2. Cập nhật bảng **Mục lục bài giảng** chuyên nghiệp tại [README.md](README.md) và [README-en.md](README-en.md).
3. Thực hiện `git add .`, `git commit` và `git push` trực tiếp lên GitHub repository.

---

## 🌐 4. Thông tin Repository & Giảng viên
- **Giảng viên:** TS. Vũ Đức Minh (minhvd@neu.edu.vn)
- **Học phần:** Cấu trúc dữ liệu và Giải thuật với Python (DSAI1002) - ĐH Kinh tế Quốc dân
- **GitHub Repository:** [vudmvn/Datastructures_and_Algorithms_in_Python](https://github.com/vudmvn/Datastructures_and_Algorithms_in_Python)
