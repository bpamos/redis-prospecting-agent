from langchain_openai import OpenAIEmbeddings
from config import settings

def get_embedding_model():
    return OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)
