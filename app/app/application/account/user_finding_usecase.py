from app.domain.user.user_repository import UserRepository


class UserFindingUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def find_by_id(self, user_id: int):
        return self.__user_repository.find_by_id(user_id)

    def find_account_of(self, user_id: int):
        return self.__user_repository.find_account_of(user_id)

    def find_adress_for_account(self, account_id: int):
        return self.__user_repository.find_account_address(account_id)
