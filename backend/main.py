from fastapi import FastAPI, BackgroundTasks
from backend.pipeline import run_pipeline

app = FastAPI()

@app.post("/create-mixtape")
def create_mixtape(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pipeline)
    return {"status": "Mixtape started in background"}


