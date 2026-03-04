from flask import Flask
from flask_restful import Resource, Api

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, world!"}, 200
