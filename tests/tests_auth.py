import unittest
from app import create_app

class AuthClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login_success(self):
        response = self.client.post('/auth/login', json={
            "username": "user",
            "password": "password"
        })
        self.assertEqual(response.status_code, 200)

    def test_login_failure(self):
        response = self.client.post('/auth/login', json={
            "username": "user",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
