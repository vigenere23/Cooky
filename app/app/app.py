from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.mysql_connection import connect_to_mysql
from app.infra.db.mysql_database_connection import MySQLDBConnection
from app.infra.db.db_connector import DBConnector
from app.infra.db.sql_transaction import SQLTransaction
from app.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from app.infra.db.refactor.recipe.mysql_recipe_repository import MySQLRecipeRepository
from app.infra.db.refactor.recipe.recipe_dao import RecipeDao
from app.infra.db.refactor.recipe.recipe_ingredient_dao import RecipeIngredientDao
from app.infra.db.refactor.user.address_dao import AddressDao
from app.infra.db.refactor.user.user_dao import UserDao
from app.infra.db.refactor.user.account_dao import AccountDao
from app.infra.db.refactor.user.mysql_user_repository import MysqlUserRepository
from app.application.recipe.recipe_editing_usecase import RecipeEditingUseCase
from app.application.authentication import AuthenticationUseCase
from app.application.account.user_finding_usecase import UserFindingUseCase
from app.application.recipe.recipe_finding_usecase import RecipeFindingUseCase
from app.application.recipe.recipe_creation_usecase import RecipeCreationUseCase
from app.application.account.signup_usecase import SignupUseCase
from app.application.account.user_editing_usecase import UserEditingUseCase


flask_app = Flask(__name__)
flask_app.config.from_object(Config)

mysql_connection = connect_to_mysql(Config.DATABASE)
db_connection = MySQLDBConnection(mysql_connection)
db = DBConnector(db_connection)
transaction = SQLTransaction(db_connection)

db_connection_2 = MysqlDBConnection(mysql_connection)
recipe_repository = MySQLRecipeRepository(db_connection_2, RecipeDao(), RecipeIngredientDao())
user_repository = MysqlUserRepository(db_connection_2, AccountDao(), UserDao(), AddressDao())

authentication_use_case = AuthenticationUseCase(user_repository)
recipe_creation_usecase = RecipeCreationUseCase(recipe_repository)
recipe_finding_usecase = RecipeFindingUseCase(recipe_repository)
recipe_editing_usecase = RecipeEditingUseCase(authentication_use_case, recipe_repository)
signup_usecase = SignupUseCase(user_repository)
user_finding_usecase = UserFindingUseCase(user_repository)
user_editing_usecase = UserEditingUseCase(user_repository)


from app.api.main import main_controller
from app.api import ingredient_controller, auth
from app.api.recipe import recipe_controller
from app.api.cart import cart_controller, command_controller
from app.api.user import user_controller, account_controller


main_controller.register_routes(flask_app)
ingredient_controller.register_routes(flask_app)
cart_controller.register_routes(flask_app)
command_controller.register_routes(flask_app)
recipe_controller.register_routes(flask_app)
user_controller.register_routes(flask_app)
account_controller.register_routes(flask_app)
auth.register_routes(flask_app)

CORS(flask_app)
