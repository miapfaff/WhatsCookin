from fastapi import FastAPI, File, UploadFile
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
    contents = await file.read()  # Read the image just to simulate use
    print(f"Received file: {file.filename}, size: {len(contents)} bytes")

    # Mock response to test frontend communication
    return {"recipe": "Mock recipe: scrambled eggs with toast!"}
