from app import db

def getColumns(table_name):
  query = 'DESC {}'.format(table_name)
  return db.select(query)
