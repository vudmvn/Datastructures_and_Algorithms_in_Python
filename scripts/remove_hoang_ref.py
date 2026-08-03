import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def replace_in_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    # Replacements
    content = content.replace("", "")
    content = content.replace("", "")
    content = content.replace("", "")
    content = content.replace("", "")
    content = content.replace("TS. Vũ Đức Minh (`minhvd@neu.edu.vn`) (`hoangnt@neu.edu.vn`)", "TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)")
    content = content.replace("Dr. Minh Duc Vu (`minhvd@neu.edu.vn`) (`hoangnt@neu.edu.vn`)", "Dr. Minh Duc Vu (`minhvd@neu.edu.vn`)")
    content = content.replace("", "")
    content = content.replace("", "")
    content = content.replace("**Lecturer:**", "**Lecturer:**")

    if content != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {os.path.relpath(file_path, root_dir)}")

for root, dirs, files in os.walk(root_dir):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith((".md", ".py", ".html", ".ipynb", ".json")):
            replace_in_file(os.path.join(root, file))

print("✅ Đã xoá toàn bộ thông tin M.Sc. Nguyen Thanh Hoang!")
