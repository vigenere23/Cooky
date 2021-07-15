from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.api.requests import parse_body
from app.api.cart.cart_edition_requests import CartItemCreationRequest, CartItemEditionRequest
from app.infra.db.models.cart import CartItemModel
from app.infra.db.daos.cart import CartDao, CartItemDao
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao

routes = Blueprint('cart', __name__, url_prefix='/user/cart')
cartDao = CartDao()
cartItemDao = CartItemDao()
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_current_user_cart():
    cart = cartDao.get_cart_of(current_identity.id)

    return response.success(cart)


@routes.route('/items', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_current_user_cart_items():
    cart = cartDao.get_cart_of(current_identity.id)
    cartItems = cartItemDao.getItemsByCart(cart.id)
    data = []

    for cartItem in cartItems:
        ingredient = ingredientDao.getById(cartItem.id_Ingredient)
        quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
        quantity = f'{int(ingredient.baseQuantity)} {quantity_unit.abbreviation}'

        data.append({
            **asdict(cartItem),
            'name': ingredient.name,
            'baseCost': ingredient.baseCost,
            'quantity': quantity
        })

    return response.success(data)


@routes.route('/items', methods=['POST'])
@jwt_required()
@response.handleExceptions
@parse_body(CartItemCreationRequest)
def addItemToCart(request_body: CartItemCreationRequest):
    cart = cartDao.get_cart_of(current_identity.id)

    cartItemModel = CartItemModel(
        id_Cart=cart.id,
        id_Ingredient=request_body.id_Ingredient
    )
    result = cartItemDao.save(cartItemModel)

    return response.success(result)


@routes.route('/items/<int:id_Ingredient>', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteItemFromCart(id_Ingredient):
    cart = cartDao.get_cart_of(current_identity.id)

    cartItemDao.deleteIngredient(cart.id, id_Ingredient)
    return response.success("", status=204)


@routes.route('/items/<int:id_Ingredient>', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(CartItemEditionRequest)
def modifyRecipeName(request_body: CartItemEditionRequest, id_Ingredient):
    cart = cartDao.get_cart_of(current_identity.id)

    result = cartItemDao.modifyQuantity(
        request_body.multiplier, cart.id, id_Ingredient)

    return response.success(result)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
