from app import db
from .model import CartModel
from app.helpers.BaseDao import BaseDao


class CartDao(BaseDao):

    def __init__(self):
        super().__init__('Cart', CartModel)

    def getCurrentUserCart(self, userId):
        query = 'SELECT * FROM Cart WHERE Cart.id_User = %(userId)s AND Cart.id NOT IN (SELECT Command.id_Cart FROM Command)'
        result = db.select(query, {'userId': userId}, 1)
        return self._mapper.from_tuple(result)

    def save(self, cartModel):
        if not isinstance(cartModel, CartModel):
            raise ValueError("cartModel should be of type cartModel")
        query = 'INSERT INTO Cart (id, id_User, totalCost) VALUES (%s, %s, %s)'
        cartId = db.insert(query, self._mapper.to_tuple(cartModel))

        if cartId:
            return self.getById(cartId)
        else:
            raise Exception("Could not save cart")
