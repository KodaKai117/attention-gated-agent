from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
Start_Time = datetime.utcnow()
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

@app.get("/health")
def get_health():
    uptime = (datetime.utcnow() - Start_Time).total_seconds()
    return {
        "status": "ok",
        "service": "llm",
        "uptime_s": int(uptime),
        "timestamp": datetime.utcnow().isoformat()
    }
