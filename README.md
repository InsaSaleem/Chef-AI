# Chef AI – Ingredient to Recipe Generator 👨‍🍳

A beginner-friendly Streamlit app that turns a list of ingredients into a fun, personalised recipe card — no external APIs required.

---

## ✨ Features

- **Flexible Input:** Type ingredients directly or upload a `.txt` or `.json` file.
- **Rule-Based Generation:** Instant recipe mapping for pasta, rice bowls, salads, and skillets.
- **Rich UI Cards:** Styled recipe card layouts with titles, steps, servings, and tags.
- **Secure Handling:** Built-in input sanitisation and data validation.
- **Vibrant UI:** Interactive floating food emoji animations (🍅🥕🍝).

---

## 📁 File Structure

```text
chef-ai-recipe-generator/
├── app.py                  # Streamlit UI
├── mcp_server.py           # Orchestration pipeline
├── security.py             # Validation & sanitisation
├── ingredient_parser.py    # Text parsing & normalisation
├── recipe_generator.py     # Rule-based recipe logic
├── narrator.py             # Emoji & personality layer
├── sample_ingredients.txt  # Quick-test ingredient file
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

🚀 How to Install
Clone the repository and install the required dependencies:
pip install -r requirements.txt

▶️ How to Run
Launch the Streamlit server from your terminal:
streamlit run app.py

Once running, open your browser and navigate to http://localhost:8501

🥘 Sample Input
You can type the following plain text into the app:
tomato, onion, pasta, garlic, olive oil

Alternatively, upload the provided sample_ingredients.txt file using the built-in file uploader.

🏗️ Architecture
Streamlit UI (app.py)
       │
       ▼
  mcp_server.py  ← Orchestrates the pipeline
       │
       ├─► security.py          – Sanitise & validate
       ├─► ingredient_parser.py – Parse & normalise
       ├─► recipe_generator.py  – Rule-based recipe logic
       └─► narrator.py          – Add fun personality & emojis


Each module is written as a clean Python file with short, focused functions. No classes, no external APIs, and no databases—just simple, readable Python code.

📝 Notes
Limits: Maximum of 30 ingredients supported per single request.

File Formats: Strictly accepts .txt and .json files.

JSON Structure: JSON files must be structured either as a flat list:

["tomato", "onion"]
Or as an object containing an "ingredients" key:
{
  "ingredients": ["tomato", "onion"]
}
