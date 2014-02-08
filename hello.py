import os

from flask import Flask, jsonify, abort, make_response
from amazon import run_test
# from db_model import get_users

app = Flask(__name__)

@app.route('/products', methods = ['GET'])
def get_products():
	return make_response(jsonify( { 'error': "Specify input" } ), 200)

@app.route('/products/<string:keyword>', methods = ['GET'])
def get_product(keyword):
	if not keyword:
		abort(404)
	results = run_test('All', keyword, 'Images, ItemAttributes, OfferSummary')
	return make_response(jsonify( { 'results': results } ), 200)


# @app.route('/users', methods = ['GET'])
# def get_users():
#     return jsonify( { 'results': get_users() })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)

