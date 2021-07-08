from dataclasses import dataclass


@dataclass
class RatingModel:
    id_Recipe: int
    id_User: int
    value: float
    id: int = None
