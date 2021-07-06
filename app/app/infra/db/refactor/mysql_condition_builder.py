from __future__ import annotations
from typing import Any, Dict, List
from app.infra.db.refactor.mysql_condition import MysqlCondition


class MysqlConditionBuilder:
    def __init__(self):
        self.__query = ''
        self.__data = {}

    def where(self, conditions: List[str], data: Dict[str, Any] = None) -> MysqlConditionBuilder:
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


    def build(self) -> MysqlCondition:
        return MysqlCondition(self.__query, self.__data)
