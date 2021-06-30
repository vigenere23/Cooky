from dataclasses import dataclass
from typing import Optional
from app.infra.db.models import BaseModel


@dataclass
class CommentModel(BaseModel):
    id: Optional[int]
    id_Recipe: int
    id_User: int
    text: str
