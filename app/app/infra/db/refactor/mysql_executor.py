from typing import Any
from mysql.connector.cursor import CursorBase

class MySQLExecutor:
    def __init__(self, cursor: CursorBase):
        self.__cursor = cursor

    def find(self, query, data) -> Any:
        self.__cursor.execute(query, data)
        result = self.__cursor.fetchone()

        self.__flush_results()

        return result

    def findAll(self, query, data, limit=None):
        self.__cursor.execute(query, data)

        if limit is None:
            return self.__cursor.fetchall()
        else:
            result = self.__cursor.fetchmany(size=limit)
            self.__flush_results()

            return result

    def create(self, query, data) -> int:
        self.__cursor.execute(query, data)
        return self.__cursor.lastrowid

    def __flush_results(self):
        try:
            self.__cursor.fetchall()
        except Exception:
            pass
