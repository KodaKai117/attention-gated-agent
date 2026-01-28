from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.post("/analyze")
def analyze(input: dict):
    return {
        "confidence": 0.0,
        "suggestion": None,
        "generated_at": datetime.utcnow().isoformat()
    }

@app.get("/pending")
def pending():
    return []
