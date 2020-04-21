from flask import Flask, request
from flask_restful import Resource, Api
# adding the security options
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

'''
    section description>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    >>creating an api for item that deals with the following
    
    1.show all items
        endpoint : /items
    2.add an item
        endpoint : /item/<name>       method :POST
        data :{
        
        }
    3.show a specific item
        endpoint : /item/<name> method :GET
    4.delete a specific item
        endpoint : /item/<name>  method : DEL
    5.update a specific item
        endpoint : /item/<name> method : PUT
        data = {}   

'''
app = Flask(__name__)

# adding the secret key option to out app
app.secret_key = 'kia'
api = Api(app)
# creating the versatile database
items = [

]

# initializing JWT
jwt = JWT(app, authenticate, identity)  # create an /auth end point


class AlreadyExist(Exception):
    pass


class Item(Resource):
    @jwt_required()
    def get(self, name):  # return the specific item only
        for i in items:
            if i['name'] == name:
                return i
        return 'not found', 404

    def post(self, name):
        try:
            if next(filter(lambda x: x['name'] == name, items), None):
                raise AlreadyExist()
            data = request.get_json()
            items.append({'name': name, 'price': data['price']})
            return True, 201
        except AlreadyExist:
            return None, 400
        except Exception:
            return False, 404

    def put(self, name):
        pass


class Items(Resource):
    @jwt_required()
    def get(self):
        return items


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=5400, debug=True)
