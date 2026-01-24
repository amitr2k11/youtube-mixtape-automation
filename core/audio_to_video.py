import subprocess
import os
from map_assets import get_audio_image_pairs

OUTPUT_DIR = "output"
CLIPS_DIR = os.path.join(OUTPUT_DIR, "clips")
FINAL_VIDEO = os.path.join(OUTPUT_DIR, "mixtape.mp4")

os.makedirs(CLIPS_DIR, exist_ok=True)

pairs = get_audio_image_pairs()
clip_files = []

for i, pair in enumerate(pairs):
    clip_path = os.path.join(CLIPS_DIR, f"clip_{i}.mp4")

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", pair["image"],
        "-i", pair["audio"],
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-vf", "scale=1280:720",
        clip_path
    ]

    subprocess.run(cmd, check=True)
    clip_files.append(clip_path)

# concat clips
with open("output/concat.txt", "w") as f:
    for clip in clip_files:
        f.write(f"file '{os.path.abspath(clip)}'\n")

subprocess.run([
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", "output/concat.txt",
    "-c", "copy",
    FINAL_VIDEO
], check=True)

print("[SUCCESS] Mixtape video created!")
