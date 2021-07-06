from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class CartItemCreationRequest:
    id_Ingredient: int

@dataclass_json
@dataclass
class CartItemEditionRequest:
    multiplier: float
