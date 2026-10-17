"""..."""
import os
from pprint import pprint
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

model_id = os.getenv("EXTRACTION_MODEL")

llm = ChatGoogleGenerativeAI(model=model_id)

agent = create_agent(model=llm)

messages = [
    HumanMessage(content="¿Cuál es la capital de La Guajira?"),
    AIMessage(content="La capital del departamento de La Guajira es **Riohacha**."),
    HumanMessage(content="Umm interesante. Por favor cuéntame más sobre esa ciudad!!")
]

response = agent.invoke({
    "messages": messages
})

pprint(response)
