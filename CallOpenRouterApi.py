import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()



llm = ChatOpenRouter(
    model="meta-llama/llama-3.3-70b-instruct",
    api_key=os.getenv("Open_Router_Api_Key"),
    temperature=0.7
)

response = llm.invoke("simple python program")
print("Response:", response.content)