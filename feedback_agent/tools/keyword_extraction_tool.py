from typing import List
from autogen import AssistantAgent
from feedback_agent.config import LLM_CONFIG

def extract_keywords(inputs: List[str]) -> List[str]:
    agent = AssistantAgent(
        name="Keyword Extraction Agent",
        system_message="You are a helpful AI assistant. "

                        "You can extract keywords from a list of customer feedbacks. "
                        "Input will be a list of feedback strings. "
                        "You must return a list (JSON array) of lists of keywords in the same order as the inputs. "
                        "Each list of keywords should contain the most relevant keywords from the corresponding feedback. "
                        "Provide the result in this exact format: [[\"keyword1\", \"keyword2\"], [\"keyword1\", \"keyword2\"], ...]. "
                        "Example result: [[\"love\", \"product\"], [\"great\", \"experience\"], [\"bad\", \"service\"]]. "
                        "Do not include any other text, explanation, or metadata. "
                        "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    reply = agent.generate_reply(
        messages=[
            {"role": "user", "content": f'extract keywords from the following feedbacks: {inputs}'}
        ],
    )
    if reply and isinstance(reply, list):
        return reply
    
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