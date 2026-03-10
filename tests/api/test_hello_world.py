import unittest
from src.db.rebuild_schema import *
from tests.testingUtilities import *

#base_url = "http://127.0.0.1:5000"

class TestHelloWorld(unittest.TestCase):

    def setUp(self):  
        rebuild_tables()
        
    def test_hello_world(self):
        response = get_rest_call(self, 'http://127.0.0.1:5000/hello')
        expected = {"message": "Hello, world!"}
        self.assertEqual(expected, response, f"Hello world test response was not {expected}")
