import os

from flask import Flask, jsonify, abort, make_response
from amazon import run_test

app = Flask(__name__)

@app.route('/products', methods = ['GET'])
def get_products():
    # return jsonify( { 'tasks': tasks } )
    return jsonify( { 'results': run_test('Toys', 'Rocket', 'Images, ItemAttributes, OfferSummary') })


@app.route('/products/<string:keyword>', methods = ['GET'])
def get_product(keyword):
    keyword = filter(lambda t: t['keyword'] == keyword, products)
    if not keyword:
        abort(404)
    return jsonify( { 'results': run_test('Toys', keyword, 'Images, ItemAttributes, OfferSummary') } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)

