from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.sql_mapper import SQLMapper
from app.infra.db.models.recipe import RecipeIngredientModel


class RecipeIngredientDao:
    def __init__(self):
        self.__mapper = SQLMapper('Recipe', RecipeIngredientModel)

    def save(self, executor: MySQLExecutor, recipe_ingredient_model: RecipeIngredientModel):
        query = 'INSERT INTO RecipeIngredient (id, id_Recipe, id_Ingredient, id_QuantityUnit, totalQuantity) VALUES (%s, %s, %s, %s, %s)'
        data = self.__mapper.to_tuple(recipe_ingredient_model)
        executor.create(query, data)
