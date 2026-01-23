import os
import shutil
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
from backend.pipeline import run_pipeline

# =====================
# CONSTANTS
# =====================
AUDIO_DIR = "audio"
OUTPUT_DIR = "output"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = FastAPI()

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
# CREATE MIXTAPE
# =====================
@app.post("/create-mixtape")
def create_mixtape(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pipeline)
    return {"status": "mixtape_started"}

# =====================
# DOWNLOAD VIDEO
# =====================
@app.get("/download/video")
def download_video():
    video_path = os.path.join(OUTPUT_DIR, "mixtape.mp4")

    if os.path.exists(video_path):
        return FileResponse(
            path=video_path,
            media_type="video/mp4",
            filename="mixtape.mp4"
        )

    return {"status": "not_ready"}

# =====================
# DOWNLOAD DESCRIPTION
# =====================
@app.get("/download/description")
def download_description():
    desc_path = os.path.join(OUTPUT_DIR, "ai_description.txt")

    if os.path.exists(desc_path):
        return FileResponse(
            path=desc_path,
            media_type="text/plain",
            filename="ai_description.txt"
        )

    return {"status": "not_ready"}
