"""..."""

import os
from pprint import pprint
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


load_dotenv()

model_id = os.getenv("EXTRACTION_MODEL")
llm = ChatGoogleGenerativeAI(model=model_id)


agent = create_agent(model=llm)

# agent.invoke("Hola") -- >>> langgraph.errors.InvalidUpdateError: Expected dict, got Hola
# Need to 

messages = {
    "messages": [
        HumanMessage(content="¿Cuál es la capital de La Guajira?")
    ]
}

agent_response = agent.invoke(input=messages)

print()
print(type(agent_response))
print()
pprint(agent_response)
print()

iterable_messages = agent_response["messages"]
print("*** Conversation ***")
for msj_obj in iterable_messages:
    print()
    print(msj_obj)

print("*** End of Conversation ***\n\n")

print("*** Agent Response - Last message ***")
print(agent_response["messages"][-1].content[0]["text"])
