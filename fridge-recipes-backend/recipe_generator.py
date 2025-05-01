import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe(ingredients: list[str]) -> str:
    prompt = f"Give me a recipe using only these ingredients: {', '.join(ingredients)}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
