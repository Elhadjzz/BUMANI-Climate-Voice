from functools import lru_cache
import io
import torch
import librosa
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from scipy.io.wavfile import write as wav_write
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, VitsModel

app = FastAPI(title="BUMANI Climate Voice API")
NLLB_MODEL = "facebook/nllb-200-distilled-600M"
LANG_CODES = {"bambara": "bam_Latn", "hausa": "hau_Latn", "moore": "mos_Latn"}
TTS_MODELS = {"bambara": "facebook/mms-tts-bam", "hausa": "facebook/mms-tts-hau", "moore": "facebook/mms-tts-mos"}

class TranslationRequest(BaseModel):
    text: str
    language: str

class TTSRequest(BaseModel):
    text: str
    language: str

@lru_cache(maxsize=1)
def load_translation_model():
    tokenizer = AutoTokenizer.from_pretrained(NLLB_MODEL)
    model = AutoModelForSeq2SeqLM.from_pretrained(NLLB_MODEL)
    model.eval()
    return tokenizer, model

@lru_cache(maxsize=1)
def load_tts_model(lang: str):
    tokenizer = AutoTokenizer.from_pretrained(TTS_MODELS[lang])
    model = VitsModel.from_pretrained(TTS_MODELS[lang])
    model.eval()
    return tokenizer, model

@app.get("/")
def root():
    return {"service": "BUMANI Climate Voice", "status": "online", "translation": "NLLB-200", "speech": "Meta MMS"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/translate")
def translate(req: TranslationRequest):
    lang = req.language.lower().strip()
    if lang not in LANG_CODES:
        raise HTTPException(400, "language must be bambara, hausa, or moore")
    text = req.text.strip()
    if not text:
        raise HTTPException(400, "text is empty")
    tokenizer, model = load_translation_model()
    tokenizer.src_lang = "eng_Latn"
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    forced = tokenizer.convert_tokens_to_ids(LANG_CODES[lang])
    with torch.no_grad():
        output = model.generate(**inputs, forced_bos_token_id=forced, max_new_tokens=256)
    return {"translation": tokenizer.batch_decode(output, skip_special_tokens=True)[0], "language": lang}

@app.post("/tts")
def tts(req: TTSRequest):
    lang = req.language.lower().strip()
    if lang not in TTS_MODELS:
        raise HTTPException(400, "language must be bambara, hausa, or moore")
    text = req.text.strip()
    if not text:
        raise HTTPException(400, "text is empty")
    tokenizer, model = load_tts_model(lang)
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        waveform = model(**inputs).waveform
    audio = waveform.squeeze().cpu().float().numpy()
    audio = librosa.effects.time_stretch(audio, rate=0.95)
    peak = max(float(abs(audio).max()), 1e-8)
    pcm16 = (audio / peak * 32767.0).astype("int16")
    buf = io.BytesIO()
    wav_write(buf, rate=model.config.sampling_rate, data=pcm16)
    return Response(content=buf.getvalue(), media_type="audio/wav")
