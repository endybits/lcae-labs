"""..."""
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model_name = os.getenv('EXTRACTION_MODEL')

llm = ChatGoogleGenerativeAI(model=model_name)

response = llm.invoke("¿Cuál es la capital de La Guajira?")
print(type(response))
print()
print(response.content)
