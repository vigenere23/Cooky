from dataclasses import dataclass


@dataclass
class CommentModel:
    id_Recipe: int
    id_User: int
    text: str
    id: int = None
