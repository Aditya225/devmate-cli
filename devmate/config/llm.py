import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq



# def get_llm():
#     print("API KEY:", os.getenv("GROQ_API_KEY"))
#     return "groq/llama3-8b-instant"

# def get_llm():
#     return "groq/llama-3.1-70b-versatile"

# def get_llm():
#     return "openrouter/mistralai/mistral-7b-instruct"

def get_llm():
    return "openrouter/openai/gpt-4o-mini"