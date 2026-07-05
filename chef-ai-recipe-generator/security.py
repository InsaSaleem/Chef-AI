"""
security.py – Input validation and sanitisation helpers.
"""

import re


ALLOWED_EXTENSIONS = {".txt", ".json"}


def is_allowed_file(filename: str) -> bool:
    """Return True only if filename ends with .txt or .json."""
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)


def sanitize_text(text: str) -> str:
    """Remove HTML/script-like content and trim surrounding whitespace."""
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove script/style block content
    text = re.sub(r"(?i)(script|style|onerror|onclick|javascript)\s*[:=]?[^\n]*", "", text)
    return text.strip()


def validate_ingredient_list(items: list) -> tuple:
    """
    Validate a list of ingredient strings.

    Returns (True, "") if valid, or (False, "error message") if not.
    Rules:
      - at least 1 ingredient
      - at most 30 ingredients
      - every item must be a non-empty string
    """
    if not items:
        return False, "Please provide at least one ingredient."

    if len(items) > 30:
        return False, f"Too many ingredients ({len(items)}). Maximum allowed is 30."

    for item in items:
        if not isinstance(item, str) or item.strip() == "":
            return False, "Each ingredient must be a non-empty piece of text."

    return True, ""
