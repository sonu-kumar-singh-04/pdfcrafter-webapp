from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .pdf_utils import merge_pdfs, split_pdf, images_to_pdf, text_to_pdf  # remove sign_pdf
from io import BytesIO
import zipfile
import logging
from typing import Optional
import os
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Set up templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/merge-pdfs/")
async def merge_pdfs_endpoint(files: list[UploadFile] = File(...)):
    pdf_streams = [BytesIO(await file.read()) for file in files]
    merged_pdf = merge_pdfs(pdf_streams)  # merged_pdf should be a BytesIO object

    return StreamingResponse(
        merged_pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=merged.pdf"}
    )

@app.post("/split-pdf/")
async def split_pdf_endpoint(file: UploadFile = File(...)):
    pdf_stream = BytesIO(await file.read())
    split_pages = split_pdf(pdf_stream)
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        for idx, page in enumerate(split_pages):
            zipf.writestr(f"page_{idx+1}.pdf", page.getvalue())
    zip_buffer.seek(0)
    return StreamingResponse(zip_buffer, media_type="application/zip", headers={
        "Content-Disposition": "attachment; filename=split_pages.zip"
    })

@app.post("/images-to-pdf/")
async def images_to_pdf_endpoint(files: list[UploadFile] = File(...)):
    image_streams = [BytesIO(await file.read()) for file in files]
    pdf = images_to_pdf(image_streams)
    return StreamingResponse(pdf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=images.pdf"
    })

@app.post("/text-to-pdf/")
async def text_to_pdf_endpoint(text: str = Form(...)):
    pdf = text_to_pdf(text)
    return StreamingResponse(pdf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=text.pdf"
    })