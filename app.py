from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Iris(Resource):
    def get(self):
        return {'message': 'iris ml model'}

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(Iris, '/iris')

if __name__ == '__main__':
    app.run()
