from dataclasses import dataclass
from typing import Optional
from app.infra.db.models import BaseModel


@dataclass
class RecipeModel(BaseModel):
    id: Optional[int]
    id_User: int
    name: str
    directives: str
    description: str
    rating: float
