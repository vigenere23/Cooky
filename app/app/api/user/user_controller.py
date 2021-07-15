from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.infra.db.models.user.user_model import UserModel


routes = Blueprint('user', __name__, url_prefix='/user')


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getCurrentUser():
    user = UserModel(
        username=current_identity.username,
        id=current_identity.id
    )
    return response.success(user)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
