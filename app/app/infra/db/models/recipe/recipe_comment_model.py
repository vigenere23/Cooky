from dataclasses import dataclass
from app.infra.db.models import BaseModel


@dataclass
class CommentModel(BaseModel):
    id_Recipe: int
    id_User: int
    text: str
    id: int = None
