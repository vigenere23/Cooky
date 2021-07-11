from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.api.requests import parse_body
from app.api.user.user_responses import AccountResponse, AddressResponse
from app.api.user.account_creation_request import AccountCreationRequest
from app.api.user.user_edition_request import AccountEditionRequest, AddressEditionRequest
from app.application.account.user_edition_dto import AccountInfoEditionDto, AddressInfoEditionDto
from app.application.account.signup_dto import AccountInfo, AddressInfo, SignupDto, UserInfo
from app.app import signup_usecase, user_finding_usecase, user_editing_usecase


routes = Blueprint('account', __name__, url_prefix='/account')


@routes.route('', methods=['POST'])
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


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAccount():
    account = user_finding_usecase.find_account_of(current_identity.id)
    address = user_finding_usecase.find_adress_for_account(account.id)
    response_data = AccountResponse(
        id=account.id,
        id_User=account.id_User,
        id_Address=account.id_Address,
        firstName=account.firstName,
        lastName=account.lastName,
        email=account.email,
        address=AddressResponse(**asdict(address))
    )
    return response.success(response_data)


@routes.route('/email', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AccountEditionRequest)
def modifyEmail(request_body: AccountEditionRequest):
    try:
        account_edition_dto = AccountInfoEditionDto(email=request_body.email)
        account = user_editing_usecase.update_account(current_identity.id, account_edition_dto)
        address = user_finding_usecase.find_adress_for_account(account.id)
        response_data = AccountResponse(
            id=account.id,
            id_User=account.id_User,
            id_Address=account.id_Address,
            firstName=account.firstName,
            lastName=account.lastName,
            email=account.email,
            address=AddressResponse(**asdict(address))
        )
        return response.success(response_data)
    except Exception as e:
        return response.error(e)


@routes.route('/password', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AccountEditionRequest)
def modifyPassword(request_body: AccountEditionRequest):
    try:
        account_edition_dto = AccountInfoEditionDto(password=request_body.password)
        account = user_editing_usecase.update_account(current_identity.id, account_edition_dto)
        address = user_finding_usecase.find_adress_for_account(account.id)
        response_data = AccountResponse(
            id=account.id,
            id_User=account.id_User,
            id_Address=account.id_Address,
            firstName=account.firstName,
            lastName=account.lastName,
            email=account.email,
            address=AddressResponse(**asdict(address))
        )
        return response.success(response_data)
    except Exception as e:
        return response.error(e)


@routes.route('/country', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modifyCountry(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(country=request_body.country)
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


@routes.route('/city', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modifyCity(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(city=request_body.city)
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


@routes.route('/street', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modifyStreet(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(street=request_body.street)
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


@routes.route('/apartment', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modifyApartment(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(apartment=request_body.apartment)
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


@routes.route('/doorNumber', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modifyDoorNumber(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(number=request_body.number)
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


@routes.route('/address', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAddress():
    account = user_finding_usecase.find_account_of(current_identity.id)
    address = user_finding_usecase.find_adress_for_account(account.id)
    return response.success(address)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
