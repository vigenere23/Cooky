from app import flask_app
from .controller import routes

flask_app.register_blueprint(routes, url_prefix='/recipes')
