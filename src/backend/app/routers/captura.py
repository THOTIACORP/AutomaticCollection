from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import shutil, os

router = APIRouter()

UPLOAD_DIR = os.path.abspath(os.path.join(os.getcwd(), "data","captures"))
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    destination = os.path.join(UPLOAD_DIR, file.filename)
    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return JSONResponse({"status":"uploaded", "path":destination})
