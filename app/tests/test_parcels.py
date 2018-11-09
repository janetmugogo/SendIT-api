import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from app.tests.base_test import BaseTest



class TestParcel(BaseTest):

    def test_create_order(self):
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_get_order(self):
        resp = self.client.get('/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_order(self):
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        response = self.client.put('/api/v1/parcels/1/cancel', data=json.dumps(self.cancel_order),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_change_destination(self):
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        response = self.client.put('/api/v1/parcels/1/changedestination', data=json.dumps(self.change_destination),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
