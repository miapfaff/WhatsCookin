from google.cloud import vision
import io
import os

# Set credentials from JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vision_key.json"

def detect_ingredients(image_path: str) -> list[str]:
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Filter labels for common food items
    ingredients = [label.description.lower() for label in labels if label.score > 0.75]

    return ingredients
