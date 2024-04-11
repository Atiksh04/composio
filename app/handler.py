from flask import jsonify
from app.llm_handler.composio_autogen import trigger_task

def get_hello_handler():
    trigger_task()
    return jsonify({'message': 'Hello, World!'})