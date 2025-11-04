from typing import List, Literal, Union
from autogen import AssistantAgent
from feedback_agent.config import LLM_CONFIG

SENTIMENT_VALUES = {"positive", "negative", "neutral"}

def analyze_sentiment(inputs: List[str]) -> Union[Literal["positive"], Literal["negative"], Literal["neutral"]]:
    agent = AssistantAgent(
        name="Sentiment Analysis Agent",
        system_message=(
            "You are a helpful AI assistant. "
            "You can analyze the sentiment of a list of customer feedbacks. "
            "Input will be a list of feedback strings. "
            "You must return a list (JSON array) of sentiments in the same order as the inputs. "
            "Each sentiment must be one of: 'positive', 'negative', or 'neutral' (lowercase). "
            "Provide the result in this exact format: [\"sentiment1\", \"sentiment2\", ...]. "
            "Example result: [\"positive\", \"neutral\", \"negative\"]. "
            "Do not include any other text, explanation, or metadata. "
            "Return 'TERMINATE' when the task is done."
        ),
        llm_config=LLM_CONFIG,
    )
    reply = agent.generate_reply(
        messages=[
            {"role": "user", "content": f'analyze the sentiment of the following feedbacks: {inputs}'}
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