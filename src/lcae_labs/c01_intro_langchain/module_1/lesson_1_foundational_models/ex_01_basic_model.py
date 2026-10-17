"""..."""

import os
from pprint import pprint

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()
ai_provider = os.getenv("AI_PROVIDER")
extraction_model = os.getenv("EXTRACTION_MODEL")
model_name = ai_provider + ":" + extraction_model

# Puedo usar la forma condensada: `google_genai:gemini-3.1-flash-lite`
# model = init_chat_model(model=model_name)
# O dar expliciatamente el model name y el provider por separado
model = init_chat_model(
    model=extraction_model,
    model_provider=ai_provider
    )

response = model.invoke("¿Cuál es la capital de La Guajira?")
print(response.content[0]['text'])
print()
print(response.content)
print()
print(response)
print()
pprint(response.response_metadata)
