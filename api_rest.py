from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
class Hello_world(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(Hello_world,'/')
if __name__=='__main__':
    app.run(debug='true')