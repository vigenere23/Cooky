from dataclasses import asdict
from app.app import transaction
from app.application.account.signup_dto import SignupDto
from app.infra.db.daos.user import UserDao, AddressDao, AccountDao
from app.infra.db.models.user import UserModel, AddressModel, AccountModel


userDao = UserDao()
addressDao = AddressDao()
accountDao = AccountDao()


def register(dto: SignupDto) -> UserModel:
    userModel = UserModel(**asdict(dto.user))
    accountModel = AccountModel(**asdict(dto.account))
    addressModel = AddressModel(**asdict(dto.address))

    userModel = transaction.execute(lambda: register_transaction(userModel, addressModel, accountModel))

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
