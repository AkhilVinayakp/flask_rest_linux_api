from flask import Flask, jsonify, request

app = Flask(__name__)
'''
                        doc:::

    developing a online store
    store and items data 

    request:
    GET : to give the data back to the client
    POST : to get data from the client


    endpoints ( resources with associated functions HTTP verbs) :
    GET /store   : list all available stores
    POST /store {data :name} create a store 
    GET /store/<string:name> give data about a specific store
    POST /store/<string:name>/item  takes the item data about a specific store {name:,prince:}
    GET /store/<string:name>/item   gives info about the items in the specific store

    notes::::::::::::::
    jsonify : make json from a python dictionary

'''
# creating the store
store = [
    {
     'name': 'my_dream_store',
     'items':
        [
            {
                'name': 'item1',
                'price': 4.63
            }
        ]

    }
]


# POST /store {data :name} create a store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    store.append(new_store)
    return jsonify({'store': store})


# GET /store   : list all available stores
@app.route('/store', methods=['GET'])
def store_data():
    return jsonify({'stores': store})


# GET /store/<string:name> give data about a specific store
@app.route('/store/<string:name>')
def store_sp_data(name):
    for i in store:
        if name == i['name']:
            return jsonify({'store': i})
    return jsonify({'message': 'no store found'})


# POST /store/<string:name>/item  takes the item data about a specific store {name:,prince:}
@app.route('/store/<string:name>/item', methods=['POST'])
def get_item_store(name):
    request_data = request.get_json()
    for i in store:
        if i['store'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            i['items'].append(new_item)
            return jsonify({'stores': store})
    return jsonify({'message': "not found"})


# GET /store/<string:name>/item   gives info about the items in the specific store
@app.route('/store/<string:name>/item')
def pass_item_store(name):
    for i in store:
        if i['name'] == name:
            return jsonify({'items': i['items']})
    return jsonify({'message': "can not find the store specified"})


app.run(port=5500)
