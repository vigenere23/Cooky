from app.domain.base_model import BaseModel


class CartItemModel(BaseModel):
    def __init__(self, id=None, id_Ingredient=None, id_Cart=None, multiplier=1, subCost=0.0):
        self.id = id
        self.id_Ingredient = id_Ingredient
        self.id_Cart = id_Cart
        self.multiplier = multiplier
        self.subCost = subCost
