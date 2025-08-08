from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Time Tool", version="0.0.1")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/time")
def time():
    return {"iso": datetime.now(timezone.utc).isoformat()}
