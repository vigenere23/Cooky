from app import db
from app.infra.db.models.ingredient import IngredientModel
from app.infra.db.daos.base_dao import BaseDao


class IngredientDao(BaseDao):

    def __init__(self):
        super().__init__('Ingredient', IngredientModel)

    def getIngredientsByName(self, name):
        query = 'SELECT * FROM Ingredient WHERE LOWER(name) LIKE LOWER(%(name)s)'
        results = db.findAll(query, {'name': '%{}%'.format(name)})
        return self._mapper.from_tuples(results)

    def save(self, ingredientModel):
        if not isinstance(ingredientModel, IngredientModel):
            raise ValueError(
                "ingredientModel should be of type IngredientModel")

        query = 'INSERT INTO Ingredient (id, id_IngredientType, id_QuantityUnit, name, baseCost, baseQuantity) VALUES (%s, %s, %s, %s, %s, %s)'
        ingredientId = db.create(query, self._mapper.to_tuple(ingredientModel))

        if ingredientId:
            return self.getById(ingredientId)
        else:
            raise Exception("Could not save ingredient")
