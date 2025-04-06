from fastapi import FastAPI
from app.schemas import TextInput
from app.model_text import get_text_toxic_classifier

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Toxicity Detection API is running."}

@app.post("/predict-text")
def predict_text(input: TextInput):
    classifier = get_text_toxic_classifier()
    result = classifier(input.text)
    return {"results": result}
