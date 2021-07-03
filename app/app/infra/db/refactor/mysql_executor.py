from typing import Any, Dict, List, Tuple, Union
from mysql.connector.cursor import CursorBase


class MySQLExecutor:
    def __init__(self, cursor: CursorBase):
        self.__cursor = cursor

    def find(self, query: str, data: Any = None) -> Dict[str, Any]:
        result = self.__cursor.execute(query, data)
        result_map = self.__map_columns_single(result)

        self.__flush_results()

        return result_map

    def findById(self, table_name: str, id: Union[str, int]):
        query = f"SELECT * FROM {table_name} WHERE id = %(id)s"
        data = { 'id': id }
        self.__cursor.execute(query, data)

        result = self.__cursor.fetchone()
        result_map = self.__map_columns_single(result)

        self.__flush_results()

        return result_map

    def findAll(self, query: str, data: Any = None, limit: int = None) -> List[Tuple]:
        self.__cursor.execute(query, data)

        if limit is None:
            results = self.__cursor.fetchall()
            return self.__map_columns_many(results)
        else:
            results = self.__cursor.fetchmany(size=limit)
            results_map = self.__map_columns_many(results)
            self.__flush_results()

            return results_map

    def create(self, query: str, data: Any = None) -> int:
        self.__cursor.execute(query, data)
        return self.__cursor.lastrowid

    def __map_columns_single(self, result: Tuple) -> Dict[str, Any]:
        columns = self.__get_columns()

        return dict(zip(columns, result))

    def __map_columns_many(self, results: List[Tuple]) -> List[Dict[str, Any]]:
        columns = self.__get_columns()

        return [dict(zip(columns, result)) for result in results]

    def __get_columns(self) -> List[str]:
        return [column_metadata[0] for column_metadata in self.__cursor.description]

    def __flush_results(self):
        try:
            self.__cursor.fetchall()
        except Exception:
            pass
