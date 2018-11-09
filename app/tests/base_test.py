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
        self.test_parcel = {"name": "username", "phonenumber": "5678954321", "idnumber": "3456890",
                            "location": "nairobi", "address": "3467134", "weight": "2"}
        self.cancel_order = {"status":"cancelled"}
        self.change_destination  = {"destination":"mombasa"}
        self.test_create_user =  {"username":"malcolm","email":"malcolm@gmail.com","password":"1234","confirm_password":"1234"}

    def tearDown(self):
        parcels.db.clear()
