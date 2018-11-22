import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.api.v1.models.parcel_model import Parcels
from app.api.v1.models.user_model import Users
from app import create_app

parcels = Parcels()
users = Users()

# inherit Testcase from unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.test_create_parcel = {
            "name": "Malcolm",
            "phonenumber":5678954321,
            "idnumber": 3456890,
            "location": "voi",
            "address": 3467134,
            "weight": 2,
            "price": 100,
            "user_id":1
            }
        self.wrong_order = {
            "name": "Malcolm",
            "phonenumber": '56789xyz',
            "idnumber": 3456890,
            "location": 4444444,
            "address": 3467134,
            "weight": "",
            "user_id":"",
            "order_id": ""
        }
        self.change_destination  = {
            "destination":"mombasa"
        }
        self.test_create_user =  {
            "username":"malcolm",
            "email":"malcolm@gmail.com",
            "password":"1234_xyz",
            "confirm_password":"1234_xyz"
        }
        self.invalid_destination_details = {
            "destination":''
        }
        self.cancel_unexisting_order = {
            "qwertytyui":''
        }

    def tearDown(self):
        parcels.db.clear()
