from app.infra.db.refactor.mysql_condition import MysqlCondition
from dataclasses import asdict
from app.infra.db.refactor.mysql_model import MysqlModel
from typing import Any, Dict, List, Optional, Tuple, Union
from mysql.connector.cursor import CursorBase


class MySQLExecutor:

    def __init__(self, cursor: CursorBase):
        self.__cursor = cursor


    def find_by_id(self, table_name: str, id: Union[str, int]) -> Dict[str, Any]:
        query = f"SELECT {table_name}.* FROM {table_name} WHERE id = %(id)s"
        data = { 'id': id }

        return self.find_from_query(query, data)


    def find(self, table_name: str, condition: MysqlCondition):
        query = f'SELECT {table_name}.* FROM {table_name} {condition.query()}'
        data = condition.data()

        return self.find_from_query(query, data=data)


    def find_all(self, table_name: str, condition: MysqlCondition, limit: int = None):
        query = f'SELECT {table_name}.* FROM {table_name} {condition.query()}'
        data = condition.data()

        return self.find_all_from_query(query, data=data, limit=limit)


    def create(self, model: MysqlModel) -> int:
        query = f'INSERT INTO {model.table_name()} {model.insert_columns_template()} VALUES {model.insert_values_template()}'
        data = asdict(model)

        return self.create_from_query(query, data)


    def update(self, model: MysqlModel):
        query = f'UPDATE {model.table_name()} SET {model.update_entries_template()} WHERE id = %(id)s'
        data = asdict(model)

        self.__cursor.execute(query, data)


    def delete(self, table_name: str, id: int):
        query = f'DELETE FROM {table_name} WHERE id = %(id)s'
        data = {'id': id}

        self.__cursor.execute(query, data)


    def find_from_query(self, query: str, data: Any = None) -> Optional[Dict[str, Any]]:
        self.__cursor.execute(query, data)

        result = self.__cursor.fetchone()
        self.__flush_results()

        return self.__map_columns_single(result) if result else None


    def find_all_from_query(self, query: str, data: Any = None, limit: int = None) -> List[Dict[str, Any]]:
        self.__cursor.execute(query, data)
        results = []

        if limit is None:
            results = self.__cursor.fetchall()
        else:
            results = self.__cursor.fetchmany(size=limit)
            self.__flush_results()

        return self.__map_columns_many(results)


    def create_from_query(self, query: str, data: Any = None) -> Optional[int]:
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


    def __flush_results(self) -> None:
        self.__cursor.fetchall()
