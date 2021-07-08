import bcrypt
from dataclasses import asdict
from app.domain.user.user_repository import UserRepository
from app.application.account.signup_dto import SignupDto
from app.infra.db.models.user import UserModel, AddressModel, AccountModel


class SignupUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def register_new_user(self, dto: SignupDto) -> UserModel:
        password = bcrypt.hashpw(dto.account.password.encode(), bcrypt.gensalt())

        account = AccountModel(
            firstName=dto.account.firstName,
            lastName=dto.account.lastName,
            email=dto.account.email,
            password=password
        )
        user = UserModel(**asdict(dto.user))
        address = AddressModel(**asdict(dto.address))

        return self.__user_repository.save(account, user, address)
