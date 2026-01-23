import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")

    # If key not present, skip safely
    if not api_key:
        print("[AI DESCRIPTION SKIPPED] OPENAI_API_KEY not set")
        return

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        input_path = os.path.join("output", "description.txt")
        output_path = os.path.join("output", "ai_description.txt")

        if not os.path.exists(input_path):
            print("[AI DESCRIPTION WARNING] description.txt not found")
            return

        with open(input_path, "r", encoding="utf-8") as f:
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

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)

        print("AI-generated title & description created")

    except Exception as e:
        print(f"[AI DESCRIPTION ERROR] {e}")


if __name__ == "__main__":
    main()
