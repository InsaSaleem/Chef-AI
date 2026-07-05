"""
mcp_server.py – Lightweight orchestration module.

Ties together: security → parser → generator → narrator.
Not a real network server; just a pipeline coordinator.
"""

from security import sanitize_text, validate_ingredient_list
from ingredient_parser import parse_ingredients
from recipe_generator import generate_recipe
from narrator import narrate_recipe


def process_input(raw_text: str) -> dict:
    """
    Full pipeline: raw text → sanitised → parsed → validated → recipe → narrated.

    Returns the final narrated recipe dict.
    Raises ValueError with a clear message on invalid input.
    """
    # Step 1 – sanitise
    clean_text = sanitize_text(raw_text)

    if not clean_text:
        raise ValueError("Input is empty after sanitisation. Please provide ingredient text.")

    # Step 2 – parse
    ingredients = parse_ingredients(clean_text)

    # Step 3 – validate
    is_valid, error_msg = validate_ingredient_list(ingredients)
    if not is_valid:
        raise ValueError(error_msg)

    # Step 4 – generate recipe
    recipe = generate_recipe(ingredients)

    # Step 5 – narrate
    result = narrate_recipe(recipe)

    return result
