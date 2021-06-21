from . import auth, routes
from .helpers.DB import DB
from .config import Config
from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv
load_dotenv()


flask_app = Flask(__name__)
flask_app.config.from_object(Config)

db = DB(Config.DATABASE)


CORS(flask_app)
