#!flask/bin/python

import os

from flask import Flask, jsonify, abort, make_response, request

# app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

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


# def index():
#     return "Hello world"

