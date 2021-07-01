from dataclasses import asdict
from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.api.recipe.recipe_creation_request import RecipeCreationRequest
from app.api.requests import receive
from app.infra.db.daos.recipe import RecipeDao, RecipeIngredientDao, LikeRecipeDao, RecipeRatingDao, RecipeCommentDao
from app.infra.db.models.recipe import LikeRecipeModel, RatingModel, CommentModel
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao
from app.infra.db.daos.user import UserDao
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app import recipe_creation_usecase, recipe_finding_usecase

routes = Blueprint('recipes', __name__)
recipe_dao = RecipeDao()
like_recipe_dao = LikeRecipeDao()
comment_dao = RecipeCommentDao()
recipe_rating_dao = RecipeRatingDao()
recipe_ingredient_dao = RecipeIngredientDao()
ingredient_dao = IngredientDao()
quantity_unit_dao = QuantityUnitDao()
user_dao = UserDao()


@routes.route('/', methods=['GET'])
@jwt_required()
@response.handleExceptions
def index():
    recipes = recipe_finding_usecase.findAll(
        name=request.args.get('name')
    )

    return response.success(list(map(asdict, recipes)))


@routes.route('/', methods=['POST'])
@jwt_required()
@response.handleExceptions
@receive(RecipeCreationRequest)
def addRecipe(request_data: RecipeCreationRequest):
    request_data.id_User = current_identity.id
    recipe_creation_dto = RecipeCreationDto(recipe={
        'id_User': request_data.id_User,
        'name': request_data.name,
        'description': request_data.description,
        'directives': request_data.directives
    }, ingredients=request_data.ingredients)
    recipe = recipe_creation_usecase.create_recipe(recipe_creation_dto)

    return response.success(asdict(recipe))


@routes.route('/<int:recipe_id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getRecipeById(recipe_id):
    recipe = recipe_finding_usecase.findById(recipe_id)
    user = user_dao.getById(recipe.id_User)
    data = {
        **asdict(recipe),
        'user': {
            **user.serialize()
        }
    }
    return response.success(data)


@routes.route('/<int:recipe_id>/', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteRecipe(recipe_id):
    recipe = recipe_finding_usecase.findById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    recipe_dao.delete(recipe_id)
    return response.empty()


@routes.route('/<int:recipe_id>/name/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeName(recipe_id):
    recipe = recipe_finding_usecase.findById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipe_dao.modifyRecipeName(body['name'], recipe_id)
    return response.success(result)


@routes.route('/<int:recipe_id>/directives/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeDirective(recipe_id):
    recipe = recipe_finding_usecase.findById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipe_dao.modifyRecipeDirective(body['directives'], recipe_id)
    return response.success(result)


@routes.route('/<int:recipe_id>/ingredientQuantity/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyIngredientQuantity(recipe_id):
    recipe = recipe_finding_usecase.findById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipe_ingredient_dao.modifyQuantity(
        recipe_id, body['id_Ingredient'], body['totalQuantity'])
    return response.success(result)


@routes.route('/<int:recipe_id>/ingredients', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
    data = []
    recipeIngredients = recipe_ingredient_dao.getIngredientsByRecipe(recipe_id)
    for recipeIngredient in recipeIngredients:
        ingredient = ingredient_dao.getById(recipeIngredient.id_Ingredient)
        quantityUnit = quantity_unit_dao.getById(
            recipeIngredient.id_QuantityUnit)
        data.append({
            'id': ingredient.id,
            'name': ingredient.name,
            'quantityUnit': quantityUnit.serialize(),
            'totalQuantity': recipeIngredient.totalQuantity
        })

    return response.success(data)


@routes.route('/<int:recipe_id>/comments')
@jwt_required()
@response.handleExceptions
def getRecipeComments(recipe_id):
    comments = comment_dao.getRecipeComments(recipe_id)
    data = []
    for comment in comments:
        user = user_dao.getById(comment.id_User)
        data.append({
            **comment.serialize(),
            'user': user.serialize()
        })
    return response.success(data)


@routes.route('/<int:recipe_id>/likes/', methods=['POST', 'DELETE'])
@jwt_required()
@response.handleExceptions
def likeRecipe(recipe_id):
    body = request.get_json(force=True)
    data = {
        'id_Recipe': recipe_id,
        'id_User': body['id_User']
    }

    response.ensureIdentity(data['id_User'], current_identity)

    likeRecipeModel = LikeRecipeModel(**data)

    if request.method == 'POST':
        result = like_recipe_dao.save(likeRecipeModel)
        return response.success(result)
    else:
        like_recipe_dao.delete(likeRecipeModel)
        return response.empty()


@routes.route('/<int:recipe_id>/ratings/', methods=['POST', 'PUT'])
@jwt_required()
@response.handleExceptions
def addRateRecipe(recipe_id):
    body = request.get_json(force=True)
    data = {
        'id_Recipe': recipe_id,
        'id_User': body['id_User'],
        'value': body['value']
    }

    response.ensureIdentity(data['id_User'], current_identity)

    ratingModel = RatingModel(**data)
    if request.method == 'POST':
        result = recipe_rating_dao.save(ratingModel)
    else:
        result = recipe_rating_dao.replace(ratingModel)
    return response.success(result)


@routes.route('/<int:recipe_id>/comments/', methods=['POST'])
@jwt_required()
@response.handleExceptions
def addCommentRecipe(recipe_id):
    body = request.get_json(force=True)
    data = {
        'id_Recipe': recipe_id,
        'id_User': body['id_User'],
        'text': body['text']
    }

    response.ensureIdentity(data['id_User'], current_identity)

    commentModel = CommentModel(**data)
    result = comment_dao.save(commentModel)
    return response.success(result)


from app import flask_app
flask_app.register_blueprint(routes, url_prefix='/recipes')
