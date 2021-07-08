from dataclasses import asdict
from typing import List
from app.domain.recipe.recipe import Recipe
from app.domain.exceptions import NotFoundException
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.refactor.recipe.recipe_ingredient_dao import RecipeIngredientDao
from app.infra.db.models.recipe.recipe_ingredient_model import RecipeIngredientModel
from app.infra.db.models.recipe import RecipeModel
from app.infra.db.refactor.recipe.recipe_dao import RecipeDao
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
        with self.__db_connection.transaction() as executor:
            recipe_model = self.__recipe_dao.find(executor, recipe_id)

            if not recipe_model:
                raise NotFoundException(f"No Recipe found with id '{recipe_id}'")

            return Recipe(**asdict(recipe_model))


    def find_all(self, name: str = None, user_id: int = None) -> List[Recipe]:
        with self.__db_connection.transaction() as executor:
            recipe_models = self.__recipe_dao.find_all(executor, name=name, user_id=user_id)

            return list(map(lambda recipe_model: Recipe(**asdict(recipe_model)), recipe_models))


    def find_all_liked_by(self, user_id: int) -> List[Recipe]:
        with self.__db_connection.transaction() as executor:
            recipe_models = self.__recipe_dao.find_all_liked_by(executor, user_id)

            return list(map(
                lambda recipe_model: Recipe(**asdict(recipe_model)),
                recipe_models
            ))


    def delete(self, recipe: Recipe) -> None:
        with self.__db_connection.transaction() as executor:
            self.__recipe_dao.delete(executor, RecipeModel(**asdict(recipe)))


    def save(self, recipe: RecipeCreationDto) -> int:
        with self.__db_connection.transaction() as executor:
            recipe_id = self.__recipe_dao.save(executor, RecipeModel(**recipe.recipe))

            for ingredient_dto in recipe.ingredients:
                recipe_ingredient_model = RecipeIngredientModel(id_Recipe=recipe_id, **ingredient_dto.to_dict())
                self.__recipe_ingredient_dao.save(executor, recipe_ingredient_model)

            # FUTURE : recipe is a domain object with comments, ratings, etc.
            # that will all need to be saved

            return recipe_id

    def replace(self, recipe: Recipe) -> Recipe:
        with self.__db_connection.transaction() as executor:
            self.__recipe_dao.update(executor, RecipeModel(**asdict(recipe)))

        return self.find_by_id(recipe.id)
