from dataclasses import asdict
from typing import List
from app.domain.recipe.recipe import Recipe
from app.domain.exceptions import NotFoundException
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.refactor.recipe_ingredient_dao import RecipeIngredientDao
from app.infra.db.models.recipe.recipe_ingredient_model import RecipeIngredientModel
from app.infra.db.models.recipe import RecipeModel
from app.infra.db.refactor.recipe_dao import RecipeDao
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.domain.recipe.recipe_repository import RecipeRepository


class MySQLRecipeRepository(RecipeRepository):
    def __init__(
        self,
        db_connection: MysqlDBConnection,
        recipe_dao: RecipeDao,
        recipe_ingredient_dao: RecipeIngredientDao
    ):
        self.__db_connection = db_connection
        self.__recipe_dao = recipe_dao
        self.__recipe_ingredient_dao = recipe_ingredient_dao

    def find_by_id(self, recipe_id: int) -> Recipe:
        recipe_model = self.__db_connection.transaction(self.__recipe_dao.find, recipe_id)

        if recipe_model is None:
            raise NotFoundException(f"No Recipe found with id '{recipe_id}'")

        return Recipe(**asdict(recipe_model))

    def find_all(self, name: str = None) -> List[Recipe]:
        recipe_models = self.__db_connection.transaction(self.__recipe_dao.find_all, name=name)
        return list(map(lambda recipe_model: Recipe(**asdict(recipe_model)), recipe_models))

    def save(self, recipe: RecipeCreationDto) -> int:
        return self.__db_connection.transaction(self.__save_transaction, recipe)

    def __save_transaction(self, executor: MySQLExecutor, recipe: RecipeCreationDto) -> int:
        recipe_id = self.__recipe_dao.save(executor, RecipeModel(**recipe.recipe))

        for ingredient_dto in recipe.ingredients:
            recipe_ingredient_model = RecipeIngredientModel(id_Recipe=recipe_id, **ingredient_dto.to_dict())
            self.__recipe_ingredient_dao.save(executor, recipe_ingredient_model)

        # FUTURE : recipe is a domain object with comments, ratings, etc.
        # that will all need to be resaved

        return recipe_id
