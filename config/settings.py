from dotenv import load_dotenv

import os

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama3.2:3b")

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434")
