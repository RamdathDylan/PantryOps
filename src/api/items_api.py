from flask import Flask
from flask_restful import Resource, Api
from src.db.items import *

class Items(Resource):
    def get(self):
        items = get_all_items()
        return items
