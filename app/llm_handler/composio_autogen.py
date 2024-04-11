import os
from autogen import AssistantAgent, UserProxyAgent
from composio_autogen import App, Action, ComposioToolset
from app.llm_handler.llm_config import super_agent, user_proxy


composio_tools = ComposioToolset()

composio_tools.register_tools(
    tools=[App.GITHUB], caller=super_agent, executor=user_proxy
)

# main function handler
def check_code_quality_and_commits(data):
    payload = data['payload']
    # for opened PRs getting PR URL to check standard checks and commit messages includes in the PR
    if payload['action'] == 'opened':
        pr_url = payload['url']

        code_quality_task = f"""Given the PR URL {pr_url}, review the file changes to ensure compliance with the following rules:
        No print statements allowed.
        Comments must accompany each added function.
        Eliminate unused variables.
        Ensure line lengths do not exceed 250 characters for readability.
        Enumerate valid and invalid steps accordingly.
        Additionally, examine commit messages within the same PR, ensuring they begin with keywords 'added' or 'removed' (case-insensitive) to denote actions taken.
        And create a issue on github with PR url if the PR doesnt compliant with these rules.
        "
        """

        response = user_proxy.initiate_chat(super_agent, message=code_quality_task)
        print("Response:",response.chat_history)

