import unittest
from tests.testingUtilities import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        version = get_rest_call(self, 'http://127.0.0.1:5000//managment/dbping')
        self.assertTrue(version[0].startswith('PostgreSQL'))