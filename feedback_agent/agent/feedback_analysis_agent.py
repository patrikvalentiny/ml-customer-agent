import json
from pprint import pprint
from autogen import ConversableAgent
from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.categorization_tool import categorize_feedback
from feedback_agent.tools.keyword_extraction_tool import extract_keywords
from feedback_agent.config import LLM_CONFIG

def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="""You are a helpful AI assistant. 
You can perform sentiment analysis on customer feedback. 
You can read customer feedback using the feedback_reader tool. It will return a list of feedback, that consists of id, text, and source. 
Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. 
You can also categorize the feedback into themes using the categorization tool. 
You can also extract keywords from the feedback using the keyword_extraction tool. 
Return valid JSON objects from both sentiment analysis, categorization and keyword extraction as the final output, MAKE SURE the key of each object matches the tool used. 
Example final output:
{
  "sentiment_analysis": [
    {"id": "1", "sentiment": "positive"},
    {"id": "2", "sentiment": "negative"}
  ],
  "categorization": [
    {"id": "1", "themes": ["usability", "design"]},
    {"id": "2", "themes": ["performance", "reliability"]}
  ],
  "keyword_extraction": [
    {"id": "1", "keywords": ["love", "product"]},
    {"id": "2", "keywords": ["great", "product"]}
  ]
}
Return 'TERMINATE' at the end of last response when the task is done.""",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
    agent.register_for_llm(name="sentiment_analysis", description="Analyze the sentiment of a customer feedback")(analyze_sentiment)
    agent.register_for_llm(name="categorization", description="Categorize feedback into themes")(categorize_feedback)
    agent.register_for_llm(name="keyword_extraction", description="Extract keywords from a customer feedback")(extract_keywords)

    return agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="feedback_reader")(query_feedback)
    user_proxy.register_for_execution(name="sentiment_analysis")(analyze_sentiment)
    user_proxy.register_for_execution(name="categorization")(categorize_feedback)
    user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
    return user_proxy


def main():
    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()
    result = user_proxy.initiate_chat(
        feedback_analysis_agent, 
        message="""
                1. Read feedback from the feedback store, using the feedback_reader tool, only call the function once.
                2. Take all the inputs and analyze the sentiment using the sentiment_analysis tool.
                3. Create a JSON object that contains the feedback id and the analyzed sentiment.
                Example:
                [
                    {"id": "1", "sentiment": "positive"},
                    {"id": "2", "sentiment": "negative"},
                    {"id": "3", "sentiment": "neutral"}
                ]
                4. Take all the feedback and categorize the feedback into themes using the categorization tool.
                5. Create a JSON object that contains the feedback id and the list of themes.
                Example:
                [
                    {"id": "1", "themes": ["usability", "design"]},
                    {"id": "2", "themes": ["performance", "reliability"]},
                    {"id": "3", "themes": ["customer service"]}
                ]
                6. Extract keywords from all the feedback using the keyword_extraction tool.
                7. Create a JSON object that contains the feedback id and the list of keywords.
                Example:
                [
                    {"id": "1", "keywords": ["love", "product"]},
                    {"id": "2", "keywords": ["great", "product"]},
                    {"id": "3", "keywords": ["great", "experience", "product"]}
                ]
                8. Return a valid JSON objects from both sentiment analysis and categorization as the final output, make sure the key matches the tool used.
                """
    )
    # print("Chat History:")
    # print(result.chat_history)
    print("Final Result:")
    # print(result.summary)
    pprint(json.loads(result.summary))

if __name__ == "__main__":
    main()
