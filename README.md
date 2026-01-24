\# 🎵 YouTube Mixtape Automation



Create a full-length YouTube-style mixtape video automatically from multiple MP3 files. This project merges audio tracks, generates a simple video, and exposes everything via a FastAPI backend with an optional Streamlit frontend.



---



\## 🚀 What This Project Does



1\. Upload multiple MP3 files

2\. Merge them into a single mixtape audio

3\. Generate a video (black background + audio)

4\. Expose APIs to download the final video



> ✅ AI description generation is \*\*optional\*\* and safely skipped if no OpenAI quota/key is available.



---



\## 🧠 Tech Stack



\* \*\*Python 3.10+\*\*

\* \*\*FastAPI\*\* – backend APIs

\* \*\*Uvicorn\*\* – ASGI server

\* \*\*FFmpeg\*\* – audio/video processing

\* \*\*Streamlit\*\* – simple frontend (optional)

\* \*\*Docker\*\* – deployment



---



\## 📂 Project Structure



```

youtube-mixtape-automation/

│

├── backend/

│   ├── main.py          # FastAPI app

│   └── pipeline.py      # Orchestrates audio → video pipeline

│

├── core/

│   ├── merge\_audio.py

│   ├── generate\_description.py

│   ├── ai\_description.py

│   └── audio\_to\_video.py

│

├── frontend/

│   └── app.py           # Streamlit UI

│

├── audio/               # Uploaded MP3s (gitignored)

├── output/              # Generated files (gitignored)

│

├── requirements.txt

├── Dockerfile

└── .gitignore

```



---



\## ▶️ Run Locally



\### 1️⃣ Create Virtual Environment



```bash

python -m venv venv

venv\\Scripts\\activate   # Windows

```



\### 2️⃣ Install Dependencies



```bash

pip install -r requirements.txt

```



\### 3️⃣ Start Backend



```bash

uvicorn backend.main:app --reload

```



Open Swagger UI:

👉 \[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



---



\## 🔌 API Endpoints



| Method | Endpoint                | Description                 |

| ------ | ----------------------- | --------------------------- |

| POST   | `/upload-audio`         | Upload MP3 files            |

| POST   | `/create-mixtape`       | Start background processing |

| GET    | `/download/video`       | Download final MP4          |

| GET    | `/download/description` | Download text description   |



---



\## 🎬 Output



\* \*\*mixtape.mp4\*\* – Final video

\* \*\*merged audio\*\* – Combined MP3



All outputs are created inside the `output/` folder.



---



\## ☁️ Deployment



Tested on:



\* \*\*Railway\*\*

\* \*\*Docker local build\*\*



> ⚠️ Free tiers may be slow due to FFmpeg processing.



---



\## 🧪 Status



✅ Stable local version

✅ Video-only pipeline works reliably

⚠️ AI description depends on OpenAI quota



---



\## 👤 Author



\*\*Amit Ranjan\*\*

GitHub: \[https://github.com/amitr2k11](https://github.com/amitr2k11)



---



\## 📜 License



MIT License – feel free to fork, improve, and learn.



