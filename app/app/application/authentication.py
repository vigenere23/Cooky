import bcrypt
from app.domain.user.user_repository import UserRepository
from app.domain.exceptions import ForbiddenException


class AuthenticationUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def ensure_same_user(self, resource_owner_id, current_user_id):
        if current_user_id != resource_owner_id:
            raise ForbiddenException()

    def get_identity(self, payload):
        try:
            return self.__user_repository.find_by_id(payload['identity'])
        except Exception:
            return None

    def authenticate(self, username, password):
        try:
            user = self.__user_repository.find_by_username(username)
            account = self.__user_repository.find_account_of(user.id)

            hashed_password = account.password

            # FUTURE see if can delete this
            if isinstance(hashed_password, bytearray):
                hashed_password = bytes(hashed_password)
            if not isinstance(hashed_password, bytes):
                hashed_password = hashed_password.encode()

            if bcrypt.checkpw(password.encode(), hashed_password):
                return user

        except Exception as e:
            print(e)
            return None
