import unittest
import sys
import os

import json
from app.tests.base_test import BaseTest


class TestParcel(BaseTest):


    def test_create_order(self):
        data = {
            "username": "melody",
            "email": "melody@gmail.com",
            "password": "123j",
            "confirm_password": "123j"
                }
        response = self.client.post("api/v2/auth/signup", json=self.register_user)
        response= self.client.post("api/v2/auth/login", json=data)
        data = json.loads(response.get_data(as_text=True))
        access_token = data['data']['access_token']
        res = self.client().post("api/v2/parcels", json=self.create_parcel, headers=dict(Authorization="Bearer " + token))
        self.assertEqual(res.status_code, 201)
        self.assertIn("order created", str(res.data))

    # def test_create_invalid_order(self):
    #     response = self.client.post('/api/v2/parcels', data=json.dumps(self.wrong_order),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #
    # def test_get_orders(self):
    #     self.client.post('/api/v2/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
    #     response = self.client.get('/api/v2/parcels' )
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_get_nonexisting_orders(self):
    #      response = self.client.get('/api/v2/parcels')
    #      self.assertIn("There are no created orders", str(response.data))
    #
    #
    # def test_get_char_insteadof_integer(self):
    #     response = self.client.get('/api/v2/parcels/Hello')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_cancel_order(self):
    #     response = self.client.post('/api/v2/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     response = self.client.put('/api/v2/parcels/1/cancel')
    #     self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
