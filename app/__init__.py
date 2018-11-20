from flask import Flask
from flask import Flask, jsonify, make_response




def create_app():
    # creates and configurs the app
    app = Flask(__name__, instance_relative_config=True)


    # register blueprints
    from app.api.v1 import version1
    from app.api.v2 import version2

    @app.errorhandler(500)
    def page_not_found():
        return jsonify({"error":"Resource not found"})

    app.register_blueprint(version1)
    app.register_blueprint(version2)

    return app
