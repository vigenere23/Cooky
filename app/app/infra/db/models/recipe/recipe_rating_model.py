from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class RatingModel(BaseModel):
    id_Recipe: int
    id_User: int
    value: float
    id: int = None
