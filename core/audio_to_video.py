import os
import subprocess

AUDIO_DIR = "audio"
OUTPUT_DIR = "output"
OUTPUT_VIDEO = os.path.join(OUTPUT_DIR, "mixtape.mp4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    audio_files = [
        os.path.join(AUDIO_DIR, f)
        for f in os.listdir(AUDIO_DIR)
        if f.endswith(".mp3")
    ]

    if not audio_files:
        print("[AUDIO TO VIDEO] No audio files found. Skipping video creation.")
        return

    print("[AUDIO TO VIDEO] Audio files found:")
    for f in audio_files:
        print(" -", f)

    # Create simple black video with ffmpeg
    duration_cmd = [
        "ffprobe", "-i", audio_files[0],
        "-show_entries", "format=duration",
        "-v", "quiet", "-of", "csv=p=0"
    ]

    try:
        duration = subprocess.check_output(duration_cmd).decode().strip()
    except Exception:
        duration = "300"  # fallback

    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", f"color=c=black:s=1280x720:d={duration}",
        "-i", audio_files[0],
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        OUTPUT_VIDEO
    ]

    subprocess.run(ffmpeg_cmd, check=True)
    print("[AUDIO TO VIDEO] Video created successfully!")

if __name__ == "__main__":
    main()

