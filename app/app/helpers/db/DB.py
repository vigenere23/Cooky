from app.helpers.db import DBConnection


class DB:
    def __init__(self, connection: DBConnection):
        self.__connection = connection

    def delete(self, query, data):
        try:
            self.__connection.execute(query, data).commit()

        except Exception as e:
            self.__connection.rollback()
            raise e

    def replace(self, query, data):
        try:
            self.__connection.execute(query, data).commit()

        except Exception as e:
            self.__connection.rollback()
            raise e

    def insert(self, query, data, autocommit=True):
        try:
            self.__connection.execute(query, data)
            if autocommit:
                self.__connection.commit()
            return self.__connection.lastrowid

        except Exception as e:
            self.__connection.rollback()
            raise e

    def select(self, query, data=None, limit=None):
        result = self.__connection.execute(query, data)

        return result.fetch_one() if limit == 1 else result.fetch_many(limit)

    def commit(self):
        try:
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise e

    def rollback(self):
        self.__connection.rollback()
