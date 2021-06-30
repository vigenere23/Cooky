from dataclasses import dataclass
from typing import Optional
from app.infra.db.models import BaseModel


@dataclass
class RecipeIngredientModel(BaseModel):
    id: Optional[int]
    id_Recipe: int
    id_Ingredient: int
    id_QuantityUnit: int
    totalQuantity: int
