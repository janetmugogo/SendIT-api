import unittest
import json
# fix import errors
import sys
import os

from app.v2tests.base_test import BaseTest


class TestUser(BaseTest):

    def test_create_user(self):
        pass
    #     resp = self.client.post('/api/v2/auth/signup', data=json.dumps(self.test_create_user), content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)

    # def test_login_user(self):
    #     resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.test_login_user), content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)





if __name__ == '__main__':
     unittest.main()
