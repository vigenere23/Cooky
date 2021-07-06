from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.mysql_connection import connect_to_mysql
from app.infra.db.mysql_database_connection import MySQLDBConnection
from app.infra.db.db_connector import DBConnector
from app.infra.db.sql_transaction import SQLTransaction
from app.infra.db.repositories.mysql_recipe_repository import MySQLRecipeRepository
from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.infra.db.refactor.recipe_dao import RecipeDao
from app.infra.db.refactor.recipe_ingredient_dao import RecipeIngredientDao


flask_app = Flask(__name__)
flask_app.config.from_object(Config)

mysql_connection = connect_to_mysql(Config.DATABASE)
db_connection = MySQLDBConnection(mysql_connection)
db = DBConnector(db_connection)
transaction = SQLTransaction(db_connection)

db_connection_2 = MysqlDBConnection(mysql_connection)
recipe_repository = MySQLRecipeRepository(db_connection_2, RecipeDao(), RecipeIngredientDao())


from app.application.recipe.recipe_editing_usecase import RecipeEditingUseCase
from app.application.recipe.recipe_finding_usecase import RecipeFindingUseCase
from app.application.recipe.recipe_creation_usecase import RecipeCreationUseCase


recipe_creation_usecase = RecipeCreationUseCase(recipe_repository)
recipe_finding_usecase = RecipeFindingUseCase(recipe_repository)
recipe_editing_usecase = RecipeEditingUseCase(recipe_repository)


# FUTURE : will not need to be imported here after DIP refactor
from app.api import main_controller, ingredient_controller, cart_controller, user_controller, auth
from app.api.recipe import recipe_controller


main_controller.register_routes(flask_app)
ingredient_controller.register_routes(flask_app)
cart_controller.register_routes(flask_app)
recipe_controller.register_routes(flask_app)
user_controller.register_routes(flask_app)
auth.register_routes(flask_app)

CORS(flask_app)
