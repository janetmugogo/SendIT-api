import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from app.tests.base_test import BaseTest



class TestParcel(BaseTest):

    def test_create_order(self):
        access_token = self.register_normal_user()
        response = self.client.post('/api/v2/create_parcel', data=json.dumps(self.test_create_parcel),
            headers = {content_type:'application/json','Authorization':'Bearer {}'.format(access_token)})
        self.assertEqual(response.status_code, 201)

    # def test_create_invalid_order(self):
    #         response = self.client.post('/api/v2/create_parcel', data=json.dumps(self.wrong_order),
    #                                     content_type='application/json')
    #         self.assertEqual(response.status_code, 400)
    #
    # def test_get_orders(self):
    #         self.client.post('/api/v2/create_parcel', data=json.dumps(self.test_parcel), content_type='application/json')
    #         response = self.client.get('/api/v1/parcels')
    #         self.assertEqual(response.status_code, 200)
    #
    # def test_get_nonexisting_orders(self):
    #         response = self.client.get('/api/v2/create_parcel')
    #         self.assertIn("There are no created orders", str(response.data))
    #
    # def test_get_char_insteadof_integer(self):
    #         response = self.client.get('/api/v1/create_parcel/Hello')
    #         self.assertEqual(response.status_code, 404)
    #
    # def test_cancel_order(self):
    #         response = self.client.post('/api/v2/create_parcel', data=json.dumps(self.test_parcel),
    #                                     content_type='application/json')
    #         self.assertEqual(response.status_code, 201)
    #         response = self.client.put('/api/v2/parcels/1/cancel')
    #         self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()