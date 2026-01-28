from fastapi import FastAPI
import requests
import threading
import time

app = FastAPI()

CV_URL = "http://cv:8000/state"
LLM_URL = "http://llm:8000/analyze"

STATE = {
    "ticks": 0,
    "last_decision": None
}

def governor_loop():
    while True:
        try:
            cv_state = requests.get(CV_URL, timeout=1).json()
        except Exception:
            cv_state = None

        decision = {
            "tick": STATE["ticks"],
            "attend": False,
            "reason": "insufficient salience",
            "cv_state": cv_state
        }

        STATE["last_decision"] = decision
        STATE["ticks"] += 1

        time.sleep(1)  # 1 Hz executive loop

@app.on_event("startup")
def start_loop():
    thread = threading.Thread(target=governor_loop, daemon=True)
    thread.start()

@app.get("/state")
def get_state():
    return STATE
