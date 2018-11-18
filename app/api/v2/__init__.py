from flask_restful import Api
from flask import Blueprint


version2 = Blueprint('apiv2', __name__, url_prefix='/api/v2')
api = Api(version2)