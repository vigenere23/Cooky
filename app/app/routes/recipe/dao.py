from app import db, transaction
from .model import RecipeModel
from app.helpers.BaseDao import BaseDao
from ..recipeIngredient.model import RecipeIngredientModel
from ..recipeIngredient.dao import RecipeIngredientDao

recipeIngredientDao = RecipeIngredientDao()


class RecipeDao(BaseDao):

    def __init__(self):
        super().__init__('Recipe', RecipeModel)

    def getRecipesByName(self, name):
        query = 'SELECT * FROM Recipe WHERE LOWER(name) LIKE LOWER(%(name)s)'
        results = db.findAll(query, {'name': '%{}%'.format(name)})
        return self._mapper.from_tuples(results)

    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * FROM Recipe WHERE id_User = %(id_User)s'
        results = db.findAll(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)

    def modifyRecipeName(self, name, id):
        query = 'UPDATE Recipe SET name = \'{}\' WHERE id = {}'.format(
            name, id)
        db.replace(query, {'id': id, 'name': name})
        return {"id": id, "name": name}

    def modifyRecipeDirective(self, directives, id):
        query = 'UPDATE Recipe SET directives = \'{}\' WHERE id = {}'.format(
            directives, id)
        db.replace(query, {'directives': directives})
        return {"id": id, "directives": directives}

    def delete(self, id):
        query = 'DELETE FROM Recipe WHERE id = %(id)s'
        db.delete(query, {'id': id})

    def save(self, recipe_model, ingredients):
        if not isinstance(recipe_model, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")

        try:
            recipe_id = transaction.execute(lambda: self.__save_transaction(recipe_model, ingredients))
            return self.getById(recipe_id)
        except Exception:
            raise Exception("Could not save recipe")

    def __save_transaction(self, recipe_model, ingredients) -> int:
        query = 'INSERT INTO Recipe (id, id_User, name, description, directives, rating) VALUES (%s, %s, %s, %s, %s, %s)'
        recipe_id = db.create(query, self._mapper.to_tuple(recipe_model), autocommit=False)

        for ingredient in ingredients:
            recipe_ingredient_model = None
            if isinstance(ingredient, RecipeIngredientModel):
                recipe_ingredient_model = ingredient
                recipe_ingredient_model.id_Recipe = recipe_id
            else:
                data = {
                    'id_Recipe': recipe_id,
                    'id_Ingredient': ingredient['id_Ingredient'],
                    'id_QuantityUnit': ingredient['id_QuantityUnit'],
                    'totalQuantity': ingredient['totalQuantity']
                }
                recipe_ingredient_model = RecipeIngredientModel(**data)

            recipeIngredientDao.save(recipe_ingredient_model, autocommit=False)

        return recipe_id
