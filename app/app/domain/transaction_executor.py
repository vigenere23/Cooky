from abc import ABC, abstractmethod
from typing import Callable, TypeVar

class TransactionExecutor(ABC):

    T = TypeVar('T')
    @abstractmethod
    def execute(self, action: Callable[[], T]):
        raise NotImplementedError()
