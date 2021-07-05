from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.models.recipe.recipe_model import RecipeModel
from app.domain.recipe_repository import RecipeRepository


class RecipeCreationUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def create_recipe(self, recipe_creation_dto: RecipeCreationDto) -> RecipeModel:
        recipe_id = self.__repository.save(recipe_creation_dto)
        return self.__repository.find_by_id(recipe_id)
