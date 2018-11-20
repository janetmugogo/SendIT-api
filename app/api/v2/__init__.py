from flask_restful import Api
from flask import Blueprint

from app.auth .user_views import Signup
from app.auth.user_views import Login
# from app.auth.user_views import Users


version2 = Blueprint('apiv2', __name__, url_prefix='/api/v2')
api = Api(version2)

api.add_resource(Signup, '/signup', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)

# api.add_resource(Users, '/users', strict_slashes=False)
# api.add_resource(Signup, '/username', strict_slashes=False)



