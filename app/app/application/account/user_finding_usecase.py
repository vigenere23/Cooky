from app.domain.user.user_repository import UserRepository


class UserFindingUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def find_account_of(self, user_id: int):
        return self.__user_repository.find_account_of(user_id)
