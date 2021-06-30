from dataclasses import dataclass
from typing import Any, List

@dataclass
class RecipeCreationDto:
    recipe: Any
    ingredients: List[Any]
