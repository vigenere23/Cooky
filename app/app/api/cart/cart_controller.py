from dataclasses import asdict
from flask import Blueprint, request
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from datetime import datetime
from app.api import response
from app.api.requests import parse_body
from app.api.cart.cart_edition_requests import CartItemCreationRequest
from app.application.authentication import ensureIdentity, ensure_same_user
from app.infra.db.models.cart import CartItemModel, CommandModel
from app.infra.db.daos.cart import CartDao, CartItemDao, CommandDao
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao

routes = Blueprint('carts', __name__, url_prefix='/carts')
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
    ensureIdentity(cart.id_User, current_identity)

    return response.success(cart)


@routes.route('/<int:id>/items')
@jwt_required()
@response.handleExceptions
def getCartItems(id):
    cart = cartDao.getById(id)
    ensureIdentity(cart.id_User, current_identity)

    cartItems = cartItemDao.getItemsByCart(id)
    data = []
    for cartItem in cartItems:
        ingredient = ingredientDao.getById(cartItem.id_Ingredient)
        quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
        quantity = str.format('{} {}', int(
            ingredient.baseQuantity), quantity_unit.abbreviation)
        data.append({
            **asdict(cartItem),
            'name': ingredient.name,
            'baseCost': ingredient.baseCost,
            'quantity': quantity
        })
    return response.success(data)


@routes.route('/<int:id>/items/', methods=['POST'])
@jwt_required()
@response.handleExceptions
@parse_body(CartItemCreationRequest)
def addItemToCart(request_body: CartItemCreationRequest, id):
    cart = cartDao.getById(id)

    ensure_same_user(cart.id_User, current_identity.id)

    cartItemModel = CartItemModel(
        id_Cart=id,
        id_Ingredient=request_body.id_Ingredient
    )
    result = cartItemDao.save(cartItemModel)

    return response.success(result)


@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteItemFromCart(id_Cart, id_Ingredient):
    cart = cartDao.getById(id_Cart)

    ensure_same_user(cart.id_User, current_identity.id)

    cartItemDao.deleteIngredient(id_Cart, id_Ingredient)
    return response.success("", status=204)


@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeName(id_Cart, id_Ingredient):
    cart = cartDao.getById(id_Cart)

    ensure_same_user(cart.id_User, current_identity.id)

    body = request.get_json(force=True)
    result = cartItemDao.modifyQuantity(
        body['multiplier'], id_Cart, id_Ingredient)
    return response.success(result)


# FUTURE get cart for current user only (not for any user)
@routes.route('/<int:id>/command/', methods=['POST'])
@jwt_required()
@response.handleExceptions
def createCommand(id):
    cart = cartDao.getById(id)

    ensure_same_user(cart.id_User, current_identity.id)

    data = {
        'id_Cart': id,
        'creationDate': datetime.now()
    }
    commandModel = CommandModel(**data)
    data = commandsDao.save(commandModel)
    return response.success(data)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
