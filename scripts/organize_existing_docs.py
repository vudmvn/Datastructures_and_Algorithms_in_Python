import os
import sys
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
intro_dir = os.path.join(base_dir, "introduction-to-algorithm")

# Week 1
w1_dir = os.path.join(base_dir, "lectures", "week-01-gioi-thieu-hoc-phan-adt")
for f in ["introduction-1.md", "introduction-to-algorithm-1.md"]:
    src = os.path.join(intro_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(w1_dir, f))

# Week 2
w2_dir = os.path.join(base_dir, "lectures", "week-02-do-phuc-tap-tiem-can-big-o")
for f in ["complexity-analysis-2.md", "master-theorem.md"]:
    src = os.path.join(intro_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(w2_dir, f))

# Week 3
w3_dir = os.path.join(base_dir, "lectures", "week-03-tim-kiem-sap-xep-co-ban")
for f in ["Part_1.md", "Part_2.md", "Part_3.md", "Part_4.md", "Problem-Set-1.md"]:
    src = os.path.join(intro_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(w3_dir, f))

# Copy images
images_src = os.path.join(intro_dir, "images")
if os.path.exists(images_src):
    for img in os.listdir(images_src):
        src = os.path.join(images_src, img)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(w1_dir, "images", img))
            shutil.copy2(src, os.path.join(w2_dir, "images", img))

# Copy root image files
for img in os.listdir(intro_dir):
    if img.endswith(".png") or img.endswith(".jpg"):
        src = os.path.join(intro_dir, img)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(w1_dir, "images", img))
            shutil.copy2(src, os.path.join(w2_dir, "images", img))

print("✅ Đã tổ chức tài liệu cũ vào các thư mục tuần tương ứng!")
