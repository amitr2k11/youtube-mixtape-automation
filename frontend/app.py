import streamlit as st
import requests
import os

st.title(" YouTube Mixtape Creator")

# Ensure audio folder exists
AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

uploaded_files = st.file_uploader(
    "Upload MP3 files",
    type=["mp3"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(AUDIO_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
    st.success("Audio files uploaded successfully!")

if st.button("Create Mixtape"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/create-mixtape",
            timeout=5
        )

        if response.status_code == 200:
            st.success("Mixtape generation started. Please wait a few minutes.")
            st.info("You can keep this page open or come back later.")
        else:
            st.error(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Backend is not running. Please start FastAPI.")

st.divider()
st.subheader("Download Output")

output_dir = "output"

video_path = os.path.join(output_dir, "mixtape.mp4")
desc_path = os.path.join(output_dir, "ai_description.txt")

if os.path.exists(video_path):
    with open(video_path, "rb") as f:
        st.download_button(
            label=" Download Video",
            data=f,
            file_name="mixtape.mp4",
            mime="video/mp4"
        )
else:
    st.info("Video not ready yet.")

if os.path.exists(desc_path):
    with open(desc_path, "rb") as f:
        st.download_button(
            label="Download AI Description",
            data=f,
            file_name="ai_description.txt",
            mime="text/plain"
        )
else:
    st.info("Description not ready yet.")
