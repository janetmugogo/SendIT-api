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
        resp = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertEqual(resp.status_code, 400)



if __name__ == '__main__':
     unittest.main()
