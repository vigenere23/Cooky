from dataclasses import dataclass


@dataclass
class LikeRecipeModel:
    id_Recipe: int
    id_User: int
    id: int = None
