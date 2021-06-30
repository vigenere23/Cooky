from app.mysql_connection import connect_to_mysql
from app.application.recipe.recipe_finding_usecase import RecipeFindingUseCase
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

connection = connect_to_mysql(Config.DATABASE)
db_connection = MySQLDBConnection(connection)
db = DBConnector(db_connection)
transaction = SQLTransaction(db_connection)

from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.infra.db.refactor.recipe_dao import RecipeDao
from app.infra.db.refactor.recipe_ingredient_dao import RecipeIngredientDao
from app.infra.db.repositories.mysql_recipe_repository import MySQLRecipeRepository
from app.application.recipe.recipe_creation_usecase import RecipeCreationUseCase

db_connection_2 = MysqlDBConnection(connection)
recipe_repository = MySQLRecipeRepository(db_connection_2, RecipeDao(), RecipeIngredientDao())
recipe_creation_usecase = RecipeCreationUseCase(recipe_repository)
recipe_finding_usecase = RecipeFindingUseCase(recipe_repository)

from . import api

CORS(flask_app)
