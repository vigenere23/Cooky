from app.infra.db.refactor.mysql_condition_builder import MysqlConditionBuilder
from typing import Optional
from app.infra.db.models.user import AccountModel
from app.infra.db.refactor.mysql_executor import MySQLExecutor


class AccountDao:

    def __init__(self):
        self.__table_name = 'Account'

    def find_by_user_id(self, executor: MySQLExecutor, user_id: int) -> Optional[AccountModel]:
        condition_builder = MysqlConditionBuilder().where(['id_User = %(user_id)s'], {'user_id': user_id})
        result = executor.find(self.__table_name, condition_builder.build())
        return AccountModel(**result) if result else None

    def find_by_id(self, executor: MySQLExecutor, account_id: int) -> Optional[AccountModel]:
        result = executor.find_by_id(self.__table_name, account_id)
        return AccountModel(**result) if result else None

    def save(self, executor: MySQLExecutor, account_model: AccountModel) -> int:
        return executor.create(account_model)

    def update(self, executor: MySQLExecutor, account_model: AccountModel):
        return executor.update(account_model)
