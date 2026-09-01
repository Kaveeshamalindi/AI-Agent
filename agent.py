import os
import requests

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()


# -----------------------------
# Model Configuration
# -----------------------------

MODEL_NAME = "gemini-3-flash-preview"

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=1.0,
    max_retries=2
)

# -----------------------------
# Web Search Tool
# -----------------------------

search_tool = DuckDuckGoSearchRun()


# -----------------------------
# Weather Tool
# -----------------------------

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": os.environ["OPENWEATHERMAP_API_KEY"],
        "units": "metric"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]

    return (
        f"Weather in {city}: "
        f"{temperature}°C, "
        f"{description}. "
        f"Feels like {feels_like}°C."
    )


# -----------------------------
# Word Counter Tool
# -----------------------------

@tool
def word_counter(text: str) -> str:
    """Count the number of words in text."""

    count = len(text.split())

    return f"The text contains {count} words."


# -----------------------------
# Tools
# -----------------------------

tools = [
    search_tool,
    get_weather,
    word_counter
]


# -----------------------------
# System Prompt
# -----------------------------

SYSTEM_PROMPT = """
You are a helpful AI research assistant.

You have access to these tools:

1. Web search
2. Weather
3. Word counter

Use tools whenever necessary.

Do not invent current information.

For multi-step questions, use the appropriate tools
and combine their results.

Give clear and concise answers.
"""


# -----------------------------
# Create Agent
# -----------------------------

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)


# -----------------------------
# Function for Streamlit
# -----------------------------

def ask_agent(user_message: str) -> str:

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        }
    )

    content = result["messages"][-1].content

    # Gemini may return content as a list of blocks
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))

        return "".join(text_parts)

    return str(content)