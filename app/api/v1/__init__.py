from flask import Blueprint
from flask_restful import Api

from .views.parcel_views import Parcels, Parcel, Cancel
from .views.user_views import Users
from .views.parcel_views import ChangeDestination

version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(Parcels, '/parcels', strict_slashes=False)
api.add_resource(Parcel, '/parcel<int:order_id>', strict_slashes=False)
api.add_resource(Cancel, '/parcels/<int:order_id>/cancel', strict_slashes=False)
api.add_resource(ChangeDestination, '/parcels/<int:order_id>/changedestination', strict_slashes=False)

api.add_resource(Users, '/users', strict_slashes=False)
