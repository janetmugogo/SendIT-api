import psycopg2
from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
from app.api.v2.models.user_model import Users
from app.api.v2.models.parcel_model import Parcels


url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"

class CreateParcel(Resource):
    #create a parcel delivery order
    parser = reqparse.RequestParser()
    parser.add_argument(
        'user_id', type=str, required=True, help='user_id  is required', location='json')
    parser.add_argument(
        'sender_name', type=str, required=True, help='sender name  is required', location='json')

    parser.add_argument(
        'phone_number', type=str, required=True, help='phone number  is required', location='json')

    parser.add_argument(
        'id_number', type=str, required=True, help='id number is required', location='json')
    parser.add_argument(
        'location', type=str, required=True, help='location is required', location='json')
    parser.add_argument(
        'address', type=str, required=True, help='address is required', location='json')
    parser.add_argument(
         'weight', type=str, required=True, help='weight is required', location='json')

    parser.add_argument(
        'destination', type=str, required=True, help='destination is required', location='json')

    @jwt_required
    def post(self):
        data = CreateParcel.parser.parse_args()
        username = get_jwt_identity()

        parcel = Parcels(data['user_id'], data['sender_name'], data['phone_number'], data['id_number'],
                         data['location'], data['address'], data['weight'],
                         data['destination'])
        if Users.find_by_username(self, username):
            # check if there is a user with that id
            parcel.store_in_db()

            return {'message': 'parcel delivery order created'}, 201
        else:

            return {'Message': 'User doesn\'t exist, please signup to create an order'}, 401
            # order = Parcels(sender_name, phone_number, id_number, location, address, weight, destination, get_jwt_identity())
        # parcel.store_in_db()
        # return {'message':'parcel delivery order created'}, 201

    @jwt_required
    def get(self):
        username = get_jwt_identity()
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if not Users.find_by_username(self,username):
            return {'message':'you cannot view parcels'}
        parcel_order = Parcels.get_all_parcels(self)
        if parcel_order:
            return parcel_order
        return {'message':'order not found'}

class Parcel(Resource):
    @jwt_required
    def get(self, order_id):
        con = psycopg2.connect(url)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        orders = Parcels().get_parcel_by_id(order_id)
        if orders:
         return orders
        return make_response(jsonify({"message":"There are no created orders "}), 404)



# cancel order class
class Cancel(Resource):
    @jwt_required
    def put(self, order_id):
        orders = Parcels().get_parcel_by_id(order_id)
        if not orders:
            return {'message':'No order by that id found'}
        result = Parcels.cancel_order(self,order_id)
            # return make_response(jsonify(result))
        return make_response(jsonify({"message":"Order has been cancelled"}), 400)


# specific user class
class SpecificUserOrder(Resource):
    @jwt_required
    #fetch all parcel delivery orders by specific id
    def get(self, user_id):
        user_id = int(user_id)
        user_order = Parcels.specific_user_order(self, user_id)
        if not user_order:
            return {'message':'No user with that id'}
        return user_order
class ChangeDestination(Resource):
    @jwt_required
    def put(self, order_id):
        destination = request.get_json()['destination'] #key in request body
        new_destination = Parcels.change_destination(self, destination, order_id)
        if new_destination:
            return {'message':'destination updated successfuly'}
        else:
            return {'message': 'No order with that id'}




