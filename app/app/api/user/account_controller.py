from dataclasses import asdict
from flask import Blueprint, request
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.api.requests import parse_body
from app.api.user.user_responses import AccountResponse, AddressResponse
from app.api.user.account_creation_request import AccountCreationRequest
from app.application.account.signup_dto import AccountInfo, AddressInfo, SignupDto, UserInfo
from app.infra.db.models.user.address_model import AddressModel
from app.infra.db.daos.recipe import RecipeRatingDao, LikeRecipeDao
from app.infra.db.daos.cart import CartDao, CommandDao
from app.infra.db.daos.user import AddressDao, AccountDao, UserDao
from app.app import signup_usecase, user_finding_usecase


routes = Blueprint('account', __name__, url_prefix='/account')
userDao = UserDao()
likeRecipeDao = LikeRecipeDao()
cartDao = CartDao()
commandDao = CommandDao()
accountDao = AccountDao()
addressDao = AddressDao()
recipeRatingDao = RecipeRatingDao()


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
    address: AddressModel = addressDao.getById(account.id_Address)
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
def modifyEmail():
    body = request.get_json(force=True)
    try:
        result = accountDao.modifyEmail(body['email'], current_identity.id)
        return response.success(result)
    except Exception as e:
        return response.error(e)


@routes.route('/password', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyPassword():
    body = request.get_json(force=True)
    try:
        accountDao.modifyPassword(body['password'], current_identity.id)
        return response.success('')
    except Exception as e:
        return response.error(e)


@routes.route('/country', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyCountry():
    account = user_finding_usecase.find_account_of(current_identity.id)
    addressId = account.id_Address
    body = request.get_json(force=True)
    data = addressDao.modifyCountry(body['country'], addressId)
    return response.success(data)


@routes.route('/city', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyCity():
    account = user_finding_usecase.find_account_of(current_identity.id)
    addressId = account.id_Address
    body = request.get_json(force=True)
    data = addressDao.modifyCity(body['city'], addressId)
    return response.success(data)


@routes.route('/street', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyStreet():
    account = user_finding_usecase.find_account_of(current_identity.id)
    addressId = account.id_Address
    body = request.get_json(force=True)
    data = addressDao.modifyStreet(body['street'], addressId)
    return response.success(data)


@routes.route('/apartment', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyApartment():
    account = user_finding_usecase.find_account_of(current_identity.id)
    addressId = account.id_Address
    body = request.get_json(force=True)
    data = addressDao.modifyApartment(body['apartment'], addressId)
    return response.success(data)


@routes.route('/doorNumber', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyDoorNumber():
    account = user_finding_usecase.find_account_of(current_identity.id)
    addressId = account.id_Address
    body = request.get_json(force=True)
    data = addressDao.modifyDoorNumber(body['number'], addressId)
    return response.success(data)


@routes.route('/address', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAddress():
    account = user_finding_usecase.find_account_of(current_identity.id)
    address = account.id_Address
    return response.success(addressDao.getAddress(address))


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
