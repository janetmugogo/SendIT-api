from flask import Blueprint
from flask_restful import Api

from .views.parcel_views import Parcels, Parcel, Cancel
from .views.user_views import Users
from .views.parcel_views import SpecificUserOrder

version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(version1, catch_all_404s=True)

api.add_resource(Parcels, '/parcels', strict_slashes=False)
api.add_resource(Parcel, '/parcel/<order_id>', strict_slashes=False)
api.add_resource(Cancel, '/parcels/<order_id>/cancel', strict_slashes=False)
api.add_resource(SpecificUserOrder, '/users/<user_id>/parcels', strict_slashes=False)
api.add_resource(Users, '/users', strict_slashes=False)
