import os

import json
from flask import Flask, jsonify, abort, make_response

from amazon import run_test, top3
import db_model as db

app = Flask(__name__)

@app.route('/products', methods = ['GET'])
def get_products():
	return make_response(jsonify( { 'error': "Specify input" } ), 200)

@app.route('/products/<string:keyword>/<string:callback>', methods = ['GET'])
def get_product(keyword, callback):
	if (not keyword) or (not callback):
		abort(404)
	results = run_test('All', keyword, 'Images, ItemAttributes, OfferSummary')
	results = json.dumps( results )
	result = callback + '(' + results + ');'
	return result

@app.route('/get_user/<string:fb_id>/<string:callback>', methods = ['GET'])
def get_user(fb_id, callback):
	if (not fb_id) or (not callback):
		abort(404)
	user_id = db.login(fb_id)
	result = json.dumps( user_id )
	result = callback + '(' + result + ');'
	return result

@app.route('/get_questions/<string:callback>', methods = ['GET'])
def get_questions(callback):
	if (not callback):
		abort(404)
	questions = db.get_questions()
	result = json.dumps( questions )
	result = callback + '(' + result + ');'
	return result

@app.route('/get_answers/<string:user_id>/<string:callback>', methods = ['GET'])
def get_answers(user_id, callback):
	if (not callback):
		abort(404)
	answers = db.get_answers(user_id)
	result = json.dumps( answers )
	result = callback + '(' + result + ');'
	return result

@app.route('/set_answer/<string:user_id>/<string:question_id>/<string:answer_text>/<string:callback>', methods = ['GET'])
def set_answer(user_id, question_id, answer_text, callback):
	if (not callback):
		abort(404)
	answers = db.set_answer(user_id, question_id, answer_text)
	result = json.dumps( answers )
	result = callback + '(' + result + ');'
	return result

@app.route('/delete_answer/<string:user_id>/<string:question_id>/<string:callback>', methods = ['GET'])
def delete_answer(user_id, question_id, callback):
	if (not callback):
		abort(404)
	response = db.delete_answer(user_id, question_id)
	result = json.dumps( response )
	result = callback + '(' + result + ');'
	return result

@app.route('/get_recs/<string:fb_id>/<string:callback>', methods = ['GET'])
def get_recs(fb_id, callback):
	if (not callback):
		abort(404)
	answers = db.get_answers_fb_id(fb_id)
	answers = answers['results']
	recs = []
	for answer in answers:
		rec = top3('All', answer['answer_text'], 'Images, ItemAttributes, OfferSummary')
		recs.append({'question_text': answer['answer_text'], 'recs': rec['results']})
	result = json.dumps( {'results': recs, 'status': 0} )
	result = callback + '(' + result + ');'
	return result

@app.route('/get_questions_without_answer/<string:user_id>/<string:callback>', methods = ['GET'])
def get_questions_without_answer(user_id, callback):
	if (not callback):
		abort(404)
	result = db.get_questions_without_answer(user_id)
	result = json.dumps( result )
	result = callback + '(' + result + ');'
	return result

# from amazonproduct import API
# from amazonproduct import NoExactMatchesFound
# api = API(locale='us', cfg='amazon-product-api.cfg')

# @app.route('/get_ids/<string:keyword>', methods = ['GET'])
# def get_ids(keyword):
# 	results = []
# 	try:
# 		items = api.item_search('All', Keywords= keyword, ResponseGroup='Images, ItemAttributes, OfferSummary')
# 		for item in items:     
# 			if (not (hasattr(item, 'ASIN'))):
# 			    continue   
# 			results.append({
#             		'source_id' : str(item.ASIN),
#                     'source': 'amazon'})
# 		results = { 'results': results }
# 	except NoExactMatchesFound, e:
# 		results = {'error': "NoExactMatchesFound"}
# 	return json.dumps(results);

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)

