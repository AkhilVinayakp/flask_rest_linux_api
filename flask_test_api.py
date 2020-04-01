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

app.run(port=5500)
