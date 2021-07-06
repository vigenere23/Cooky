from typing import Any, Dict


class MysqlCondition:
    def __init__(self, query: str, data: Dict[str, Any]):
        self.__query = query
        self.__data = data

    def query(self) -> str:
        return self.__query

    def data(self) -> Dict[str, Any]:
        return self.__data
