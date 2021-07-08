from dataclasses import dataclass
from datetime import datetime


@dataclass
class CommandModel:
    id_Cart: int
    creationDate: datetime
    arrivalDate: datetime = None
    id: int = None
