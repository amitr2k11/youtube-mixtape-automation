from fastapi import UploadFile, File
import shutil

from fastapi import FastAPI, BackgroundTasks
from backend.pipeline import run_pipeline
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.post("/create-mixtape")
def create_mixtape(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pipeline)
    return {"status": "Mixtape started in background"}

@app.get("/download/video")
def download_video():
    video_path = "output/mixtape.mp4"

    if os.path.exists(video_path):
        return FileResponse(
            path=video_path,
            media_type="video/mp4",
            filename="mixtape.mp4"
        )

    return {"status": "not_ready"}

@app.get("/download/description")
def download_description():
    desc_path = "output/ai_description.txt"

    if os.path.exists(desc_path):
        return FileResponse(
            path=desc_path,
            media_type="text/plain",
            filename="ai_description.txt"
        )

    return {"status": "not_ready"}

from fastapi.responses import FileResponse
import os

@app.get("/download/video")
def download_video():
    video_path = "output/mixtape.mp4"

    if os.path.exists(video_path):
        return FileResponse(
            path=video_path,
            media_type="video/mp4",
            filename="mixtape.mp4"
        )

    return {"status": "not_ready"}


@app.get("/download/description")
def download_description():
    desc_path = "output/ai_description.txt"

    if os.path.exists(desc_path):
        return FileResponse(
            path=desc_path,
            media_type="text/plain",
            filename="ai_description.txt"
        )

    return {"status": "not_ready"}

@app.post("/upload-audio")
async def upload_audio(files: list[UploadFile] = File(...)):
    os.makedirs("audio", exist_ok=True)

    for file in files:
        file_path = os.path.join("audio", file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {"status": "uploaded"}





