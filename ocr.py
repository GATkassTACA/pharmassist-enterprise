
import pdfplumber
import pytesseract
from PIL import Image
import os

def extract_text_from_pdf(pdf_path, output_path):
    full_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(image)
            full_text.append(text)
    with open(output_path, "w") as f:
        f.write("\n".join(full_text))
