import pypdf
import os
import re

def main():
    pdf_path = "Narasimha Karumanchi - Data Structure and Algorithmic Thinking with Python_ Data Structure and Algorithmic Puzzles-CareerMonk Publications (2020) (1).pdf"
    md_path = "Narasimha Karumanchi - Data Structure and Algorithmic Thinking with Python_ Data Structure and Algorithmic Puzzles-CareerMonk Publications (2020) (1).md"
    
    print(f"Reading PDF from {pdf_path}...")
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages to convert: {total_pages}")
    
    # We will do some basic cleanup of common mangled words in CareerMonk publications if possible,
    # but primarily write the extracted text page by page.
    # Note: CareerMonk publications use some obfuscated fonts that map to Syriac/Arabic Unicode ranges.
    
    print("Writing markdown file...")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Data Structure and Algorithmic Thinking with Python\n")
        f.write(f"## Data Structure and Algorithmic Puzzles\n\n")
        f.write(f"**Author:** Narasimha Karumanchi\n")
        f.write(f"**Publisher:** CareerMonk Publications (2020)\n\n")
        f.write(f"---\n\n")
        
        for i in range(total_pages):
            if i % 50 == 0:
                print(f"Converting page {i}/{total_pages}...")
            
            page = reader.pages[i]
            text = page.extract_text() or ""
            
            # Simple clean up of trailing spaces on each line
            lines = [line.rstrip() for line in text.split('\n')]
            cleaned_text = "\n".join(lines)
            
            f.write(f"## Page {i + 1}\n\n")
            f.write(cleaned_text)
            f.write("\n\n---\n\n")
            
    print(f"Successfully converted PDF to Markdown at: {md_path}")
    print(f"File size: {os.path.getsize(md_path)} bytes")

if __name__ == "__main__":
    main()
