from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.rag import search_document

load_dotenv()

model = init_chat_model('openai:gpt-4.1-mini')

agent = create_agent(
    model=model,
    tools=[search_document],
    system_prompt='Você é um assistente político especializado nos planos de governo dos candidatos à presidência do Brasil, em 2026.',
    checkpointer=InMemorySaver()
)