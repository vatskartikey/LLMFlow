import fitz  # PyMuPDF for PDF
from docx import Document

def extract_text_from_file(filepath):
    if filepath.endswith(".pdf"):
        text = ""
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
        return text

    elif filepath.endswith(".docx"):
        doc = Document(filepath)
        return "\n".join([p.text for p in doc.paragraphs])

    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    else:
        return "Unsupported file format."
