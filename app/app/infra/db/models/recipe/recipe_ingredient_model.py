from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class RecipeIngredientModel(BaseModel):
    id_Recipe: int
    id_Ingredient: int
    id_QuantityUnit: int
    totalQuantity: int
    id: int = None
