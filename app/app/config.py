import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY', '4729ef76-3d15-4356-8c0c-a54137c1250a')
  JWT_AUTH_URL_RULE = '/login/'
  DATABASE = {
    'user': os.environ.get('MYSQL_USER', 'api'),
    'password': os.environ.get('MYSQL_PASSWORD', 'e7364202-2f94-4355-b354-c95907adfef6'),
    'host': os.environ.get('DB_HOST', 'db'),
    'port': os.environ.get('DB_PORT', '3306'),
    'database': os.environ.get('MYSQL_DATABASE', 'projet'),
    'connection_timeout': 5,
    'use_pure': True
  }
