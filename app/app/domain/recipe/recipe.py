from dataclasses import dataclass

# FUTURE make domain driven
@dataclass
class Recipe:
    id_User: int
    name: str
    directives: str
    description: str
    id: int = None
    rating: float = 0
