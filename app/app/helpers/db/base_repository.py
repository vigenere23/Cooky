from typing import Callable, TypeVar
from app.helpers.db import DBConnection


class BaseRepository:
    def __init__(self, connection: DBConnection):
        self.__connection = connection

    def delete(self, query, data):
        try:
            self.__connection.execute(query, data)
            self.__connection.commit()

        except Exception as e:
            self.__connection.rollback()
            raise e

    def replace(self, query, data):
        try:
            self.__connection.execute(query, data)
            self.__connection.commit()

        except Exception as e:
            self.__connection.rollback()
            raise e

    def create(self, query, data, autocommit=True):
        try:
            result = self.__connection.execute(query, data)
            if autocommit:
                self.__connection.commit()
            return result.last_id()

        except Exception as e:
            self.__connection.rollback()
            raise e

    def find(self, query, data=None):
        result = self.__connection.execute(query, data)

        return result.fetch_one()

    def findAll(self, query, data=None, limit=None):
        result = self.__connection.execute(query, data)

        return result.fetch_many(limit)

    T = TypeVar('T')
    def transaction(self, action: Callable[[], T]) -> T:
        try:
            result = action()
            self.__connection.commit()
            return result
        except Exception as e:
            self.__connection.rollback()
            raise e
