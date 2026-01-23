import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYTHON_EXEC = sys.executable

def run_pipeline():
    scripts = [
        "core/merge_audio.py",
        "core/generate_description.py",
        "core/ai_description.py",   # optional
        "core/audio_to_video.py",   # MUST RUN
    ]

    for script in scripts:
        script_path = os.path.join(BASE_DIR, script)
        print(f"[PIPELINE] Running: {script_path}", flush=True)

        result = subprocess.run(
            [PYTHON_EXEC, script_path],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(result.stdout, flush=True)

        #  ONLY fail pipeline if audio_to_video fails
        if result.returncode != 0:
            print(result.stderr, flush=True)

            if "audio_to_video.py" in script:
                raise RuntimeError(
                    f"[PIPELINE ERROR] Critical script failed: {script}"
                )
            else:
                print(
                    f"[PIPELINE WARNING] Non-critical script failed: {script}",
                    flush=True
                )

    print("[PIPELINE] Video pipeline completed successfully.", flush=True)
