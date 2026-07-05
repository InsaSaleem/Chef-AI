"""
app.py – Streamlit UI for Chef AI Recipe Generator.
"""

import json
import streamlit as st
from mcp_server import process_input
from security import is_allowed_file, sanitize_text

# ──────────────────────────────────────────────
# Page config
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Chef AI – Ingredient to Recipe",
    page_icon="👨‍🍳",
    layout="centered",
)

# ──────────────────────────────────────────────
# Floating food emoji animation (HTML/CSS)
# ──────────────────────────────────────────────
FLOATING_EMOJIS_HTML = """
<style>
@keyframes float-up {
    0%   { transform: translateY(0px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-80px) rotate(20deg); opacity: 0; }
}

.emoji-float-container {
    display: flex;
    justify-content: center;
    gap: 18px;
    margin-bottom: 4px;
    overflow: hidden;
    height: 56px;
}

.emoji-float {
    font-size: 1.8rem;
    animation: float-up 3s ease-in-out infinite;
    display: inline-block;
}

.emoji-float:nth-child(1) { animation-delay: 0s; }
.emoji-float:nth-child(2) { animation-delay: 0.4s; }
.emoji-float:nth-child(3) { animation-delay: 0.8s; }
.emoji-float:nth-child(4) { animation-delay: 1.2s; }
.emoji-float:nth-child(5) { animation-delay: 1.6s; }
.emoji-float:nth-child(6) { animation-delay: 2.0s; }

/* Recipe card */
.recipe-card {
    background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
    border: 1px solid #44445a;
    border-radius: 16px;
    padding: 28px 32px;
    margin-top: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    color: #e8e8f0;
    font-family: 'Segoe UI', sans-serif;
}

.recipe-title {
    font-size: 1.7rem;
    font-weight: 700;
    color: #f8b94b;
    margin-bottom: 6px;
}

.recipe-note {
    font-style: italic;
    color: #a0a0c0;
    margin-bottom: 18px;
    font-size: 0.92rem;
}

.section-label {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #7878a0;
    margin: 16px 0 6px;
}

.tag-pill {
    display: inline-block;
    background: #3a3a5c;
    border: 1px solid #5555aa;
    color: #aaaaee;
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.78rem;
    margin: 3px 4px 3px 0;
}

.step-item {
    margin: 6px 0;
    line-height: 1.6;
}

.ingredient-chip {
    display: inline-block;
    background: #2e2e4a;
    border: 1px solid #44445a;
    color: #ccccee;
    border-radius: 8px;
    padding: 2px 10px;
    font-size: 0.85rem;
    margin: 3px 4px 3px 0;
}
</style>

<div class="emoji-float-container">
  <span class="emoji-float">🍅</span>
  <span class="emoji-float">🥕</span>
  <span class="emoji-float">🧄</span>
  <span class="emoji-float">🍝</span>
  <span class="emoji-float">🥗</span>
  <span class="emoji-float">🍳</span>
</div>
"""

st.markdown(FLOATING_EMOJIS_HTML, unsafe_allow_html=True)

# ──────────────────────────────────────────────
# Header
# ──────────────────────────────────────────────
st.markdown("## 👨‍🍳 Chef AI – Ingredient to Recipe")
st.markdown("*Drop your ingredients. Get a delicious recipe in seconds.*")
st.divider()

# ──────────────────────────────────────────────
# Input section
# ──────────────────────────────────────────────
st.markdown("### 📝 Enter Your Ingredients")

col1, col2 = st.columns([3, 1])

with col1:
    text_input = st.text_area(
        label="Type ingredients (comma or line separated)",
        placeholder="e.g. tomato, onion, pasta, garlic, olive oil",
        height=130,
        key="ingredient_text",
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Or upload a file",
        type=["txt", "json"],
        key="ingredient_file",
        help="Accepted formats: .txt or .json",
    )

# ──────────────────────────────────────────────
# File reading helper
# ──────────────────────────────────────────────
def read_uploaded_file(file) -> str:
    """Read a .txt or .json uploaded file and return its text content."""
    filename = file.name

    if not is_allowed_file(filename):
        raise ValueError(f"File type not allowed: {filename}. Use .txt or .json only.")

    raw_bytes = file.read()

    if filename.lower().endswith(".json"):
        try:
            data = json.loads(raw_bytes)
            # Accept a list of strings or a dict with an "ingredients" key
            if isinstance(data, list):
                return ", ".join(str(i) for i in data)
            elif isinstance(data, dict) and "ingredients" in data:
                items = data["ingredients"]
                return ", ".join(str(i) for i in items)
            else:
                raise ValueError("JSON must be a list of ingredients or {\"ingredients\": [...]}.")
        except json.JSONDecodeError:
            raise ValueError("Could not parse the JSON file. Please check its format.")
    else:
        return raw_bytes.decode("utf-8", errors="replace")


# ──────────────────────────────────────────────
# Generate button
# ──────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🍴 Generate Recipe", use_container_width=True, type="primary")

if generate_btn:
    raw_text = ""

    # Prefer file upload over text area
    if uploaded_file is not None:
        try:
            raw_text = read_uploaded_file(uploaded_file)
        except ValueError as e:
            st.error(f"⚠️ File error: {e}")
            st.stop()
    elif text_input.strip():
        raw_text = text_input.strip()
    else:
        st.warning("⚠️ Please enter some ingredients or upload a file first.")
        st.stop()

    # Run the full pipeline
    with st.spinner("Chef AI is cooking… 🍳"):
        try:
            result = process_input(raw_text)
        except ValueError as e:
            st.error(f"⚠️ {e}")
            st.stop()

    # ──────────────────────────────────────────
    # Render recipe card
    # ──────────────────────────────────────────
    ingredients_html = "".join(
        f'<span class="ingredient-chip">{i}</span>' for i in result["ingredients"]
    )

    tags_html = "".join(
        f'<span class="tag-pill">#{t}</span>' for t in result["tags"]
    )

    steps_html = "".join(
        f'<p class="step-item"><strong>Step {idx}.</strong> {step}</p>'
        for idx, step in enumerate(result["steps"], 1)
    )

    card_html = f"""
    <div class="recipe-card">
        <div class="recipe-title">{result["display_title"]}</div>
        <div class="recipe-note">✨ {result["note"]}</div>

        <div class="section-label">🛒 Ingredients</div>
        <div>{ingredients_html}</div>

        <div class="section-label">📋 Steps</div>
        {steps_html}

        <div class="section-label">🍽️ Servings</div>
        <p>Serves {result["servings"]} people</p>

        <div class="section-label">🏷️ Tags</div>
        <div>{tags_html}</div>
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)
    st.success("Recipe ready! Enjoy your meal 🥳")

# ──────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────
st.divider()
st.markdown(
    "<p style='text-align:center; color:#606080; font-size:0.8rem;'>"
    "Chef AI · No real chefs were harmed in the making of this app 👨‍🍳</p>",
    unsafe_allow_html=True,
)
