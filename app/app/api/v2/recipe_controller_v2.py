from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.api import response
from app import recipe_creation_usecase

routes = Blueprint('recipes2', __name__)

@routes.route('/', methods=['POST'])
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

    recipe_creation_dto = RecipeCreationDto(recipe_dto=data, ingredient_dtos=body['ingredients'])
    result = recipe_creation_usecase.create_recipe(recipe_creation_dto)

    return response.success(result)


from app import flask_app
flask_app.register_blueprint(routes, url_prefix='/recipes')
