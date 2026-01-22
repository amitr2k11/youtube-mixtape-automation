import streamlit as st
import requests

# =====================
# CONFIG
# =====================
BASE_URL = "https://youtube-mixtape-automation-production.up.railway.app"
# YOUR REAL RAILWAY URL — NO < >

UPLOAD_URL = BASE_URL + "/upload-audio"
API_URL = BASE_URL + "/create-mixtape"
VIDEO_DOWNLOAD_URL = BASE_URL + "/download/video"
DESC_DOWNLOAD_URL = BASE_URL + "/download/description"

# =====================
# UI
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
        ("files", (f.name, f.getbuffer(), "audio/mpeg"))
        for f in uploaded_files
    ]

    with st.spinner("Uploading files to cloud backend..."):
        r = requests.post(UPLOAD_URL, files=files)

    if r.status_code == 200:
        st.success("Audio files uploaded successfully to cloud!")
    else:
        st.error("Failed to upload files to backend.")

# =====================
# Create Mixtape
# =====================
if st.button("Create Mixtape"):
    try:
        requests.post(API_URL, timeout=3)
        st.success("Mixtape generation started. Please wait a few minutes.")
        st.info("Cloud backend is processing your request.")
    except requests.exceptions.ReadTimeout:
        st.success("Mixtape generation started. Backend is waking up.")
    except requests.exceptions.ConnectionError:
        st.error("Cloud backend unreachable.")

# =====================
# Download Output
# =====================
st.subheader("Download Output")

if st.button("Download Video"):
    st.markdown(f"[Click here to download video]({VIDEO_DOWNLOAD_URL})")

if st.button("Download AI Description"):
    st.markdown(f"[Click here to download description]({DESC_DOWNLOAD_URL})")
