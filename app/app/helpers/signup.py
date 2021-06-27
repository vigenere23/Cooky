from app import db
from ..routes.users.dao import UserDao
from ..routes.users.model import UserModel
from ..routes.address.dao import AddressDao
from ..routes.address.model import AddressModel
from ..routes.account.dao import AccountDao
from ..routes.account.model import AccountModel

userDao = UserDao()
addressDao = AddressDao()
accountDao = AccountDao()


def register(user, address, account) -> UserModel:
    userModel = UserModel(**user)
    addressModel = AddressModel(**address)
    accountModel = AccountModel(**account)

    userModel = db.transaction(lambda: register_transaction(userModel, addressModel, accountModel))

    return userModel


def register_transaction(userModel, addressModel, accountModel) -> UserModel:
    try:
        userModel = userDao.save(userModel, autocommit=False)
    except Exception as e:
        print(e)
        if 'Duplicate' in str(e):
            raise ValueError('Username already taken')
        raise ValueError('User informations are not valid')

    try:
        addressModel = addressDao.save(addressModel, autocommit=False)
    except Exception as e:
        print(e)
        raise ValueError('Address informations are not valid')

    accountModel.id_User = userModel.id
    accountModel.id_Address = addressModel.id

    try:
        accountDao.save(accountModel, autocommit=False)
    except Exception as e:
        print(e)
        raise ValueError('Account informations are not valid')

    return userModel
