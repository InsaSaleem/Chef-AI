"""
narrator.py – Add personality, emojis, and a cheerful note to a recipe dict.
"""

# Emoji map for common step keywords
STEP_EMOJIS = {
    "boil": "♨️",
    "sauté": "🍳",
    "saute": "🍳",
    "stir": "🥄",
    "cook": "🔥",
    "toss": "🥗",
    "chop": "🔪",
    "slice": "🔪",
    "wash": "🚿",
    "garnish": "🌿",
    "serve": "🍽️",
    "season": "🧂",
    "heat": "🔥",
    "rinse": "💧",
    "combine": "🥣",
    "mix": "🥣",
    "drizzle": "🫙",
    "add": "➕",
}

TITLE_EMOJIS = {
    "pasta": "🍝",
    "rice": "🍚",
    "salad": "🥗",
    "skillet": "🍳",
    "bowl": "🥣",
    "tomato": "🍅",
    "carrot": "🥕",
    "onion": "🧅",
    "garlic": "🧄",
    "potato": "🥔",
    "mushroom": "🍄",
    "pepper": "🌶️",
    "spinach": "🥬",
    "cucumber": "🥒",
    "lettuce": "🥬",
}

CHEERFUL_NOTES = [
    "Enjoy your meal and don't forget to share the love! ❤️",
    "Cooking is an act of kindness – bon appétit! 😊",
    "Made with simple ingredients, served with lots of love! 🥰",
    "Great cooking doesn't need a fancy kitchen – just great ingredients! ✨",
    "Your kitchen smells amazing right now, we just know it! 🌟",
]


def _pick_emoji(title: str) -> str:
    """Pick the most relevant emoji for the recipe title."""
    lower = title.lower()
    for keyword, emoji in TITLE_EMOJIS.items():
        if keyword in lower:
            return emoji
    return "🍴"


def _emoji_for_step(step: str) -> str:
    """Find the earliest-occurring matching action emoji for a step string."""
    lower = step.lower()
    best_pos = None
    best_emoji = "👨‍🍳"
    for keyword, emoji in STEP_EMOJIS.items():
        pos = lower.find(keyword)
        if pos != -1 and (best_pos is None or pos < best_pos):
            best_pos = pos
            best_emoji = emoji
    return best_emoji


def _add_step_emojis(steps: list) -> list:
    """Prepend a relevant emoji to each step."""
    return [f"{_emoji_for_step(s)} {s}" for s in steps]


def _fun_title(title: str) -> str:
    """Wrap the recipe title in a cheerful prefix and an emoji."""
    emoji = _pick_emoji(title)
    return f"Chef's Special {title} {emoji}"


def narrate_recipe(recipe: dict) -> dict:
    """
    Add fun personality to a plain recipe dict.

    Input keys expected: title, servings, ingredients, steps, tags.
    Returns a new dict with: display_title, ingredients, steps, servings, tags, note.
    """
    import random

    return {
        "display_title": _fun_title(recipe["title"]),
        "ingredients": recipe["ingredients"],
        "steps": _add_step_emojis(recipe["steps"]),
        "servings": recipe["servings"],
        "tags": recipe["tags"],
        "note": random.choice(CHEERFUL_NOTES),
    }
