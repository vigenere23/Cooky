from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class CartModel(BaseModel):
    id_User: int
    totalCost: float = 0.0
    id: int = None
