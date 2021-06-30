from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class LikeRecipeModel(BaseModel):
    id_Recipe: int
    id_User: int
    id: int = None
