from typing import List
from autogen import AssistantAgent
from feedback_agent.config import LLM_CONFIG

def categorize_feedback(feedback: List[str]) -> List[str]:
    agent = AssistantAgent(
        name="Categorization Agent",
        system_message="You are a helpful AI assistant. "
                      "You can categorize customer feedback into themes. "
                      "Given a customer feedback, you can use the categorization tool to categorize the feedback. "
                      "You will provide a list of themes in the following format: '[theme1, theme2, ...]'. "
                      "Example result: '[usability, performance]'. "
                      "Don't include any other text in your response."
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    reply = agent.generate_reply(
        messages=[
            {"role": "user", "content": f'categorize the following feedback into themes: {feedback}'}
        ],
    )

    if not reply:
        raise ValueError("No reply found")

    reply_value = ""
    if isinstance(reply, dict):
        reply_content = reply["content"]
        if reply_content:
            reply_value = reply_content
        else:
            raise ValueError("No content found in the reply")
    else:
        reply_value = reply


    return reply_value