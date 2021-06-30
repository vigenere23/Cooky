import time
from mysql.connector import MySQLConnection
from mysql.connector import connect

def connect_to_mysql(config, remaining_tries: int = 10, timeout: int = 5) -> MySQLConnection:
    while remaining_tries > 0:
        try:
            return connect(**config)
        except Exception as e:
            remaining_tries -= 1
            print('Database connection failed.')
            print(e)
            time.sleep(timeout)

    if remaining_tries == 0:
        raise Exception(
            'Could not connect to database after 5 tries. Aborting.')

    print('Successfully connected to database')
