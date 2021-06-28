from flask_jwt import JWT
from app.application.authentication import authenticate, identity
from app import flask_app
from . import response

jwt = JWT(flask_app, authenticate, identity)

@jwt.auth_response_handler
@response.handleExceptions
def jwt_response_handler(access_token, identity):
    return response.success({
        'token': access_token.decode('utf-8'),
        'id': identity.id,
        'username': identity.username
    })

@jwt.jwt_error_handler
@response.handleExceptions
def jwt_error_handler(error):
    return response.error(
        error.description,
        status=error.status_code
    )
