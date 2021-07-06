from typing import List
from app.infra.db.refactor.mysql_condition_builder import MysqlConditionBuilder
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.models.recipe.recipe_model import RecipeModel


class RecipeDao:

    def __init__(self):
        self.__table_name = 'Recipe'


    def find(self, executor: MySQLExecutor, recipe_id: int) -> RecipeModel:
        result = executor.find_by_id(self.__table_name, recipe_id)

        return RecipeModel(**result)


    def find_all(self, executor: MySQLExecutor, name: str = None, user_id: int = None) -> List[RecipeModel]:
        conditions = []
        data = {}

        if name:
            conditions.append('LOWER(name) LIKE LOWER(%(name)s)')
            data['name'] = f'%{name}%'

        if user_id:
            conditions.append('id_User = %(user_id)s')
            data['user_id'] = user_id


        condition = MysqlConditionBuilder().where(conditions, data=data).build()
        results = executor.find_all(self.__table_name, condition)

        return [RecipeModel(**result) for result in results]


    def find_all_liked_by(self, executor: MySQLExecutor, user_id: int) -> List[RecipeModel]:
        query = '''
            SELECT Recipe.* FROM Recipe
            JOIN LikeRecipe ON LikeRecipe.id_Recipe = Recipe.id
            WHERE LikeRecipe.id_User = %(user_id)s
        '''
        data = {'user_id': user_id}

        results = executor.find_all_from_query(query, data)

        return [RecipeModel(**result) for result in results]


    def save(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> int:
        return executor.create(recipe_model)


    def update(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> None:
        executor.update(recipe_model)


    def delete(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> None:
        executor.delete(recipe_model.table_name(), recipe_model.id)
