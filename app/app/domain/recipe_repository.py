from abc import ABC, abstractmethod
from typing import List
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.models.recipe.recipe_model import RecipeModel

class RecipeRepository(ABC):

    # FUTURE: return domain Recipe instead
    @abstractmethod
    def find(self, recipe_id: int) -> RecipeModel:
        raise NotImplementedError()

    # FUTURE: return domain Recipes instead
    @abstractmethod
    def findAll(self, name: str = None) -> List[RecipeModel]:
        raise NotImplementedError()

    # FUTURE: save domain Recipe instead
    @abstractmethod
    def save(self, recipe: RecipeCreationDto):
        raise NotImplementedError()
