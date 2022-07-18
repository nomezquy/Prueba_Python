from unittest import result
from flask import Flask, jsonify
from data import data
from response import generate_response

app = Flask(__name__)
dataOrders = data

@app.route('/')
def default_response():
    response = generate_response(result= True, message="EndPoint incompleto")    
    return jsonify(response)

@app.route('/Orders')
def return_all_orders():
    response = generate_response(result=True, message="", response=dataOrders)
    return jsonify(response)

@app.route('/Orders/<id>')
def search_order(id):
    for order in dataOrders:
        if order.get('id') == id:
            response = generate_response(result=True, message="", response=order)            
            return jsonify(response)

app.run(port=9001)
