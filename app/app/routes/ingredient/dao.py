from app import db
from .model import IngredientModel
from app.helpers.BaseDao import BaseDao

class IngredientDao(BaseDao):
    
    def __init__(self):
        super().__init__('Ingredient', IngredientModel)
    
    def getIngredientsByName(self, name):
        query = 'SELECT * FROM Ingredient WHERE LOWER(name) LIKE LOWER(%(name)s)'
        results = db.select(query, {'name': '%{}%'.format(name)})
        return self._mapper.from_tuples(results)
    
    def save(self, ingredientModel):
        if not isinstance(ingredientModel, IngredientModel):
            raise ValueError("ingredientModel should be of type IngredientModel")
        
        query = 'INSERT INTO Ingredient (id, id_IngredientType, id_QuantityUnit, name, baseCost, baseQuantity) VALUES (%s, %s, %s, %s, %s, %s)'
        ingredientId = db.insert(query, self._mapper.to_tuple(ingredientModel))
        
        if ingredientId:
            return self.getById(ingredientId)
        else:
            raise Exception("Could not save ingredient")

