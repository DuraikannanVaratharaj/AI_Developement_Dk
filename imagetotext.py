from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HuggingFace_Api_Key")
)

image = client.text_to_image(
    "A cute robot reading a book in a library, Pixar style",
    model="ideogram-ai/ideogram-4-fp8"
)

image.save("robot.png")