import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recipe(ingredients):

    ingredient_text = ", ".join(ingredients)

    prompt = f"""
You are a professional chef.

The user has these ingredients:

{ingredient_text}

Create ONE delicious recipe.

Return ONLY valid JSON.

The JSON MUST look EXACTLY like this:

{{
"title":"Recipe name",
"ingredients":[
"ingredient1",
"ingredient2"
],
"steps":[
"step one",
"step two",
"step three"
],
"servings":"2",
"tags":[
"Quick",
"Dinner",
"Healthy"
]
}}

Rules:

- Do NOT use markdown.
- Do NOT use HTML.
- Do NOT use ```json.
- Only output valid JSON.
- Ingredients must be an array.
- Steps must be an array.
- Tags must be an array.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    # Remove markdown fences if Gemini adds them
    if text.startswith("```json"):
        text = text[7:]

    if text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    return json.loads(text)