from langchain.chat_models import Ollama

llm = Ollama(
    model="llama3"
)

response = llm.invoke("Machine Learning என்றால் என்ன?")

print(response.content)
