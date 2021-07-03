from app.infra.db.refactor.mysql_executor import MySQLExecutor
from typing import Callable, TypeVar
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase


class MysqlDBConnection:
    def __init__(self, connection: MySQLConnection):
        self.__connection = connection

    # FUTURE : try to fix typing for `action` to accept `*args` and `**kwargs`
    T = TypeVar('T')
    def transaction(self, action: Callable[[MySQLExecutor], T], *args, **kwargs) -> T:
        cursor: CursorBase = self.__connection.cursor()
        executor = MySQLExecutor(cursor)

        try:
            result = action(executor, *args, **kwargs)
            self.__connection.commit()
            return result
        except Exception as e:
            self.__connection.rollback()
            raise e
        finally:
            cursor.close()
