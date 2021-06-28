from app import db
from .model import UserModel
from app.infra.db.base_dao import BaseDao
from app.domain.exceptions import NotFoundException


class UserDao(BaseDao):

    def __init__(self):
        super().__init__('User', UserModel)

    def getByUsername(self, username):
        query = 'SELECT * FROM User WHERE username = %(username)s'
        result = db.find(query, {'username': username})
        if result:
            return self._mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format(
                "No user found with username '%s'", username))

    def save(self, userModel, autocommit=True):
        if not isinstance(userModel, UserModel):
            raise ValueError("userModel should be of type UserModel")
        query = 'INSERT INTO User (id, username) VALUES (%s, %s)'
        userId = db.create(query, self._mapper.to_tuple(userModel), autocommit)

        if userId:
            return self.getById(userId)
        else:
            raise Exception("Could not save user")
