import unittest
from app.api.v1.models.parcel_model import Parcels

parcels = Parcels()
"""inherit Testcase from unittest"""
from app import create_app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_parcel = {"name": "username", "phonenumber": "5678954321", "idnumber": "3456890",
                            "location": "nairobi", "address": "3467134", "weight": "2"}

    def tearDown(self):
        parcels.db.clear()
