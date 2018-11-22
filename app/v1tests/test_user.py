import unittest
import json
# fix import errors
import sys
import os

from app.tests.base_test import BaseTest


class TestUser(BaseTest):

    def test_create_user(self):
        resp = self.client.post('/api/v1/users', data=json.dumps(self.test_create_user), content_type='application/json')
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
