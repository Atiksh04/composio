import os
from autogen import AssistantAgent, UserProxyAgent
from composio_autogen import App, Action, ComposioToolset
from app.llm_handler.llm_config import super_agent, user_proxy


composio_tools = ComposioToolset()

composio_tools.register_tools(
    tools=[App.GITHUB], caller=super_agent, executor=user_proxy
)


task = """star the repository named:"composio" """

# something
def trigger_task():
    response = user_proxy.initiate_chat(super_agent, message=task)
    print(response.chat_history)

# something2
def check_code_quality(data):
    print(data)
    payload = data['payload']
    if payload['action'] == 'open':
        pr_url = payload['action']['url']
        print('-pr-url-', pr_url)

        task = f"""For this PR URL: {PR_URL}. Check all the file 
        changes that are made and these changes used comply these rules: 
        any print statements should not be present, comments should be 
        added for each function added, unused variables shouldn't be
        present and length of any line shouldn't be more than 250 
        characters to ensure readibility. Mention all the rules these
        code changes are ensuring or not ensuring
        """

        response = user_proxy.initiate_chat(super_agent, message=task)
        print(response.chat_history)




def check_commit_name(data):
    print(data)
