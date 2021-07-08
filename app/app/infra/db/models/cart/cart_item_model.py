from dataclasses import dataclass


@dataclass
class CartItemModel:
    id_Ingredient: int
    id_Cart: int
    multiplier: int = 1
    subCost: float = 0.0
    id: int = None
