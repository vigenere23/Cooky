from app.domain.exceptions import NotFoundException
from app.domain.user.user_repository import UserRepository
from app.infra.db.refactor.user.address_dao import AddressDao
from app.infra.db.refactor.user.user_dao import UserDao
from app.infra.db.refactor.user.account_dao import AccountDao
from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.infra.db.models.user import AccountModel, UserModel, AddressModel

class MysqlUserRepository(UserRepository):

    def __init__(
        self,
        db_connection: MysqlDBConnection,
        account_dao: AccountDao,
        user_dao: UserDao,
        address_dao: AddressDao
    ):
        self.__db_connection = db_connection
        self.__account_dao = account_dao
        self.__user_dao = user_dao
        self.__address_dao = address_dao

    def find_by_username(self, username: str):
        with self.__db_connection.transaction() as executor:
            user = self.__user_dao.find_by_username(executor, username)

            if not user:
                raise NotFoundException(f"No user found with username '{username}'")

            return user

    def find_by_id(self, user_id: int):
        with self.__db_connection.transaction() as executor:
            user = self.__user_dao.find_by_id(executor, user_id)

            if not user:
                raise NotFoundException(f"No user found with id '{user_id}'")

            return user

    def find_account_of(self, user_id: int) -> AccountModel:
        with self.__db_connection.transaction() as executor:
            return self.__account_dao.find_by_user_id(executor, user_id)

    def find_account_address(self, account_id: int) -> AddressModel:
        with self.__db_connection.transaction() as executor:
            return self.__address_dao.find_for_account(executor, account_id)

    def save(self, account: AccountModel, user: UserModel, address: AddressModel) -> UserModel:
        with self.__db_connection.transaction() as executor:
            user_id = self.__user_dao.save(executor, user)
            address_id = self.__address_dao.save(executor, address)

            account.id_User = user_id
            account.id_Address = address_id

            self.__account_dao.save(executor, account)

            return self.find_by_id(user_id)

    def replace_account(self, account: AccountModel) -> AccountModel:
        with self.__db_connection.transaction() as executor:
            self.__account_dao.update(executor, account)

        return self.find_account_of(account.id_User)


    def replace_address(self, account_id: int, address: AddressModel) -> AddressModel:
        with self.__db_connection.transaction() as executor:
            self.__address_dao.update(executor, address)

        return self.find_account_address(account_id)
