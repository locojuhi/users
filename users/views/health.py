from flask import request, jsonify
from users import app


@app.route("/ping", methods=['GET'])
def hello_world():
    return jsonify({'message': 'pong'})
