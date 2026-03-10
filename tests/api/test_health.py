import unittest
from src.db.rebuild_schema import *
from tests.testingUtilities import *

#base_url = "http://127.0.0.1:5000"

class TestHealth(unittest.TestCase):

    def setUp(self):  
        rebuild_tables()

    def test_health_status(self):
        response = get_rest_call(self, "http://127.0.0.1:5000/health")       
        expected = {'status': 'ok'}
        self.assertEqual(expected, response, f"Health status not {expected}")


