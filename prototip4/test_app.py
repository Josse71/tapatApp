import unittest
from app import app  # Asegúrate de importar tu archivo Flask

class TestWebServices(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_valid_user(self):
        response = self.app.post('/login', json={"username": "mare", "password": "12345"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def test_login_invalid_user(self):
        response = self.app.post('/login', json={"username": "invalid", "password": "wrong"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["coderesponse"], "0")

    def test_get_children(self):
        response = self.app.post('/child', json={"iduser": 1})
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json["children"]), 0)

    def test_get_taps(self):
        response = self.app.post('/taps', json={"idchild": 1})
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json["taps"]), 0)

    def test_get_taps_no_taps(self):
        response = self.app.post('/taps', json={"idchild": 99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["taps"]), 0)

if __name__ == '__main__':
    unittest.main()
