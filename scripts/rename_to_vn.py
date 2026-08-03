import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lectures"))

renames = [
    ("week-01-gioi-thieu-hoc-phan-adt", "introduction-1.md", "introduction-1-vn.md"),
    ("week-01-gioi-thieu-hoc-phan-adt", "introduction-to-algorithm-1.md", "introduction-to-algorithm-1-vn.md"),
    ("week-02-do-phuc-tap-tiem-can-big-o", "complexity-analysis-2.md", "complexity-analysis-2-vn.md"),
    ("week-02-do-phuc-tap-tiem-can-big-o", "master-theorem.md", "master-theorem-vn.md"),
    ("week-03-tim-kiem-sap-xep-co-ban", "Part_1.md", "part-1-vn.md"),
    ("week-03-tim-kiem-sap-xep-co-ban", "Part_2.md", "part-2-vn.md"),
    ("week-03-tim-kiem-sap-xep-co-ban", "Part_3.md", "part-3-vn.md"),
    ("week-03-tim-kiem-sap-xep-co-ban", "Part_4.md", "part-4-vn.md"),
    ("week-03-tim-kiem-sap-xep-co-ban", "Problem-Set-1.md", "problem-set-1-vn.md"),
]

for folder, src_name, dst_name in renames:
    src = os.path.join(base_dir, folder, src_name)
    dst = os.path.join(base_dir, folder, dst_name)
    if os.path.exists(src):
        os.rename(src, dst)
        print(f"Renamed: {src_name} -> {dst_name}")
