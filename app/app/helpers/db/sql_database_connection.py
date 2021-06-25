import time
from typing import Tuple
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase
from mysql.connector import connect
from app.helpers.db.sql_result import SQLResult
from . import DBConnection

class SQLDBConnection(DBConnection):
    def __init__(self, config, remaining_tries: int = 10, timeout: int = 5):
        while remaining_tries > 0:
            try:
                self.__connection: MySQLConnection = connect(**config)
                self.__cursor: CursorBase = self.__connection.cursor()
                break
            except Exception as e:
                remaining_tries -= 1
                print('Database connection failed.')
                print(e)
                time.sleep(timeout)

        if remaining_tries == 0:
            raise Exception(
                'Could not connect to database after 5 tries. Aborting.')

        print('Successfully connected to database')

    def execute(self, query: str, data: Tuple) -> SQLResult:
        self.__cursor.execute(query, data)
        return SQLResult(self.__cursor)

    def commit(self):
        self.__connection.commit()

    def rollback(self):
        self.__connection.rollback()
