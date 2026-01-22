from pydub import AudioSegment
import os

audio_folder = "audio"

current_time = 0  # in seconds
timestamps = []

for file in os.listdir(audio_folder):
    if file.endswith(".mp3"):
        song = AudioSegment.from_mp3(os.path.join(audio_folder, file))
        timestamps.append((file, current_time))
        current_time += len(song) // 1000  # convert ms to seconds

# Print timestamps
print("\n TIMESTAMPS:")
for song, time in timestamps:
    minutes = time // 60
    seconds = time % 60
    print(f"{minutes:02}:{seconds:02} - {song}")
