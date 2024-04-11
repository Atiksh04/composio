from app.handler import get_hello_handler

def hello_route():
    return get_hello_handler()

def handle_trigger_endpoint():
    print ("asdas")