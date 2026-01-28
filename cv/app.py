from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/state")
def get_state():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "salience": 0.0,
        "novelty": 0.0,
        "summary": None
    }
