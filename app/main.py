from fastapi import FastAPI, UploadFile, File, HTTPException
from app.model_text import analyze_text
from app.model_image import analyze_image
from app.schemas import TextInput, TextResult
from fastapi.middleware.cors import CORSMiddleware
import os
import traceback

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port)

    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Toxicity Detection API"}

@app.post("/analyze/text", response_model=TextResult)
async def analyze_text_route(payload: TextInput):
    return analyze_text(payload.text)

@app.post("/detect-nsfw-image")
async def detect_nsfw_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = analyze_image(contents)
        return result
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
