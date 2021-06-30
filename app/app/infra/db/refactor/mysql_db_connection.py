import time
from app.infra.db.refactor.mysql_executor import MySQLExecutor
from typing import Callable, TypeVar
from mysql.connector import MySQLConnection, connect
from mysql.connector.cursor import CursorBase


class MysqlDBConnection:
    def __init__(self, config, remaining_tries: int = 10, timeout: int = 5):
        while remaining_tries > 0:
            try:
                self.__connection: MySQLConnection = connect(**config)
                break
            except Exception as e:
                remaining_tries -= 1
                print('Database connection failed.')
                print(e)
                time.sleep(timeout)

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
        except Exception:
            self.__connection.rollback()
        finally:
            cursor.close()
