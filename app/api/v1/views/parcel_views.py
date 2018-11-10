from flask_restful import Resource, Api, reqparse
from app.api.v1.models.parcel_model import Parcels
from flask import Flask, request, jsonify, make_response

db = Parcels()


# Multiple parcels class
class Parcels(Resource):

    # the user creates an order
    def post(self):
        data = request.get_json(force=True)
        name = data['name']
        phonenumber = data['phonenumber']
        idnumber = data['idnumber']
        location = data['location']
        address = data['address']
        weight = data['weight']
        user_id = 'user_id'

        db.save_parcel(name, phonenumber, idnumber, location, address, weight, user_id)
        return make_response(jsonify({"message": "order created successfully"}))

    # the user can fetch all parcel delivery orders
    def get(self):
        return db.get_all_parcels(), 200


# single parcel class
class Parcel(Resource):
    # the user can fetch for a specific parcel deivery order using order_id
    def get(self, order_id):
        order = db.get_single_order(order_id)
        if order:
            return order, 200
        return make_response(jsonify({"message": "order does not exist"})), 404


# cancel order class
class Cancel(Resource):
    # the user can cancel a specific order only when it is in-transit
    def put(self, order_id):
        data = request.get_json()
        status = data['status']
        order = db.get_single_order(order_id)
        if order:
            db.cancel_order(order_id, status)
            return {"message": "order status updated successfully"}
        return make_response(jsonify({"message": "order does not exist"})), 404


# change destination of a parcel class
class ChangeDestination(Resource):
    # change destination of a specific order in their list of orders only when it is in transit
    def put(self, order_id):
        data = request.get_json()
        destination = data['destination']
        order = db.get_single_order(order_id)
        if order:
            db.change_destination(order_id, destination)
            return {"message": "destination updated successfully"}
        return make_response(jsonify({"message": "order does not exist"})), 404


# cancel order class
class SpecificUserOrder(Resource):
    # the user can cancel a specific order only when it is intransit
    def get(self, user_id):
        order = db.specific_user_order(user_id)
        return make_response(jsonify(order), 200)

#