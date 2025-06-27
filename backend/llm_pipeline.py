import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not set in environment")

embeddings_client = OpenAIEmbeddings(openai_api_key=openai_api_key)

def get_embedding(text: str) -> list[float]:
    """
    Return the embedding vector for the given text.
    """
    return embeddings_client.embed_query(text)
