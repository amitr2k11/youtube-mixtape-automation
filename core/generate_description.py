from pydub import AudioSegment
import os

audio_folder = "audio"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

current_time = 0
description_lines = []

for file in os.listdir(audio_folder):
    if file.endswith(".mp3"):
        song_path = os.path.join(audio_folder, file)
        song = AudioSegment.from_mp3(song_path)

        minutes = current_time // 60
        seconds = current_time % 60

        description_lines.append(
            f"{minutes:02}:{seconds:02} - {file.replace('.mp3','')}"
        )

        current_time += len(song) // 1000

# Save description to file
description_path = os.path.join(output_folder, "description.txt")

with open(description_path, "w", encoding="utf-8") as f:
    f.write(" Tracklist\n\n")
    for line in description_lines:
        f.write(line + "\n")

print(" YouTube description created!")
