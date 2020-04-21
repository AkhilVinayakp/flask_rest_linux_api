from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# adding the security options
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from werkzeug.security import safe_str_cmp

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
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help="this field required")
        data = parser.parse_args()
        item = next(filter(lambda x: safe_str_cmp(x['name'], name), items), None)
        if item is None:
            items.append({'name': name, 'price': data['price']})
        else:
            item.update(data)
        return item

    # method to delete an item in the list

    def delete(self, name):
        global items
        rmd_item = next(filter(lambda x: safe_str_cmp(x['name'], name), items), None)
        if rmd_item is not None:
            items.remove(rmd_item)
            return {'message': "Item with name {} removed".format(rmd_item)}
        else:
            return {'message': "There is not item with the name{} ".format(name)}


class Items(Resource):
    def get(self):
        return items


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=5400, debug=True)
