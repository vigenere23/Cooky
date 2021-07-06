from app.domain.recipe.recipe_repository import RecipeRepository


class RecipeFindingUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.__repository = recipe_repository

    def find_by_id(self, recipe_id: int):
        return self.__repository.find_by_id(recipe_id)

    def find_all(self, name: str = None, user_id: int = None):
        return self.__repository.find_all(name=name, user_id=user_id)

    def find_all_liked_by(self, user_id: id):
        return self.__repository.find_all_liked_by(user_id)
