from app.domain.recipe.recipe import Recipe
from app.application.recipe.recipe_edition_dto import RecipeEditionDto
from app.application.authentication import ensureIdentity
from app.domain.recipe.recipe_repository import RecipeRepository


class RecipeEditingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def delete_recipe(self, current_identity, recipe_id: int) -> None:
        recipe = self.__repository.find_by_id(recipe_id)
        ensureIdentity(recipe.id_User, current_identity)
        self.__repository.delete(recipe)

    def edit_recipe(self, current_identity, dto: RecipeEditionDto) -> Recipe:
        recipe = self.__repository.find_by_id(dto.id)
        ensureIdentity(recipe.id_User, current_identity)

        if dto.name:
            recipe.name = dto.name

        if dto.directives:
            recipe.directives = dto.directives

        return self.__repository.replace(recipe)
