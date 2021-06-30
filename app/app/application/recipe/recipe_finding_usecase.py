from app.infra.db.models.recipe.recipe_model import RecipeModel
from app.domain.recipe_repository import RecipeRepository


class RecipeFindingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def findById(self, recipe_id: int) -> RecipeModel:
        return self.__repository.find(recipe_id)

    def findAll(self, name: str = None):
        return self.__repository.findAll(name=name)
