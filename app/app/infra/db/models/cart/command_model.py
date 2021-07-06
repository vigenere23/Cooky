from dataclasses import dataclass
from datetime import datetime
from app.infra.db.models import BaseModel


@dataclass
class CommandModel(BaseModel):
    id_Cart: int
    creationDate: datetime
    arrivalDate: datetime = None
    id: int = None
