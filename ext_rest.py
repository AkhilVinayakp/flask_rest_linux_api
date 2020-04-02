from flask import Flask, jsonify
from flask_restful import Resource, Api
'''
    section description>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    >>creating an api for item that deals with the following
    
    1.show all items
        endpoint : /items
    2.add an item
        endpoint : /items       method :POST
        data :{
        
        }
    3.show a specific item
        endpoint : /items/<name> method :GET
    4.delete a specific item
        endpoint : /items/<name>  method : DEL
    5.update a specific item
        endpoint : /item/<name> method : PUT
        data = {}   

'''