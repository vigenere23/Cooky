import bcrypt
from app.application.account.user_edition_dto import AccountInfoEditionDto, AddressInfoEditionDto
from app.domain.user.user_repository import UserRepository


class UserEditingUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def update_account(self, current_user_id: int, dto: AccountInfoEditionDto):
        account = self.__user_repository.find_account_of(current_user_id)

        if dto.email:
            account.email = dto.email
        if dto.password:
            account.password = bcrypt.hashpw(dto.password.encode(), bcrypt.gensalt())

        self.__user_repository.replace_account(account)

        return self.__user_repository.find_account_of(current_user_id)

    def update_address(self, current_user_id: int, dto: AddressInfoEditionDto):
        account = self.__user_repository.find_account_of(current_user_id)
        address = self.__user_repository.find_account_address(account.id)

        if dto.country:
            address.country = dto.country

        if dto.city:
            address.city = dto.city

        if dto.street:
            address.street = dto.street

        if dto.number:
            address.number = dto.number

        if dto.apartment:
            address.apartment = dto.apartment

        self.__user_repository.replace_address(account.id, address)

        return self.__user_repository.find_account_address(account.id)
