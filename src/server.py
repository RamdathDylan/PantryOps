from flask import Flask
from flask_restful import Resource, Api

from src.api.items_api import Items
from src.api.managment import DbPing
from src.api.health import Health
from src.api.helloWorld import HelloWorld

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Health, "/health")
    api.add_resource(HelloWorld, "/hello")
    api.add_resource(DbPing, "/managment/dbping")
    api.add_resource(Items, "/items")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)    