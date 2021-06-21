from app import db
from .model import IngredientTypeModel
from app.helpers.BaseDao import BaseDao

class IngredientTypeDao(BaseDao):

    def __init__(self):
        super().__init__('IngredientType', IngredientTypeModel)
    
    def save(self, ingredientTypeModel):
        if not isinstance(ingredientTypeModel, IngredientTypeModel):
            raise ValueError("ingredientTypeModel should be of type IngredientTypeModel")
        pass