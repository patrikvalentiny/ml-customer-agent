from pprint import pprint
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor, DockerCommandLineCodeExecutor
from config import LLM_CONFIG


# plot a line chart using matplotlib that shows closing prices over time for PLTR stock
def code_executor_pltr_closing():
    agent = AssistantAgent(
        name="PLTR Closing Price Plotter",
        system_message="""You are a helpful AI assistant.
        Generate code and give instruction to user how to run the code.
        Make sure python code is in .py file format.
        Use pip to install required packages.
        Plot a line chart using matplotlib.
        Use yfinance to fetch the stock market data.
        Generate an image in PNG format.
        Ask the user proxy to execute the code in after you generate it.
        Return 'TERMINATE' only and only after the code has been run successfully by the user.
        """,
        llm_config=LLM_CONFIG,
    )

    user_proxy = UserProxyAgent(
        name = "User Proxy",
        system_message="You are a user proxy that helps the agent to execute code in command line.",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            # "enabled": True,
            # "allowed_modules": ["matplotlib", "yfinance"],
            "executor": DockerCommandLineCodeExecutor(work_dir="coding")
        }
    )

    user_proxy.initiate_chat(
        agent, 
        message="Please generate a plot of the closing prices from exactly 2025-01-01 to 2025-10-14 for PLTR stock. " \
        # "Execute the returned code in command line.",
    )

    # print("Final chat result:")
    # pprint(chat)

if __name__ == "__main__":
    code_executor_pltr_closing()