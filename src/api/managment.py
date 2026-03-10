from flask import Flask
from flask_restful import Resource, Api
from src.db.db_utils import exec_get_one

class DbPing(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))
    