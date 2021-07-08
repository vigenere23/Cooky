from app.app import db
from app.infra.db.models.user import AccountModel
from app.infra.db.daos.base_dao import BaseDao


class AccountDao(BaseDao):

    def __init__(self):
        super().__init__('Account', AccountModel)

    def modifyEmail(self, email, id_User):
        query = 'UPDATE Account SET email = \'{}\' WHERE id_User = {}'.format(
            email, id_User)
        db.replace(query, {'id_User': id_User, 'email': email})
        return {"id_User": id_User, "email": email}

    def modifyPassword(self, password, id_User):
        query = 'UPDATE Account SET password = \'{}\' WHERE id_User = {}'.format(
            password, id_User)
        db.replace(query, {'id_User': id_User, 'password': password})
        return {"id_User": id_User, "password": password}
