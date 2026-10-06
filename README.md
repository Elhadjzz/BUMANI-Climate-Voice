# BUMANI Climate Voice

**Sahel Climate Voice** is a multilingual climate-information system for English-to-Bambara, English-to-Hausa, and English-to-Mooré text and speech delivery.

The cloud backend provides:
- NLLB-200 multilingual translation
- Meta MMS/VITS text-to-speech
- FastAPI REST endpoints for translation and audio generation
- HTTPS cloud inference for the Android application

## BUMANI_CIC — Climate Information Corpus

The repository now includes the application-oriented **BUMANI_CIC** resource used as the domain-specific climate terminology layer.

- English–Bambara: 1,633 bilingual records
- English–Hausa: 1,633 bilingual records
- English–Mooré: 1,633 bilingual records
- Total: 4,899 bilingual records
- Strict common English inventory: 1,608 case-normalized headwords

See [`BUMANI_CIC/README.md`](BUMANI_CIC/README.md) for corpus construction, file descriptions, scope, citation, and reuse information.

### Corpus files

- [`BUMANI_CIC/english_bambara.csv`](BUMANI_CIC/english_bambara.csv)
- [`BUMANI_CIC/english_hausa.csv`](BUMANI_CIC/english_hausa.csv)
- [`BUMANI_CIC/english_moore.csv`](BUMANI_CIC/english_moore.csv)
- [`BUMANI_CIC/manifest.json`](BUMANI_CIC/manifest.json)

## API

- `GET /` — service status
- `GET /health` — health check
- `POST /translate` — English-to-Bambara/Hausa/Mooré translation
- `POST /tts` — target-language speech synthesis

## Model configuration

Translation: `facebook/nllb-200-distilled-600M`

Speech synthesis:
- Bambara: `facebook/mms-tts-bam`
- Hausa: `facebook/mms-tts-hau`
- Mooré: `facebook/mms-tts-mos`

## Research scope

The repository separates two components clearly:

1. **BUMANI_CIC** — a domain-specific climate terminology/concept resource.
2. **Production AI service** — the current backend uses the pretrained NLLB-200 checkpoint for full-sentence translation and MMS/VITS for speech synthesis.

Historical fine-tuning experiments should therefore not be interpreted as the model checkpoint currently served by the production backend.