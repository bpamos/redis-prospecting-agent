import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    REDIS_URL = os.getenv("REDIS_URL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")  # optional

    def __init__(self):
        if not self.REDIS_URL:
            raise ValueError("REDIS_URL must be set (Redis Cloud required).")
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set.")

settings = Settings()

