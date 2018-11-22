import os
from app import create_app
from flask_jwt_extended import JWTManager
# app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
# jwt = JWTManager(app)
#pick flaskenv from env
config = os.getenv("FLASK_ENV")
app = create_app(config)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run()
