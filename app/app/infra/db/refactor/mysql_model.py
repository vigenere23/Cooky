from abc import abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class MysqlModel:
    @abstractmethod
    def table_name(self) -> str:
        raise NotImplementedError()

    def columns(self) -> List[str]:
        return list(self.__dict__.keys())

    def insert_columns_template(self) -> str:
        return f"({', '.join(self.columns())})"

    def insert_values_template(self) -> str:
        columns = map(lambda key: f'%({key})s', self.columns())
        return f"({', '.join(columns)})"
