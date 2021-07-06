from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

@dataclass_json
@dataclass
class RecipeCreationIngredientRequest:
    id_Ingredient: int
    id_QuantityUnit: int
    totalQuantity: int

@dataclass_json
@dataclass
class RecipeCreationRequest:
    name: str
    description: str
    directives: str
    ingredients: List[RecipeCreationIngredientRequest]
