import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR / ".env")

APP_TITLE = "Asistente de Escritura Automática con OpenAI"
APP_ICON = "✍️"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

AVAILABLE_MODELS = [
    "gpt-4.1-mini"
]

DEFAULT_MODEL = AVAILABLE_MODELS[0]