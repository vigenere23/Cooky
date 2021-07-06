from abc import abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class MysqlModel:
    @abstractmethod
    def table_name(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_id(self) -> str:
        raise NotImplementedError()

    def columns(self) -> List[str]:
        return list(self.__dict__.keys())

    def insert_columns_template(self) -> str:
        return f"({', '.join(self.columns())})"

    def insert_values_template(self) -> str:
        columns = map(lambda column: f'%({column})s', self.columns())
        return f"({', '.join(columns)})"

    def update_entries_template(self) -> str:
        columns = filter(lambda col: col != 'id', self.columns())
        entries = map(lambda column: f'{column} = %({column})s', columns)
        return ', '.join(entries)
