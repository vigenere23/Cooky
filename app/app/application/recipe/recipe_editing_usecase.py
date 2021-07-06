from werkzeug.local import LocalProxy
from app.application.authentication import ensureIdentity
from app.domain.recipe.recipe_repository import RecipeRepository


class RecipeEditingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def delete_recipe(self, current_identity: LocalProxy, recipe_id: int) -> None:
        recipe = self.__repository.find_by_id(recipe_id)
        ensureIdentity(recipe.id_User, current_identity)
        self.__repository.delete(recipe)
