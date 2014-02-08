import os

from flask import Flask, jsonify, abort, make_response
from amazon import run_test
# from db_model import get_users

app = Flask(__name__)

results = [
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/410qw8Bt8AL.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-1469-Tandem-X-Launch-Set/dp/B002VLP67S%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB002VLP67S", 
      "price": "$19.87", 
      "title": "Estes 1469 Tandem-X Launch Set"
    }];

@app.route('/products', methods = ['GET'])
def get_products():
	return make_response(jsonify( { 'results': results } ), 200)


@app.route('/products/<string:keyword>', methods = ['GET'])
def get_product(keyword):
    keyword = filter(lambda t: t['keyword'] == keyword, products)
    if not keyword:
        abort(404)
	return make_response(jsonify( { 'results': results } ), 200)


# @app.route('/users', methods = ['GET'])
# def get_users():
#     return jsonify( { 'results': get_users() })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)

