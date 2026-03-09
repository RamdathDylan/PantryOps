import unittest
from tests.testingUtilities import *
class TestDBSchema(unittest.TestCase):

    #base_url = "http://127.0.0.1:5000"

    def test_health_status(self):
        response = get_rest_call(self, "http://127.0.0.1:5000/health")       
        expected = {'status': 'ok'}
        self.assertEqual(expected, response)
