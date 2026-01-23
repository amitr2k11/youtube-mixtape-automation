from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
import os
import shutil

from backend.pipeline import run_pipeline

app = FastAPI()

# =====================
# PATHS
# =====================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
VIDEO_PATH = os.path.join(OUTPUT_DIR, "mixtape.mp4")
DESC_PATH = os.path.join(OUTPUT_DIR, "ai_description.txt")


os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================
# UPLOAD AUDIO
# =====================
@app.post("/upload-audio")
async def upload_audio(files: list[UploadFile] = File(...)):
    for file in files:
        file_path = os.path.join(AUDIO_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {"status": "uploaded"}

# =====================
# CREATE MIXTAPE (ASYNC)
# =====================
@app.post("/create-mixtape")
def create_mixtape(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pipeline)
    return {"status": "processing"}

# =====================
# DOWNLOAD VIDEO
# =====================
@app.get("/download/video")
def download_video():
    if not os.path.exists(VIDEO_PATH):
        return {"status": "not_ready"}

    return FileResponse(
        path=VIDEO_PATH,
        media_type="video/mp4",
        filename="mixtape.mp4"
    )

# =====================
# DOWNLOAD DESCRIPTION
# =====================
@app.get("/download/description")
def download_description():
    if not os.path.exists(DESC_PATH):
        return {"status": "not_ready"}

    return FileResponse(
        path=DESC_PATH,
        media_type="text/plain",
        filename="ai_description.txt"
    )
