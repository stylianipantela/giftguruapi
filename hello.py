import os

from flask import Flask, jsonify
from amazon import run_test


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    # return jsonify( { 'tasks': tasks } )
    return jsonify( { 'results': run_test('Toys', 'Rocket', 'Images, ItemAttributes, OfferSummary') })

if __name__ == '__main__':
    app.run(debug = True)

