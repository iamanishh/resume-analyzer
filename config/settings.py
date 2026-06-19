from dotenv import load_dotenv

import os


load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL",
                            "http://localhost:11434")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is not configured")

if not OLLAMA_BASE_URL:
    raise ValueError("OLLAMA_BASE_URL is not configured")

