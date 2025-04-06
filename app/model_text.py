from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_text_toxic_classifier():
    return pipeline("text-classification", model="unitary/toxic-bert", top_k=None)
