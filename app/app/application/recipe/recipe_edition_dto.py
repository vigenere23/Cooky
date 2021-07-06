from dataclasses import dataclass

@dataclass
class RecipeEditionDto:
    id: int
    name: str = None
    directives: str = None
