from flask_restful import Resource, Api, reqparse
from app.api.v1.models.parcel_model import Parcels
from flask import Flask, request, jsonify, make_response

db = Parcels()


# Multiple parcels class
class Parcels(Resource):
    def __init__(self):
        self.user_id = 1

    # the user creates an order
    def post(self):
        data = request.get_json(force=True)
        required_params = ('name', 'phonenumber', 'idnumber', 'location', 'address', 'weight', 'price', 'user_id')
        for param in required_params:
            if param not in data:
                return make_response(jsonify(message="incomplete request"), 400)
        name = data['name']
        phonenumber = data['phonenumber']
        idnumber = data['idnumber']
        location = data['location']
        address = data['address']
        weight = data['weight']
        price = data['price']
        user_id = self.user_id + 1

        db.save_parcel(name, phonenumber, idnumber, location, address, weight, price, user_id)

        return make_response(jsonify (message = "order created successfully"), 201)

    # the user can fetch all parcel delivery orders
    def get(self):
        parcel_order = db.get_all_parcels()
        if parcel_order:
            payload ={

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
        try:
            int(order_id)
        except ValueError:
            return "invalid order_id"
        else:
            order_id = int(order_id)
        order = db.get_single_order(order_id)
        if order:
            payload ={
                "order": order
            }
            return make_response(jsonify(payload), 200)
        return make_response(jsonify({"message": "order does not exist"}), 400)

# specific user class
class SpecificUserOrder(Resource):
    #fetch all parcel delivery orders by specific id
    def get(self, user_id):
        try:
            int(user_id)
        except ValueError:
            return "invalid user_id"
        else:
            user_id = int(user_id)
        user_order = db.specific_user_order(user_id)
        return user_order


# cancel order class
class Cancel(Resource):
    # the user can cancel a specific order only when it is in-transit
    def put(self, order_id):
        order = db.get_single_order(order_id)
        if order:
            result = db.cancel_order(order_id)
            return make_response(jsonify(result))
        return make_response(jsonify({"message":"Order not found"}), 404)

