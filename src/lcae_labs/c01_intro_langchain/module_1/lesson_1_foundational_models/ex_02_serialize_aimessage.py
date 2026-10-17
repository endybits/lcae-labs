"""..."""

import os

from langchain.chat_models import init_chat_model
from langchain_core.load import dumpd, load
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

ai_prov = os.getenv("AI_PROVIDER")
extract_model = os.getenv("EXTRACTION_MODEL")
model_name = ai_prov + ":" + extract_model

llm = init_chat_model(model_name)

ai_response = llm.invoke("¿Cuál es la capital de La Guajira?")

# print(ai_response.content)
print()

serialized = dumpd(ai_response)
print(serialized)
print()
print(serialized)
print(type(serialized))
restored = load(serialized, allowed_objects='messages')

print(type(restored))
print()
print(restored.content)
print()
print(restored.content[0]['text'])



####

template = PromptTemplate.from_template("Say {foo}")
template.format(foo="Hola")

serialized_template = dumpd(template)
print(type(serialized_template))
print(serialized_template)


print()
print(load(serialized_template, allowed_objects='core'))
