from flask import Blueprint
from flask_restful import Api

from .views.parcel_views import Parcels
from .views.user_views import Users

version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(version1)


api.add_resource(Parcels, '/parcels')
api.add_resource(Users, '/users')