import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_AUTH_URL_RULE = '/login'
    DATABASE = {
        'user': 'api',
        'password': os.environ.get('MYSQL_PASSWORD'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT'),
        'database': 'projet',
        'connection_timeout': 5,
        'use_pure': True
    }
