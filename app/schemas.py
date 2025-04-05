from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class TextResult(BaseModel):
    toxicity: float
    flags: list[str]
