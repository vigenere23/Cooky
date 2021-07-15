from dataclasses import asdict
from flask import Blueprint, Flask
from app.api import response
from app.api.requests import parse_body
from app.api.user.account_creation_request import AccountCreationRequest
from app.application.account.signup_dto import AccountInfo, AddressInfo, SignupDto, UserInfo
from app.app import signup_usecase


routes = Blueprint('accounts', __name__, url_prefix='/accounts')


@routes.route('', methods=['POST'])
@response.handleExceptions
@parse_body(AccountCreationRequest)
def signup_route(request_body: AccountCreationRequest):
    if not request_body.user:
        return response.error('user field cannot be empty', status=400)

    if not request_body.account:
        return response.error('account field cannot be empty', status=400)

    if not request_body.address:
        return response.error('address field cannot be empty', status=400)

    try:
        dto = SignupDto(
            user=UserInfo(**asdict(request_body.user)),
            account=AccountInfo(**asdict(request_body.account)),
            address=AddressInfo(**asdict(request_body.address))
        )
        result = signup_usecase.register_new_user(dto)
        return response.success(result)
    except ValueError as e:
        print(e)
        return response.error(e, status=400)
    except Exception as e:
        raise e


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
