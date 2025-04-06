# app/main.py
from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
classifier = None  # Lazy loading

@app.get("/")
def read_root():
    return {"message": "API is live"}

@app.post("/analyze")
async def analyze(request: Request):
    global classifier
    if classifier is None:
        classifier = pipeline("text-classification", model="distilbert-base-uncased")
    data = await request.json()
    result = classifier(data["text"])
    return {"result": result}
