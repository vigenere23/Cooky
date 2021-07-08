from dataclasses import dataclass


@dataclass
class QuantityUnitModel:
    id_QuantityType: int
    name: str
    abbreviation: str
    id: int = None
