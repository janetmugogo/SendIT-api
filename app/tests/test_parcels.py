import unittest
import sys
import os

import json
from app.tests.base_test import BaseTest
import pdb

class TestParcel(BaseTest):



    def test_create_invalid_order(self):
        resp = self.client.post('/api/v2/auth/signup', json=self.register_user)
        resp = self.client.post('/api/v2/auth/login', json=self.login_user)
        data = json.loads(resp.get_data(as_text=True))
        token = data['access_token']
        response = self.client.post('/api/v2/create_parcel', data=json.dumps(self.invalid_order),
                                    content_type='application/json',  headers=dict(Authorization="Bearer " + token))
        self.assertEqual(response.status_code, 400)



    def test_cancel_order(self):
        response = self.client.post('/api/v2/create_parcel', data=json.dumps(self.cancel_unexisting_order ), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.put('/api/v2/get_parcel/1/cancel')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
