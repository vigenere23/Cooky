from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.refactor.recipe_ingredient_dao import RecipeIngredientDao
from app.infra.db.models.recipe.recipe_ingredient_model import RecipeIngredientModel
from app.infra.db.models.recipe import RecipeModel
from app.infra.db.refactor.recipe_dao import RecipeDao
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.domain.recipe_repository import RecipeRepository


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

    def find(self, recipe_id: int) -> RecipeModel:
        self.__db_connection.execute(lambda executor: self.__recipe_dao.find(executor, recipe_id))

    def save(self, recipe: RecipeCreationDto):
        self.__db_connection.execute(lambda executor: self.__save_transaction(executor, recipe))

    def __save_transaction(self, executor: MySQLExecutor, recipe: RecipeCreationDto):
        recipe_id = self.__recipe_dao.save(executor, RecipeModel(**recipe.recipe_dto))

        for ingredient_dto in recipe.ingredient_dtos:
            recipe_ingredient_model = RecipeIngredientModel(id_Recipe=recipe_id, **ingredient_dto)
            self.__recipe_ingredient_dao.save(executor, recipe_ingredient_model)

        # FUTURE : recipe is a domain object with comments, ratings, etc.
        # that will all need to be resaved
