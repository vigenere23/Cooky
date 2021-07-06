from typing import List
from app.infra.db.refactor.mysql_condition import MysqlCondition
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.models.recipe.recipe_model import RecipeModel


class RecipeDao:
    def __init__(self):
        self.__table_name = 'Recipe'

    def find(self, executor: MySQLExecutor, recipe_id: int) -> RecipeModel:
        result = executor.find_by_id(self.__table_name, recipe_id)

        return RecipeModel(**result)

    def find_all(self, executor: MySQLExecutor, name: str = None) -> List[RecipeModel]:
        conditions = []
        data = {}

        if name is not None:
            conditions.append('LOWER(name) LIKE LOWER(%(name)s)')
            data['name'] = f'%{name}%'

        condition = MysqlCondition().where(conditions, data=data)
        results = executor.find_all(self.__table_name, condition)

        return [RecipeModel(**result) for result in results]

    def save(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> int:
        return executor.create(recipe_model)

    def update(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> None:
        executor.update(recipe_model)
