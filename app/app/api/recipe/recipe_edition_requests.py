from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RecipeEditionRequest:
    name: Optional[str]
    directives: Optional[str]

@dataclass_json
@dataclass
class CommentCreationRequest:
    text: str

@dataclass_json
@dataclass
class RatingCreationRequest:
    value: int
