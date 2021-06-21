from app import db
from .model import RecipeIngredientModel
from app.helpers.BaseDao import BaseDao
from app.helpers.exceptions import NotFoundException

class RecipeIngredientDao(BaseDao):

    def __init__(self):
        super().__init__('RecipeIngredient', RecipeIngredientModel)

    def getIngredientsByRecipe(self, id_Recipe):
        querry = 'SELECT * FROM RecipeIngredient WHERE id_Recipe = %(id_Recipe)s'
        results = db.select(querry, {'id_Recipe': id_Recipe})
        return self._mapper.from_tuples(results)

    def modifyQuantity(self, id_Recipe, id_Ingredient, totalQuantity):
        query = 'UPDATE RecipeIngredient SET totalQuantity = \'{}\' Where id_Recipe = {} AND id_Ingredient = {}'.format(totalQuantity, id_Recipe, id_Ingredient)
        db.replace(query, {'id_Recipe': id_Recipe, 'id_Ingredient': id_Ingredient, 'totalQuantity': totalQuantity})
        return {'id_Recipe': id_Recipe, 'id_Ingredient': id_Ingredient, 'totalQuantity': totalQuantity}
    
    def save(self, recipeIngredientModel):
        if not isinstance(recipeIngredientModel, RecipeIngredientModel):
            raise ValueError("recipeIngredientModel should be of type RecipeIngredientModel")
        pass
        query = 'INSERT INTO RecipeIngredient (id, id_Recipe, id_Ingredient, id_QuantityUnit, totalQuantity) VALUES (%s, %s, %s, %s, %s)'
        newRecipeId = db.insert(query, self._mapper.to_tuple(recipeIngredientModel))
      
        if newRecipeId:
            return self.getById(newRecipeId)
        else:
            raise Exception("Could not save ingredient to cart")