# 🎵 YouTube Mixtape Automation

A **full‑stack automation project** that converts multiple MP3 audio tracks into a **single YouTube‑ready mixtape video** with minimal manual effort.

This project demonstrates **real‑world backend engineering**, media processing with **FFmpeg**, background task handling, and **cloud deployment troubleshooting**.

---

## 🚀 What This Project Does

1. Upload multiple MP3 audio files
2. Automatically merge them into a single mixtape audio
3. Generate timestamps & descriptions
4. Convert merged audio into a **YouTube‑ready MP4 video**
5. Allow video & description download via API

All processing runs **asynchronously in the backend**.

---

## 🧠 Why This Project Matters

This project focuses on **execution over idea** and solves real engineering challenges:

* Handling large media files
* FFmpeg command orchestration
* Background task execution in FastAPI
* Cloud deployment (Railway / Docker)
* Memory & quota constraints
* Graceful failure handling (AI optional)

---

## 🏗️ Architecture Overview

```
Frontend (Streamlit)
        │
        ▼
FastAPI Backend
        │
        ├── upload-audio
        ├── create-mixtape (background task)
        ├── download/video
        └── download/description
        │
        ▼
Core Processing Pipeline
        ├── merge_audio.py
        ├── generate_description.py
        ├── ai_description.py (optional)
        └── audio_to_video.py
```

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **FastAPI** – backend API
* **Streamlit** – frontend UI
* **FFmpeg** – audio/video processing
* **Docker** – containerization
* **Railway** – cloud deployment

---

## 📁 Project Structure

```
youtube-mixtape-automation/
│
├── backend/
│   ├── main.py          # FastAPI app
│   └── pipeline.py      # Orchestrates processing
│
├── core/
│   ├── merge_audio.py
│   ├── generate_description.py
│   ├── ai_description.py
│   └── audio_to_video.py
│
├── frontend/
│   └── app.py           # Streamlit UI
│
├── output/              # Generated files (gitignored)
├── audio/               # Uploaded audio (gitignored)
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/amit2k11/youtube-mixtape-automation.git
cd youtube-mixtape-automation
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

### 5️⃣ Start Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

---

## 🌐 API Endpoints

| Method | Endpoint                | Description                 |
| ------ | ----------------------- | --------------------------- |
| POST   | `/upload-audio`         | Upload MP3 files            |
| POST   | `/create-mixtape`       | Start background processing |
| GET    | `/download/video`       | Download final video        |
| GET    | `/download/description` | Download description        |

---

## ⚠️ AI Description (Optional)

AI‑based description generation uses OpenAI **if API key is available**.

If not:

* Pipeline continues without failure
* Video generation still completes successfully

This was intentionally designed to **avoid hard dependency on AI**.

---

## 🧪 What I Learned

* Handling long‑running background jobs safely
* Debugging FFmpeg failures
* Cloud deployment limitations (memory, quotas)
* Writing fault‑tolerant pipelines
* API‑first design

---

## 🎯 Ideal Use Cases

* YouTube creators
* Podcast compilations
* DJ mixtapes
* Audio‑only content repurposing

---

## 📌 Status

✅ Stable locally
✅ Cloud‑ready (Railway)
⚠️ AI optional based on quota

---

## 🤝 Collaboration

This project was shared with peers for learning and collaboration.
Contributions and feedback are welcome.

---

## 📄 License

MIT License

---

## ⭐ Final Note

This repository represents **real‑world engineering work**, not a tutorial demo.

If you're reviewing this for an interview:

> Ask me how I debugged this — I can walk you through every failure.

---

**Built with persistence, debugging, and a lot of coffee ☕**

