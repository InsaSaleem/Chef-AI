"""
ingredient_parser.py – Parse and normalise raw ingredient text.
"""

import re


# Simple plural → singular normalisation map
PLURAL_MAP = {
    "tomatoes": "tomato",
    "potatoes": "potato",
    "onions": "onion",
    "carrots": "carrot",
    "cloves": "clove",
    "leaves": "leaf",
    "peppers": "pepper",
    "mushrooms": "mushroom",
    "beans": "bean",
    "peas": "pea",
    "noodles": "noodle",
    "chunks": "chunk",
    "chops": "chop",
    "spices": "spice",
    "herbs": "herb",
    "chillies": "chilli",
    "chilies": "chili",
    "eggs": "egg",
    "olives": "olive",
    "shrimps": "shrimp",
}


def _normalize_plural(word: str) -> str:
    """Replace known plural forms with their singular equivalents."""
    return PLURAL_MAP.get(word, word)


def parse_ingredients(raw_text: str) -> list:
    """
    Parse raw ingredient text into a clean, deduplicated list.

    Steps:
      1. Split on commas and newlines.
      2. Lowercase and strip whitespace.
      3. Remove empty values.
      4. Normalise simple plurals.
      5. Remove duplicates while preserving order.
    """
    # Split on commas or newlines (one or more)
    tokens = re.split(r"[,\n]+", raw_text)

    seen = set()
    result = []

    for token in tokens:
        cleaned = token.lower().strip()
        if not cleaned:
            continue

        # Normalise plurals word-by-word
        normalized = " ".join(_normalize_plural(w) for w in cleaned.split())

        if normalized not in seen:
            seen.add(normalized)
            result.append(normalized)

    return result
