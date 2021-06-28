import bcrypt
from ..modules.users.dao import UserDao
from ..modules.account.dao import AccountDao

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
    except Exception:
        return None
