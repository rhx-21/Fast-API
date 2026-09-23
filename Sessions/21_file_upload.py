from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Ensure, Folder exist or not

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
    
# static file setup
# URL:http://127.0.0.1:8000/files/<filename>

app.mount("/files",StaticFiles(directory=UPLOAD_DIR), name="files")

# API - Upload file

@app.post("/upload")
def upload_file(file:UploadFile=File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)
    
    if not filename == file.filename:
        raise HTTPException(
            status_code=400,
            detail="File not Selected"
        )

# Save file in binary

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
    return {
        "Message":"File Uploaded Successfully",
        "filename":filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
         }
        
#  API - Get File

@app.get("/files/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )
        
    return{
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


@app.get("/")
def home():
    return{
        "Message": "Here, You can upload the Files"
    }
