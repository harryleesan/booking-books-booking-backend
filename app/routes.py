from app import app, db, metrics
from flask import Flask, jsonify, abort, make_response, request
from app.models import User, Booking
from sqlalchemy.sql.expression import and_
import requests

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not Found'}), 404)


# @app.route('/api/1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})

# @app.route('/api/1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})

# @app.route('/api/1.0/tasks', methods=["POST"])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201

@app.route('/api/1.0/create/user', methods=["POST"])
def create_user():
    if not request.json or not 'first_name' in request.json or not 'last_name' in request.json:
        abort(400)
    u = User(first_name=request.json['first_name'], last_name=request.json['last_name'])
    db.session.add(u)
    db.session.commit()
    u_id = User.query.filter_by(first_name=request.json['first_name']).first().id
    return jsonify({'message': "User created with id {0}".format(u_id)}), 201

@app.route('/api/1.0/create/booking', methods=["POST"])
def create_booking():
    if not request.json or not 'book_id' in request.json or not 'user_id' in request.json or not 'start_date' in request.json or not 'end_date' in request.json:
        abort(400)
    u = User.query.get(int(request.json['user_id']))
    b_id = request.json['book_id']
    if not u or not b_id:
        abort(500)
    book_id_api = requests.get("http://host.docker.internal:8080/book/id/{0}".format(b_id))
    if book_id_api.status_code != 200:
        abort(500)
    book_id = book_id_api.json()
    b = Booking(book_id=book_id["id"], booker=u, start_date=request.json["start_date"], end_date=request.json["end_date"])
    db.session.add(b)
    db.session.commit()
    return jsonify({'message': 'Booking completed'}), 201

@app.route('/api/1.0/get/booking', methods=["POST"])
def get_booking():
    if not request.json or not 'start_date' in request.json or not 'end_date' in request.json:
        abort(400)
    b = Booking.query.filter(and_(Booking.start_date >= request.json["start_date"], Booking.end_date <= request.json["end_date"])).all()
    return jsonify(bookings=[i.serialize for i in b]), 200

