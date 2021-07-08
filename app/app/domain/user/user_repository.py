from abc import ABC, abstractmethod
from app.infra.db.models.user import AccountModel, UserModel, AddressModel

class UserRepository(ABC):

    # FUTURE change to domain entity
    @abstractmethod
    def save(self, account: AccountModel, user: UserModel, address: AddressModel):
        raise NotImplementedError()
