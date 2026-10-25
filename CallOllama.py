from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma4:latest",
    temperature=0.7,
)

response = llm.invoke("Explain LangChain in simple words.")

print(response.content)
