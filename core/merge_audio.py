from pydub import AudioSegment
import os

# Folder paths
audio_folder = "audio"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Empty audio file
final_audio = AudioSegment.empty()

# Loop through all mp3 files
for file in os.listdir(audio_folder):
    if file.endswith(".mp3"):
        print(f"Adding {file}")
        song_path = os.path.join(audio_folder, file)
        song = AudioSegment.from_mp3(song_path)
        final_audio += song

# Export final mixtape
output_path = os.path.join(output_folder, "mixtape.mp3")
final_audio.export(output_path, format="mp3")

print(" Mixtape created successfully!")
