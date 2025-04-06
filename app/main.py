from fastapi import FastAPI, UploadFile, File
from app.model_text import analyze_text
from app.model_image import analyze_image
from app.schemas import TextInput, TextResult
import os

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Toxicity Detection API"}

@app.post("/analyze/text", response_model=TextResult)
async def analyze_text_route(payload: TextInput):
    return analyze_text(payload.text)

@app.post("/analyze/image")
async def analyze_image_route(file: UploadFile = File(...)):
    contents = await file.read()
    return analyze_image(contents)
