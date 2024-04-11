from flask import Flask
from app.routes import hello_route

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def get_hello():
    return hello_route()

if __name__ == '__main__':
    app.run(debug=True)