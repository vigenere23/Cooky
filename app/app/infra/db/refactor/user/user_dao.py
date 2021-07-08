from typing import Optional
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from app.infra.db.refactor.mysql_condition_builder import MysqlConditionBuilder
from app.infra.db.models.user import UserModel


class UserDao:

    def __init__(self):
        self.__table_name = 'User'

    def find_by_id(self, executor: MySQLExecutor, user_id: int) -> Optional[UserModel]:
        result = executor.find_by_id(self.__table_name, user_id)
        return UserModel(**result) if result else None

    def find_by_username(self, executor: MySQLExecutor, username: str) -> Optional[UserModel]:
        condition_builder = MysqlConditionBuilder().where(['username = %(username)s'], {'username': username})
        result = executor.find(self.__table_name, condition_builder.build())
        return UserModel(**result) if result else None

    def save(self, executor: MySQLExecutor, user_model: UserModel) -> int:
        return executor.create(user_model)
