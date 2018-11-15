from flask import Flask
from flask import Flask, jsonify, make_response


# from config import app_config

def create_app():
    # creates and configurs the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    # create_tables()

    # register blueprints
    from app.api.v1 import version1

    @app.errorhandler(400)
    def page_not_found(e):
        return jsonify({"Resource not found"})
    app.register_blueprint(version1)

    return app
