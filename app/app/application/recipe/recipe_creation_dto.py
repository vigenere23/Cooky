from dataclasses import dataclass
from typing import Any, List

@dataclass
class RecipeCreationDto:
    recipe_dto: Any
    ingredient_dtos: List[Any]
