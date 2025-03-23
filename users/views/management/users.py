from flask import request, jsonify
from users import app


@app.route("/users", methods=['POST'])
def create():
    return jsonify({'message': 'Create user'})

@app.route("/users/<int:user_id>", methods=['GET'])
def read():
    return jsonify({'message': 'Read user'})

@app.route("/users/<int:user_id>", methods=['PUT', 'PATCH'])
def edit():
    return jsonify({'message': 'Update user'})

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete():
    return jsonify({'message': 'Delete user'})

@app.route("/users/", methods=['GET'])
def list():
    return jsonify({'message': 'List users'})
