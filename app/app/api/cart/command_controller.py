from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.infra.db.daos.cart import CartDao, CommandDao


routes = Blueprint('commands', __name__, url_prefix='/commands')
cartDao = CartDao()
commandDao = CommandDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getUserCommands():
    commands = commandDao.getUserCommands(current_identity.id)
    data = []
    for command in commands:
        cart = cartDao.getById(command.id_Cart)
        data.append({
            **asdict(command),
            'totalCost': cart.totalCost
        })
    return response.success(data)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
