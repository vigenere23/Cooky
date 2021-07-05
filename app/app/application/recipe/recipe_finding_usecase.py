from typing import List
from app.infra.db.models.recipe.recipe_model import RecipeModel
from app.domain.recipe_repository import RecipeRepository


class RecipeFindingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def findById(self, recipe_id: int) -> RecipeModel:
        return self.__repository.find_by_id(recipe_id)

    def findAll(self, name: str = None) -> List[RecipeModel]:
        return self.__repository.find_all(name=name)
