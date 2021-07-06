from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.models.recipe import RecipeIngredientModel


class RecipeIngredientDao:
    def save(self, executor: MySQLExecutor, recipe_ingredient_model: RecipeIngredientModel) -> int:
        return executor.create(recipe_ingredient_model)
