from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

# Ensure it loads regardless of where you run from
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env.example")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recipe(ingredients: list[str]) -> str:
    return "Mock recipe: scrambled eggs with toast!"
