from pydub import AudioSegment
import os

AUDIO_DIR = "audio"
OUTPUT_FILE = "output/merged.mp3"

combined = AudioSegment.empty()

for file in sorted(os.listdir(AUDIO_DIR)):
    if file.endswith(".mp3"):
        combined += AudioSegment.from_mp3(os.path.join(AUDIO_DIR, file))

combined.export(OUTPUT_FILE, format="mp3")
print("Merged audio created:", OUTPUT_FILE)
