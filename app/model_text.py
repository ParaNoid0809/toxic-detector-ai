from transformers import pipeline

# Load model
classifier = pipeline("text-classification", model="unitary/toxic-bert")

def analyze_text(text: str):
    result = classifier(text)[0]
    toxicity = round(result["score"], 3)
    label = result["label"].lower()

    flags = []
    if label == "toxic":
        flags.append("toxic")

    return {
        "toxicity": toxicity,
        "flags": flags
    }
