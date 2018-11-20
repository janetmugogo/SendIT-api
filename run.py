from app import create_app
from flask_jwt_extended import JWTManager
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app = create_app()

if __name__ == '__main__':
    app.run()
