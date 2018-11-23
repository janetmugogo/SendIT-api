from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_refresh_token_required,jwt_required, get_jwt_identity
from app.utilities.validation import check_email


from app.api.v2.models.user_model import Users

class Signup(Resource):
    # resource for a user to signup
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help='username  is required', location='json')
    parser.add_argument(
        'email', type=str, required=True, help='email  is required', location='json')

    parser.add_argument(
        'password', type=str, required=True, help='password is required', location='json')

    def post(self):
        data = Signup.parser.parse_args()
        user = Users(data['username'], data['email'], data['password'])
        if not check_email(data['email']):
            return  {'Message': 'Invalid email'}, 401
        # instantiate a user

        # if user.find_by_username(data['username']):
        #     # check if the user with that username exists in the database
        #     return {'Message': 'username already registered by another user'}, 409
        new_user = Users(
            user_name=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password']))

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
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 401
        if check_password_hash(user[3], data['password']):
            access_token = create_access_token(identity=[data['username']])
            return {
                'message': 'Logged in as {}'.format(data['username']),
                'access_token': access_token
            }, 200
        else:
            return {'Message': 'Invalid Username or Password'}, 401
class AdminRoute(Resource):
    # resource for a user to signup
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help='username  is required', location='json')
    parser.add_argument(
        'email', type=str, required=True, help='email  is required', location='json')

    parser.add_argument(
        'password', type=str, required=True, help='password is required', location='json')

    def post(self):
        data = Signup.parser.parse_args()
        user = Users(data['username'], data['email'], data['password'])
        if not check_email(data['email']):
            return {'Message': 'Invalid email'}, 401
        new_user = Users(
            user_name=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password']))

        new_user.admin()
        try:

            new_user.admin()
            return {
                       'message': 'User {} was created'.format(data['username'])

                   }, 201
        except:
            return {'message': 'something went wrong'}, 500
