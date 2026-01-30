from fastapi import FastAPI
from datetime import datetime
from contextlib import asynccontextmanager
import threading
from worker import run

Start_Time = datetime.utcnow()

@asynccontextmanager
async def lifespan(app:FastAPI):
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    yield

app = FastAPI(lifespan=lifespan)

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


