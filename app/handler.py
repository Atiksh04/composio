from flask import jsonify

def get_hello_handler():
    return jsonify({'message': 'Hello, World!'})