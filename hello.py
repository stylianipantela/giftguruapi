import os

import json
from flask import Flask, jsonify, abort, make_response

from amazon import run_test
# from db_model import get_users

app = Flask(__name__)

@app.route('/products', methods = ['GET'])
def get_products():
	return make_response(jsonify( { 'error': "Specify input" } ), 200)

@app.route('/products/<string:keyword>/<string:callback>', methods = ['GET'])
def get_product(keyword, callback):
	if (not keyword) or (not callback):
		abort(404)
	results = run_test('All', keyword, 'Images, ItemAttributes, OfferSummary')
	results = json.dumps( { 'results': results } )
	result = callback + '(' + results + ');'
	# return make_response(jsonify( { 'result': "Specify input3" } ), 200)
	return result

# @app.route('/users', methods = ['GET'])
# def get_users():
#     return jsonify( { 'results': get_users() })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)

