from flask import Flask
# from .db_config import create_tables


# from config import app_config

def create_app():
    # creates and configurs the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    # create_tables()

    # register blueprints
    from app.api.v1 import version1

    app.register_blueprint(version1)

    return app
