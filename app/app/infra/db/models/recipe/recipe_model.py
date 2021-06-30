from dataclasses import dataclass
from app.infra.db.models import BaseModel


# see usage for `frozen` attribute
@dataclass
class RecipeModel(BaseModel):
    id_User: int
    name: str
    directives: str
    description: str
    id: int = None
    rating: float = 0
