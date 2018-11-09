import unittest
import json
from .base_test import BaseTest


class TestParcel(BaseTest):

    def test_create_order(self):
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.test_parcel), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_get_order(self):
        resp = self.client.get('/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)
