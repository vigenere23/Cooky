from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.application import signup


routes = Blueprint('main', __name__)


@routes.route('/')
def index():
    return response.success("App is running correctly")


@routes.route('/signup/', methods=['POST'])
@response.handleExceptions
def signup_route():
    body = request.get_json(force=True)

    user = address = account = None

    try:
        user = body['user']
    except Exception as e:
        print(e)
        return response.error('user field cannot be empty', status=400)

    try:
        address = body['address']
    except Exception as e:
        print(e)
        return response.error('address field cannot be empty', status=400)

    try:
        account = body['account']
    except Exception as e:
        print(e)
        return response.error('account field cannot be empty', status=400)

    try:
        result = signup.register(user, address, account)
        return response.success(result)
    except ValueError as e:
        print(e)
        return response.error(e, status=400)
    except Exception as e:
        raise e


@routes.route('/userInfos/')
@jwt_required()
@response.handleExceptions
def getUserInfos():
    return response.success(current_identity.serialize())


from app import flask_app
flask_app.register_blueprint(routes, url_prefix='/')
