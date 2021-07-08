from flask.app import Flask
from flask_jwt import JWT
from app.app import authentication_use_case
from app.api import response

def register_routes(flask_app: Flask):
    jwt = JWT(flask_app, authentication_use_case.authenticate, authentication_use_case.get_identity)

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
