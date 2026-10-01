from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="BUMANI Climate Voice Free API")

class TranslationRequest(BaseModel):
    text: str
    language: str

@app.get("/")
def root():
    return {"service":"BUMANI Climate Voice","status":"online","mode":"free-lightweight"}

@app.get("/health")
def health():
    return {"status":"ok","mode":"free-lightweight"}

@app.post("/translate")
def translate(req: TranslationRequest):
    lang=req.language.lower().strip()
    if lang not in {"bambara","hausa","moore"}:
        raise HTTPException(400,"language must be bambara, hausa, or moore")
    if not req.text.strip():
        raise HTTPException(400,"text is empty")
    return {
        "translation": None,
        "language": lang,
        "mode": "offline_corpus",
        "message": "Use the BUMANI_CIC corpus embedded in the Android app for offline translation."
    }
