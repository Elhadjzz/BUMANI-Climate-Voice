# BUMANI_CIC — Climate Information Corpus

BUMANI_CIC is the domain-specific terminology resource used by **Sahel Climate Voice** for climate-information access in three West African languages:

- **BU** — Burkina Faso → **Mooré**
- **MA** — Mali → **Bambara**
- **NI** — Niger → **Hausa**

## Corpus files

| File | Language pair | Bilingual records | Unique case-normalized English headwords |
|---|---|---:|---:|
| `english_bambara.csv` | English–Bambara | 1,633 | 1,633 |
| `english_hausa.csv` | English–Hausa | 1,633 | 1,632 |
| `english_moore.csv` | English–Mooré | 1,633 | 1,633 |

**Total bilingual records:** 4,899  
**Strict three-language common English inventory:** 1,608 case-normalized headwords.

## Construction summary

The initial working corpus combined:

1. **1,002 curated climate-change concepts**, and
2. **517 weather and climate glossary entries**,

for an initial total of **1,519 concepts**.

The source knowledge base was assembled from scientific literature and institutional climate-information resources. The broader research workflow used 650 scientific documents (481 ScienceDirect papers and 169 papers identified through Google Scholar), together with terminology and conceptual materials from WASCAL, IPCC, ACMAD, WMO, UNFCCC, and BRACED.

Translation and localization followed a **functional-equivalence** approach rather than strict word-for-word substitution. Depending on the concept, the process used borrowing/transliteration, compounding, explanatory paraphrase, and contextual localization. Back-translation and native-speaker review were used as semantic and linguistic checks.

The application-oriented corpus was subsequently cleaned, alphabetically ordered by English headword, whitespace-normalized, and subjected to duplicate control, yielding 1,633 bilingual records for each language pair.

## CSV structure

Each file contains two columns:

```text
english,target-language
```

Example:

```text
english,bambara
(sand) Dune,cɛncɛn kulu
```

The target-language column is named `bambara`, `hausa`, or `moore` in the corresponding file.

## Important scope note

BUMANI_CIC is primarily a **terminology and concept corpus**, not a large sentence-level parallel corpus. It is intended to support climate-domain terminology lookup, multilingual application development, and controlled evaluation of climate-specific translation.

The current production Sahel Climate Voice backend uses the pretrained `facebook/nllb-200-distilled-600M` checkpoint for full-sentence translation. The BUMANI_CIC files provide the explicit climate-domain terminology layer and should not be interpreted as evidence that the production endpoint is serving historical fine-tuned checkpoints.

## Data quality note

The Hausa file contains 1,633 records but 1,632 unique case-normalized English headwords because one English item is represented in two case variants in the curated source. This is preserved in the current release for traceability.

## Citation

If you use this resource, please cite the associated manuscript:

> ELH MAMAN GARBA Ibrahim et al. *Sahel Climate Voice: An AI-Driven Multilingual Mobile System for Climate Information Translation and Speech Delivery in Bambara, Hausa, and Mooré.* Manuscript under submission.

The final bibliographic citation will be updated after publication.

## License and reuse

No separate dataset license has yet been declared for BUMANI_CIC in this repository. Please contact the corresponding author before redistribution or reuse beyond research inspection:

**ELH MAMAN GARBA Ibrahim**  
Graduate Study Programme on Climate Change and Education, WASCAL / University of The Gambia  
Email: `ibrahim.e@edu.wascal.org`

## Integrity

`manifest.json` records row counts, uniqueness statistics, and SHA-256 checksums for the CSV files.