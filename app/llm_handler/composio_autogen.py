import os
from autogen import AssistantAgent, UserProxyAgent
from composio_autogen import App, Action, ComposioToolset
from app.llm_handler.llm_config import super_agent, user_proxy


composio_tools = ComposioToolset()

composio_tools.register_tools(
    tools=[App.GITHUB], caller=super_agent, executor=user_proxy
)


task = """star the repository named:"composio" """


def trigger_task():
    response = user_proxy.initiate_chat(super_agent, message=task)
    print(response.chat_history)