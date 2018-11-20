from flask import Flask
from flask import Flask, jsonify, make_response
from flask_jwt_extended import JWTManager

from app import db_config
from app.db_config import drop_tables,create_tables

url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"


def create_app():
    # creates and configurs the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    JWTManager(app)
    # register blueprints
    from app.api.v1 import version1
    from app.api.v2 import version2
    # db_init()
    # query = """INSERT INTO users VALUES(DEFAULT ,%s,%s,%s,%s)"""
    # cur.execute(query, ('one', 'two', 'two', 'three'))
    # con.commit()
    @app.errorhandler(500)
    def page_not_found():
        return jsonify({"error":"Resource not found"})



    app.register_blueprint(version1)
    app.register_blueprint(version2)

    return app
