from dotenv import load_dotenv
import os

from autogen import AssistantAgent, UserProxyAgent

# llm config
llm_config = {
    "config_list": [
        {
            "model": "gpt-4-1106-preview",
            "api_key": os.environ.get(
                "OPENAI_SECRET", "sk-123131****"
            ),
        }
    ]
}

super_agent = AssistantAgent(
    "chatbot",
    system_message="""You are a super intelligent personal assistant.
    You have been given a set of tools that you are supposed to choose from.
    You decide the right tool and execute it to achieve your task.
    Reply TERMINATE when the task is done or when user's content is empty""",
    llm_config=llm_config,
)


user_proxy = UserProxyAgent(
    "user_proxy",
    is_termination_msg=lambda x: x.get("content", "")
    and "TERMINATE" in x.get("content", ""),
    human_input_mode="NEVER", 
    code_execution_config={"use_docker": False},
)
