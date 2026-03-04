from flask import Flask
from flask_restful import Resource, Api
from db.db_utils import exec_get_one

class DbPing(Resource):
    def get(self):
        row = exec_get_one("SELECT 1;")
        return {"db": "ok", "result": row[0]}, 200