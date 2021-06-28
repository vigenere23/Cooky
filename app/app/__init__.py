from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from .config import Config
from .infra.db.db_connector import DBConnector
from app.infra.db.mysql_database_connection import MySQLDBConnection
from app.infra.db.sql_transaction import SQLTransaction

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

db_connection = MySQLDBConnection(Config.DATABASE)
db = DBConnector(db_connection)
transaction = SQLTransaction(db_connection)

from . import modules
from .api import auth, recipe_controller, ingredient_controller

CORS(flask_app)
