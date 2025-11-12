import os
from dotenv import load_dotenv

# load .env from project root / current working directory
load_dotenv()

LLM_CONFIG = {
    "model": "gemini-2.5-flash",
    "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
    "api_type": "openai",
    "api_key": os.environ.get("LLM_API_KEY"),
    "cache_seed": None,
    "price":[0.1 / 1000, 0.4 / 1000],  # [input, output] per 1K tokens
    # "reasoning_effort": "none",
    # "hide_tools": "if_any_run",
    # "native_tool_call": True,
    # "cache_seed": None,
}