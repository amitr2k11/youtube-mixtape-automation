import streamlit as st
import requests
import os

# =====================
# CONFIG
# =====================
API_URL = "https://youtube-mixtape-automation.onrender.com/create-mixtape"
VIDEO_DOWNLOAD_URL = "https://youtube-mixtape-automation.onrender.com/download/video"
DESC_DOWNLOAD_URL = "https://youtube-mixtape-automation.onrender.com/download/description"

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# =====================
# UI: TITLE
# =====================
st.title("YouTube Mixtape Creator")

# =====================
# Upload MP3 files
# =====================
uploaded_files = st.file_uploader(
    "Upload MP3 files",
    type=["mp3"],
    accept_multiple_files=True
)

if uploaded_files:
    files = [
        ("files", (file.name, file.getvalue(), "audio/mpeg"))
        for file in uploaded_files
    ]

    response = requests.post(
        "https://youtube-mixtape-automation.onrender.com/upload-audio",
        files=files
    )

    if response.status_code == 200:
        st.success("Audio files uploaded successfully to cloud!")
    else:
        st.error("Failed to upload audio files.")

# =====================
# Create Mixtape Button
# =====================
if st.button("Create Mixtape"):
    try:
        requests.post(API_URL, timeout=3)

        st.success("Mixtape generation started. Please wait a few minutes.")
        st.info("Cloud backend is processing your request.")
        st.stop()

    except (requests.exceptions.ReadTimeout, requests.exceptions.Timeout):
        st.success("Mixtape generation started. Backend is waking up.")
        st.info("Render free tier may take 1–2 minutes. Please wait.")
        st.stop()

    except requests.exceptions.ConnectionError:
        st.error("Cloud backend unreachable. Please check Render service.")
        st.stop()

# =====================
# Download Output
# =====================
st.divider()
st.subheader("Download Output")

st.markdown(
    f"[Download Video]({VIDEO_DOWNLOAD_URL})",
    unsafe_allow_html=True
)

st.markdown(
    f"[Download AI Description]({DESC_DOWNLOAD_URL})",
    unsafe_allow_html=True
)

st.info("If download does not start, video may still be processing. Try again after a minute.")
