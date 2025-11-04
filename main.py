from feedback_agent.config import LLM_CONFIG
from feedback_agent.agent.calculator_agent import main as calculator_main
from feedback_agent.agent.feedback_analysis_agent import main as feedback_analysis_main

def main():
    print("Hello from ml-customer-feedback-agent!")
    # calculator_main()
    feedback_analysis_main()


if __name__ == "__main__":
    main()
