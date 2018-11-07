from flask_restful import Resource, Api, reqparse
from app.api.v1.models.parcel_model import Parcels
from flask import request, jsonify, make_response

db = Parcels()


class Parcels(Resource):
    def post(self):
        data = request.get_json(force=True)
        name = data['name']
        phonenumber = data['phonenumber']
        idnumber = data['idnumber']
        location = data['location']
        address = data['address']
        weight = data['weight']

        db.save_parcel(name, phonenumber, idnumber, location, address, weight)
        return make_response(jsonify({"message": "order created successfully"}))

    def get(self):
        """get all orders from the database"""
        return db.get_all_parcels()


class Parcel(Resource):
    def get(self, order_id):
        """fetches a single order for the user/admin"""

        return db.get_single_order(order_id)
