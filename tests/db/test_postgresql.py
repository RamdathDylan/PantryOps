import unittest
from src.db.rebuild_schema import *
from tests.testingUtilities import *

#base_url = "http://127.0.0.1:5000"

class TestPostgreSQL(unittest.TestCase):

    def setUp(self):  
            rebuild_tables()

    def test_can_connect(self):
        version = get_rest_call(self, 'http://127.0.0.1:5000/managment/dbping')
        self.assertTrue(version[0].startswith('PostgreSQL'))