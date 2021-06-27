from app import db
from .model import RecipeIngredientModel
from app.helpers.BaseDao import BaseDao


class RecipeIngredientDao(BaseDao):

    def __init__(self):
        super().__init__('RecipeIngredient', RecipeIngredientModel)

    def getIngredientsByRecipe(self, id_Recipe):
        querry = 'SELECT * FROM RecipeIngredient WHERE id_Recipe = %(id_Recipe)s'
        results = db.findAll(querry, {'id_Recipe': id_Recipe})
        return self._mapper.from_tuples(results)

    def modifyQuantity(self, id_Recipe, id_Ingredient, totalQuantity):
        query = 'UPDATE RecipeIngredient SET totalQuantity = \'{}\' Where id_Recipe = {} AND id_Ingredient = {}'.format(
            totalQuantity, id_Recipe, id_Ingredient)
        db.replace(query, {'id_Recipe': id_Recipe,
                   'id_Ingredient': id_Ingredient, 'totalQuantity': totalQuantity})
        return {'id_Recipe': id_Recipe, 'id_Ingredient': id_Ingredient, 'totalQuantity': totalQuantity}

    def save(self, recipeIngredientModel, autocommit=True):
        if not isinstance(recipeIngredientModel, RecipeIngredientModel):
            raise ValueError(
                "recipeIngredientModel should be of type RecipeIngredientModel")
        query = 'INSERT INTO RecipeIngredient (id, id_Recipe, id_Ingredient, id_QuantityUnit, totalQuantity) VALUES (%s, %s, %s, %s, %s)'
        newRecipeId = db.create(
            query, self._mapper.to_tuple(recipeIngredientModel), autocommit=autocommit)

        if newRecipeId:
            return self.getById(newRecipeId)
        else:
            raise Exception("Could not save ingredient to cart")
