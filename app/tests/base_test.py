import unittest
from app import create_app
import json
import sys
import os
import psycopg2
import psycopg2.extras
from app.db_config import drop_tables,create_tables


from app.api.v2.models.parcel_model import Parcels
from app.api.v2.models.user_model import Users

config = os.getenv("FLASK_ENV")

parcels = Parcels()
users = Users()

# inherit Testcase from unittest
class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        create_tables()
        # print(config)
        self.client = self.app.test_client()

        self.register_user = {
            "username": "melany",
            "email": "melany@gmail.com",
            "password": "123j",
            "confirm_password": "123j"
         }
        self.login_user = {
            "username": "melany",
            "password": "123j"

        }
        self.wrong_login_user = {
            "username": "juzi",
            "password": "123j"

        }
        self.create_parcel = {
            "user_id": '1',
            "sender_name": "Melody",
            "phone_number": 5678954321,
            "id_number": 3456890,
            "location": "kenya",
            "address": 3467134,
            "weight": 2,
            "destination":"tanzania"
        }
        self.invalid_order = {
            "user_id":"700",
            "sender_name": "Malcolm",
            "phone_number": '56789xyz',
            "id_number": 3456890,
            "location": 4444444,
            "address": 3467134,
            "weight": "",
            # "user_id": ""
            # "order_id": ""
        }
        self.change_destination = {
            "destination": "mombasa"
        }

        # self.invalid_destination_details = {
        #     "destination": ''
        # }
        self.cancel_unexisting_order = {
            "qwertytyui": ''
        }





    def tearDown(self):
        drop_tables()




