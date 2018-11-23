from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from instance.config import app_config
from app import db_config
from app.db_config import drop_tables, create_tables


def create_app(config):
    # creates and configurs the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config])
    create_tables()
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

    JWTManager(app)
    # register blueprints
    from app.api.v1 import version1
    from app.api.v2 import version2


    @app.errorhandler(500)
    def page_not_found():
        return jsonify({"error":"Resource not found"})



    app.register_blueprint(version1)
    app.register_blueprint(version2)

    return app
