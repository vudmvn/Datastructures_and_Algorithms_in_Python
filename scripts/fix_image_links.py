import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
lectures_dir = os.path.join(root_dir, "lectures")

def fix_image_links_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    lecture_folder = os.path.dirname(file_path)
    images_dir = os.path.join(lecture_folder, "images")
    
    # 1. Replace markdown image links ![alt](path) if path doesn't start with images/ or http
    def replace_md_img(match):
        alt = match.group(1)
        path = match.group(2)
        if path.startswith("http://") or path.startswith("https://") or path.startswith("images/") or path.startswith("/"):
            return match.group(0)
        
        filename = os.path.basename(path)
        # Check if file exists in images/
        new_path = f"images/{filename}"
        return f'<p align="center">\n  <img src="{new_path}" alt="{alt}" width="800" />\n</p>'

    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_img, content)

    # 2. Replace html <img src="path"> if path doesn't start with images/ or http
    def replace_html_img(match):
        full_tag = match.group(0)
        src = match.group(2)
        if src.startswith("http://") or src.startswith("https://") or src.startswith("images/") or src.startswith("/"):
            return full_tag
        filename = os.path.basename(src)
        new_src = f"images/{filename}"
        return full_tag.replace(src, new_src)

    content = re.sub(r'<img([^>]+)src=["\']([^"\']+)["\']', replace_html_img, content)

    if content != orig_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Đã cập nhật link ảnh trong {os.path.relpath(file_path, root_dir)}")

def main():
    if not os.path.exists(lectures_dir):
        print("Thư mục lectures không tồn tại.")
        return

    for root, dirs, files in os.walk(lectures_dir):
        for file in files:
            if file.endswith(".md"):
                fix_image_links_in_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
