from flask import Flask
from flask_cors import CORS
from .config import Config
from .helpers.DB import DB

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

db = DB(Config.DATABASE)

from . import auth, routes

CORS(flask_app)
