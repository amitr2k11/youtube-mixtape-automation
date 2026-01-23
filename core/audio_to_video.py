print(">>> AUDIO TO VIDEO SCRIPT STARTED")
print("Audio file:", audio_file)
print("Image file:", image_file)
print("Output file:", output_video)

import os
import subprocess

audio_file = os.path.join("output", "mixtape.mp3")
image_file = os.path.join("assets", "images.jpg")
output_video = os.path.join("output", "mixtape.mp4")

command = [
    "ffmpeg",
    "-y",                     #  AUTO overwrite
    "-loop", "1",
    "-i", image_file,
    "-i", audio_file,
    "-c:v", "libx264",
    "-c:a", "aac",
    "-shortest",
    output_video
]


subprocess.run(command)

print("Video created successfully!")
