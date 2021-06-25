from abc import ABC, abstractmethod
from app.helpers.db.sql_result import SQLResult
from typing import Tuple

class DBConnection(ABC):

    @abstractmethod
    def execute(self, query: str, data: Tuple) -> SQLResult:
        raise NotImplementedError()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()
