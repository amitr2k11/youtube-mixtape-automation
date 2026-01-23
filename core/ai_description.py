import os

INPUT_DESC = os.path.join("output", "description.txt")
OUTPUT_AI_DESC = os.path.join("output", "ai_description.txt")

def main():
    try:
        from openai import OpenAI

        # Use API key from environment
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Check if input description exists
        if not os.path.exists(INPUT_DESC):
            print("[AI DESCRIPTION WARNING] description.txt not found. Skipping AI description.")
            return

        with open(INPUT_DESC, "r", encoding="utf-8") as f:
            tracklist = f.read()

        prompt = f"""
Create a catchy YouTube title and an engaging description
for a music mixtape using the following tracklist.

Tracklist:
{tracklist}

Return output in this format:

Title:
<one line title>

Description:
<short YouTube friendly description>
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

        with open(OUTPUT_AI_DESC, "w", encoding="utf-8") as f:
            f.write(result)

        print("[AI DESCRIPTION] AI-generated title & description created successfully.")

    except Exception as e:
        # IMPORTANT: Do NOT crash pipeline
        print(f"[AI DESCRIPTION WARNING] {e}")
        print("[AI DESCRIPTION WARNING] Skipping AI description and continuing pipeline.")

if __name__ == "__main__":
    main()
