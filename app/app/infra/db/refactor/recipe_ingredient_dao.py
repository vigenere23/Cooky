from dataclasses import asdict
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.models.recipe import RecipeIngredientModel


class RecipeIngredientDao:
    def save(self, executor: MySQLExecutor, recipe_ingredient_model: RecipeIngredientModel) -> int:
        query = f'INSERT INTO {recipe_ingredient_model.table_name()} {recipe_ingredient_model.insert_columns_template()} VALUES {recipe_ingredient_model.insert_values_template()}'
        data = asdict(recipe_ingredient_model)

        return executor.create(query, data)
