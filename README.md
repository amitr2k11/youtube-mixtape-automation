# YouTube Mixtape Automation 🎶📹

## Features
- Upload multiple MP3 files
- Merge audio into a single mixtape
- Auto-generate YouTube description
- Create video from audio using FFmpeg

## Tech Stack
- FastAPI
- Python
- FFmpeg
- Streamlit (frontend)
- OpenAI (optional)

## How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
