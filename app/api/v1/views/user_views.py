from flask_restful import Resource, Api, reqparse
from app.api.v1.models.user_model import Users
from flask import request, jsonify, make_response

db = Users()


class Users(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help='username field is required', location='json')

    parser.add_argument(
        'email', type=str, required=True, help='email field is required', location='json')

    parser.add_argument(
        'password', type=str, required=True, help='password field is required', location='json')

    parser.add_argument(
        'confirm_password', type=str, required=True, help='confirm_password field is required', location='json')

    def post(self):
        data = Users.parser.parse_args()
        for input in data.values():
            if input == "":
                return make_response(jsonify({"error": "fields cannot be blank"})), 400
            username = data['username']
            email = data['email']
            password = data['password']
            confirm_password = data['confirm_password']

            db.save_user(username, email, password, confirm_password)
            return make_response(jsonify({"message": "user created successfully"}))
