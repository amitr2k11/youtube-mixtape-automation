import os
from openai import OpenAI

client = OpenAI()

INPUT_DESC = os.path.join("output", "description.txt")
OUTPUT_AI_DESC = os.path.join("output", "ai_description.txt")

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

print("AI-generated title & description created")
