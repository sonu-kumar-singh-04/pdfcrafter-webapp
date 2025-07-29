from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from typing import List
from io import BytesIO
from PIL import Image
from fpdf import FPDF
import io
import base64

def merge_pdfs(pdf_files: List[BytesIO]) -> BytesIO:
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    output = BytesIO()
    merger.write(output)
    output.seek(0)
    return output

def split_pdf(pdf_file: BytesIO) -> List[BytesIO]:
    reader = PdfReader(pdf_file)
    outputs = []
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output = BytesIO()
        writer.write(output)
        output.seek(0)
        outputs.append(output)
    return outputs

def images_to_pdf(image_files: List[BytesIO]) -> BytesIO:
    images = [Image.open(img).convert("RGB") for img in image_files]
    output = BytesIO()
    images[0].save(output, format="PDF", save_all=True, append_images=images[1:])
    output.seek(0)
    return output

def text_to_pdf(text: str) -> BytesIO:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.cell(0, 10, line, ln=True)
    output = BytesIO(pdf.output(dest='S').encode('latin1'))
    output.seek(0)
    return output