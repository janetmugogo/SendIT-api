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
        return db.get_all_parcels(), 200


class Parcel(Resource):
    def get(self, order_id):
        """fetches a single order for the user/admin"""
        order = db.get_single_order(order_id)
        if order:
            return order, 200
        return make_response(jsonify({"message": "order does not exist"})), 404


class Cancel(Resource):
    def put(self, order_id):
        """allows user to cancel a specific order"""
        data = request.get_json()
        status = data['status']
        order = db.get_single_order(order_id)
        if order:
            db.cancel_order(order_id, status)
            return {"message": "order status updated successfully"}
        return make_response(jsonify({"message": "order does not exist"})), 404


class ChangeDestination(Resource):
    def put(self, order_id):
        """allow user to change destination"""
        data = request.get_json()
        destination = data['destination']
        order = db.get_single_order(order_id)
        if order:
            db.change_destination(order_id, destination)
            return {"message": "destination updated successfully"}
        return make_response(jsonify({"message": "order does not exist"})), 404
