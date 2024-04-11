from flask import Flask, request
from app.routes import hello_route, handle_trigger_endpoint
from composio import Composio

client = Composio("9qi05clkeqxtudolljveh") 

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def get_hello():
    return hello_route()

@app.route('/webhook/trigger', methods=['POST'])
def handler_trigger():
    return handle_trigger_endpoint()


if __name__ == '__main__':
    app.run(debug=True)