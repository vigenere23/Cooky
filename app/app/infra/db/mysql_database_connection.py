from typing import Tuple
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase
from app.infra.db.sql_result import SQLResult
from .db_connection import DBConnection

class MySQLDBConnection(DBConnection):
    def __init__(self, connection: MySQLConnection):
        self.__connection = connection
        self.__cursor: CursorBase = connection.cursor()

    def execute(self, query: str, data: Tuple) -> SQLResult:
        self.__cursor.execute(query, data)
        return SQLResult(self.__cursor)

    def commit(self):
        self.__connection.commit()

    def rollback(self):
        self.__connection.rollback()
