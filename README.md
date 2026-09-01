# 🤖 AI Research Agent

A beginner-friendly AI Agent built with **Python, LangChain, Google Gemini, and Streamlit**.

The agent can understand user questions, use external tools when required, and provide a final response through a simple Streamlit chat interface.

---

## 🚀 Features

* 🤖 Google Gemini AI model
* 🔎 Web search using DuckDuckGo
* 🌤️ Current weather information
* 🔢 Word counting tool
* 🛠️ Custom LangChain tools
* 💬 Streamlit chat interface
* 🔐 Environment variable support for API keys
* 🧠 Agent-based tool calling using LangChain

---

## 🏗️ Project Structure

```text
ai-agent/
│
├── app.py
├── agent.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Technologies Used

* **Python**
* **LangChain**
* **Google Gemini**
* **Streamlit**
* **DuckDuckGo Search**
* **OpenWeatherMap API**

---

## 🧠 AI Model

This project uses:

```python
MODEL_NAME = "gemini-3-flash-preview"
```

The model is connected to LangChain using:

```python
from langchain_google_genai import ChatGoogleGenerativeAI
```

---

## 🔧 Tools

**The agent has three tools.**

### 1. Web Search

The agent can search the web when it needs external or current information.

```python
search_tool = DuckDuckGoSearchRun()
```

### 2. Weather

The custom weather tool uses the OpenWeatherMap API.

```python
@tool
def get_weather(city: str) -> str:
    ...
```

Example:

```text
What's the current weather in Colombo?
```

### 3. Word Counter

A custom tool counts the number of words in a given text.

```python
@tool
def word_counter(text: str) -> str:
    ...
```

Example:

```text
Count the words in this sentence:
AI agents can use tools.
```

---

## 🔑 API Keys

The `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

The `.gitignore` is included:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project directory:

```bash
cd ai-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 💬 Example Questions

Try asking:

```text
What is an AI agent?
```

```text
What is the current weather in Kandy?
```

```text
Search the web for the latest developments in AI agents.
```

```text
Count the words in:
AI agents can use external tools.
```

The agent decides when a tool is required and uses the appropriate tool before generating the final response.

---

## 🔄 How It Works

```text
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
          LangChain AI Agent
                  │
                  ▼
        Gemini 3 Flash Preview
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
   Web Search  Weather  Word Counter
        │         │         │
        └─────────┼─────────┘
                  ▼
            Final Response
                  │
                  ▼
                User
```

---

## 📚 What I Learned

Through this project, I practiced:

* Building an AI agent with LangChain
* Using Google Gemini with LangChain
* Creating custom tools with `@tool`
* Tool calling and agent workflows
* Working with external APIs
* Web search integration
* Environment variable management
* Building a conversational UI with Streamlit
* Handling API errors and quota limits
* Separating AI logic from the user interface

---

## ⚠️ API Quota

The Gemini API has usage limits depending on the Google AI API project and billing tier.

If you receive:

```text
429 RESOURCE_EXHAUSTED
```

check your Gemini API quota and usage.

---

## 📌 Future Improvements

Possible improvements include:

* 💾 Conversation memory
* 📄 PDF document analysis
* 🔍 RAG implementation
* 🔐 User authentication
* 🎨 Improved Streamlit UI
* ☁️ Deployment to Streamlit Community Cloud

---

This project was created as part of my learning journey in **Artificial Intelligence, AI Agents, and Software Engineering**.
