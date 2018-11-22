import unittest
import json
import sys
import os
import psycopg2
import psycopg2.extras
from app.db_config import drop_tables


from app.api.v2.models.parcel_model import Parcels
from app.api.v2.models.user_model import Users
from app import create_app

parcels = Parcels()
users = Users()
config = os.getenv('FLASK_ENV')
# inherit Testcase from unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config)
        self.client = self.app.test_client()

        self.test_create_user = {
            "username": "jj",
            "email": "jj@gmail.com",
            "password": "123j",
            "confirm_password": "123j"
         }
        self.test_login_user = {
            "username": "lona",
            "password": "123j"

        }
        self.create_parcel = {
            "name": "Malcolm",
            "phonenumber": 5678954321,
            "idnumber": 3456890,
            "location": "voi",
            "address": 3467134,
            "weight": 2,
            "price": 100,
            "user_id": 1
        }
        self.wrong_order = {
            "name": "Malcolm",
            "phonenumber": '56789xyz',
            "idnumber": 3456890,
            "location": 4444444,
            "address": 3467134,
            "weight": "",
            "user_id": "",
            "order_id": ""
        }
        self.change_destination = {
            "destination": "mombasa"
        }

        self.invalid_destination_details = {
            "destination": ''
        }
        self.cancel_unexisting_order = {
            "qwertytyui": ''
        }

    def register_normal__user(self):
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.test_create_user),content_type='application/json')
        resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.test_login_user),content_type='application/json')
        return resp["access_token"]


    def tearDown(self):
        pass

