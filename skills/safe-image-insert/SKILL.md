---
name: safe-image-insert
description: Skill chuyên dụng đảm bảo bảo vệ hình ảnh, tuyệt đối không xóa hoặc ghi đè (never overwrite/delete) lên các ảnh cũ khi chèn hình ảnh mới vào bài giảng Markdown hoặc Jupyter Notebooks. Tự động phát hiện trùng tên, tự động cấp phát tên mới (auto-rename with counter e.g., image-1.png, image-2.png) và tự động căn giữa (centered <p align="center"><img .../></p>) trong tệp Markdown/Notebook.
---

# Skill: Bảo vệ Hình ảnh & Chèn Ảnh Chống Ghi Đè (Safe Image Insertion & Preservation)

Skill này thiết lập quy trình nghiêm ngặt và công cụ tự động để **BẢO VỆ HÌNH ẢNH CŨ**, tuyệt đối **KHÔNG XÓA HOẶC GHI ĐÈ** bất kỳ tệp ảnh nào đã tồn tại trong repository môn học `Datastructures_and_Algorithms_in_Python`.

---

## 🛡️ 1. Quy tắc Bảo vệ Ảnh Tuyệt đối (Absolute Non-Overwrite Rules)

1. **Kiểm tra Tồn tại (Existence Check)**:
   - Trước khi lưu, copy hoặc chuyển bất kỳ tệp ảnh nào vào thư mục `images/` (hoặc `assets/images/`), hệ thống **bắt buộc kiểm tra** tệp đã tồn tại hay chưa.

2. **Tự động Đổi tên Chống Trùng (Auto-rename Collision Handling)**:
   - Nếu tên tệp dự định lưu (ví dụ `linked_list.png`) đã tồn tại, hệ thống **tự động bổ sung chỉ số thứ tự tăng dần**:
     - `linked_list.png` (ảnh cũ - giữ nguyên 100%)
     - `linked_list-1.png` (ảnh mới)
     - `linked_list-2.png` (ảnh mới tiếp theo)

3. **Bắt buộc Căn giữa Ảnh (Mandatory Image Centering)**:
   - Mọi liên kết chèn ảnh trong `.md` hoặc `.ipynb` **phải sử dụng cú pháp HTML căn giữa chuẩn**:
     ```html
     <p align="center">
       <img src="images/linked_list-1.png" alt="Mô tả hình ảnh" width="800" />
     </p>
     ```

4. **Sử dụng Helper Script Chuyên dụng**:
   - Khi chèn ảnh từ dòng lệnh hoặc Python script, luôn gọi helper `scripts/safe_insert_image.py` để đảm bảo an toàn tuyệt đối.

---

## 🛠️ 2. Hướng dẫn Sử dụng Helper Script (`scripts/safe_insert_image.py`)

Chạy lệnh để chèn ảnh an toàn:
```bash
python scripts/safe_insert_image.py --src <duong-dan-anh-nguon> --dest <thu-muc-dich> [--name <ten-file-mong-muon>]
```

*Ví dụ:*
```bash
python scripts/safe_insert_image.py --src C:/tmp/diagram.png --dest lectures/week-01-gioi-thieu-hoc-phan-adt/images --name overview.png
```
Nếu `overview.png` đã có sẵn trong `images/`, script sẽ tự động lưu thành `overview-1.png` và in ra cú pháp HTML căn giữa để sẵn sàng dán vào bài giảng.
