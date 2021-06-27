from typing import Callable, TypeVar
from app.infra.db.db_connection import DBConnection
from app.domain.transaction_executor import TransactionExecutor

class SQLTransaction(TransactionExecutor):

    def __init__(self, connection: DBConnection):
        self.__connection = connection

    T = TypeVar('T')
    def execute(self, action: Callable[[], T]):
        try:
            result = action()
            self.__connection.commit()
            return result
        except Exception as e:
            self.__connection.rollback()
            raise e
