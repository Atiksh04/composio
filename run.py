from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, make_response
from app.routes import  handle_trigger_endpoint
from composio import Composio

load_dotenv()

client = Composio(os.environ["COMPOSIO_KEY"]) 

app = Flask(__name__)

# defining a dummy home route
@app.route('/', methods=['GET'])
def get_hello():
    response_data = {}  
    status_code = 200  
    return make_response("PR code review", status_code)

# defining route for webhook trigger
@app.route('/webhook/trigger', methods=['POST'])
def handler_trigger():
    return handle_trigger_endpoint()


if __name__ == '__main__':
    app.run(debug=True)