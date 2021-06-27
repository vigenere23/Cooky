from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from .config import Config
from .infra.db.db_connector import DBConnector
from app.infra.db.mysql_database_connection import MySQLDBConnection

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

db_connection = MySQLDBConnection(Config.DATABASE)
db = DBConnector(db_connection)

from . import auth, routes

CORS(flask_app)
