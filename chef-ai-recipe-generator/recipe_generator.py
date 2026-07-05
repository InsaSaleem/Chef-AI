"""
recipe_generator.py – Rule-based recipe generation from a list of ingredients.
"""


# ---------- helpers ----------

def _title_case(text: str) -> str:
    return text.title()


def _has(ingredients: list, *keywords) -> bool:
    """Return True if any keyword appears in the ingredient list."""
    return any(kw in ingredients for kw in keywords)


# ---------- recipe builders ----------

def _pasta_recipe(ingredients: list) -> dict:
    key = next((i for i in ingredients if i in ("pasta", "spaghetti", "penne", "noodle")), "pasta")
    main_veg = next((i for i in ingredients if i not in (key,)), "tomato")

    return {
        "title": f"{_title_case(main_veg)} {_title_case(key)}",
        "servings": 2,
        "ingredients": ingredients,
        "steps": [
            f"Boil the {key} in salted water until al dente, then drain.",
            f"Sauté {main_veg} with olive oil and garlic over medium heat for 5 minutes.",
            "Toss the cooked pasta into the pan and stir well.",
            "Season with salt, pepper, and your favourite herbs. Serve hot.",
        ],
        "tags": ["quick", "vegetarian", "pasta", "easy"],
    }


def _rice_recipe(ingredients: list) -> dict:
    main_veg = next((i for i in ingredients if i != "rice"), "vegetable")

    return {
        "title": f"{_title_case(main_veg)} Rice Bowl",
        "servings": 2,
        "ingredients": ingredients,
        "steps": [
            "Rinse the rice and cook it according to package instructions.",
            f"Stir-fry {main_veg} with oil, garlic, and a pinch of salt for 4–5 minutes.",
            "Combine with the cooked rice and mix evenly.",
            "Garnish with sesame seeds or fresh herbs. Serve warm.",
        ],
        "tags": ["quick", "vegetarian", "rice bowl", "easy"],
    }


def _salad_recipe(ingredients: list) -> dict:
    base = next((i for i in ingredients if i in ("lettuce", "cucumber", "spinach")), "lettuce")

    return {
        "title": f"Fresh {_title_case(base)} Salad",
        "servings": 2,
        "ingredients": ingredients,
        "steps": [
            f"Wash and chop the {base} and any other greens.",
            "Slice tomatoes, cucumbers, or other vegetables into bite-sized pieces.",
            "Toss everything together in a large bowl.",
            "Drizzle with olive oil, lemon juice, salt, and pepper. Serve immediately.",
        ],
        "tags": ["fresh", "vegetarian", "salad", "no-cook"],
    }


def _skillet_recipe(ingredients: list) -> dict:
    main = ingredients[0] if ingredients else "vegetable"
    second = ingredients[1] if len(ingredients) > 1 else "garlic"

    return {
        "title": f"{_title_case(main)} & {_title_case(second)} Skillet",
        "servings": 2,
        "ingredients": ingredients,
        "steps": [
            f"Heat oil in a skillet over medium-high heat.",
            f"Add {main} and {second}; cook for 5–7 minutes, stirring occasionally.",
            "Add remaining ingredients, season with salt, pepper, and spices of your choice.",
            "Cook for another 5 minutes until everything is tender. Serve with bread or rice.",
        ],
        "tags": ["quick", "vegetarian", "one-pan", "easy"],
    }


# ---------- public API ----------

def generate_recipe(ingredients: list) -> dict:
    """
    Generate a rule-based recipe from a list of ingredient strings.

    Returns a dict with keys: title, servings, ingredients, steps, tags.
    """
    if _has(ingredients, "pasta", "spaghetti", "penne", "noodle", "macaroni"):
        return _pasta_recipe(ingredients)

    if _has(ingredients, "rice"):
        return _rice_recipe(ingredients)

    if _has(ingredients, "lettuce", "cucumber", "spinach"):
        return _salad_recipe(ingredients)

    return _skillet_recipe(ingredients)
