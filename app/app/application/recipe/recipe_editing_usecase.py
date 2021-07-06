from app.domain.recipe.recipe import Recipe
from app.application.recipe.recipe_edition_dto import RecipeEditionDto
from app.application.authentication import ensure_same_user
from app.domain.recipe.recipe_repository import RecipeRepository


class RecipeEditingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def delete_recipe(self, current_user_id: int, recipe_id: int) -> None:
        recipe = self.__repository.find_by_id(recipe_id)

        ensure_same_user(recipe.id_User, current_user_id)

        self.__repository.delete(recipe)

    def edit_recipe(self, current_user_id: int, dto: RecipeEditionDto) -> Recipe:
        recipe = self.__repository.find_by_id(dto.id)

        ensure_same_user(recipe.id_User, current_user_id)

        if dto.name:
            recipe.name = dto.name

        if dto.directives:
            recipe.directives = dto.directives

        return self.__repository.replace(recipe)
