from typing import List, Tuple
from mysql.connector.cursor import CursorBase

class SQLResult:
    def __init__(self, cursor: CursorBase):
        self.__cursor = cursor

    def fetch_one(self) -> Tuple:
        result = self.__cursor.fetchone()
        self.__flush_results()

        return result

    def fetch_many(self, n: int = None) -> List[Tuple]:
        results = self.__cursor.fetchall() if n is None else self.__cursor.fetchmany(n)
        self.__flush_results()

        return results

    def last_id(self) -> int:
        return self.__cursor.lastrowid

    def __flush_results(self):
        try:
            self.__cursor.fetchall()
        except Exception:
            pass
