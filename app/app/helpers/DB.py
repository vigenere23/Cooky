import time
from mysql.connector import connect

class DB:
  def __init__(self, config):
    remaining_tries = 10
    while remaining_tries > 0:
      try:
        self.__connection = connect(**config)
        self.__cursor = self.__connection.cursor()
        break
      except Exception as e:
        remaining_tries -= 1
        print('Database connection failed.')
        print(e)
        time.sleep(5)

    if (remaining_tries == 0):
      raise Exception('Could not connect to database after 5 tries. Aborting.')
    else:
      print('Successfully connected to database')

  def delete(self, query, data):
    try:
      self.__cursor.execute(query, data)
      self.__connection.commit()

    except Exception as e:
      self.__connection.rollback()
      raise e

  def replace(self, query, data):
    try:
      self.__cursor.execute(query, data)
      self.__connection.commit()

    except Exception as e:
      self.__connection.rollback()
      raise e

  def insert(self, query, data, autocommit=True):
    try:
      self.__cursor.execute(query, data)
      if autocommit:
        self.__connection.commit()
      return self.__cursor.lastrowid

    except Exception as e:
      self.__connection.rollback()
      raise e

  def select(self, query, data=None, limit=0):
    self.__cursor.execute(query, data)
    results = None
    if limit == 1:
      results = self.__cursor.fetchone()
    elif limit > 1:
      results = self.__cursor.fetchmany(int(limit))
    else:
      return self.__cursor.fetchall()
    
    try:
      self.__cursor.fetchall()
    except:
      pass
    
    return results

  def commit(self):
    try:
      self.__connection.commit()
    except Exception as e:
      self.__connection.rollback()
      raise e

  def rollback(self):
    self.__connection.rollback()

  def start_transaction(self):
    self.__connection.start_transaction()
