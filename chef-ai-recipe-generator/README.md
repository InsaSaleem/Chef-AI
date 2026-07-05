# Chef AI – Ingredient to Recipe Generator 👨‍🍳

A beginner-friendly Streamlit app that turns a list of ingredients into a fun, personalised recipe card — no external APIs required.

---

## ✨ Features

- Type ingredients directly **or** upload a `.txt` / `.json` file
- Instant rule-based recipe generation (pasta, rice bowl, salad, skillet)
- Styled recipe card with title, steps, servings, and tags
- Input sanitisation and validation built in
- Floating food emoji animation 🍅🥕🍝

---

## 📁 File Structure

```
chef-ai-recipe-generator/
├── app.py                  # Streamlit UI
├── mcp_server.py           # Orchestration pipeline
├── security.py             # Validation & sanitisation
├── ingredient_parser.py    # Text parsing & normalisation
├── recipe_generator.py     # Rule-based recipe logic
├── narrator.py             # Emoji & personality layer
├── sample_ingredients.txt  # Quick-test ingredient file
├── requirements.txt
└── README.md
```

---

## 🚀 How to Install

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 🥘 Sample Input

```
tomato, onion, pasta, garlic, olive oil
```

Or upload `sample_ingredients.txt` using the file uploader.

---

## 🏗️ Architecture

```
Streamlit UI (app.py)
       │
       ▼
  mcp_server.py  ← orchestrates the pipeline
       │
       ├─► security.py        – sanitise & validate
       ├─► ingredient_parser.py – parse & normalise
       ├─► recipe_generator.py  – rule-based recipe
       └─► narrator.py          – add fun & emojis
```

Each module is a plain Python file with short, focused functions.  
No classes, no external APIs, no database — just simple Python.

---

## 📝 Notes

- Maximum **30 ingredients** supported per request.
- Accepted file formats: `.txt` and `.json`.
- JSON files must be either a flat list `["tomato", "onion"]` or  
  an object with an `"ingredients"` key: `{"ingredients": ["tomato", "onion"]}`.
