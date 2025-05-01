from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from recipe_generator import generate_recipe
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Save the file (or process it in-memory)
    contents = await file.read()
    with open("temp.jpg", "wb") as f:
        f.write(contents)

    # MOCK INGREDIENTS (replace with real parser later)
    ingredients = ["eggs", "milk", "spinach"]

    recipe = generate_recipe(ingredients)
    return {"recipe": recipe}
