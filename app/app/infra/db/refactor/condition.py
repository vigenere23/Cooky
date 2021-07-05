from __future__ import annotations
from typing import Any, Dict, List


class Condition:
    def __init__(self):
        self.__query = ''
        self.__data = {}

    def where(self, conditions: List[str], data: Dict[str, Any] = None) -> Condition:
        if len(conditions) == 0 or conditions is None:
            return self

        if len(self.__query) != 0:
            self.__query += ' OR ('
        else:
            self.__query = 'WHERE ('


        self.__query += ' AND '.join(conditions) + ')'

        if data is not None:
            self.__data.update(data)

        return self


    def query(self) -> str:
        return self.__query

    def data(self) -> Dict[str, Any]:
        return self.__data
