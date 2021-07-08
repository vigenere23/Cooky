from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.app import signup_usecase
from app.api import response
from app.api.requests import parse_body
from app.api.main.account_creation_request import AccountCreationRequest
from app.application.account.signup_dto import AccountInfo, AddressInfo, SignupDto, UserInfo
from app.infra.db.models.user.user_model import UserModel


routes = Blueprint('main', __name__, url_prefix='/')


@routes.route('')
def index():
    return response.success("App is running correctly")


@routes.route('/signup', methods=['POST'])
@response.handleExceptions
@parse_body(AccountCreationRequest)
def signup_route(request_data: AccountCreationRequest):
    if not request_data.user:
        return response.error('user field cannot be empty', status=400)

    if not request_data.account:
        return response.error('account field cannot be empty', status=400)

    if not request_data.address:
        return response.error('address field cannot be empty', status=400)

    try:
        dto = SignupDto(
            user=UserInfo(**asdict(request_data.user)),
            account=AccountInfo(**asdict(request_data.account)),
            address=AddressInfo(**asdict(request_data.address))
        )
        result = signup_usecase.register_new_user(dto)
        return response.success(result)
    except ValueError as e:
        print(e)
        return response.error(e, status=400)
    except Exception as e:
        raise e


@routes.route('/userInfos')
@jwt_required()
@response.handleExceptions
def getUserInfos():
    user = UserModel(
        username=current_identity.username,
        id=current_identity.id
    )
    return response.success(user)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
