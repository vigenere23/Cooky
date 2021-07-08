from abc import ABC, abstractmethod
from app.infra.db.models.user import AccountModel, UserModel, AddressModel

class UserRepository(ABC):

    # FUTURE change to domain entity
    @abstractmethod
    def find_by_username(self, username: str) -> UserModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def find_by_id(self, user_id: int) -> UserModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    # FUTURE make Account children of User (aggregate)
    @abstractmethod
    def find_account_of(self, user_id: int) -> AccountModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def save(self, account: AccountModel, user: UserModel, address: AddressModel) -> UserModel:
        raise NotImplementedError()
