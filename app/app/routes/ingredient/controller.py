from flask import Blueprint, request
from flask_jwt import jwt_required
from app.helpers import response, exceptions, queries
from .dao import IngredientDao
from ..quantityUnit.dao import QuantityUnitDao

routes = Blueprint('ingredients', __name__)
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()

@routes.route('/')
@jwt_required()
@response.handleExceptions
def index():
  populated_ingredients = []
  ingredients = []

  search_name = request.args.get('name')
  if (search_name):
    ingredients = ingredientDao.getIngredientsByName(search_name)
  else:
    ingredients = ingredientDao.getAll()

  for ingredient in ingredients:
    quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
    quantity = str.format('{} {}', int(ingredient.baseQuantity), quantity_unit.abbreviation)
    populated_ingredients.append({
      'id': ingredient.id,
      'name': ingredient.name,
      'quantity': quantity,
      'price': ingredient.baseCost
    })
  return response.success(populated_ingredients)

@routes.route('/<int:id>/mesures')
@jwt_required()
@response.handleExceptions
def getMesures(id):
  quantityUnits = quantityUnitDao.getAllQuantityUnitsByIngredientId(id)
  return response.success(quantityUnits)
