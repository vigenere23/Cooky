from typing import Generator
from contextlib import contextmanager
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase
from app.infra.db.refactor.mysql_executor import MySQLExecutor


class MysqlDBConnection:
    def __init__(self, connection: MySQLConnection):
        self.__connection = connection


    @contextmanager
    def transaction(self) -> Generator[MySQLExecutor, None, None]:
        cursor: CursorBase = self.__connection.cursor()
        executor = MySQLExecutor(cursor)

        try:
            yield executor
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise e
        finally:
            cursor.close()
