import bcrypt
from flask_jwt import JWT
from app import flask_app
from .helpers import response
from .routes.users.dao import UserDao
from .routes.account.dao import AccountDao

def authenticate(username, password):
  userDao = UserDao()
  accountDao = AccountDao()
  try:
    user = userDao.getByUsername(username)
    account = accountDao.getAccountByUserId(user.id)

    hashed_password = account.password
    if isinstance(hashed_password, bytearray):
      hashed_password = bytes(hashed_password)
    if not isinstance(hashed_password, bytes):
      hashed_password = hashed_password.encode()

    if bcrypt.checkpw(password.encode(), hashed_password):
      return user
  except Exception as e:
    print(e)
    return None

def identity(payload):
  userDao = UserDao()
  user_id = payload['identity']
  try:
    return userDao.getById(user_id)
  except:
    return None

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
