from fastapi import FastAPI
from pydantic import BaseModel

from intent_extractor import extract_intent

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():

    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate_app(request: PromptRequest):

    result = extract_intent(request.prompt)

    return {
        "result": result
    }