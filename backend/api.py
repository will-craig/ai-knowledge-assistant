from fastapi import FastAPI, File, UploadFile
import shutil
import os
from ingest import extract_text_from_pdf

app = FastAPI()

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Knowledge Assistant!"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_location)
    
    return {"filename": file.filename, "text_preview": extracted_text[:500]}  