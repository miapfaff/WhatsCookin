from detect_ingredients import detect_ingredients
from recipe_generator import generate_recipe
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Save the uploaded image temporarily
        image_path = "temp.jpg"
        with open(image_path, "wb") as f:
            f.write(contents)

        # Detect ingredients from image
        ingredients = detect_ingredients(image_path)
        print(f"\n📸 Detected ingredients: {ingredients}\n")

        # Generate recipe from detected ingredients
        recipe = generate_recipe(ingredients)
        print(f"\n👩‍🍳 Generated recipe: {recipe}\n")

        return {"recipe": recipe}

    except Exception as e:
        print("🔥 Error in /upload route:", e)
        return {"recipe": "Error: " + str(e)}
