from app.infra.db.refactor.mysql_executor import MySQLExecutor
from typing import Callable, TypeVar
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase


class MysqlDBConnection:
    def __init__(self, connection: MySQLConnection):
        self.__connection = connection

    # FUTURE : see if possible to do
    #   execute(action, *args): action(executor, *args)
    # with type annotations
    T = TypeVar('T')
    def execute(self, action: Callable[[MySQLExecutor], T], *args) -> T:
        cursor: CursorBase = self.__connection.cursor()
        executor = MySQLExecutor(cursor)

        try:
            result = action(executor, *args)
            self.__connection.commit()
            return result
        except Exception as e:
            self.__connection.rollback()
            raise e
        finally:
            cursor.close()
