#!/usr/bin/env python3
"""
Script tự động quét tất cả tệp .md trong `lectures/` và cập nhật dòng ngày "Cập nhật lần cuối: <ngày>" / "Last updated: <date>"
"""

import os
import sys
import re
from datetime import datetime

VIETNAMESE_MONTHS = [
    "", "tháng 1", "tháng 2", "tháng 3", "tháng 4", "tháng 5", "tháng 6",
    "tháng 7", "tháng 8", "tháng 9", "tháng 10", "tháng 11", "tháng 12"
]

def get_formatted_date_vn(dt=None):
    if dt is None:
        dt = datetime.now()
    return f"{dt.day} {VIETNAMESE_MONTHS[dt.month]} năm {dt.year}"

def get_formatted_date_en(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%B %d, %Y")

def update_file_date(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    is_english = file_path.endswith("-en.md") or "README-en.md" in file_path
    
    if is_english:
        date_str = f"**Last updated:** {get_formatted_date_en()}"
        pattern = r"\*\*Last updated:\*\*.*"
    else:
        date_str = f"**Cập nhật lần cuối:** {get_formatted_date_vn()}"
        pattern = r"\*\*Cập nhật lần cuối:\*\*.*"

    if re.search(pattern, content):
        new_content = re.sub(pattern, date_str, content)
    else:
        # Chèn bên dưới tiêu đề # đầu tiên
        lines = content.splitlines()
        inserted = False
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if not inserted and line.startswith("# "):
                new_lines.append("")
                new_lines.append(date_str)
                inserted = True
        new_content = "\n".join(new_lines)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Đã cập nhật ngày trong {os.path.basename(file_path)}")

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    if os.path.exists(lectures_dir):
        for root, dirs, files in os.walk(lectures_dir):
            for file in files:
                if file.endswith(".md"):
                    update_file_date(os.path.join(root, file))

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
