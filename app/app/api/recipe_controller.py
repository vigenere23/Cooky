from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.infra.db.daos.recipe import RecipeDao, RecipeIngredientDao, LikeRecipeDao, RecipeRatingDao, RecipeCommentDao
from app.infra.db.models.recipe import RecipeModel, LikeRecipeModel, RatingModel, CommentModel
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao
from app.infra.db.daos.user import UserDao

routes = Blueprint('recipes', __name__)
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
commentDao = RecipeCommentDao()
RecipeRatingDao = RecipeRatingDao()
recipeIngredientDao = RecipeIngredientDao()
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()
userDao = UserDao()


@routes.route('/', methods=['GET'])
@jwt_required()
@response.handleExceptions
def index():
    searched_name = request.args.get('name')
    if searched_name:
        return response.success(recipeDao.getRecipesByName(searched_name))
    else:
        return response.success(recipeDao.getAll())


# @routes.route('/', methods=['POST'])
@jwt_required()
@response.handleExceptions
def addRecipe():
    body = request.get_json(force=True)
    data = {
        'id_User': body['id_User'],
        'name': body['name'],
        'directives': body['directives']
    }

    response.ensureIdentity(data['id_User'], current_identity)

    recipeModel = RecipeModel(**data)
    result = recipeDao.save(recipeModel, body['ingredients'])
    return response.success(result)


@routes.route('/<int:recipe_id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getRecipeById(recipe_id):
    recipe = recipeDao.getById(recipe_id)
    user = userDao.getById(recipe.id_User)
    data = {
        **recipe.serialize(),
        'user': {
            **user.serialize()
        }
    }
    return response.success(data)


@routes.route('/<int:recipe_id>/', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteRecipe(recipe_id):
    recipe = recipeDao.getById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    recipeDao.delete(recipe_id)
    return response.empty()


@routes.route('/<int:recipe_id>/name/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeName(recipe_id):
    recipe = recipeDao.getById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipeDao.modifyRecipeName(body['name'], recipe_id)
    return response.success(result)


@routes.route('/<int:recipe_id>/directives/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyRecipeDirective(recipe_id):
    recipe = recipeDao.getById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipeDao.modifyRecipeDirective(body['directives'], recipe_id)
    return response.success(result)


@routes.route('/<int:recipe_id>/ingredientQuantity/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyIngredientQuantity(recipe_id):
    recipe = recipeDao.getById(recipe_id)
    response.ensureIdentity(recipe.id_User, current_identity)

    body = request.get_json(force=True)
    result = recipeIngredientDao.modifyQuantity(
        recipe_id, body['id_Ingredient'], body['totalQuantity'])
    return response.success(result)


@routes.route('/<int:recipe_id>/ingredients', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
    data = []
    recipeIngredients = recipeIngredientDao.getIngredientsByRecipe(recipe_id)
    for recipeIngredient in recipeIngredients:
        ingredient = ingredientDao.getById(recipeIngredient.id_Ingredient)
        quantityUnit = quantityUnitDao.getById(
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
    comments = commentDao.getRecipeComments(recipe_id)
    data = []
    for comment in comments:
        user = userDao.getById(comment.id_User)
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
        result = likeRecipeDao.save(likeRecipeModel)
        return response.success(result)
    else:
        likeRecipeDao.delete(likeRecipeModel)
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
        result = RecipeRatingDao.save(ratingModel)
    else:
        result = RecipeRatingDao.replace(ratingModel)
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
    result = commentDao.save(commentModel)
    return response.success(result)


from app import flask_app
flask_app.register_blueprint(routes, url_prefix='/recipes')
