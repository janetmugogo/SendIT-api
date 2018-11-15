from flask_restful import Resource, Api, reqparse
from app.api.v1.models.parcel_model import Parcels
from flask import Flask, request, jsonify, make_response

db = Parcels()


# Multiple parcels class
class Parcels(Resource):

    # the user creates an order
    def post(self):
        data = request.get_json(force=True)
        if "price" not in data:
            return make_response(jsonify(message="incomplete request"), 400)
        name = data['name']
        phonenumber = data['phonenumber']
        idnumber = data['idnumber']
        location = data['location']
        address = data['address']
        weight = data['weight']
        price = data['price']
        user_id = data['user_id']

        db.save_parcel(name, phonenumber, idnumber, location, address, weight, price, user_id)

        return make_response(jsonify (message = "order created successfully"), 201)

    # the user can fetch all parcel delivery orders
    def get(self):
        parcel_order = db.get_all_parcels()
        if parcel_order:
            payload ={
                "message":"created order",
                "parcel delivery order": parcel_order
            }
            return make_response(jsonify(payload), 200)
        else:
            payload = {
                "message": "There are no created orders"
            }

        return make_response(jsonify(payload), 404)

# single parcel class
class Parcel(Resource):
    # the user can fetch for a specific parcel deivery order using order_id
    def get(self, order_id):
        order = db.get_single_order(order_id)
        if order:
            payload ={
                "message":"your order",
                "order": order
            }
            return make_response(jsonify(payload), 200)
        return make_response(jsonify({"message": "order does not exist"}), 400)

# specific user class
class SpecificUserOrder(Resource):
    # the user can cancel a specific order only when it is intransit
    def get(self, user_id):
        user_order = self.specific_user_order(user_id)
        if user_order:
            payload = {
                "message": "your order",
                "order": user_order
            }
            return make_response(jsonify(payload), 200)
        else:
            payload = {
                "message": "The user order is not found"
            }
            return make_response(jsonify(payload), 404)

# cancel order class
class Cancel(Resource):
    # the user can cancel a specific order only when it is in-transit
    def put(self, order_id):
        cancel_order = db.cancel_order(order_id)
        if cancel_order:
            payload = {
                "message":"order cancelled",
                "order":cancel_order
            }
            return make_response(jsonify(payload), 200)
        else:
            payload = {
                "message":"The order has been cancelled"
            }
        return make_response(jsonify(payload), 404)


# change destination of a parcel class
class ChangeDestination(Resource):
    # change destination of a specific order in their list of orders only when it is in transit
    def put(self, order_id):
        data = request.get_json()
        order_parcel = db.get_single_order(order_id)
        if order_parcel:
         order_destination = data['destination']
        if len(order_destination) < 5 or order_destination == '':
            payload = {
                "message": "please provide a valid destination address"
            }
            return make_response(jsonify(payload), 404)
        if not isinstance(order_destination, str):
            payload = {
                "message": "Destination must be characters"
            }
            return make_response(jsonify(payload), 404)
        else:
            db.change_destination(order_id, order_destination)
            payload = {
                "message":"order destination changed succesfully"
            }
            return make_response(jsonify(payload), 200)


