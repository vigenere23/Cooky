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


def register(user, address, account):
    userModel = addressModel = None

    try:
        try:
            userModel = UserModel(**user)
            userModel = userDao.save(userModel, autocommit=False)
        except Exception as e:
            print(e)
            if 'Duplicate' in str(e):
                raise ValueError('Username already taken')
            raise ValueError('User informations are not valid')

        try:
            addressModel = AddressModel(**address)
            addressModel = addressDao.save(addressModel, autocommit=False)
        except Exception as e:
            print(e)
            raise ValueError('Address informations are not valid')

        try:
            accountModel = AccountModel(**account)
            accountModel.id_User = userModel.id
            accountModel.id_Address = addressModel.id
            accountDao.save(accountModel, autocommit=False)
        except Exception as e:
            print(e)
            raise ValueError('Account informations are not valid')

        db.commit()
        return userDao.getById(userModel.id)

    except Exception as e:
        db.rollback()
        raise e
