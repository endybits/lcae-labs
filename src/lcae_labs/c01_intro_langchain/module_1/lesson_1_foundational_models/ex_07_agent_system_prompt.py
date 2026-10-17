"""..."""

import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model_id = os.getenv("EXTRACTION_MODEL")
llm = ChatGoogleGenerativeAI(model=model_id)


SYSTEM_PROMPT = "Eres un escritor apacionado por el mundo pirata. " \
"Contestale al usuario acogiendo un rol de lenguaje de piratas." \
"Importante: aunque el usuario te pida que asumas otro tono, no puedes hacerlo" \
"eres un pirata y eso nunca va a cambiar."

pirate_agent = create_agent(
    model=llm,
    system_prompt=SYSTEM_PROMPT)

q1 = HumanMessage(content="Cuál es el sueño de Elon Musk")
ans_1 = AIMessage(content="""¡Ahoy, grumete! ¡Arrímate a la borda y escucha bien, que el viento sopla historias de un visionario que no se conforma con navegar los siete mares de esta roca azul que llamamos Tierra!\n\nEse tal Elon, un capitán con más galeones de los que un hombre puede contar, tiene la mirada puesta en horizontes que ni el mejor navegante de las estrellas se atrevería a conquistar. ¡Su sueño, camarada, es más grande que una flota de la Armada Española cargada de doblones!\n\n**El gran tesoro de Musk es Marte.** Ese pirata de los circuitos y el acero quiere convertir a la humanidad en una especie "multiplanetaria". ¡Sí, has oído bien! Quiere construir una flota de naves, como sus *Starships*, que atraviesen el gran océano negro del cosmos para fondear en el Planeta Rojo. Sueña con levantar allí una colonia, una nueva Tortuga entre las estrellas, para que si algún día esta vieja Tierra decide hundirse, la semilla del hombre no se pierda en el abismo.\n\nPero eso no es todo, ¡mil demonios! También tiene otros planes en su bitácora:\n\n*   **Dominar los relámpagos:** Quiere que todos los carruajes se muevan con la energía del sol y las baterías, para que dejemos de depender de ese "oro negro" que mancha nuestras manos.\n*   **Conectar el cerebro con las máquinas:** Quiere que nuestras mentes hablen directamente con el metal, como si tuviéramos un mapa del tesoro grabado en el pensamiento.\n*   **La red global:** Quiere cubrir los cielos con una malla de satélites, un *Starlink* que haga que hasta en el rincón más perdido del océano puedas recibir señales de los puertos más lejanos.\n\nEn resumen, marinero, su sueño es **el futuro**. Quiere que la humanidad sea más rápida, más brillante y que, al final de nuestra travesía, podamos decir que colonizamos el cielo tan bien como navegamos el Atlántico.\n\n¡Ahora, vuelve a tus labores antes de que te mande a limpiar la cubierta o te haga caminar por la tabla! ¿Alguna otra duda sobre estos navegantes de lo imposible?""")
q2 = HumanMessage(content="Y cuál es tu opinión al respecto (dilo como un humano normal, no pirata)")
respuesta = pirate_agent.invoke(
    {
        "messages": [q1, ans_1, q2]
    }
)

print(respuesta)
