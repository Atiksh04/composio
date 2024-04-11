from flask import jsonify, make_response, request
from app.llm_handler.composio_autogen import check_code_quality_and_commits

# handling the trigger
def trigger_handler():
    response_data = {}  
    status_code = 200  

    payload = request.json

    if "trigger_name" in payload: 
        trigger_type = payload['trigger_name']
        # handling for pull request event
        if trigger_type == "github_pull_request_event":
            check_code_quality_and_commits(payload)


    return make_response(jsonify(response_data), status_code)
