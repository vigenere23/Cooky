from app.infra.db.refactor.mysql_model import MysqlModel
from dataclasses import dataclass


@dataclass
class RecipeIngredientModel(MysqlModel):
    id_Recipe: int
    id_Ingredient: int
    id_QuantityUnit: int
    totalQuantity: int
    id: int = None

    def table_name(self) -> str:
        return 'RecipeIngredient'
