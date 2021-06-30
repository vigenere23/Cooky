from abc import ABC, abstractmethod
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.models.recipe.recipe_model import RecipeModel

class RecipeRepository(ABC):

    # FUTURE: return domain Recipe instead
    @abstractmethod
    def find(self, recipe_id: int) -> RecipeModel:
        raise NotImplementedError()

    # FUTURE: save domain Recipe instead
    @abstractmethod
    def save(self, recipe: RecipeCreationDto):
        raise NotImplementedError()
