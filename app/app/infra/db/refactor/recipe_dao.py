from dataclasses import asdict
from typing import List
from app.infra.db.models.recipe.recipe_model import RecipeModel
from app.infra.db.refactor.mysql_executor import MySQLExecutor


class RecipeDao:
    def __init__(self):
        self.__table_name = 'Recipe'

    def find(self, executor: MySQLExecutor, recipe_id: int) -> RecipeModel:
        result = executor.findById(self.__table_name, recipe_id)

        return RecipeModel(**result)

    def findAll(self, executor: MySQLExecutor, name: str = None) -> List[RecipeModel]:
        query = "SELECT * FROM Recipe"
        data = {}

        if name is not None:
            query += " WHERE LOWER(name) LIKE LOWER(%(name)s)"
            data['name'] = f'%{name}%'

        results = executor.findAll(query, data)
        print(results)

        return [RecipeModel(**result) for result in results]

    def save(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> int:
        query = f'INSERT INTO {recipe_model.table_name()} {recipe_model.insert_columns_template()} VALUES {recipe_model.insert_values_template()}'
        data = asdict(recipe_model)

        return executor.create(query, data)
