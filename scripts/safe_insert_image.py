import os
import shutil
import sys
import argparse

def safe_insert_image(src_path, dest_dir, preferred_name=None):
    """
    Safely copies an image to dest_dir without overwriting any existing image.
    If preferred_name exists, automatically appends -1, -2, etc. (e.g. image-1.png).
    Returns the final filename, relative path, and HTML centered code snippet.
    """
    os.makedirs(dest_dir, exist_ok=True)
    if not preferred_name:
        preferred_name = os.path.basename(src_path)
    
    base, ext = os.path.splitext(preferred_name)
    counter = 1
    target_name = preferred_name
    target_path = os.path.join(dest_dir, target_name)
    
    while os.path.exists(target_path):
        target_name = f"{base}-{counter}{ext}"
        target_path = os.path.join(dest_dir, target_name)
        counter += 1
        
    shutil.copy2(src_path, target_path)
    rel_path = os.path.join("images", target_name).replace("\\", "/")
    html_code = f'<p align="center">\n  <img src="{rel_path}" alt="{base}" width="800" />\n</p>'
    
    print(f"✅ Successfully inserted image without overwriting existing files!")
    print(f"📁 Saved to: {target_path}")
    print(f"🔗 HTML Centered Snippet:\n{html_code}")
    
    return target_name, target_path, html_code

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    parser = argparse.ArgumentParser(description="Safely copy image without overwriting existing files.")
    parser.add_argument("--src", required=True, help="Source image path")
    parser.add_argument("--dest", required=True, help="Destination directory (e.g., lectures/week-01/images)")
    parser.add_argument("--name", help="Preferred destination filename")
    
    args = parser.parse_args()
    safe_insert_image(args.src, args.dest, args.name)

if __name__ == "__main__":
    main()
