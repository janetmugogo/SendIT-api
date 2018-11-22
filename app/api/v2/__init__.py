from flask_restful import Api
from flask import Blueprint

from app.api.v2.views.user_views import Signup
from app.api.v2.views.user_views import Login
from app.api.v2.views.parcel_views import CreateParcel, Parcel, Cancel, SpecificUserOrder, ChangeDestination




version2 = Blueprint('apiv2', __name__, url_prefix='/api/v2')
api = Api(version2)

api.add_resource(Signup, '/auth/signup', strict_slashes=False)
api.add_resource(Login, '/auth/login', strict_slashes=False)
api.add_resource(CreateParcel, '/create_parcel', strict_slashes=False) #createparcel
api.add_resource(Parcel, '/parcel/<int:order_id>', strict_slashes=False) #getorderbyid
api.add_resource(Cancel, '/create_parcel/<order_id>/cancel', strict_slashes=False) #cancelorder
api.add_resource(SpecificUserOrder, '/users/<user_id>/parcel', strict_slashes=False)
api.add_resource(ChangeDestination, '/parcel/<int:order_id>/destination', strict_slashes=False)




