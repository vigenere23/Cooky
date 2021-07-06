from app.app import db
from app.infra.db.models.cart import CartItemModel
from app.infra.db.daos import BaseDao


class CartItemDao(BaseDao):

    def __init__(self):
        super().__init__('CartItem', CartItemModel)

    def getItemsByCart(self, id_Cart):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s'
        results = db.findAll(query, {'id_Cart': id_Cart})
        return self._mapper.from_tuples(results)

    def getByCartAndIngredientIds(self, id_Cart, id_Ingredient):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        result = db.find(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient})
        return self._mapper.from_tuple(result)

    def deleteIngredient(self, id_Cart, id_Ingredient):
        query = 'DELETE FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        print(query)
        print(id_Cart)
        print(id_Ingredient)
        db.delete(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient})

    def modifyQuantity(self, multiplier, id_Cart, id_Ingredient):
        query = 'UPDATE CartItem SET multiplier = %(multiplier)s WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        db.replace(query, {
                   'id_Cart': id_Cart, 'id_Ingredient': id_Ingredient, "multiplier": multiplier})
        return self.getByCartAndIngredientIds(id_Cart, id_Ingredient)

    def save(self, cartItemModel):
        if not isinstance(cartItemModel, CartItemModel):
            raise ValueError("cartItemModel should be of type CartItemModel")
        query = 'INSERT INTO CartItem (id, id_Ingredient, id_Cart, multiplier, subCost) VALUES (%s, %s, %s, %s, %s)'
        newItemId = db.create(query, self._mapper.to_tuple(cartItemModel))

        if newItemId:
            return self.getById(newItemId)
        else:
            raise Exception("Could not save ingredient to cart")
