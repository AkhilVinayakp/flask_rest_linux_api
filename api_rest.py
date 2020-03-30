from flask import Flask,jso
from flask_restful import Api, Resource
import request
import os
import subprocess
app = Flask(__name__)
api = Api(app)

# adding a class that will resolve according to that


class Hello_world(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Hello_world, '/')


if __name__ == '__main__':
    app.run(debug='true')
