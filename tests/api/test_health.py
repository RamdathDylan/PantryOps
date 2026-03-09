import unittest
import requests

class TestDBSchema(unittest.TestCase):

    base_url = "http://127.0.0.1:5000"

    def test_health_status(self):
        response = requests.get(self.base_url+"/health")
        expected_code = 200
        self.assertEqual(expected_code, response.status_code, f'Response code to {self.base_url}/health not {expected_code}')
