from app.domain.base_model import BaseModel


class QuantityUnitModel(BaseModel):
    def __init__(self, id=None, id_QuantityType=None, name=None, abbreviation=None):
        self.id = id
        self.id_QuantityType = id_QuantityType
        self.name = name
        self.abbreviation = abbreviation
