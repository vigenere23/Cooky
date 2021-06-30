from app.domain.exceptions import NotFoundException
from app.infra.db.sql_mapper import SQLMapper
from app.infra.db.models.recipe.recipe_model import RecipeModel
from app.infra.db.refactor.mysql_executor import MySQLExecutor


class RecipeDao:
    def __init__(self):
        self.__mapper = SQLMapper('Recipe', RecipeModel)

    def find(self, executor: MySQLExecutor, recipe_id: int) -> RecipeModel:
        query = 'SELECT * FROM Recipe WHERE id = %s'
        data = (recipe_id,)
        result = executor.find(query, data)

        if result:
            return self.__mapper.from_tuple(result)
        else:
            raise NotFoundException(
                "No Recipe found with id '{:d}'".format(id))

    def save(self, executor: MySQLExecutor, recipe_model: RecipeModel) -> int:
        query = 'INSERT INTO Recipe (id, id_User, name, description, directives, rating) VALUES (%s, %s, %s, %s, %s, %s)'
        data = self.__mapper.to_tuple(recipe_model)
        return executor.create(query, data)
