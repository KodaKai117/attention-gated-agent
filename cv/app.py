from fastapi import FastAPI
from datetime import datetime

Start_Time = datetime.utcnow()
app = FastAPI()

@app.get("/state")
def get_state():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "salience": 0.0,
        "novelty": 0.0,
        "summary": None
    }
@app.get("/health")
def get_health():
    uptime = (datetime.utcnow() - Start_Time).total_seconds()
    return {
        "status": "ok",
        "service": "cv",
        "uptime_s": int(uptime),
        "timestamp": datetime.utcnow().isoformat()
    }