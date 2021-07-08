from dataclasses import dataclass


@dataclass
class CartModel:
    id_User: int
    totalCost: float = 0.0
    id: int = None
