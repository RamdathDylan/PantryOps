from flask import Flask
from flask_restful import Resource, Api
from api.health import Health
from api.helloWorld import HelloWorld
from api.managment import DbPing

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Health, "/")
    api.add_resource(HelloWorld, "/hello")
    api.add_resource(DbPing, "/managment/dbping")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=4999, debug=True)    