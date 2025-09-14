from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AAIE LLM API")

class ClassifyIn(BaseModel):
    student_submission: str
    prompt_text: str | None = None
    chat_log: list[dict] | None = None

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.post("/llm/classify")
def classify(inp: ClassifyIn):
    # TODO: replace with your real model call
    return {"classification": "Human", "confidence": 0.91, "version": "v1"}
