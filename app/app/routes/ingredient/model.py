from app.helpers.BaseModel import BaseModel


class IngredientModel(BaseModel):
    def __init__(self, id=None, id_IngredientType=None, id_QuantityUnit=None, name=None, baseCost=None, baseQuantity=1):
        self.id = id
        self.id_IngredientType = id_IngredientType
        self.id_QuantityUnit = id_QuantityUnit
        self.name = name
        self.baseCost = baseCost
        self.baseQuantity = baseQuantity
