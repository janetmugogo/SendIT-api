import unittest
import json
# fix import errors
import sys
import os

from app.tests.base_test import BaseTest


class TestUser(BaseTest):

    def test_register_user(self):
        resp = self.client.post('/api/v2/auth/signup', json=self.register_user)
        self.assertEqual(resp.status_code, 201)

    def test_inexistent_user(self):
        self.client.post('/api/v2/auth/signup', json=self.register_user)
        resp = self.client.post('/api/v2/auth/login', json=self.wrong_login_user)
        self.assertEqual(resp.status_code, 403)
    def test_login_user(self):
        self.client.post('/api/v2/auth/signup', json=self.register_user)
        resp = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('access_token', str(resp.data))




if __name__ == '__main__':
     unittest.main()
