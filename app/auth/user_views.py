from flask_restful import Resource, reqparse
import psycopg2
from app.api.v2.models.user_model import Users
# from app.db_config import url, cur, con
from flask_jwt_extended import create_access_token, jwt_refresh_token_required
from werkzeug.security import generate_password_hash, check_password_hash

url = "dbname='SendIT' host='localhost' port='5432' user='postgres' password='new1'"


# users=Users()
class Signup(Resource):
    # resource to signup a user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help='username  is required', location='json')

    parser.add_argument(
        'email', type=str, required=True, help='email  is required', location='json')

    parser.add_argument(
        'password', type=str, required=True, help='password is required', location='json')

    def post(self):
        data = Signup.parser.parse_args()
        # instantiate a user
        user = Users(data['username'], data['email'], data['password'])

        # check if the user with that username exists in the database
        if user.find_by_username(data['username']):
            return {'Message': 'username already registered by another user'}, 409
        new_user = Users(
            user_name=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password']))
        # print(new_user.password)
        new_user.signup()
        try:

            new_user.signup()
            return {
                       'message': 'User {} was created'.format(data['username'])

                   }, 201
        except:
            return {'message': 'something went wrong'}, 500



class Login(Resource):
    # resource to login a user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help='username  is required', location='json')
    parser.add_argument(
        'password', type=str, required=True, help='password  is required', location='json')

    def post(self):
        data = Login.parser.parse_args()
        user = Users(data['username'], data['password'])
        user = user.find_by_username(data['username'])
        # print(user)

        if not user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        if check_password_hash(user[3], data['password']):
            access_token = create_access_token(identity=data['username'])
            return {
                'message': 'Logged in as {}'.format(data['username']),
                'access_token': access_token
            }
        else:
            return {'Message': 'Invalid Username or Password'}, 401

