import os
import sys
import urllib.request

def download_covers():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    assets_dir = os.path.join(root_dir, "assets", "images")
    os.makedirs(assets_dir, exist_ok=True)
    
    books = {
        "data-structures-algorithms-necaise-cover.jpg": "https://covers.openlibrary.org/b/isbn/9780470618295-M.jpg",
        "data-structures-algorithms-goodrich-cover.jpg": "https://covers.openlibrary.org/b/isbn/9781118290279-M.jpg",
        "fundamentals-python-data-structures-lambert-cover.jpg": "https://covers.openlibrary.org/b/isbn/9780357122754-M.jpg",
        "data-structure-algorithmic-thinking-karumanchi-cover.jpg": "https://covers.openlibrary.org/b/isbn/9788194254003-M.jpg"
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for filename, url in books.items():
        filepath = os.path.join(assets_dir, filename)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    download_covers()
