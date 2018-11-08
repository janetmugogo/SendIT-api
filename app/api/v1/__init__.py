from flask import Blueprint
from flask_restful import Api

from .views.parcel_views import Parcels
from .views.parcel_views import Parcel
from .views.parcel_views import Cancel
from .views.parcel_views import ChangeDestination



version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(version1)


api.add_resource(Parcels, '/parcels')
api.add_resource(Parcel, '/parcel/<int:order_id>')
api.add_resource(Cancel, '/parcels/<int:order_id>/cancel')
api.add_resource(ChangeDestination, '/parcels/<int:order_id>/changedestination')