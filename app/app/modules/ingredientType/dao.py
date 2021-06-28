from .model import IngredientTypeModel
from app.infra.db.base_dao import BaseDao


class IngredientTypeDao(BaseDao):

    def __init__(self):
        super().__init__('IngredientType', IngredientTypeModel)

    def save(self, ingredientTypeModel):
        if not isinstance(ingredientTypeModel, IngredientTypeModel):
            raise ValueError(
                "ingredientTypeModel should be of type IngredientTypeModel")
