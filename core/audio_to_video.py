import os
import subprocess

# Paths
MERGED_AUDIO = os.path.join("output", "merged.mp3")   # MUST match merge_audio.py
OUTPUT_VIDEO = os.path.join("output", "mixtape.mp4")

# Safety check
if not os.path.exists(MERGED_AUDIO):
    raise RuntimeError("Merged audio not found at output/merged.mp3")

print("[AUDIO TO VIDEO] Using merged audio:", MERGED_AUDIO)

# FFmpeg command
cmd = [
    "ffmpeg",
    "-y",
    "-f", "lavfi",
    "-i", "color=c=black:s=1280x720",  # no hardcoded duration
    "-i", MERGED_AUDIO,
    "-shortest",                      # video ends with audio
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "128k",
    OUTPUT_VIDEO
]

# Run FFmpeg
subprocess.run(cmd, check=True)

print("[AUDIO TO VIDEO] Video created successfully!")