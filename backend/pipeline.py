import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYTHON_EXEC = sys.executable

def run_pipeline():
    scripts = [
        "core/merge_audio.py",
        "core/generate_description.py",
        "core/audio_to_video.py",
    ]

    for script in scripts:
        script_path = os.path.join(BASE_DIR, script)
        print(f"[PIPELINE] Running: {script_path}")

        result = subprocess.run(
            [PYTHON_EXEC, script_path],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(result.stderr)
            raise RuntimeError(f"Script failed: {script}")
