import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HuggingFace_Api_Key")
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke([
    SystemMessage(content="You are a helpful assistant that provides information about cricket matches."),
    HumanMessage(content="Yesterday cricket match details.")
])

print(response.content)