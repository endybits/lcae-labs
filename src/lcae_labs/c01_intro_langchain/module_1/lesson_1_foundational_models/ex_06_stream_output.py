"""..."""
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model_id = os.getenv("EXTRACTION_MODEL")
llm = ChatGoogleGenerativeAI(model=model_id)

messages = [
    HumanMessage(content="¿Cuál es la capital de La Guajira?"),
    AIMessage(content="La capital del departamento de La Guajira es **Riohacha**."),
    HumanMessage(content="Umm interesante. Por favor cuéntame más sobre esa ciudad!!")
]

agent = create_agent(model=llm)

print()
input_tokens = 0
output_tokens = 0
for token, metadata in agent.stream({"messages": messages}, stream_mode="messages"):
    # if metadata:
    #     print(metadata)
    if token.content:
        print(token.content[0]["text"], end="", flush=True)
        print(token)
    if token.usage_metadata:
        usage_metadata = token.usage_metadata
        input_tokens += usage_metadata.get("input_tokens", 0)
        output_tokens += usage_metadata.get("output_tokens", 0)

print("*** Tokens Usage ***")
print("Input tokens: ", input_tokens)
print("Output tokens: ", output_tokens)
