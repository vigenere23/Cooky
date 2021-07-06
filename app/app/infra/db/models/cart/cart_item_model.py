from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class CartItemModel(BaseModel):
    id_Ingredient: int
    id_Cart: int
    multiplier: int = 1
    subCost: float = 0.0
    id: int = None
