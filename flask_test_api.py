from flask import Flask

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



'''


# POST /store {data :name} create a store
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store   : list all available stores
@app.route('/store', methods=['GET'])
def store_data():
    pass


# GET /store/<string:name> give data about a specific store
@app.route('/store/<string:name')
def store_sp_data(name):
    pass


# POST /store/<string:name>/item  takes the item data about a specific store {name:,prince:}
@app.route('/store/<string:name>/item', methods= ['POST'])
def get_item_store(name):
    pass


# GET /store/<string:name>/item   gives info about the items in the specific store
@app.route('/store/<string:name>/item')
def pass_item_store(name):
    pass


app.run(port=5500)
