from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.infra.db.daos.recipe import RecipeRatingDao
from app.infra.db.daos.user import UserDao
from app.app import recipe_finding_usecase, authentication_use_case


routes = Blueprint('users', __name__, url_prefix='/users')
userDao = UserDao()
recipeRatingDao = RecipeRatingDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def index():
    return response.success(userDao.getAll())


@routes.route('/<int:id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getUser(id):
    data = userDao.getById(id)
    return response.success(data)


@routes.route('/<int:id>/recipes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAllRecipesByUser(id):
    recipes = recipe_finding_usecase.find_all(user_id=id)
    return response.success(list(map(asdict, recipes)))


@routes.route('/<int:id>/likes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getLikeRecipes(id):
    recipes = recipe_finding_usecase.find_all_liked_by(id)

    return response.success(list(map(asdict, recipes)))


@routes.route('/<int:id>/ratings', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getRatings(id):
    authentication_use_case.ensure_same_user(id, current_identity.id)

    data = recipeRatingDao.getRatingsByUser(id)
    return response.success(data)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
