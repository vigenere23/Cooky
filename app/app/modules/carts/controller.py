from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from ...api import response
from datetime import datetime
from .dao import CartDao
from ..cartItem.dao import CartItemDao
from ..cartItem.model import CartItemModel
from ..commands.dao import CommandDao
from ..commands.model import CommandModel
from ..ingredient.dao import IngredientDao
from ..quantityUnit.dao import QuantityUnitDao

routes = Blueprint('carts', __name__)
cartDao = CartDao()
cartItemDao = CartItemDao()
commandsDao = CommandDao()
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()


@routes.route('/<int:id>')
@jwt_required()
@response.handleExceptions
def getCart(id):
    cart = cartDao.getById(id)
    response.ensureIdentity(cart.id_User, current_identity)

    return response.success(cart)


@routes.route('/<int:id>/items')
@jwt_required()
@response.handleExceptions
def getCartItems(id):
    cart = cartDao.getById(id)
    response.ensureIdentity(cart.id_User, current_identity)

    cartItems = cartItemDao.getItemsByCart(id)
    data = []
    for cartItem in cartItems:
        ingredient = ingredientDao.getById(cartItem.id_Ingredient)
        quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
        quantity = str.format('{} {}', int(
            ingredient.baseQuantity), quantity_unit.abbreviation)
        data.append({
            **cartItem.serialize(),
            'name': ingredient.name,
            'baseCost': ingredient.baseCost,
            'quantity': quantity
        })
    return response.success(data)


@routes.route('/<int:id>/items/', methods=['POST'])
@jwt_required()
@response.handleExceptions
def addItemToCart(id):
    cart = cartDao.getById(id)
    response.ensureIdentity(cart.id_User, current_identity)

    body = request.get_json(force=True)
    data = {
        'id_Ingredient': body['id_Ingredient'],
        'id_Cart': id
    }
    cartItemModel = CartItemModel(**data)
    result = cartItemDao.save(cartItemModel)
    return response.success(result)


@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteItemFromCart(id_Cart, id_Ingredient):
    cart = cartDao.getById(id_Cart)
    response.ensureIdentity(cart.id_User, current_identity)

    cartItemDao.deleteIngredient(id_Cart, id_Ingredient)
    return response.success("", status=204)


@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeName(id_Cart, id_Ingredient):
    cart = cartDao.getById(id_Cart)
    response.ensureIdentity(cart.id_User, current_identity)

    body = request.get_json(force=True)
    result = cartItemDao.modifyQuantity(
        body['multiplier'], id_Cart, id_Ingredient)
    return response.success(result)


@routes.route('/<int:id>/command/', methods=['POST'])
@jwt_required()
@response.handleExceptions
def createCommand(id):
    cart = cartDao.getById(id)
    response.ensureIdentity(cart.id_User, current_identity)

    data = {
        'id_Cart': id,
        'creationDate': datetime.now()
    }
    commandModel = CommandModel(**data)
    data = commandsDao.save(commandModel)
    return response.success(data)
